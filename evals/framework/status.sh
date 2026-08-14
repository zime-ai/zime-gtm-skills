#!/usr/bin/env python3
"""Per-skill status from evals/runs.jsonl + evals/amendments.jsonl:
last run, last field_recall, delta vs the previous run for that skill, and
count of pending amendments. Not a 7d/30d trend table -- there isn't enough
run history yet for one to mean anything (see the plan this came from).

Usage: evals/framework/status.sh
"""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RUNS_LOG = REPO_ROOT / "evals" / "runs.jsonl"
LEDGER = REPO_ROOT / "evals" / "amendments.jsonl"


def read_jsonl(path):
    if not path.exists():
        return []
    rows = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            print(f"WARN: skipping malformed line in {path.name}: {line[:80]}", file=sys.stderr)
    return rows


def latest_amendments(rows):
    # amend.sh appends a slim {id, status, note, recorded_at} row -- it
    # doesn't repeat 'skill'/'proposal' from the original pending row. Merge
    # rather than replace, or deciding an amendment erases which skill it
    # belonged to.
    merged = {}
    for row in rows:
        merged.setdefault(row["id"], {}).update(row)
    return merged


def main():
    runs = read_jsonl(RUNS_LOG)
    if not runs:
        print(f"No runs recorded yet ({RUNS_LOG.relative_to(REPO_ROOT)} doesn't exist or is empty).")
        return

    amendments = read_jsonl(LEDGER)
    latest = latest_amendments(amendments)
    pending_by_skill = {}
    for row in latest.values():
        if row.get("status") == "pending" and row.get("skill"):
            pending_by_skill[row["skill"]] = pending_by_skill.get(row["skill"], 0) + 1

    by_skill = {}
    for row in runs:
        by_skill.setdefault(row["skill"], []).append(row)

    for skill, rows in sorted(by_skill.items()):
        rows.sort(key=lambda r: r["recorded_at"])
        last = rows[-1]
        prev = rows[-2] if len(rows) > 1 else None
        line = f"{skill}: last run {last['run_id']} ({last['case']})  field_recall={last['field_recall']:.3f}"
        if prev:
            delta = last["field_recall"] - prev["field_recall"]
            arrow = "▲" if delta > 0 else ("▼" if delta < 0 else "=")
            line += f"  ({arrow} {delta:+.3f} vs {prev['run_id']})"
        pending = pending_by_skill.get(skill, 0)
        if pending:
            line += f"  [{pending} pending amendment(s)]"
        print(line)


if __name__ == "__main__":
    main()
