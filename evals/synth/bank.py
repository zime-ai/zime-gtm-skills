#!/usr/bin/env python3
"""Planted-fact test banks for any skill that scores dimensions as Covered / Partial / Missed.

A bank is a spec (see evals/synth/banks/): a call is assembled from one module per
dimension at a known level (full, partial, absent), so the answer key is true by
construction, with no model giving an opinion. Twin cases remove exactly one fact.
Scoring parses the skill's printed statuses and compares them with the plant.

Run from the repo root:
  python3 evals/synth/bank.py <skill> <bank A|B> <reps> <variants>
variants: skill (installed skill), skill_old (the committed SKILL.md), rubric, bare.
"""
import importlib, json, os, random, re, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).parent))
MODEL = "claude-haiku-5-5"
EXPECT = {"full": "Covered", "partial": "Partial", "absent": "Missed"}


def load(skill, bank):
    return importlib.import_module(f"banks.{skill.replace('-', '_')}").BANKS[bank]


def render(spec, levels):
    lines = list(spec["open"])
    for d in spec["dims"]:
        lines += spec["modules"][d][levels[d]]
    lines += spec["close"]
    out = list(spec["header"]) + ["[Synthetic transcript for evaluation only. No real company or person]", ""]
    t = 1
    for who, text in lines:
        out.append(f"{t // 60:02d}:{t % 60:02d} {who}: {text}\n")
        t += 14 + len(text) // 9
    return "\n".join(out)


def key(spec, levels):
    out = ["# Planted-fact answer key, true by construction", ""]
    for d, name in spec["dims"].items():
        lvl = levels[d]
        out += [f"## {name}", f"Expected status: {EXPECT[lvl]}"]
        buyer = " ".join(t for w, t in spec["modules"][d][lvl] if w == spec["speaker"])
        out += [f'Planted evidence: "{buyer}"' if lvl != "absent" and buyer else
                "Planted evidence: none. Nothing in the call addresses this dimension.", ""]
    return "\n".join(out)


def cases(spec, skill):
    full = {d: "full" for d in spec["dims"]}
    yield f"synth-{skill}-all-full", dict(full)
    yield f"synth-{skill}-all-partial", {d: "partial" for d in spec["dims"]}
    yield f"synth-{skill}-all-absent", {d: "absent" for d in spec["dims"]}
    for d in spec["dims"]:
        yield f"synth-{skill}-twin-no-{d}", {**full, d: "absent"}
    rng = random.Random(7)
    for i in range(1, 7):
        yield f"synth-{skill}-mixed-{i}", {d: rng.choice(["full", "partial", "absent"]) for d in spec["dims"]}


def leak_audit(spec):
    """(dimension, term, other dimension) for any planted detail that shows up in another dimension's module."""
    bad = []
    for d, terms in spec["leak_terms"].items():
        for o in spec["dims"]:
            if o != d:
                text = " ".join(t for lv in spec["modules"][o].values() for _, t in lv)
                bad += [(d, t, o) for t in terms if t.lower() in text.lower()]
    return bad


def example_collisions(spec, skill):
    """Planted details that also appear in the skill's own text. The skill could then 'find' them from its examples."""
    own = " ".join(f.read_text() for f in (ROOT / "skills" / skill).rglob("*.md")).lower()
    return sorted(t for ts in spec["leak_terms"].values() for t in ts if t.lower() in own)


def parse(text, spec):
    got = {}
    for line in text.split("\n"):
        m = re.search(r"[—–-]+\s*\**\s*(Covered|Partial|Missed|Unclear)\b", line)
        if not m:
            continue
        head = line[:m.start()].lower()
        for d, kws in spec["match"].items():
            if d not in got and (re.match(rf"\W*{d}\.", head) or any(k in head for k in kws)):
                got[d] = "Missed" if m[1] == "Unclear" else m[1]
                break
    return got


def prompt_for(variant, spec, skill):
    names = "; ".join(f"{d}. {n}" for d, n in spec["dims"].items())
    fmt = ("Output exactly one line per dimension, in this form, then stop:\n**N. Name** — Status\n"
           f"where Status is Covered, Partial or Missed. Score dimensions 1 to {len(spec['dims'])} only.")
    bare = f"Read the sales call transcript at ./transcript.txt. Score the call on these dimensions: {names}.\n{fmt}"
    if variant == "bare":
        return bare
    if variant == "rubric":
        return bare + "\n\nUse these definitions:\n\n" + (ROOT / f"skills/{skill}/references/rubric.md").read_text()
    return (f"/{skill} ./transcript.txt\n\nScore dimensions 1 to {len(spec['dims'])} only. " + fmt.split("\n", 1)[1])


def run(job):
    skill, bank, variant, name, levels, rep = job
    spec = load(skill, bank)
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        (d / "transcript.txt").write_text(render(spec, levels))
        if variant.startswith("skill"):
            (d / ".claude/skills").mkdir(parents=True)
            shutil.copytree(ROOT / "skills" / skill, d / f".claude/skills/{skill}")
            if variant == "skill_old":
                old = subprocess.run(["git", "show", f"HEAD:skills/{skill}/SKILL.md"], cwd=ROOT,
                                     capture_output=True, text=True, check=True).stdout
                (d / f".claude/skills/{skill}/SKILL.md").write_text(old)
        p = subprocess.run(["claude", "-p", prompt_for(variant, spec, skill), "--model", MODEL,
                            "--setting-sources", "project", "--dangerously-skip-permissions"],
                           cwd=d, capture_output=True, text=True, timeout=600)
    return {"variant": variant, "case": name, "rep": rep, "levels": levels, "got": parse(p.stdout, spec)}


def metrics(res, v, spec):
    res = [{**r, "levels": {int(k): x for k, x in r["levels"].items()},
            "got": {int(k): x for k, x in r["got"].items()}} for r in res if r["variant"] == v]
    dims = list(spec["dims"])
    cells = [(r, d) for r in res for d in dims]
    by = {}
    for lvl in EXPECT:
        c = [(r, d) for r, d in cells if r["levels"][d] == lvl]
        by[lvl] = round(sum(r["got"].get(d) == EXPECT[lvl] for r, d in c) / len(c), 3) if c else None
    full = [r for r in res if r["case"].endswith("all-full")]
    twins = [r for r in res if "twin-no-" in r["case"]]
    tw = lambda r: int(r["case"].rsplit("-", 1)[1])  # noqa: E731
    return {"exact": sum(r["got"].get(d) == EXPECT[r["levels"][d]] for r, d in cells) / len(cells),
            "parsed": sum(d in r["got"] for r, d in cells) / len(cells), "by_level": by,
            "false_faults": sum(r["got"].get(d) != "Covered" for r in full for d in dims) / max(1, len(full) * len(dims)),
            "flips": sum(r["got"].get(tw(r)) == "Missed" and all(r["got"].get(d) == "Covered" for d in dims if d != tw(r))
                         for r in twins), "twins": len(twins),
            "failed_cells": sorted({(r["case"], d) for r, d in cells if r["got"].get(d) != EXPECT[r["levels"][d]]})}


def main():
    skill, bank = sys.argv[1], sys.argv[2]
    reps = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    variants = sys.argv[4].split(",") if len(sys.argv) > 4 else ["skill"]
    spec = load(skill, bank)
    leaks = leak_audit(spec)
    assert not leaks, f"modules leak across dimensions: {leaks}"
    clash = example_collisions(spec, skill)
    assert not clash, f"planted details also appear in the skill's own text: {clash}"
    jobs = [(skill, bank, v, n, lv, r) for v in variants for n, lv in cases(spec, skill) for r in range(reps)]
    with ThreadPoolExecutor(6) as ex:
        res = list(ex.map(run, jobs))
    out = ROOT / "evals/runs" / f"bank-{skill}-{bank}-{time.strftime('%Y%m%d-%H%M%S')}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(res, indent=1))
    for v in variants:
        m = metrics(res, v, spec)
        print(f"{v:9s} exact={m['exact']:.3f} parsed={m['parsed']:.3f} by_level={m['by_level']} "
              f"false_faults={m['false_faults']:.3f} clean_twin_flips={m['flips']}/{m['twins']}")
    print("saved", out)


if __name__ == "__main__":
    main()
