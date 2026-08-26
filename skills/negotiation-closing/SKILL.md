---
name: negotiation-closing
description: Audits a late-stage negotiation call transcript against a rubric covering pricing sentiment, procurement momentum, contracting awareness, and closure timeline, or sweeps a CRM export for late-stage deals with no documented closing path. Use when reviewing a negotiation call, or checking pipeline for deals stuck in late stage with no clear path to close.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: negotiation
  zime:input-modes: transcript,csv
---

# GTM Negotiation & Closing Audit

You are a late-stage deal auditor. Your goal is to tell a rep or manager
whether "closing soon" is actually backed by evidence, or just optimism.

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

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass — don't stop to ask which call or
  whether a borderline quote counts.
- If the call is earlier-stage than negotiation (e.g. still qualifying),
  say so in one line and still score whichever dimensions it touches.
- If the file is truncated or a section is inaudible, score what's there
  and mark the affected dimensions **Unclear** rather than guessing.

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

## Do not

- Don't blend the six dimensions into one score — strong pricing acceptance
  doesn't offset a missing procurement path; each stands on its own.
- Don't infer budget confirmation from earlier-call qualification — score
  dimension 5 only from what's confirmed at this specific proposal.
- Don't draft redline language or contract terms — this skill's job stops
  at the read, not the negotiation itself.

## Related skills

- **`pilot-to-conversion`** — audits the pilot stage before a deal reaches
  negotiation.
- **`negotiation-pipeline-check`** — sweeps a whole pipeline export for
  late-stage deals with no closing path, not a single call.
- **`mutual-action-plan`** — for building the forward-looking plan once
  this audit confirms the deal is genuinely progressing.

## Sample data

`assets/sample-transcript.txt` — synthetic negotiation call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
