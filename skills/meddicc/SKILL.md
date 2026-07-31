---
name: meddicc
description: Audits a B2B sales call transcript against the MEDDICC qualification framework (Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion, Competition), or sweeps a CRM export for deals missing MEDDICC fields. Use when qualifying an opportunity, prepping for a deal-review or forecast call, or checking whether a deal in the pipeline has real MEDDICC coverage.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: MEDDICC
  zime:vertical-aware: true
  zime:input-modes: transcript,csv
---

# MEDDICC Qualification Audit

Audits a sales conversation against the seven MEDDICC letters. Unlike the
stage skills in this repo, MEDDICC isn't tied to one point in the deal —
run it against a discovery call, a technical call, or a late-stage
negotiation, and it scores whatever letters that specific call could
plausibly have surfaced.

## When to use this

- Prepping for a forecast or deal-review call and want a structured read on
  qualification gaps before a manager asks.
- A rep wants to know which MEDDICC letters this call actually covered vs.
  which are still open.
- RevOps wants to sweep a pipeline export for deals missing MEDDICC fields
  before a QBR.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run meddicc on ./calls/acme-call.txt"
```

Read the transcript, then score it against each letter in
`references/rubric.md`. For every letter, output:

- **Status** — Covered / Partial / Missed / Not applicable to this call
- **Evidence** — a direct quote from the transcript. If a letter genuinely
  wasn't addressable on this specific call (e.g. a first discovery call
  can't reasonably cover Decision process in depth), say **Not applicable**
  rather than scoring it Missed — a MEDDICC read that penalizes every call
  for not being the final negotiation call is not useful.
- **Note** — one line, only if Partial or Missed

Close with the **single biggest qualification risk** if this deal were
forecast today, and what call or action would close it.

If `skills/vertical-context/` is available and a vertical is named, load the
matching reference pack and use its vocabulary/priors for Economic buyer and
Decision process — but never let the pack override what the transcript
actually shows; an inferred buyer title from the pack is not a substitute for
the transcript naming who signs.

### CSV mode (`.csv`)

```
claude "run meddicc on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality claim — say so explicitly. For
each deal row, check whether fields corresponding to the seven letters are
present and non-trivial. Output a table: deal name, deal value, letters
missing, sorted by deal value descending.

## Sample data

`assets/sample-transcript.txt` is a synthetic mid-stage qualification call —
run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
