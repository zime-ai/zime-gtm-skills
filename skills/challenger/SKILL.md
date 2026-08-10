---
name: challenger
description: Audits a B2B sales call transcript against the Challenger Sale framework (teach, tailor, take control, plus the commercial-teaching pitch arc), or sweeps a CRM export for deals with no teaching insight logged. Use when a rep leans on discovery-question skill but rarely brings a point of view, when prepping a rep for a competitive or status-quo-defending deal, or when a manager wants to know if a call taught the buyer something new rather than just restating their stated problem.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Challenger
  zime:input-modes: transcript,csv
---

# Challenger Sale Audit

Audits a sales conversation against the Challenger Sale's core claim: the
reps who win complex deals teach the buyer something they didn't already
know, tailor that teaching to the specific stakeholder in front of them, and
take control of the conversation instead of deferring entirely to the
buyer's stated agenda. Unlike a discovery-focused skill, this one scores
whether the rep pushed a point of view, not just whether they asked good
questions.

## When to use this

- A rep is skilled at discovery but the deal stalls on "we'll think about
  it" — check whether any call actually taught the buyer something.
- Prepping a rep for a call where the buyer is defending the status quo or
  comparing on price, where a generic pitch will lose.
- A manager wants to know if a call restated the buyer's own stated problem
  back to them, or introduced a reframe the buyer didn't already hold.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run challenger on ./calls/acme-call.txt"
```

Read the transcript, then score it against `references/rubric.md`. For
**Teach**, **Tailor**, and **Take control**, output:

- **Status** — Covered / Partial / Missed / Not applicable to this call
- **Evidence** — a direct quote from the transcript
- **Note** — one line, only if Partial or Missed

Then check the call against the **commercial-teaching pitch arc** (Warmer,
Reframe, Rational Drowning, Emotional Impact, New way, Our solution/a-ha):
list which steps appeared, which were skipped, and whether the reframe step
introduced a genuine insight or just repeated what the buyer already said.

Close with the **single biggest missed teaching opportunity** on this call —
a moment where the buyer stated a problem or assumption and the rep could
have reframed it but didn't.

### CSV mode (`.csv`)

```
claude "run challenger on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality claim — say so explicitly. Flag
deal rows with no logged teaching moment, insight, or point-of-view field
populated. Output a table: deal name, deal value, gap, sorted by deal value
descending.

## Sample data

`assets/sample-transcript.txt` is a synthetic mid-stage call — run the
skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
