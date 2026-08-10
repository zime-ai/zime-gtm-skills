---
name: poc-pilot-pipeline-check
description: Sweeps a CRM pipeline export for POCs and pilots running with no exit criteria, no sponsor, or no conversion date. Use when RevOps or a manager wants a pipeline-wide read on which POCs/pilots can actually convert versus which are drifting with nothing written down.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: POC/pilot pipeline
  zime:input-modes: csv,connector
---

# POC/Pilot Pipeline Check

Sweeps every deal sitting in a POC or pilot stage and asks which of them can
never convert because nobody wrote down what winning looks like. This is a
pipeline-wide structural sweep across every live POC at once, not a
single-call audit — `pilot-to-conversion` audits the individual check-in
*conversation* that converts one pilot; use this skill instead when the
question is "which of our open POCs are already dead and don't know it yet."

## When to use this

- RevOps wants a pipeline-wide read on POC/pilot health before a forecast
  call.
- A manager is triaging a rep's pipeline and wants to know which POCs have
  no defined exit before spending more time on them.
- Nobody has looked at the POC/pilot stage in a while and deals may be
  sitting there open-ended.

## Input

A `.csv` deal/pipeline export. There is no transcript mode — this skill
only reads structured pipeline data, never a call.

Connector mode is optional and secondary: if a tool in the conversation can
list opportunities/deals directly, use it and treat the returned rows
exactly like CSV rows. Otherwise, work from the CSV file.

## How to run it

```
claude "run poc-pilot-pipeline-check on ./exports/pipeline.csv"
```

1. **Detect columns.** Match headers case-insensitively, ignoring
   `_`/`-`/space differences. Accepted synonyms are listed in
   `references/rubric.md`. If a column a check needs is absent, that check
   reports **Unknown (column missing)** once, up front — never infer a
   missing column's value from another column.
2. **Filter to stage.** Keep rows whose stage fuzzy-matches POC/pilot (e.g.
   `POC`, `Pilot`, `POC/Pilot`, `Proof of Concept`). Report how many rows
   were in scope out of the export's total.
3. **Run every check in `references/rubric.md`** against each in-scope row.
   Each check returns **Flagged**, **Clean**, or **Unknown**.
4. **Cite evidence.** Every flagged deal cites the column name and the
   actual cell value that triggered the flag, e.g. `champion = (empty)` or
   `poc_end_date = 2026-01-14`. A flag with no cited cell does not ship.
5. **Reads-well-too check.** Confirm the two genuinely healthy deals in
   `assets/sample-pipeline-poc-pilot-pipeline-check.csv` come back Clean. A
   rubric that flags everything is useless.

## Output

One markdown table, flagged deals first, most flags first:

| Deal | Flags | Evidence | Suggested action |

Then two closing lines:

- `N of M deals in <stage> flagged`
- The single most common flag across them

Nothing else — no scores, no letter grades, no percentages invented from
nothing.

## Sample data

`assets/sample-pipeline-poc-pilot-pipeline-check.csv` — synthetic pipeline
export, run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file (or connector rows) you point it at and
nothing else.
