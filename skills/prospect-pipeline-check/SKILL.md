---
name: prospect-pipeline-check
description: Sweeps a CRM pipeline export for prospect-stage deals with no real two-way engagement from the prospect side — the earliest "is this even a deal" gate, before budget, buyer, or pain are even in scope. Use when auditing a prospect-stage pipeline for zombie deals a rep is carrying forward on outbound activity alone, or before a pipeline review to separate real opportunities from unanswered outreach.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: Prospect pipeline
  zime:input-modes: csv,connector
---

# GTM Prospect Pipeline Check

Sweeps a deal/pipeline export for prospect-stage deals that have no real
two-way engagement — no reply, no meeting, no inbound signal from the
prospect, only rep-side outbound. This is the earliest gate in the deal
lifecycle: it never asks about budget, buyer, or pain (that's
`qualify-pipeline-check`'s job). It only asks whether a human on the other
side has engaged at all. Runs entirely on the file (or connector rows) you
give it — no network calls, no credentials, nothing leaves your machine
beyond an already-connected CRM tool.

## When to use this

- RevOps or a sales manager wants to find prospect-stage deals a rep is
  carrying forward on outbound activity alone, with no prospect response.
- Before a pipeline review, to separate deals with real two-way signal from
  ones that are really just unanswered sequences sitting in a stage.
- A rep wants a gut-check on their own prospect list before it goes stale.

## How to run it

```
claude "run prospect-pipeline-check on ./exports/pipeline.csv"
```

**Input.** A `.csv` deal/pipeline export. There is no transcript mode for
this skill. If the conversation has a connector tool that can list
opportunities/deals, you may use it instead and treat the returned rows
exactly like CSV rows — CSV is the default path.

**Column detection.** Match headers case-insensitively, ignoring
`_`/`-`/space differences, and accept the synonyms listed in
`references/rubric.md`. If a column a check needs is missing, that check
reports **Unknown (column missing)** for every row — state this once up
front, and never infer the value from another column.

**Stage filter.** Operate only on rows whose stage fuzzy-matches "Prospect"
(e.g. `Prospect`, `Prospecting`, `Prospect pipeline`). Report how many rows
were in scope against how many the export held in total.

**Checks.** Run all six checks in `references/rubric.md` against every
in-scope row. Each check returns **Flagged**, **Clean**, or **Unknown**.
Every flagged row must cite the column name and the actual cell value that
triggered it (e.g. `close_date = 2026-01-14`, or `champion = (empty)`) — a
flag with no cited cell does not ship.

Before finalizing, run the reads-well-too check in `references/rubric.md`
— if a deal that clearly has a real, responsive prospect on the other end
still comes back flagged, the rubric is reading too strictly.

**Output.** One markdown table, flagged deals first, most flags first:

| Deal | Flags | Evidence | Suggested action |

Close with exactly two lines: `N of M deals in Prospect pipeline flagged`
and the single most common flag across the flagged deals. Nothing else —
no scores, no letter grades, no percentages invented from nothing.

## Sample data

`assets/sample-pipeline-prospect-pipeline-check.csv` — a synthetic
prospect-stage pipeline export with several deals that deliberately trigger
flags and at least two genuinely healthy deals. Run against it first.

## What this does not do

No CRM connection beyond an already-connected tool the conversation
provides, no API calls of its own, no telemetry, no data retention beyond
the current session. It reads the file (or rows) you point it at and
nothing else.
