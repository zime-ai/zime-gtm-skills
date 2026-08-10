---
name: won-pipeline-check
description: Sweeps a closed-won deal export for missing handoff and record data the post-sale team needs — CS owner, kickoff date, signed value/term, contract reference, and date/stage consistency. Use when a deal desk or RevOps person wants to check closed-won deals before they hand off to onboarding/CS, or audit a pipeline export for won deals with incomplete records.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: Won pipeline
  zime:input-modes: csv,connector
---

# Won Pipeline Check

Sweeps a deal export for closed-won deals missing the data the next team
needs to run the handoff. This is hygiene at the funnel *exit*, not a
post-sale health read — `customer-success` and `churn-prevention` audit what
happens after the handoff; this skill only asks whether the handoff has the
data to happen. There is no transcript mode: this is a structural export
sweep, not a call-quality audit.

## When to use this

- A deal desk or RevOps person wants to check closed-won deals before they
  hand off to onboarding/CS.
- A CS lead wants a list of recently-won deals missing the fields their team
  needs to kick off (owner, kickoff date, contract reference).
- Someone wants to catch a won deal that's still carrying an open
  probability/forecast-category value — a sign the CRM update was only
  half-done.

## How to run it

```
claude "run won-pipeline-check on ./exports/pipeline.csv"
```

**Input.** A `.csv` deal/pipeline export. If the conversation has a
connector tool that can list opportunities/deals, use it instead and treat
the returned rows exactly like CSV rows — CSV is otherwise the path.

**Column detection.** Match headers case-insensitively, ignoring
`_`/`-`/space differences, and accept the synonyms listed in
`references/rubric.md`. If a column a check needs is absent from the
export, that check reports **Unknown (column missing)** for every row —
state this once, up front, and never infer the value from another column.

**Stage filter.** Operate only on rows whose stage fuzzy-matches "Won
pipeline" (i.e. Closed Won and close synonyms — see
`references/rubric.md`). Report how many rows were in scope and how many
the export held in total.

**Run each of the six checks in `references/rubric.md`** against every
in-scope row. Each check returns **Flagged**, **Clean**, or **Unknown**.

**Evidence rule.** Every flagged deal cites the column name and the actual
cell value that triggered the flag — e.g. `close_date = 2026-01-14`, or
`champion = (empty)`. A flag with no cited cell does not ship.

**Reads-well-too check.** Apply the check in `references/rubric.md` before
finalizing — a rubric that flags everything is useless.

## Output

One markdown table, flagged deals first, most flags first:

| Deal | Flags | Evidence | Suggested action |

Then two closing lines:

- `N of M deals in Won pipeline flagged`
- The single most common flag across them.

Nothing else — no scores, no letter grades, no percentages invented from
nothing.

## Sample data

`assets/sample-pipeline-won-pipeline-check.csv` is a synthetic closed-won
pipeline export — run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
