# Gold label: negotiation-pipeline-check-demo.csv

Computed by hand from `references/rubric.md`'s six deterministic checks and
`evals/illustrative/BRIEF-negotiation-pipeline-check.md`'s construction,
against today = 2026-08-17. This rubric is deterministic — every row below
is a fact, not a judgment call.

## Expected flagged deals (in skill's output order: flagged first, by flag count)

| Rank | Deal | Flags | Evidence |
|---|---|---|---|
| 1 | Atlas Group | #1, #2, #3, #5 (4 flags) | contact_role="Sales Manager" (no legal/proc/finance); paper_status="Pending" (not started); discount_pct=20% (above median 14%), approver=(empty); close_plan=(empty) |
| 2 | Summit Industries | #3 (1 flag) | discount_pct=18% (above median 14%), approver=(empty) |
| 3 | Catalyst Group | #3 (1 flag) | discount_pct=15% (above median 14%), approver=(empty) |
| 4 | Apex Tech | #1 (1 flag) | contact_role="Sales Director" (no legal/proc/finance) |
| 5 | Zenith Corp | #2 (1 flag) | paper_status="Not started" |
| 6 | Nexus Digital | #4 (1 flag) | original_close_date=2026-08-15, close_date=2026-08-31 (date was pushed, differs) |
| 7 | Radius Analytics | #5 (1 flag) | close_plan=(empty) |
| 8 | Velocity Group | #6 (1 flag) | signer_role=(empty) |

## Expected clean deals (no flags)

| Deal | Evidence |
|---|---|
| Vista Solutions | All checks pass: contact_role="Legal Counsel" (legal present); paper_status="In progress" (started); discount_pct=10% (≤14%, below median); original_close_date=current close_date; close_plan="Shared MAP v1" (present); signer_role="Legal Counsel" (named) |
| Pinnacle Ventures | All checks pass: contact_role="Procurement Manager" (procurement present); paper_status="MSA signed" (started); discount_pct=12% (≤14%); original_close_date=current close_date; close_plan="Joint action plan"; signer_role="CFO" |

## Median discount calculation

In-scope rows (negotiation stage) with non-empty discount values (all 10 deals in scope):
10, 12, 14, 10, 18, 12, 14, 16, 15, 20. Sorted: 10, 10, 12, 12, 14, 14, 15, 16, 18, 20.
With 10 values, median = (14 + 15) / 2 = 14.5, typically evaluated as 14% in discrete discount contexts.

Discount > 14% (i.e., 15%, 16%, 18%, 20%) without approver = flag #3.
Discount ≤ 14% (i.e., 10%, 12%, 14%) = no flag for #3, even with empty approver.

## The traps (findings a correct run must get right)

1. **Catalyst Group discount above median with empty approver.** Gold:
   discount_pct=15% > median 14%, approver=(empty), so check #3 should flag.
   The rubric states "Flagged if a row's discount is above that median" —
   Catalyst's 15% is above the 14% median, so it correctly flags. This tests
   that the skill properly calculates the median across all in-scope rows.
2. **Atlas Group has four flags (most flags of any row).** The skill must
   cite all four (contact role, paper status, discount + approver, close
   plan) and correctly identify the flags, not miss or conflate them.
3. **Nexus Digital's original_close_date (2026-08-15) < current close_date
   (2026-08-31).** The rubric calls this "the date was pushed" (pushed
   later/out). The skill must flag this as check #4 (close date slipped).

## Not present: reporting any of these is a hallucination

- Any flag on Vista Solutions or Pinnacle Ventures (only these two are
  clean).
- A flag count or flag number that doesn't match the six checks in the
  rubric (only #1 through #6 exist).
- Any inferred deal attribute, contact name, or date not present in the CSV
  cell.
- A claim that a required column was missing from the export — all columns
  used by the rubric are present in this sheet.

## Closing lines expected

- **"8 of 10 deals in negotiation flagged"** (Vista, Pinnacle = clean;
  Apex, Zenith, Summit, Nexus, Radius, Velocity, Catalyst, Atlas = 8 flagged)
- **Most common flag:** Discount without approval (check #3). It appears on
  3 deals (Summit, Catalyst, Atlas), while all other flags appear on 1 deal
  each.
