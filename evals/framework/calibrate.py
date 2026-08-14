#!/usr/bin/env python3
"""
The bias check the judge panel alone cannot do: Cohen's kappa between the
judge's majority verdict and a hand-labeled ground truth, per EVALS.md's
"multi-sampling fixes variance, not bias" limitation.

Multiple same-family judge samples reduce scatter; only a human comparison
catches a systematic lean. Run this whenever you add a case, and whenever the
judge model/rubric changes (RUBRIC_VERSION bump in judge.py).

Usage: python3 evals/framework/calibrate.py <skill> <case> <run-dir>

Requires evals/labels/<skill>-<case>.json: {"field name": "present|missing|wrong|extra", ...}
hand-labeled by you (or ideally someone who didn't write the skill), ~10+ fields.
"""
import json
import sys
from collections import Counter
from pathlib import Path


def cohens_kappa(pairs):
    labels = sorted(set(a for a, b in pairs) | set(b for a, b in pairs))
    n = len(pairs)
    po = sum(1 for a, b in pairs if a == b) / n
    pa = Counter(a for a, b in pairs)
    pb = Counter(b for a, b in pairs)
    pe = sum((pa[l] / n) * (pb[l] / n) for l in labels)
    if pe >= 1:
        return 1.0
    return (po - pe) / (1 - pe)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    skill, case, run_dir = sys.argv[1], sys.argv[2], Path(sys.argv[3])

    label_file = Path("evals/labels") / f"{skill}-{case}.json"
    if not label_file.exists():
        sys.exit(f"No labels at {label_file} -- hand-label ~10 fields first (see evals/framework/README.md)")
    human = json.loads(label_file.read_text())

    judge_verdicts = {}
    verdict_files = sorted((run_dir / "verdicts").glob(f"{skill}-{case}-judge-*.json"))
    if not verdict_files:
        sys.exit(f"No verdicts under {run_dir}/verdicts/ -- run eval.sh {skill} first")
    for f in verdict_files:
        sample = json.loads(f.read_text())
        for field, v in sample.get("fields", {}).items():
            judge_verdicts.setdefault(field, []).append(v.get("verdict"))

    pairs = []
    confusion = Counter()
    for field, human_label in human.items():
        votes = judge_verdicts.get(field, [])
        if not votes:
            print(f"  (no judge verdict for '{field}', skipping)")
            continue
        majority = Counter(votes).most_common(1)[0][0]
        pairs.append((human_label, majority))
        confusion[(human_label, majority)] += 1

    if not pairs:
        sys.exit("No overlapping fields between labels and judge verdicts.")

    kappa = cohens_kappa(pairs)
    print(f"Cohen's kappa (judge vs human), {skill}/{case}: {kappa:.3f}")
    print("(<0.4 weak, 0.4-0.6 moderate, 0.6-0.8 substantial, >0.8 near-perfect --")
    print(" re-tune JUDGE_PROMPT_TEMPLATE in judge.py on whichever field the confusion below clusters on)")
    print()
    print("Confusion (human -> judge majority):")
    for (h, j), n in sorted(confusion.items(), key=lambda kv: -kv[1]):
        flag = "" if h == j else "  <-- disagreement"
        print(f"  {h:>10} -> {j:<10} x{n}{flag}")


if __name__ == "__main__":
    main()
