---
name: win-loss-brief
description: Writes a structured brief on why one specific deal was won or lost — outcome, 3-5 cited drivers (competitive displacement, champion strength or loss, pricing/procurement friction, timing, technical fit), and forward-looking notes for a similar deal. Use for a manager/leader ritual like a QBR or win-loss review on a single closed deal, not a whole-book pipeline sweep.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript,csv
---

# Win-Loss Brief

Writes a brief on why one specific closed deal was won or lost. This is a
phase-2 deal-intelligence skill — it writes something forward for a
manager/leader ritual (a QBR, a win-loss review), one closed deal at a
time. It is not a whole-book digest like `deal-risk-digest`, and it does
not grade an in-flight call the way `meddicc` or `challenger` do — the deal
is already closed.

## When to use this

- A manager preparing a QBR wants a written brief on why a specific deal
  was won or lost, not a live scoring of the call.
- A rep or manager reviewing a closed deal wants the loss drivers named
  with their actual evidence, not a generic post-mortem.
- Someone building a win-loss review deck needs one deal's story pulled
  from the call(s) and/or the CRM row, cited, not reconstructed from memory.

## Inputs

Either a call transcript (or several from the same deal, read in
chronological order) or a CRM export row for the closed deal, or both.
Both together produces a fuller brief; neither is required alone.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run win-loss-brief on ./calls/deal-final-call.txt"
```

Read the transcript(s) in order. Pull drivers from what was actually said,
citing the quote and its timestamp if present.

### CSV mode (`.csv`)

```
claude "run win-loss-brief on ./exports/pipeline.csv"
```

Find the row for the deal (by name, or ask which row if the file has
several closed deals and it isn't obvious which one). Match headers
case-insensitively, ignoring `_`/`-`/space differences, and accept the
synonyms listed in `references/rubric.md`. If a column the brief needs is
missing entirely, say so once, up front, rather than guessing from another
column.

A CSV-only brief is a **structural claim, not a call-quality claim** — the
same disclaimer `won-pipeline-check` and the other `*-pipeline-check`
skills use. It reports what the row's own fields say (outcome, reason,
competitor, value, close date), not what happened on any call.

### Both together

Read the transcript(s) first, then use the CSV row to fill gaps (a close
date or value the call never stated) or to flag a mismatch between what the
call implied and what the CRM row records (e.g. call reads as a clean win,
row's `reason` column says "price"). Note any such mismatch explicitly.

## Brief structure

1. **Outcome** — won or lost, close date, deal value. Cite the source
   (quote/timestamp, or column name + cell value).
2. **What drove it** — 3-5 cited factors, each tagged with one of the
   driver categories in `references/rubric.md` (competitive displacement,
   champion strength or loss, pricing/procurement friction, timing,
   technical fit). Every factor cites its quote/timestamp or its column
   name + cell value — a driver with no cited evidence does not ship.
3. **What a similar deal should do differently** — one or two
   forward-looking notes, each grounded in a driver actually named in
   section 2. No generic sales advice ("build more urgency") disconnected
   from what was cited.

## Driver confidence

Tag each driver in section 2 as **clear** (the transcript or CSV states it
plainly) or **tentative** (the closest thing said is a hedge, a guess, or
an unconfirmed aside — quote it as such, don't upgrade it to a confident
driver). See `references/rubric.md` for the full test. If every driver
comes back tentative, say so explicitly — that's a finding about how thin
the evidence is, not something to paper over with confident language.

## Sample data

`assets/sample-transcript.txt` is a synthetic late-stage call from a deal
that was ultimately lost. `assets/sample-pipeline-won-loss.csv` is a
synthetic closed-deal export with both won and lost rows. Run the skill
against either, or both, first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
