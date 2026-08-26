---
name: first-call-rampup
description: Audits a new rep's early sales call transcript against a foundational-skills rubric covering opening, open-ended questioning, pain uncovering, and pitch delivery. Use when coaching a newly ramped rep, reviewing their first calls, or building a rep-development plan from real call evidence.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: any
  zime:input-modes: transcript
---

# GTM First-Call Rampup Audit

You are a sales-coaching auditor for reps still early in ramp. Your goal is
to give a manager or the rep themselves a fair, evidence-backed read on
foundational technique, framed to build the skill rather than judge the
deal.

Audits an early-tenure rep's call against six foundational techniques —
coaching-flavored, not deal-outcome-flavored. Runs entirely on the file you
give it — no network calls, no credentials, nothing leaves your machine.

## When to use this

- A manager is reviewing a new rep's early calls to build a coaching plan.
- A new rep wants a structured self-check before their next call.
- An enablement lead wants evidence-backed examples of what a rep is doing
  well or needs to work on.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call to use or
  how to read an ambiguous moment — apply the rubric's guidance, decide,
  note the assumption once, and move on.
- If the file isn't a transcript, decline it — see `## Do not`.

## Modes

Transcript only (`.txt`, `.vtt`, `.json`, `.md`) — this skill is about
technique on a specific call, not pipeline-wide data, so there's no CSV
mode.

### Transcript mode

```
claude "run first-call-rampup on ./calls/new-rep-call-1.txt"
```

1. Read the whole transcript before scoring anything.
2. Score each of the six dimensions in `references/rubric.md`
   independently — a strong pitch shouldn't offset a weak opening, or vice
   versa.
3. Run the rubric's reads-well-too check before finalizing: coaching
   feedback that reads as uniformly harsh is unlikely to be acted on.
4. Write the output in the exact shape under `## Output format`.

## Output format

For all six dimensions, in the rubric's numbered order:

```
**1. Strong opening** — Covered
Evidence: "before we dive in, I wanted to walk through what we usually
cover in a first call and then hear what's top of mind for you — sound
good?"

**2. Open-ended questioning** — Partial
Evidence: "so you're using spreadsheets for this right now?"
Note: mostly closed questions; one open "walk me through" moment mid-call
```

Close with exactly one **thing to work on before the next call** — not a
list, the single highest-leverage item, framed as coaching. No recap
section repeating all six scores again after this.

## Do not

- Don't accept a `.csv` file — decline it plainly and explain this skill
  audits rep technique on one call, not pipeline-wide data, rather than
  attempting a partial read.
- Don't let a wall of Missed items stand if the reads-well-too check flags
  it as uniformly harsh — loosen what counts as evidence before shipping
  the read.
- Don't add a "suggested talk track for the next call" section beyond the
  one closing coaching note — this skill audits the call that happened.

## Related skills

- **`deep-discovery`** — for the nine-dimension depth read once a rep is
  past ramp and the question shifts from technique to discovery quality.
- **`next-step-commitment`** — for auditing specifically how the call
  closed, independent of the rest of the technique read here.
- **`bant`** — for a qualification-outcome read (advance/no-advance)
  rather than this skill's coaching-on-technique read.

## Sample data

`assets/sample-transcript.txt` — synthetic early-tenure rep call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
