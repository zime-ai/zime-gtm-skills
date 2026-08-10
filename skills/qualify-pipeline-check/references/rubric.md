# Qualify pipeline check rubric

Six flags, checked against the CRM record only — this never reads a call.
A deal that trips zero flags is Clean; a deal missing an underlying column
entirely reports Unknown for that flag rather than being scored either way.

## Column synonyms

Match case-insensitively, ignoring `_`/`-`/space differences.

| Concept | Synonyms |
|---|---|
| Economic buyer / authority | `buyer`, `economic_buyer`, `decision_maker`, `champion`, `authority`, `contact_role` |
| Pain / problem | `pain`, `problem`, `use_case`, `pain_point` |
| Budget | `budget`, `budget_signal` |
| Deal value | `amount`, `deal_value`, `value`, `arr`, `deal_size` |
| Close date | `close_date`, `closedate`, `expected_close`, `expected_close_date` |
| Procurement/legal timeline | `procurement_timeline`, `legal_timeline`, `procurement_cycle` |
| Next step | `next_step`, `next_meeting`, `nextstep` |
| Actively worked status | `status`, `deal_status`, `activity_status` |
| Qualification framework score | `meddicc_score`, `meddpicc_score`, `bant_score`, `qualification_score` |

## 1. No economic buyer

Flagged if no contact on the deal is marked buyer/decision-maker, or the
authority/role column is empty on every contact row for that deal. If the
export has no authority/role column at all, report Unknown (column
missing).

## 2. No stated pain

Flagged if the pain/problem/use-case field is empty. Unknown if the column
is absent.

## 3. No budget signal

Flagged only if **both** the budget field and the deal value field are
empty — a deal can have a real deal-value number standing in for an
explicit budget line. Unknown if both columns are absent from the export.

## 4. Close date inside the procurement cycle

Flagged if the close date is sooner than the deal's own stated
procurement/legal timeline column. If that column is absent, fall back to
comparing the close date against the export's median qualify-to-close
window for deals of similar value (same order of magnitude); flag if the
close date implies a cycle far shorter than that median. State which of the
two comparisons was used. Unknown if close date itself is missing.

## 5. No next step

Flagged if the next-step/next-meeting field is empty while the deal's
status marks it as actively worked (not on-hold/stalled). If there is no
status column to establish "actively worked," treat every in-scope row as
actively worked by default — Qualify-stage rows in an export are assumed
live unless marked otherwise. Unknown only if the next-step column itself
is absent.

## 6. Advanced without a qualification record

Flagged if a qualification-framework column (MEDDICC/BANT/etc. score) is
present in the export as a column but empty on this specific row. If no
such column exists anywhere in the export, this check does not apply —
report Unknown (column missing), not Flagged, since there is nothing to be
empty.

## Reads-well-too check

The sample data must include at least two deals with every relevant field
filled in credibly (real buyer name + role, a specific pain, a budget or
deal value, a close date at or after the stated procurement timeline, a
next step, and a filled qualification score). Running the skill against
`assets/sample-pipeline-qualify-pipeline-check.csv` must return those rows
Clean on all six checks. A rubric that flags a well-documented deal is
useless — loosen the read before finalizing, not the other way around.
