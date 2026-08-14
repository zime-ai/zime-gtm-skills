---
name: competitor-battlecard
description: Reads a single sales call transcript and writes a battlecard for whichever competitor (or status quo) the buyer actually named on that call — how they framed it, what they said it does better or differently, what the rep countered with, and what went unanswered, citing every line to the transcript. Use right after a call surfaces a competitive frame, to arm the rep for the next call or brief a manager on it — not to score how well the rep handled the objection (see challenger) or to write a post-close loss review (see win-loss-brief).
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript
---

# Competitor Battlecard

Writes a battlecard for whichever competitor was actually named on a call —
a reusable artifact a rep could bring into the next call, not a grade of how
well this one was handled. This is a phase-2 deal-intelligence skill, for
one in-flight deal at a time. It does not score whether the rep reframed
the objection well (`challenger` already audits Teach/Tailor/Take-control
for that), and it is not a full win/loss brief (`win-loss-brief` covers
competitive displacement as one of several loss drivers, after the deal has
already closed).

**Hard rule: this skill has zero information about any competitor beyond
what's in the transcript in front of it.** It may only state what the
transcript says. No outside knowledge of the named competitor's real
product, pricing, or actual weaknesses — see `references/rubric.md` for
what this rules out.

## When to use this

- A call just named a competitor (or the buyer is defending doing nothing)
  and the rep wants a reusable card for the next conversation.
- A manager wants to know exactly how a specific competitive frame came up
  on a call, without re-litigating the whole call.
- Someone is prepping for a follow-up call and needs the buyer's actual
  competitor claims restated with citations, not paraphrased from memory.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run competitor-battlecard on ./calls/acme-call.txt"
```

Read the transcript. If no competitor (including "doing nothing"/status
quo — see `references/rubric.md`) is named anywhere in it, stop after step
1 and say so plainly. Do not invent a hypothetical competitive frame to
fill the rest of the template.

If a competitor is named, write:

1. **Competitor named** — quote where/how they came up.
2. **How the buyer framed them** — cited.
3. **What the buyer said the competitor does better/differently** — cited,
   each claim tagged **clear** or **tentative** using the confidence test
   in `references/rubric.md` (the same test `win-loss-brief` uses for
   driver confidence).
4. **What the rep countered with** — cited. If the rep never countered a
   claim, it does not appear here — it belongs in section 5 instead.
5. **Left unanswered** — any claim from section 3 the rep never addressed
   anywhere later in the same call. If the rep addressed everything, say so
   rather than forcing an entry here.

Every claim in every section cites its quote or timestamp. A claim with no
citation does not ship.

## Sample data

`assets/sample-transcript.txt` is a synthetic mid-stage call naming a
synthetic competitor, with one buyer claim about it the rep never
addresses. Run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
