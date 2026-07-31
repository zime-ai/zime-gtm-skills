---
name: pilot-to-conversion
description: Audits a pilot/POC check-in call transcript against a rubric covering plan alignment, technical readiness, user engagement, and results against criteria, or sweeps a CRM export for pilots at risk of stalling before conversion. Use when reviewing a pilot check-in call, or checking pipeline for POCs that have run long without a documented result.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: pilot
  zime:input-modes: transcript,csv
---

# GTM Pilot-to-Conversion Audit

Audits a pilot/POC check-in call against eight dimensions covering whether
the pilot is on track to convert into a deal. Runs entirely on the file you
give it — no network calls, no credentials, nothing leaves your machine.

## When to use this

- A rep or CSM is checking in mid-pilot and wants a structured read on
  whether it's on track.
- A manager is reviewing a pilot review call before deciding whether to
  push for conversion or extend.
- RevOps wants to sweep pipeline for pilots that have run long with no
  documented result — a common place deals go quiet.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run pilot-to-conversion on ./calls/acme-pilot-checkin.txt"
```

Score against `references/rubric.md`. Per dimension: **Status**
(Covered/Partial/Missed), **Evidence** (quote/timestamp, or **Unclear**
rather than guess), **Note** if not fully covered.

Close with an on-track / at-risk / stalled read, and what's driving it. Run
the reads-well-too check first.

### CSV mode (`.csv`)

```
claude "run pilot-to-conversion on ./exports/pipeline.csv"
```

Structural sweep only. For deals in a pilot/POC stage, check whether
success-criteria and results fields are populated, and flag pilots open
longer than a typical cycle with no result recorded. Table: deal, value,
days in pilot, dimensions missing.

## Sample data

`assets/sample-transcript.txt` — synthetic pilot check-in call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
