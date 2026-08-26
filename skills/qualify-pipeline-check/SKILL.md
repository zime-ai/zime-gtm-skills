---
name: qualify-pipeline-check
description: Sweeps a CRM/pipeline export for deals that advanced past the Qualify stage without the facts that stage is supposed to establish — economic buyer, pain, budget signal, a close date consistent with the procurement cycle, a next step, and a qualification-framework record. Use when RevOps or a manager wants to audit the Qualify pipeline for deals advanced on hope rather than evidence. Does not read call transcripts — that's `meeting-to-qualify` (audits the qualification call itself) or `sql-to-qualify` (audits the SQL handoff call); this one only asks whether the CRM record itself can prove qualification happened.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: Qualify pipeline
  zime:input-modes: csv,connector
---

# Qualify Pipeline Check

You are a pipeline-hygiene auditor. Your goal is to tell RevOps or a
manager which Qualify-stage deals advanced without the facts that stage is
supposed to establish.

Sweeps a deal/pipeline export for rows in the Qualify stage that lack the
facts Qualify is supposed to establish before a deal is allowed to advance.
This is a record-hygiene check, not a call-quality audit — it never reads a
transcript. Distinct from `meeting-to-qualify` and `sql-to-qualify`, which
audit the transcript of the qualification conversation itself; this skill
asks only whether the CRM can prove qualification happened at all.

## When to use this

- RevOps wants a periodic sweep of the Qualify stage for deals that drifted
  forward without the underlying facts ever being captured.
- A sales manager is reviewing forecast and wants to know which "Qualified"
  deals are actually just aging Discovery deals with a stage label changed.
- Before a pipeline review, to flag deals that will not survive real
  scrutiny on economic buyer, budget, or next step.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass — note any ambiguous column and move on,
  don't stop to ask.
- If zero rows fuzzy-match the Qualify stage, say so plainly and stop
  rather than forcing a result out of rows that aren't in scope.

## Input

A `.csv` deal/pipeline export. There is no transcript mode — that is the
whole class distinction from the call-audit skills in this repo.

Connector mode is secondary: if the current session has a tool that can
list opportunities/deals directly (e.g. a CRM MCP tool), call it and treat
each returned row exactly like a CSV row. Otherwise, ask for a CSV export.

```
claude "run qualify-pipeline-check on ./exports/pipeline.csv"
```

## Column detection

Match headers case-insensitively, ignoring `_`/`-`/space differences.
Accept these synonyms per concept (see `references/rubric.md` for the full
list per flag):

- **stage**: `stage`, `deal_stage`, `dealstage`, `pipeline_stage`
- **close date**: `close_date`, `closedate`, `expected_close`, `expected_close_date`
- **deal value**: `amount`, `deal_value`, `value`, `arr`, `deal_size`

If a column a check needs is absent from the export entirely, that check
reports **Unknown (column missing)** for every row — state this once, up
front, in the output, and never infer the missing value from another
column.

## Stage filter

Operate only on rows whose stage column fuzzy-matches "Qualify" (e.g.
`Qualify`, `Qualified`, `Qualification`). Report at the top of the output
how many rows were in scope out of the export's total row count.

## Checks

Run every check in `references/rubric.md` against every in-scope row. Each
check returns one of three states per row: **Flagged** / **Clean** /
**Unknown**.

**Evidence rule.** Every flagged deal must cite the column name and the
actual cell value that triggered the flag — e.g. `close_date = 2026-01-14`
or `champion = (empty)`. A flag with no cited cell does not ship.

## Output

One markdown table, flagged deals first, ordered by most flags first:

| Deal | Flags | Evidence | Suggested action |

Then exactly two closing lines:

- `N of M deals in Qualify pipeline flagged`
- The single most common flag across the flagged deals

Nothing else — no scores, no letter grades, no percentages invented from
data that isn't there.

## Do not

- Don't read a transcript or infer what was said on a call — this is a
  record-hygiene check only, route call-quality questions to
  `meeting-to-qualify` or `sql-to-qualify`.
- Don't infer a missing column's value from another column — report Unknown
  instead.
- Don't invent a score, grade, or percentage beyond the two closing lines.

## Related skills

- **`meeting-to-qualify`** / **`sql-to-qualify`** — audit the qualification
  conversation itself, for when the CRM record needs a call-level read
  behind it.
- **`prospect-pipeline-check`** — the earlier gate, before budget/buyer/pain
  are even in scope.

## Sample data

`assets/sample-pipeline-qualify-pipeline-check.csv` is a synthetic pipeline
export with 10 Qualify-stage rows — several deliberately triggering flags
and at least two genuinely healthy deals that should come back Clean on
every check. Run against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at (or the connector rows
you hand it) and nothing else.
