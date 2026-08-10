---
name: evaluation-pipeline-check
description: Sweeps a deal/pipeline export for technical evaluations running without defined success criteria, a technical champion, or an evaluation end date, and flags evaluations running long, stalled, or missing a security/procurement review relative to the export's own norms. Use when reviewing deals sitting in a technical evaluation stage, or auditing a pipeline export before a forecast call.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: Evaluation pipeline
  zime:input-modes: csv,connector
---

# Evaluation Pipeline Check

Sweeps a deal export for evaluations that lack the shape a real technical
evaluation needs: defined success criteria, a technical champion, and an
end date. Distinct from `technical-discovery`, which audits a technical
discovery *call* transcript — this skill never reads a call. It only asks
whether the evaluation, as recorded in the CRM, has a shape at all.

## When to use this

- A deal is sitting in "Technical Evaluation" and a manager wants a
  structural gut-check before the forecast call.
- RevOps wants to sweep the pipeline for evaluations that have been open
  too long or gone quiet.
- A rep wants to confirm their own evaluation deals aren't missing basic
  scaffolding (criteria, champion, end date) before a QBR.

## Modes

### CSV mode (`.csv`)

```
claude "run evaluation-pipeline-check on ./exports/pipeline.csv"
```

1. **Column detection.** Match headers case-insensitively, ignoring
   `_`/`-`/space differences. Accepted synonyms are listed in
   `references/rubric.md`. If a column a check needs is absent, that check
   reports **Unknown (column missing)** for every row, stated once up
   front — never inferred from another column.
2. **Stage filter.** Keep rows whose stage fuzzy-matches "Evaluation" (e.g.
   `Technical Evaluation`, `Eval`, `Evaluating`). Report rows in scope vs.
   total rows in the export.
3. **Score each in-scope row** against the six checks in
   `references/rubric.md`. Each check returns Flagged / Clean / Unknown.
   Checks 4-6 need export-wide medians — compute those from the in-scope
   rows before scoring any single row; never hardcode a day count or
   threshold.
4. **Evidence rule.** Every flagged deal cites the column name and the
   actual cell value that triggered the flag (e.g. `champion = (empty)`,
   `days_in_stage = 71`). An uncited flag doesn't ship.
5. **Output** one markdown table, flagged deals first, most flags first:

   | Deal | Flags | Evidence | Suggested action |

   Then two closing lines: `N of M deals in Evaluation flagged` and the
   single most common flag across them. Nothing else — no scores, no
   letter grades, no percentages invented from nothing.

### Connector mode

If the conversation has a tool that can list opportunities/deals, use it
and treat the returned rows exactly like CSV rows — same column detection,
same six checks, same output. Optional and secondary to CSV mode.

## Sample data

`assets/sample-pipeline-evaluation-pipeline-check.csv` is a synthetic
10-row export with a mix of flagged and healthy evaluation deals — run the
skill against it first. At least two rows are genuinely healthy and must
come back Clean on every check; a rubric that flags everything is useless.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at (or the connector
result, in connector mode) and nothing else.
