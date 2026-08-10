---
name: negotiation-pipeline-check
description: Sweeps a deal/pipeline export for deals in negotiation with no paper process started, no named approver on a discount, no credible close date, or no named signature path. Use when reviewing forecast-stage negotiation deals for whether they have a real mechanical path to signature, not just a stated intent to close.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: Negotiation pipeline
  zime:input-modes: csv,connector
---

# Negotiation Pipeline Check

Sweeps a deal export for deals sitting in negotiation with no mechanical
path to a signature — no paper started, no approver on a discount, no
credible close date, no mutual close plan, no named signer. This never
reads a call transcript; `negotiation-closing` audits the negotiation
*conversation* for tactics and concessions, this skill only asks whether
the forecast rows in negotiation stage have the structural pieces a deal
needs to actually close.

## When to use this

- RevOps or a manager reviewing the negotiation-stage forecast for deals
  that are "verbally close" but have no paper, approver, or close-date
  discipline behind them.
- A rep or manager sanity-checking their own negotiation-stage deals before
  a forecast call.
- Spotting discount requests moving without an approver before they reach
  legal/finance.

## Step 1: Choose an input source

**CSV mode** (default) — read the `.csv` file the user points at directly.

**Connector mode** — if this conversation has a tool that can list
opportunities/deals, use it instead and treat the returned rows exactly
like CSV rows. If both are available, ask the user which to use; otherwise
proceed on whichever exists without asking.

There is no transcript mode in this skill.

## Step 2: Column detection

Match headers case-insensitively, ignoring `_`/`-`/space differences.
Accept the synonyms listed in `references/rubric.md`. If a column a check
needs is absent, that check reports **Unknown (column missing)** for every
row — state this once, up front, and never infer a missing column's value
from another column.

## Step 3: Filter to negotiation stage

Keep rows whose stage column fuzzy-matches "negotiation" (e.g.
`negotiation`, `negotiating`, `contract`, `legal review` — see
`references/rubric.md` for the exact match list). Report how many rows were
in scope out of the export's total row count.

## Step 4: Run the six checks

Score every in-scope row against the six checks in `references/rubric.md`.
Each check returns **Flagged**, **Clean**, or **Unknown**. Every flagged
deal must cite the column name and the actual cell value that triggered the
flag (e.g. `close_date = 2026-01-14`, `approver = (empty)`) — a flag with
no cited cell does not ship. Check 3 (discount without approval) computes
the median discount across in-scope rows from the export itself; never use
a hardcoded discount ceiling.

Run the reads-well-too check from `references/rubric.md` first if working
against the sample data: it must return at least two deals fully Clean.

## Step 5: Output

One markdown table, flagged deals first, most flags first:

| Deal | Flags | Evidence | Suggested action |
|---|---|---|---|

Then two closing lines:
- `N of M deals in negotiation flagged`
- The single most common flag across the flagged deals.

Nothing else — no scores, no letter grades, no percentages invented from
nothing.

Run this end to end in one pass. Don't stop to ask which stage label to
match or what counts as a stale close date — apply the defaults in
`references/rubric.md`, decide, and note the assumption once.

## Sample data

`assets/sample-pipeline-negotiation-pipeline-check.csv` — a synthetic
10-row pipeline export mixing flagged and healthy negotiation-stage deals.
Run the skill against it first:

```
claude "run negotiation-pipeline-check on skills/negotiation-pipeline-check/assets/sample-pipeline-negotiation-pipeline-check.csv"
```

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at (or what a connector
already present in the conversation returns) and nothing else.
