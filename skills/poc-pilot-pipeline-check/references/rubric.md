# POC/pilot pipeline check rubric

Six flags, applied to every row in scope after the stage filter. Each check
returns Flagged, Clean, or Unknown (column missing) — never inferred from a
different column.

## Column synonyms

- **Stage**: `stage`, `deal_stage`, `dealstage`, `pipeline_stage`
- **Exit criteria**: `exit_criteria`, `poc_success_criteria`,
  `success_criteria`, `poc_exit_criteria`
- **Conversion date**: `conversion_date`, `planned_conversion`,
  `poc_end_date`, `pilot_end_date`, `expected_conversion_date`
- **POC end date**: `poc_end_date`, `pilot_end_date`, `planned_end_date`,
  `end_date`
- **Decision**: `decision`, `poc_decision`, `outcome`, `result`
- **Sponsor / exec contact**: `sponsor`, `exec_sponsor`, `champion_role`,
  `contact_role`, `stakeholder_role`
- **Usage/milestone evidence**: `usage`, `adoption`, `milestone`,
  `usage_notes`, `milestone_notes`
- **POC status (live)**: `poc_status`, `status`, `deal_status`
- **POC start date**: `poc_start_date`, `pilot_start_date`, `start_date`

## 1. No written exit criteria

Flagged if the exit-criteria / POC-success-criteria column is empty or
whitespace-only. The single most important flag in this skill — a POC with
no written definition of success cannot be judged won or lost.

## 2. No conversion date

Flagged if there is no planned POC end date and no conversion date — both
columns empty or both missing.

## 3. Past its own end date

Flagged if the planned POC end date is in the past, the deal is still in
the POC/pilot stage, and the decision field is empty. A deal past its own
deadline with no recorded decision is stalled, not just slow.

## 4. No executive sponsor

Flagged if no contact on the deal has an exec/sponsor role recorded. This
check applies regardless of deal value — a small deal with no sponsor is
just as unlikely to convert as a large one.

## 5. No usage or milestone evidence

Applies only when the usage/adoption/milestone column exists and the POC
status marks the deal as live. Flagged if that column is empty for a live
POC — a running POC with zero recorded usage is a red flag, not a data gap.

## 6. Open-ended

Flagged if the POC start date is older than the export's median POC
duration (median of `end_date - start_date` across in-scope rows with both
dates present) and there is no end date at all. Note the computed median
once, up front, as the assumption driving this check.

## Reads-well-too check

The sample data must contain at least two deals with written exit criteria,
a conversion date, an exec sponsor, and (if live) recorded usage — these
must come back Clean on every check. A rubric that flags everything is
useless.
