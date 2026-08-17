# Brief: evaluation-pipeline-check-demo CSV

Same discipline as the deal-risk-digest brief, adapted for the technical
evaluation shape check: decide the row roster and each row's expected flags
*before* writing values, per `references/rubric.md`'s exact six-check
deterministic rubric.

Reference date for every relative date below: **2026-08-17** (the date this
brief was authored). Days-in-stage and last-activity-gap thresholds are
derived from the export's own medians — reproducing this on a much later
date could shift boundary rows across those medians.

## Deliberate construction (per row, decided before the sheet)

- **Rows 1-2 — clean, must flag nothing (0 flags)**: the rubric requires at
  least two deals with all scaffolding in place (criteria defined, champion
  named, end date set, recent activity, in-stage duration near median,
  security review in progress if above-median value). A rubric that flags
  every row is broken.
- **Row 3 — single flag: missing criteria**: tests that check 1 (success
  criteria) stands alone without forcing other flags.
- **Row 4 — two flags: long running + stalled**: tests days_in_stage (check
  4) and last_activity gap (check 6) together, isolated from the others.
- **Row 5 — maximum flags (three): long running + security review missing +
  stalled**: above-median deal value with no security review started, plus
  old activity, plus in-stage duration over median. Tests checks 4, 5, 6
  together.
- **Row 6 — two flags: long running + stalled (different values than row
  4)**: confirms the medians are computed per export, not hardcoded.
- **Row 7 — two flags: missing champion + security review not started**: 
  above-median deal value without a champion OR a started security review.
  Tests checks 2 and 5 together.
- **Row 8 — trap: missing criteria + stalled, tests boundary condition**:
  below-median deal value with stalled activity and missing criteria. The
  trap is that stalling alone (check 6) is distinct from missing
  scaffolding (checks 1-3).

## Expected median calculations (from 8 rows)

**days_in_stage values**: 12, 15, 18, 20, 20, 25, 35, 70
- Median: (20 + 20) / 2 = 20 days
- Rows > 20: Row 4 (70), Row 5 (35), Row 6 (25) only

**deal_value values**: 80k, 95k, 100k, 110k, 130k, 150k, 180k, 200k
- Median: (110k + 130k) / 2 = 120k
- Rows above median: Row 5 (180k), Row 7 (200k)

**last_activity_date gaps (from 2026-08-17)**: 1, 2, 3, 4, 5, 16, 28, 58 days
- Median: (4 + 5) / 2 = 4.5 days
- Rows > 4.5: Row 4 (16), Row 5 (28), Row 6 (58), Row 8 (5)

## Expected flag table (decided before the sheet, checked against rubric)

| Deal | Flags | Evidence |
|---|---|---|
| Acme Systems | none | (all clean) |
| Globex Corp | none | (all clean) |
| Initech Holdings | criteria | success_criteria = (empty) |
| Umbrella Corp | days_in_stage, stalled | days_in_stage = 70 (> median 20); last_activity_date = 2026-08-01 (16 days gap, > median 4.5) |
| Soylent Industries | days_in_stage, security_review, stalled | days_in_stage = 35 (> 20); security_review = (empty) with deal_value 180k (> median 120k); last_activity_date = 2026-07-20 (28 days gap, > 4.5) |
| Wayne Industries | days_in_stage, stalled | days_in_stage = 25 (> 20); last_activity_date = 2026-06-20 (58 days gap, > 4.5) |
| Stark Corp | champion, security_review | champion = (empty); security_review = Not started with deal_value 200k (> median 120k) |
| Horizon Tech | criteria, stalled | success_criteria = (empty); last_activity_date = 2026-08-12 (5 days gap, > median 4) |

Closing lines expected: **"7 of 8 deals in Evaluation flagged"**, and the
single most common flag across them is **"stalled"** (5 of 7: Umbrella,
Soylent, Wayne, Horizon, and also shared by none — recount: Umbrella, Soylent,
Wayne = 3 of 7). Actually the most common is **"days_in_stage"** (4 of 7:
Umbrella, Soylent, Wayne, Initech... wait, Initech has criteria, not
days_in_stage). Let me recount:
- Criteria (Row 3, 8): 2
- Days_in_stage (Row 4, 5, 6): 3
- Champion (Row 7): 1
- Security_review (Row 5, 7): 2
- Stalled (Row 4, 5, 6, 8): 4

Most common: **"stalled"** (4 of 7 flagged deals).
