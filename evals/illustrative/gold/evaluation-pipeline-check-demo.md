# Gold label: evaluation-pipeline-check-demo.csv, scored against `evaluation-pipeline-check`

Computed by hand from `references/rubric.md`'s exact six-check rubric and
`evals/illustrative/BRIEF-evaluation-pipeline-check.md`'s construction, against
today = 2026-08-17. This rubric is deterministic — every flag below is a fact
derived from the export's own medians (including grouped medians per check 4), not a judgment call.

## Expected output table (flagged deals first, most flags first; clean deals second)

| Deal | Flags | Evidence | Suggested action |
|---|---|---|---|
| Soylent Industries | 3 | days_in_stage=35 (group median 20, high-value group); security_review=(empty), deal_value=180000 (above median 120000); last_activity_date=2026-07-20, 28 days idle (median gap 4.5) | Push for security review kickoff, get eval end-date reconfirmed, re-engage stalled deal |
| Umbrella Corp | 2 | days_in_stage=70 (group median 21.5, low-value group); last_activity_date=2026-08-01, 16 days idle (median gap 4.5) | Re-engage immediately, evaluation has drifted well past group norm |
| Wayne Industries | 2 | days_in_stage=25 (group median 21.5, low-value group); last_activity_date=2026-06-20, 58 days idle (median gap 4.5) | Likely dead/stalled eval, confirm still active or disqualify |
| Stark Corp | 2 | champion=(empty); security_review=Not started, deal_value=200000 (above median 120000) | Get a named technical champion, kick off security review given deal size |
| Horizon Tech | 2 | success_criteria=(empty); last_activity_date=2026-08-12, 5 days idle (median gap 4.5) | Define pass/fail criteria, quick check-in to prevent stall |
| Initech Holdings | 1 | success_criteria=(empty) | Get success criteria documented before eval progresses further |
| Acme Systems | Clean | — | — |
| Globex Corp | Clean | — | — |

Closing lines expected:
1. **"6 of 8 deals in Evaluation flagged"**
2. The single most common flag is **"stalled"** — present on 4 of the 6 flagged
   deals (Soylent, Umbrella, Wayne, Horizon).

## Median calculations (verified from 8 rows)

- **deal_value export median**: (110000 + 130000) / 2 = 120000
  - High-value group (≥ 120k): Acme (150k), Soylent (180k), Stark (200k), Horizon (130k)
  - Low-value group (< 120k): Globex (80k), Initech (100k), Umbrella (110k), Wayne (95k)

- **days_in_stage (grouped by deal value)**:
  - High-value group values: 20, 35, 12, 20 → sorted: 12, 20, 20, 35 → median = 20
  - Low-value group values: 15, 18, 70, 25 → sorted: 15, 18, 25, 70 → median = 21.5
  - Flagged (exceeds group median): Soylent (35 > 20), Umbrella (70 > 21.5), Wayne (25 > 21.5)

- **security_review (check 5)**: Flag if empty/not-started AND deal_value > export median
  - Above-median deals: Acme (In Progress, clean), Soylent (empty, flag), Stark (Not started, flag), Horizon (In Progress, clean)
  - Below-median deals: Globex (Not started, but below median so clean per rubric)

- **last_activity_date gaps** (sorted): 1, 2, 3, 4, 5, 16, 28, 58 days → median = 4.5 days
  - Flagged (gap > 4.5): Umbrella (16), Soylent (28), Wayne (58), Horizon (5)

## The traps (findings a correct run must get right)

1. **Grouped median logic for check 4**: Umbrella and Wayne must be compared to
   the low-value group median (21.5), not the export-wide median. Both exceed
   21.5 and flag correctly. Soylent must be compared to the high-value group
   median (20) and exceeds it. Acme and Horizon are both 20 in the high-value
   group and do NOT flag (equal to, not exceeding).

2. **Globex must NOT flag on security_review despite "Not started"** — deal_value
   80000 is below the export median (120000), so check 5 doesn't apply per the
   rubric; report Clean on that check.

3. **Acme must NOT flag despite being above-median value with "In Progress"
   security review** — "In Progress" is the expected state, not a flag
   condition.

## Not present: reporting any of these is a hallucination

- Any flag on Acme Systems or Globex Corp beyond "Clean" — both are clean.
- A flag count other than 3 for Soylent, 2 for Umbrella/Wayne/Stark/Horizon, 1
  for Initech, or 0 for Acme/Globex.
- Any days_in_stage comparison against the export median rather than the
  group-specific median — check 4 explicitly requires grouping by deal value.
- Any inferred detail about champion identity, criteria content, or date not
  present in the CSV cell.
- A claim that any column was missing — every column used by the rubric is
  present in this export.
