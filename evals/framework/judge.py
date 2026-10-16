#!/usr/bin/env python3
"""
promptfoo python assertion — stage 2 (GAP) of the eval framework.

get_assert(output, context) -> GradingResult dict.

Design constraints (see EVALS.md Tier 0 and the plan this was built from):
- No API keys in this environment: `claude` authenticates off a subscription,
  so the judge shells out to `claude -p` itself rather than using promptfoo's
  built-in llm-rubric providers.
- N independent judge sessions (EVAL_JUDGES env, default 3), each isolated in
  its own scratch dir seeing only the generated output + ground truth +
  transcript. Never the skill's SKILL.md -- the judge grades the artifact,
  not the author's intent.
- This fixes VARIANCE (random scatter across samples), not systematic bias --
  every sample is still the same model family. Run calibrate.py against a
  hand-labeled set to check for the latter; see evals/framework/README.md.
- Per-sample ground-truth field-order shuffle (seeded by sample index) is the
  applicable analogue of judge position-swap for pointwise reference grading
  (there's no A/B slot to swap here, only field order).
"""
import json
import os
import random
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
EVAL_MODEL = os.environ.get("EVAL_MODEL", "claude-haiku-5-5")  # judge and runner share one pinned model
RUBRIC_VERSION = "1"  # bump and re-run calibrate.py whenever JUDGE_PROMPT changes meaningfully

JUDGE_PROMPT_TEMPLATE = """Compare the generated output in ./output/ against the ground truth in ./{gt_name}.

Enumerate every distinct field or entry in the ground truth -- markdown '## '
sections if it's markdown, top-level keys if it's JSON -- and judge each one
against ./output/ as one of: present | missing | wrong | extra.

For every 'missing' field, also say whether it was derivable from
./transcript.txt: true = the skill should have found it (a real bug),
false = genuinely absent from the transcript (correct to omit).

Respond with ONLY valid JSON, no prose, no markdown fences, in exactly this
shape:
{{"fields": {{"<field name>": {{"verdict": "present|missing|wrong|extra", "derivable": true|false|null, "evidence": "<short quote or empty>"}}}}}}
"""


def _shuffle_gt(gt_text, seed):
    rng = random.Random(seed)
    try:
        obj = json.loads(gt_text)
        if isinstance(obj, dict):
            keys = list(obj.keys())
            rng.shuffle(keys)
            return json.dumps({k: obj[k] for k in keys}, indent=2)
        return gt_text
    except (json.JSONDecodeError, ValueError):
        pass
    blocks = re.split(r"(?=^## )", gt_text, flags=re.MULTILINE)
    if len(blocks) > 1:
        header, rest = blocks[0], blocks[1:]
        rng.shuffle(rest)
        return header + "".join(rest)
    return gt_text


def _run_claude(prompt, cwd):
    proc = subprocess.run(
        ["claude", "-p", prompt, "--model", EVAL_MODEL, "--setting-sources", "project", "--dangerously-skip-permissions"],
        cwd=cwd, capture_output=True, text=True, timeout=600,
    )
    return proc.stdout


# Cross-family judge panel via OpenRouter. One sample per model, so the three
# judges come from three labs and do not share one family's blind spots.
JUDGE_BACKEND = os.environ.get("JUDGE_BACKEND", "claude")  # claude | openrouter
OR_MODELS = [m for m in os.environ.get(
    "JUDGE_MODELS", "z-ai/glm-5.3-flash").split(",") if m]
CAP_USD = float(os.environ.get("JUDGE_CAP_USD", "10"))      # per month, hard stop
RUN_CAP_USD = float(os.environ.get("JUDGE_RUN_CAP_USD", "0.50"))  # per process, hard stop
_RUN = {"spent": 0.0, "remote": None}
LEDGER = Path.home() / ".config" / "gtm-loop" / "spend.json"
KEY_FILE = Path.home() / ".config" / "gtm-loop" / "openrouter.key"


_LEDGER_LOCK = __import__("threading").Lock()


def _spend_month():
    key = __import__("time").strftime("%Y-%m")
    try:
        return key, float(json.loads(LEDGER.read_text()).get(key, 0.0))
    except (OSError, ValueError):
        return key, 0.0


def _run_openrouter(prompt, cwd, model):
    import urllib.request
    key = os.environ.get("OPENROUTER_API_KEY") or KEY_FILE.read_text().strip()
    month, spent = _spend_month()
    if _RUN["remote"] is None:  # OpenRouter's own monthly figure is the truth, the local ledger can lag
        req0 = urllib.request.Request("https://openrouter.ai/api/v1/key", headers={"Authorization": f"Bearer {key}"})
        with urllib.request.urlopen(req0, timeout=30) as r0:
            _RUN["remote"] = float(json.loads(r0.read())["data"].get("usage_monthly") or 0)
    spent = max(spent, _RUN["remote"] + _RUN["spent"])
    if spent >= CAP_USD:
        raise RuntimeError(f"judge spend cap reached: {spent:.2f} of {CAP_USD:.2f} USD this month")
    if _RUN["spent"] >= RUN_CAP_USD:
        raise RuntimeError(f"judge run cap reached: {_RUN['spent']:.2f} of {RUN_CAP_USD:.2f} USD in this run")
    files = sorted(p for p in Path(cwd).rglob("*") if p.is_file())
    inline = prompt + "\n\n" + "\n\n".join(
        f"=== ./{p.relative_to(cwd)} ===\n{p.read_text(errors='ignore')}" for p in files)
    body = json.dumps({"model": model, "temperature": 0, "max_tokens": 6000, "usage": {"include": True},
                       "messages": [{"role": "user", "content": inline}]}).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions", data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        resp = json.loads(r.read())
    with _LEDGER_LOCK:  # re-read inside the lock so parallel judges do not overwrite each other
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        month, spent = _spend_month()
        cost = float(resp.get("usage", {}).get("cost", 0) or 0)
        _RUN["spent"] += cost
        LEDGER.write_text(json.dumps({month: spent + cost}))
    return resp["choices"][0]["message"].get("content") or ""


def _judge(prompt, cwd, i):
    if JUDGE_BACKEND == "openrouter":
        return _run_openrouter(prompt, cwd, OR_MODELS[i % len(OR_MODELS)])
    return _run_claude(prompt, cwd)


def _parse_json_block(text):
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        raise ValueError("judge did not return JSON: " + text[:300])
    return json.loads(m.group(0))


def get_assert(output, context):
    vars_ = context.get("vars", {})
    skill = vars_["skill"]
    transcript = vars_["transcript"]
    gt_name = vars_["gt"]
    # gt_dir lets a case point at evals/gt-web/ (web-harvested, third-party
    # ground truth) instead of the default evals/gt/ (hand-authored).
    gt_dir = vars_.get("gt_dir", "gt")
    case = context.get("test", {}).get("description", "case")
    judges = int(os.environ.get("EVAL_JUDGES", str(len(OR_MODELS) if JUDGE_BACKEND == "openrouter" else 3)))
    run_dir = Path(os.environ.get("EVAL_RUN_DIR", str(REPO_ROOT / "evals" / "runs" / "adhoc")))
    out_dir = run_dir / "output" / skill / case
    gt_file = REPO_ROOT / "evals" / gt_dir / gt_name
    transcript_file = REPO_ROOT / "evals" / "transcripts" / f"{transcript}.txt"
    verdicts_dir = run_dir / "verdicts"
    verdicts_dir.mkdir(parents=True, exist_ok=True)

    if not gt_file.exists():
        return {
            "pass": False, "score": 0,
            "reason": f"No ground truth at evals/{gt_dir}/{gt_name} -- see evals/gt/README.md",
        }

    gt_text = gt_file.read_text()
    gt_name_in_scratch = "gt" + (gt_file.suffix or ".txt")

    marker_count = 0
    for f in out_dir.glob("*"):
        if f.is_file():
            try:
                marker_count += len(re.findall(r"TBC|TBD|TBA|\[\[TBD", f.read_text(errors="ignore")))
            except Exception:
                pass

    prompt_template = JUDGE_PROMPT_TEMPLATE.format(gt_name=gt_name_in_scratch)
    samples = []
    for i in range(judges):
        scratch = Path(f"/tmp/skill-eval-{skill}-{case}-judge-{i}")
        if scratch.exists():
            shutil.rmtree(scratch)
        (scratch / "output").mkdir(parents=True)
        for f in out_dir.glob("*"):
            if f.is_file():
                shutil.copy(f, scratch / "output" / f.name)
        (scratch / gt_name_in_scratch).write_text(_shuffle_gt(gt_text, seed=i))
        if transcript_file.exists():
            shutil.copy(transcript_file, scratch / "transcript.txt")
        try:
            raw = _judge(prompt_template, scratch, i)
            parsed = _parse_json_block(raw)
        except (ValueError, OSError) as e:
            raw = f"{type(e).__name__}: {e}"
            parsed = {"fields": {}, "_error": raw[:500]}
        samples.append(parsed)
        (verdicts_dir / f"{skill}-{case}-judge-{i}.json").write_text(json.dumps(parsed, indent=2))

    if not any(s.get("fields") for s in samples):
        errors = "; ".join(s.get("_error", "")[:120] for s in samples)
        return {"pass": False, "score": 0, "reason": f"All judges failed or returned no fields: {errors}"}

    all_fields = set()
    for s in samples:
        all_fields.update(s.get("fields", {}).keys())

    agg = {}
    low_agreement = []
    for field in sorted(all_fields):
        verdicts = [s.get("fields", {}).get(field, {}).get("verdict") for s in samples]
        verdicts = [v for v in verdicts if v]
        if not verdicts:
            continue
        counts = {}
        for v in verdicts:
            counts[v] = counts.get(v, 0) + 1
        winner, top = max(counts.items(), key=lambda kv: kv[1])
        agreement = top / len(verdicts)
        if len(set(verdicts)) > 1:
            low_agreement.append(field)
        derivable_votes = [
            s.get("fields", {}).get(field, {}).get("derivable")
            for s in samples
            if s.get("fields", {}).get(field, {}).get("verdict") == "missing"
        ]
        derivable = any(d is True for d in derivable_votes)
        agg[field] = {"verdict": winner, "votes": counts, "agreement": agreement, "derivable": derivable}

    total = len(agg) or 1
    present = sum(1 for f in agg.values() if f["verdict"] == "present")
    missing = [f for f, v in agg.items() if v["verdict"] == "missing"]
    derivable_miss = sum(1 for f in missing if agg[f]["derivable"])
    extra = sum(1 for f in agg.values() if f["verdict"] == "extra")
    wrong = sum(1 for f in agg.values() if f["verdict"] == "wrong")
    exact_match = sum(1 for f in agg.values() if f["agreement"] >= 0.999) / total

    named_scores = {
        "field_recall": round(present / total, 3),
        "derivable_miss_rate": round(derivable_miss / total, 3),
        "hallucination_rate": round(extra / (present + extra + 1e-9), 3),
        "judge_agreement": round(exact_match, 3),
        "unresolved_marker_count": marker_count,
    }

    summary = (
        f"{total} GT fields: {present} present, {len(missing)} missing "
        f"({derivable_miss} derivable), {wrong} wrong, {extra} extra"
    )
    lines = [
        f"# Gaps: {skill} / {case}", "",
        summary,
        (f"Judge contract: {judges} samples via openrouter, models {','.join(OR_MODELS)}, rubric v{RUBRIC_VERSION}"
         if JUDGE_BACKEND == "openrouter" else
         f"Judge contract: {judges}x claude-cli (subscription, model {EVAL_MODEL}), rubric v{RUBRIC_VERSION}"),
        "",
    ]
    for field, v in agg.items():
        flag = " **LOW_AGREEMENT**" if field in low_agreement else ""
        lines.append(f"- **{field}**: {v['verdict']}{flag} (votes: {v['votes']}, derivable={v['derivable']})")
    (run_dir / f"gaps-{skill}-{case}.md").write_text("\n".join(lines))

    return {
        "pass": True,  # descriptive assertion, not a hard pass/fail gate
        "score": named_scores["field_recall"],
        "reason": summary,
        "namedScores": named_scores,
    }


if __name__ == "__main__":
    # Manual smoke test: python3 judge.py <output-text-file> <context.json>
    out_text = Path(sys.argv[1]).read_text()
    ctx = json.loads(Path(sys.argv[2]).read_text())
    print(json.dumps(get_assert(out_text, ctx), indent=2))
