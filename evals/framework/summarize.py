#!/usr/bin/env python3
"""Print the named-score scoreboard for a promptfoo results.json, averaged
across test cases, with an optional diff against a baseline results.json.

Usage: python3 evals/framework/summarize.py <results.json> [baseline.json]
"""
import json
import sys
from pathlib import Path


def load_scores(path):
    data = json.loads(Path(path).read_text())
    results = data["results"]["results"]
    agg = {}
    for r in results:
        for k, v in (r.get("namedScores") or {}).items():
            agg.setdefault(k, []).append(v)
    return {k: sum(v) / len(v) for k, v in agg.items()}, len(results)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    run_path = sys.argv[1]
    baseline_path = sys.argv[2] if len(sys.argv) > 2 else None

    scores, n = load_scores(run_path)
    baseline = {}
    if baseline_path and Path(baseline_path).exists():
        baseline, _ = load_scores(baseline_path)

    print(f"{n} test case(s)")
    for k, v in scores.items():
        line = f"  {k:<24} {v:.3f}"
        if k in baseline:
            delta = v - baseline[k]
            arrow = "▲" if delta > 0 else ("▼" if delta < 0 else "=")
            line += f"   (baseline {baseline[k]:.3f}  {arrow} {delta:+.3f})"
        print(line)


if __name__ == "__main__":
    main()
