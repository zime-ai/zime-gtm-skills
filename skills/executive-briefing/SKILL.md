---
name: executive-briefing
description: Writes the short brief a rep sends upward out of one deal — to their own exec or the buyer's exec sponsor — covering deal snapshot, status, what's at risk, and the ask, each claim cited to a quote or a CSV column/cell. Use when someone who will never read the transcript needs to act on one deal, not a call-by-call digest or a whole-pipeline sweep.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript,csv
---

# Executive Briefing

Writes the short brief a rep sends upward out of one deal: what it is,
where it stands, what's at risk, what's being asked for. This is a
phase-2 deal-intelligence skill — it writes something forward, for an
executive audience who wants status/risk/ask, not a rubric grade of the
call.

**Distinct from `deal-highlights`**: `deal-highlights` digests one call for
a manager to skim (a list of moments — commitment, objection, buying
signal, competitive mention, risk). This skill is deal-level, not
call-level — if several calls on the same deal are given, it briefs the
deal as a whole, read in order, not call-by-call — and decision-oriented
for an executive audience, not an exhaustive moment list. Use
`deal-highlights` right after a single call; use `executive-briefing` when
someone above the deal needs to act on it.

## When to use this

- A rep needs something to send their own manager or VP on where a deal
  stands, without the exec reading the transcript.
- A rep is prepping the buyer's exec sponsor for a check-in and needs a
  short, cited status they can forward as-is.
- A manager wants the risk and the ask on one specific deal, not a
  pipeline-wide risk sweep (`deal-risk-digest`) or a closed-deal
  postmortem (`win-loss-brief`).

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run executive-briefing on ./calls/deal-checkin.txt"
```

If several transcripts from the same deal are given, read them in
chronological order and brief the deal as a whole. Every claim cites the
quote (and timestamp, if present) it came from.

### CSV mode (`.csv`)

```
claude "run executive-briefing on ./exports/pipeline.csv"
```

Find the row for the deal (by name, or ask which row if several deals are
in the file and it isn't obvious which one). Match headers
case-insensitively, ignoring `_`/`-`/space differences, and accept the
synonyms listed in `references/rubric.md`. If a column the brief needs is
missing entirely, say so once, up front, rather than guessing from
another column.

A CSV-only brief is a **structural claim, not a call-quality claim** — the
same disclaimer `deal-risk-digest` and `win-loss-brief` use. It reports
what the row's own fields say, not what happened on any call.

### Both together

Read the transcript(s) first, then use the CSV row to fill gaps (a close
date or deal value the call never stated). If the row and the call
disagree, note the mismatch explicitly rather than silently picking one.

## Brief structure

1. **Deal snapshot** — company, stage, value, close date. Cite each
   (quote/timestamp, or column name + cell value). If the deal value or
   close date isn't stated anywhere in the input, say so explicitly —
   never estimate it or carry over a number from a similar-looking deal.
2. **Status in one paragraph** — where the deal stands right now, in
   plain language an exec who wasn't on the call can act on.
3. **What's at risk** — 1-3 cited risks specific to this deal, not a
   generic risk checklist. See `references/rubric.md` for what counts.
4. **The ask** — what needs to happen next, from whom, and by when. Tag
   it `heard` (the call or CSV states it as agreed) or `inferred` (it's
   the rep's own proposal, not locked down) using the three-part test in
   `references/rubric.md`. An `inferred` ask ships labeled as the rep's
   proposal, not dressed up as a confirmed next step.

Nothing else — no invented deal value, no confidence score, no generic
"next steps" boilerplate disconnected from what was actually said or
recorded.

## Sample data

`assets/sample-transcript.txt` is a synthetic late-stage call that never
states the deal's dollar value. `assets/sample-pipeline-executive-briefing.csv`
is a synthetic pipeline export with a blank `deal_value` cell for the same
deal. Run the skill against either, or both, first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
