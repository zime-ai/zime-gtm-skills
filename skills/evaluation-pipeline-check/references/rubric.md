# Evaluation pipeline check — rubric

Applies to rows whose stage fuzzy-matches "Evaluation" (`Technical
Evaluation`, `Eval`, `Evaluating`, `Evaluation pipeline`, `Tech Eval`).
Every check returns **Flagged**, **Clean**, or **Unknown (column
missing)** — never inferred from another column.

## Column synonyms accepted (case-insensitive, `_`/`-`/space-insensitive)

| Concept | Accepted headers |
|---|---|
| Deal name | `deal_name`, `deal`, `opportunity`, `opportunity_name`, `name` |
| Stage | `stage`, `deal_stage`, `dealstage` |
| Deal value | `deal_value`, `amount`, `value`, `deal_amount` |
| Success criteria | `success_criteria`, `evaluation_criteria`, `eval_criteria`, `criteria` |
| Technical champion | `champion`, `technical_champion`, `champion_role`, `champion_name` |
| Evaluation end date | `evaluation_end`, `evaluation_end_date`, `eval_end_date`, `evaluation_milestone` |
| Days in stage | `days_in_stage`, `days_in_evaluation`, `stage_duration`, `days_in_current_stage` |
| Security/procurement review | `security_review`, `procurement_review`, `security_review_started`, `procurement_status` |
| Last activity date | `last_activity`, `last_activity_date`, `last_touch`, `last_touchpoint` |

## The six checks

1. **No defined success criteria** — `success_criteria` (or synonym) is
   empty or whitespace-only. Flagged if empty; Clean if any non-trivial
   text is present.

2. **No technical champion** — no contact attached to the deal carries a
   technical/champion role. If the export has a single `champion` field,
   empty means Flagged. If contacts are modeled as multiple rows/columns,
   Flagged only if none of them indicate a champion or technical-owner
   role.

3. **No evaluation end date** — `evaluation_end` (or synonym) is empty.
   Flagged if empty; Clean if any date is present, regardless of whether
   it's past or future (a stale end date is covered by check 6, not this
   one).

4. **Evaluation running long** — compute the median `days_in_stage` across
   all in-scope rows, grouped by rows of similar deal value (e.g. above/
   below the export's own median deal value, or terciles if the export is
   large enough to support them). Flag a row whose `days_in_stage` exceeds
   its group's median. Never hardcode a day count — always derive it from
   the export in hand. If deal value is missing, fall back to the median
   across all in-scope rows.

5. **No security/procurement review started** — only evaluated when the
   export has a security/procurement review column *and* the deal's value
   exceeds the export-wide median deal value. Flagged if that value cell
   is empty or indicates "not started". Below-median deals are never
   flagged on this check — report Clean, not Unknown, for them.

6. **Stalled** — compute the median gap between `last_activity` and today
   (or the export's stated as-of date, if the export declares one) across
   all in-scope rows. Flag a row whose gap exceeds that median.

## Reads-well-too check

`assets/sample-pipeline-evaluation-pipeline-check.csv` carries at least two
deals with defined criteria, a named champion, a set end date, an
in-progress security review where applicable, normal days-in-stage, and
recent activity. Running this skill against the sample must return those
rows Clean on every check. A rubric that flags every row in the sample is
broken and should be fixed before shipping.
