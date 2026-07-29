---
name: negotiation-closing
description: Audits a late-stage negotiation call transcript against a rubric covering pricing sentiment, procurement momentum, contracting awareness, and closure timeline, or sweeps a CRM export for late-stage deals with no documented closing path. Use when reviewing a negotiation call, or checking pipeline for deals stuck in late stage with no clear path to close.
license: MIT
metadata:
  zime:category: new-business
  zime:input-modes: transcript,csv
---

# GTM Negotiation & Closing Audit

Audits a late-stage negotiation call against six dimensions covering
whether a deal is genuinely moving toward signature. Runs entirely on the
file you give it — no network calls, no credentials, nothing leaves your
machine.

## When to use this

- A rep just had a pricing or contract conversation and wants a read on
  whether it's really progressing.
- A manager is reviewing forecast-stage deals for how solid "closing soon"
  actually is.
- RevOps wants to sweep pipeline for late-stage deals with no documented
  closing path — a common forecast-inflation pattern.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run negotiation-closing on ./calls/acme-negotiation.txt"
```

Score against `references/rubric.md`. Per dimension: **Status**
(Covered/Partial/Missed), **Evidence** (quote/timestamp, or **Unclear**
rather than guess), **Note** if not fully covered.

Close with a realistic read on close timing versus what's being forecast.
Run the reads-well-too check first.

### CSV mode (`.csv`)

```
claude "run negotiation-closing on ./exports/pipeline.csv"
```

Structural sweep only. For deals in a negotiation/closing stage, check
whether closure-timeline and procurement fields are populated. Table: deal,
value, forecast close date, dimensions missing.

## Sample data

`assets/sample-transcript.txt` — synthetic negotiation call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
