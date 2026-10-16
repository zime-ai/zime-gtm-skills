#!/usr/bin/env python3
"""Referee for the improvement loop. A plain script, not an agent: its verdict is final.

Usage: python3 scripts/referee.py <skill> [--baseline]
  default     test the working-tree skill, print ACCEPT / REJECT / ESCALATE
  --baseline  test the working-tree skill and store its scores as the new baseline

Scores come from planted-fact banks (evals/synth/), where the answer key is true by
construction. Bank A is the dev bank, and its failures are printed so the author can
fix them. Bank B is held out: only its aggregate numbers are printed.
"""
import json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals/synth"))
BASELINE = ROOT / "evals/loop/baseline.json"
REPS = int(os.environ.get("REFEREE_REPS", "2"))
NOISE = 0.02          # a held-out change smaller than this is not an improvement
MIN_GAIN = 0.01       # needed on held-out to call a change an improvement
BAR = 0.98            # a skill at or above this held-out score is left alone
MAX_DIFF_LINES = 300
MAX_SKILL_LINES = 500
SKILLS = {p.stem.replace("_", "-") for p in (ROOT / "evals/synth/banks").glob("*.py") if p.stem != "__init__"}  # skills with planted banks


def bank_scores(skill, bank):
    p = subprocess.run([sys.executable, "-I", str(ROOT / "evals/synth/bank.py"), skill, bank, str(REPS), "skill"],
                       cwd=ROOT, capture_output=True, text=True)
    m = re.search(r"saved (\S+)", p.stdout)
    if not m:
        sys.exit(f"ESCALATE: bank {bank} run failed: {(p.stderr or p.stdout)[-300:]}")
    import bank as bank_mod
    return bank_mod.metrics(json.loads(Path(m[1]).read_text()), "skill", bank_mod.load(skill, bank))


def changed_files():
    out = subprocess.run(["git", "diff", "--name-only", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout
    return [f for f in out.split("\n") if f]


def pick():
    """Next target. A skill with a bank but no baseline is measured first. Otherwise the weakest skill below the bar."""
    base = json.loads(BASELINE.read_text()) if BASELINE.exists() else {}
    for sk in sorted(SKILLS):
        if sk not in base:
            return f"BASELINE:{sk}"
    weak = sorted((base[sk]["B"]["exact"], sk) for sk in SKILLS if base[sk]["B"]["exact"] < BAR)
    return f"TARGET:{weak[0][1]}" if weak else "NONE"


def main():
    if sys.argv[1] == "--pick":
        print(pick())
        return
    skill = sys.argv[1]
    if skill not in SKILLS:
        sys.exit(f"ESCALATE: no planted bank for {skill}")
    sf = ROOT / "skills" / skill / "SKILL.md"
    lines = len(sf.read_text().splitlines())
    A, B = bank_scores(skill, "A"), bank_scores(skill, "B")
    now = {"A": {k: A[k] for k in ("exact", "false_faults", "flips")},
           "B": {k: B[k] for k in ("exact", "false_faults", "flips")}, "skill_lines": lines}
    (ROOT / "evals/loop/state").mkdir(parents=True, exist_ok=True)
    (ROOT / "evals/loop/state/last_run.json").write_text(json.dumps({"skill": skill, **now, "A_failed": A["failed_cells"]}))
    print("dev bank A:", json.dumps(now["A"]), "failed cells:", A["failed_cells"][:12])
    print("held-out B:", json.dumps(now["B"]))
    if "--baseline" in sys.argv:
        base = json.loads(BASELINE.read_text()) if BASELINE.exists() else {}
        base[skill] = now
        BASELINE.write_text(json.dumps(base, indent=1))
        print("baseline stored")
        return
    base = json.loads(BASELINE.read_text()).get(skill)
    if not base:
        sys.exit("ESCALATE: no baseline stored, run with --baseline on a clean checkout")
    why = []
    bad = [f for f in changed_files() if not f.startswith(f"skills/{skill}/")]
    if bad:
        why.append(f"touched protected paths: {bad[:3]}")
    stat = subprocess.run(["git", "diff", "--numstat", "HEAD", "--", f"skills/{skill}"], cwd=ROOT,
                          capture_output=True, text=True).stdout.split("\n")
    if sum(int(a) + int(b) for a, b, *_ in (l.split("\t") for l in stat if l)) > MAX_DIFF_LINES:
        why.append("diff over 300 lines")
    if lines > MAX_SKILL_LINES:
        why.append("SKILL.md over 500 lines")
    if subprocess.run(["./validate-skills.sh"], cwd=ROOT, capture_output=True).returncode != 0:
        why.append("validate-skills.sh failed")
    if B["exact"] >= 0.999:
        print("ESCALATE: perfect held-out score, check for a leak before accepting")
        return
    gain = B["exact"] - base["B"]["exact"]
    simpler = lines < base["skill_lines"]
    if gain < -NOISE:
        why.append(f"held-out exact fell {gain:+.3f}")
    elif gain < MIN_GAIN and not (abs(gain) <= NOISE and simpler):
        why.append(f"held-out gain {gain:+.3f} below {MIN_GAIN} and not a simplification")
    if B["false_faults"] > base["B"]["false_faults"]:
        why.append("more false faults on a fully covered call")
    if B["flips"] < base["B"]["flips"] - 1:
        why.append("fewer clean single-fact flips")
    if A["exact"] < base["A"]["exact"] - NOISE:
        why.append("dev bank exact fell")
    print("REJECT: " + "; ".join(why) if why else "ACCEPT")


if __name__ == "__main__":
    main()
