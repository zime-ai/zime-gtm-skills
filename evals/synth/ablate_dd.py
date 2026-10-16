#!/usr/bin/env python3
"""Ablation: what does the deep-discovery skill add over the plain model?

Scores three variants on the planted-fact cases by parsing statuses, with no
LLM judge, so nobody's opinion decides the result.

  bare   : the model gets only the 8 dimension names.
  rubric : bare plus references/rubric.md pasted in (the definitions).
  skill  : the installed skill, run as /deep-discovery.

Needs the cases from evals/synth/deep_discovery.py. Usage, from the repo root:
  python3 evals/synth/ablate_dd.py [repeats]
Results go to evals/runs/ablate-dd-<time>.json (gitignored).
"""
import json, os, re, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).parent))
import importlib
dd = importlib.import_module("deep_discovery_b" if os.environ.get("DD_BANK") == "B" else "deep_discovery")  # noqa: E402

MODEL = "claude-haiku-5-5"
NAMES = ["Pain & business impact", "Current state & tooling", "Trigger (why now)", "Desired outcome & success criteria",
         "Decision process & stakeholders", "Budget & timeline", "Procurement & buying path", "Competitive landscape"]
EXPECT = {"full": "Covered", "partial": "Partial", "absent": "Missed"}
FORMAT = ("Output exactly one line per dimension, in this form, then stop:\n"
          "**N. Name** — Status\nwhere Status is Covered, Partial or Missed. Score dimensions 1 to 8 only.")
BARE = ("Read the sales discovery call transcript at ./transcript.txt. Score the call on these dimensions: "
        + "; ".join(f"{i}. {n}" for i, n in enumerate(NAMES, 1)) + ".\n" + FORMAT)


def prompt_for(variant):
    if variant == "bare":
        return BARE
    if variant == "rubric":
        return BARE + "\n\nUse these definitions:\n\n" + (ROOT / "skills/deep-discovery/references/rubric.md").read_text()
    return "/deep-discovery ./transcript.txt\n\nScore dimensions 1 to 8 only. " + FORMAT.split("\n", 1)[1]


def run(job):
    variant, name, levels, rep = job
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        (d / "transcript.txt").write_text(dd.render(levels))
        if variant.startswith("skill"):
            (d / ".claude/skills").mkdir(parents=True)
            shutil.copytree(ROOT / "skills/deep-discovery", d / ".claude/skills/deep-discovery")
            if variant == "skill_old":  # the committed version, before this working-tree edit
                old = subprocess.run(["git", "show", "HEAD:skills/deep-discovery/SKILL.md"], cwd=ROOT,
                                     capture_output=True, text=True, check=True).stdout
                (d / ".claude/skills/deep-discovery/SKILL.md").write_text(old)
        p = subprocess.run(["claude", "-p", prompt_for(variant), "--model", MODEL, "--setting-sources", "project",
                            "--dangerously-skip-permissions"], cwd=d, capture_output=True, text=True, timeout=600)
    got = {}
    for m in re.finditer(r"(?m)^\W*([1-8])\.[^\n]*?[—–-]+\s*\**\s*(Covered|Partial|Missed|Unclear)\b", p.stdout):
        got.setdefault(int(m[1]), "Missed" if m[2] == "Unclear" else m[2])
    return {"variant": variant, "case": name, "rep": rep, "got": got, "levels": levels, "raw_len": len(p.stdout)}


def main():
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    variants = sys.argv[2].split(",") if len(sys.argv) > 2 else ["bare", "rubric", "skill"]
    jobs = [(v, n, lv, r) for v in variants for n, _, lv in dd.cases() for r in range(reps)]
    with ThreadPoolExecutor(6) as ex:
        res = list(ex.map(run, jobs))
    out = ROOT / "evals/runs" / f"ablate-dd-{os.environ.get('DD_BANK', 'A')}-{time.strftime('%Y%m%d-%H%M%S')}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(res, indent=1))
    for v in variants:
        m = metrics(res, v)
        print(f"{v:9s} exact={m['exact']:.3f} parsed={m['parsed']:.3f} by_level={m['by_level']} "
              f"false_faults_on_all_full={m['false_faults']:.3f} clean_twin_flips={m['flips']}/{m['twins']}")
    print("saved", out)


def metrics(res, v):
    # JSON turns the integer dimension keys into strings, so normalise both
    res = [{**r, "levels": {int(k): x for k, x in r["levels"].items()},
            "got": {int(k): x for k, x in r["got"].items()}} for r in res]
    rows = [r for r in res if r["variant"] == v]
    cells = [(r, d) for r in rows for d in dd.DIMS]
    by = {}
    for lvl in EXPECT:
        c = [(r, d) for r, d in cells if r["levels"][d] == lvl]
        by[lvl] = round(sum(r["got"].get(d) == EXPECT[lvl] for r, d in c) / len(c), 3)
    full = [r for r in rows if r["case"] == "synth-dd-all-full"]
    twins = [r for r in rows if "twin-no-" in r["case"]]
    flips = sum(r["got"].get(int(r["case"][-1])) == "Missed" and
                all(r["got"].get(d) == "Covered" for d in dd.DIMS if d != int(r["case"][-1])) for r in twins)
    return {"exact": sum(r["got"].get(d) == EXPECT[r["levels"][d]] for r, d in cells) / len(cells),
            "parsed": sum(d in r["got"] for r, d in cells) / len(cells), "by_level": by,
            "false_faults": sum(r["got"].get(d) != "Covered" for r in full for d in dd.DIMS) / max(1, len(full) * 8),
            "flips": flips, "twins": len(twins),
            "failed_cells": sorted({(r["case"], d) for r, d in cells if r["got"].get(d) != EXPECT[r["levels"][d]]})}


if __name__ == "__main__":
    main()
