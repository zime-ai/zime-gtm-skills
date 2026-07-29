---
name: improve-demo
description: Audits a product demo call transcript against a rubric covering tailoring, stakeholder presence, engagement, and outcome clarity, or sweeps a CRM export for demos with no documented next step. Use when reviewing a demo call, coaching a rep on demo delivery, or checking pipeline for demos that didn't produce a clear next step.
license: MIT
metadata:
  zime:category: new-business
  zime:input-modes: transcript,csv
---

# GTM Demo Audit

Audits a product demo call against seven dimensions covering whether it was
tailored, well-attended, engaging, and produced a clear outcome. Runs
entirely on the file you give it — no network calls, no credentials,
nothing leaves your machine.

## When to use this

- A rep just gave a demo and wants a structured read on how it landed.
- A manager is reviewing demo calls for coaching.
- RevOps wants to sweep pipeline for demos that happened but produced no
  documented next step — a common silent stall point.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run improve-demo on ./calls/acme-demo.txt"
```

Score against `references/rubric.md`. Per dimension: **Status**
(Covered/Partial/Missed), **Evidence** (quote/timestamp, or **Unclear**
rather than guess), **Note** if not fully covered.

Close with the single biggest thing that would have made this demo land
better. Run the reads-well-too check first.

### CSV mode (`.csv`)

```
claude "run improve-demo on ./exports/pipeline.csv"
```

Structural sweep only. For deals with a demo marked complete, check whether
next-step and stakeholder fields are populated. Table: deal, value,
dimensions missing, sorted by value descending.

## Sample data

`assets/sample-transcript.txt` — synthetic demo call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
