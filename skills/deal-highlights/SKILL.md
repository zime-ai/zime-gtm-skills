---
name: deal-highlights
description: Writes a short highlights digest of one sales call — the moments that actually matter (a commitment, an objection, a buying signal, a competitive mention, a risk, a number that matters), each citing the quote it came from. Use when a rep needs something to skim or forward to a manager right after a call, not a full rubric grade of it.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript
---

# Deal Highlights

Writes a short highlights digest out of what was actually said on a call:
the handful of moments a manager needs to know about without reading the
transcript. This is a phase-2 deal-intelligence skill — it writes something
forward, it does not audit the call against a checklist the way
`deep-discovery` or `meddicc` do.

## When to use this

- A rep just finished a call and wants something quick to forward to a
  manager, instead of a transcript nobody has time to read.
- A manager wants the two or three things from a call that actually matter
  — a commitment, a risk, a competitor mention — without a full scorecard.
- Someone needs a fast gut-check on whether a call moved the deal forward
  or just filled an hour.

## What counts as a highlight

Only these earn a line:

- A real commitment, made by either side (a date, a deliverable, an
  approval).
- An objection raised.
- A buying signal.
- A competitive mention.
- A risk or blocker.
- A number that matters — budget, timeline, headcount.

Generic rapport-building, scheduling chatter, and small talk are not
highlights, no matter how much of the call they fill. If the call was
thin, output fewer items — don't pad to hit a count.

## The evidence rule

Every highlight cites the quote or timestamp it came from. No citation, no
highlight — same standard `next-step-commitment` and every other skill in
this repo already holds to. See `references/rubric.md` for the full
highlight-type list and what disqualifies a candidate line.

## Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run deal-highlights on ./calls/call.txt"
```

Read the transcript, then output a bulleted list, 5-10 items typical for a
normal call, fewer if the call was thin. Each item is one line: the
highlight, then the quote or timestamp it came from.

Close with one line — "why this call matters" — a manager could read alone
and still get the gist of the call.

## Sample data

`assets/sample-transcript.txt` is a synthetic call with a deliberate mix: a
genuine commitment, an objection, and a competitive mention, plus small
talk that isn't a highlight — run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
