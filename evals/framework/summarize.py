#!/usr/bin/env python3
"""Print the named-score scoreboard for a promptfoo results.json, averaged
across test cases, with an optional diff against a baseline results.json.
Also appends one row per test case to evals/runs.jsonl (the run log --
see EVALS.md's Tier 0).

Usage: python3 evals/framework/summarize.py <results.json> [baseline.json] [skill]
"""
import datetime
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RUNS_LOG = REPO_ROOT / "evals" / "runs.jsonl"

# A malformed row (missing field, wrong type) can't poison later reads by
# status.sh -- validate before appending, same spirit as judge.py's own
# named-score contract.
REQUIRED_FIELDS = {
    "run_id": str, "skill": str, "case": str, "rubric_version": str,
    "judges": int, "field_recall": float, "derivable_miss_rate": float,
    "hallucination_rate": float, "judge_agreement": float,
    "recorded_at": str,
}


def load_scores(path):
    data = json.loads(Path(path).read_text())
    results = data["results"]["results"]
    agg = {}
    for r in results:
        for k, v in (r.get("namedScores") or {}).items():
            agg.setdefault(k, []).append(v)
    return {k: sum(v) / len(v) for k, v in agg.items()}, len(results), results


def case_name(r):
    return r.get("testCase", {}).get("description") or r.get("description") or "case"


def rubric_version(r):
    grading = r.get("gradingResult") or {}
    return str((r.get("namedScores") or {}).get("rubric_version") or grading.get("rubric_version") or "1")


def judges_count():
    return int(os.environ.get("EVAL_JUDGES", "3"))


def validate_row(row):
    for field, typ in REQUIRED_FIELDS.items():
        if field not in row:
            raise ValueError(f"run log row missing '{field}': {row}")
        if not isinstance(row[field], typ):
            raise ValueError(f"run log row field '{field}' expected {typ.__name__}, got {type(row[field]).__name__}: {row}")


def append_run_log(results, skill, run_id):
    recorded_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    rows = []
    for r in results:
        scores = r.get("namedScores") or {}
        if "field_recall" not in scores:
            continue  # not a judge.py-graded result -- skip rather than write a partial row
        row = {
            "run_id": run_id,
            "skill": skill,
            "case": case_name(r),
            "rubric_version": rubric_version(r),
            "judges": judges_count(),
            "field_recall": float(scores["field_recall"]),
            "derivable_miss_rate": float(scores.get("derivable_miss_rate", 0.0)),
            "hallucination_rate": float(scores.get("hallucination_rate", 0.0)),
            "judge_agreement": float(scores.get("judge_agreement", 0.0)),
            "recorded_at": recorded_at,
        }
        validate_row(row)
        rows.append(row)
    if not rows:
        return
    with RUNS_LOG.open("a") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    print(f"-> {len(rows)} row(s) appended to {RUNS_LOG.relative_to(REPO_ROOT)}")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    run_path = sys.argv[1]
    baseline_path = sys.argv[2] if len(sys.argv) > 2 else None
    skill = sys.argv[3] if len(sys.argv) > 3 else "unknown"

    scores, n, results = load_scores(run_path)
    baseline = {}
    if baseline_path and Path(baseline_path).exists():
        baseline, _, _ = load_scores(baseline_path)

    print(f"{n} test case(s)")
    for k, v in scores.items():
        line = f"  {k:<24} {v:.3f}"
        if k in baseline:
            delta = v - baseline[k]
            arrow = "▲" if delta > 0 else ("▼" if delta < 0 else "=")
            line += f"   (baseline {baseline[k]:.3f}  {arrow} {delta:+.3f})"
        print(line)

    run_id = Path(run_path).parent.name
    append_run_log(results, skill, run_id)


if __name__ == "__main__":
    main()
