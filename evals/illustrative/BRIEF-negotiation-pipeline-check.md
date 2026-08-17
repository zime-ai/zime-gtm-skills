# Brief: negotiation-pipeline-check-demo CSV

Same discipline as the deal-risk-digest brief, adapted for negotiation
pipeline checks: decide the row roster and each row's expected flag
state *before* writing values into the sheet, per `references/rubric.md`'s
six deterministic checks.

Reference date for every relative date below: **2026-08-17** (the date
this brief was authored).

## Deliberate construction (per row, decided before the sheet)

- **Rows 1-2 — completely clean, no flags**: the rubric requires at least
  two such rows (`references/rubric.md`'s reads-well-too check). All six
  checks pass: legal/procurement contact present, paper started, discount at
  or below median (no approver needed), no close-date slip, mutual close plan
  present, signer named.
- **Row 3 — only check #1 (no legal/procurement/finance contact)**: has
  sales contact, no legal/proc/finance role present. Everything else passes.
- **Row 4 — only check #2 (paper not started)**: paper_status = "Not
  started". Everything else passes.
- **Row 5 — only check #3 (discount without approval)**: discount is above
  the median discount across in-scope rows, approver column is empty.
  Everything else passes.
- **Row 6 — only check #4 (close date slipped)**: original_close_date
  exists and differs from (is earlier than) current close_date. Everything
  else passes.
- **Row 7 — only check #5 (no mutual close plan)**: close_plan is empty.
  Everything else passes.
- **Row 8 — only check #6 (signature path unnamed)**: signer_role is empty.
  Everything else passes.
- **Row 9 — boundary discount above median**: discount is above the median
  discount (15% > 14%). Approver is empty, so check #3 should flag. Tests
  that the skill correctly calculates the median and applies the > threshold.
- **Row 10 — multiple flags**: sales contact (flag #1), paper "Pending"
  (flag #2), discount above median + no approver (flag #3), no close plan
  (flag #5). Checks #4 and #6 pass. Tests whether the skill aggregates
  multiple flags correctly.

## Expected median discount

Across all in-scope (negotiation-stage) rows with non-empty discount values:
10%, 10%, 12%, 12%, 14%, 14%, 15%, 16%, 18%, 20% (10 values).
Median = (14 + 15) / 2 = **14.5%**, evaluated as **14%** in discrete contexts.

Therefore, discounts > 14% (i.e., 15%, 16%, 18%, 20%) without an approver
should flag check #3. Discounts ≤ 14% should not flag for check #3, even
with no approver.

## Expected final flagging (hand-computed from the rubric)

| Deal | Flags | Count | Notes |
|---|---|---|---|
| Vista Solutions | None | 0 | Clean — all checks pass |
| Pinnacle Ventures | None | 0 | Clean — all checks pass |
| Apex Tech | #1 (no legal/proc/finance) | 1 | Sales contact only |
| Zenith Corp | #2 (paper not started) | 1 | paper_status = "Not started" |
| Summit Industries | #3 (discount without approval) | 1 | discount 18% > median 14%, no approver |
| Nexus Digital | #4 (close date slipped) | 1 | original_close_date = 2026-08-15, current = 2026-08-31 |
| Radius Analytics | #5 (no mutual close plan) | 1 | close_plan empty |
| Velocity Group | #6 (signature path unnamed) | 1 | signer_role empty |
| Catalyst Group | #3 (discount without approval) | 1 | discount 15% > median 14%, approver empty |
| Atlas Group | #1, #2, #3, #5 | 4 | Sales contact, paper "Pending", discount 20% + no approver, no close plan |

Closing lines expected:
- **"8 of 10 deals in negotiation flagged"** (Vista, Pinnacle = clean; all others = 8 flagged)
- **Most common flag: #3 (discount without approval)** — appears on 3 deals (Summit, Catalyst, Atlas), while all other flags appear on 1 deal each
