---
name: technical-discovery
description: Audits a technical/solution-fit call transcript against a rubric covering current stack, future-state vision, POC scope, and technical stakeholders, or sweeps a CRM export for deals missing technical-fit data. Use when reviewing a technical discovery or solution-engineering call, or checking pipeline for deals heading into a POC without technical groundwork.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: technical-discovery
  zime:input-modes: transcript,csv
---

# GTM Technical Discovery Audit

Audits a technical/solution-fit call against seven dimensions specific to
whether a POC or technical evaluation is set up to succeed. Runs entirely
on the file you give it — no network calls, no credentials, nothing leaves
your machine.

## When to use this

- A solutions engineer or AE just ran a technical discovery call and wants
  a structured read before scoping a POC.
- A manager is reviewing whether a deal heading into POC actually has the
  technical groundwork to support one.
- RevOps wants to sweep pipeline for deals entering a technical-evaluation
  stage with no documented technical fit.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run technical-discovery on ./calls/acme-tech-disco.txt"
```

Score against `references/rubric.md`. Per dimension: **Status**
(Covered/Partial/Missed), **Evidence** (quote or timestamp, or mark
**Unclear** rather than guess), **Note** if not fully covered.

Close with whether this deal is ready to scope a POC, and what's missing if
not. Run the reads-well-too check in `references/rubric.md` first.

### CSV mode (`.csv`)

```
claude "run technical-discovery on ./exports/pipeline.csv"
```

Structural sweep only. For deals in or entering a technical-evaluation
stage, check whether fields for current stack, success criteria, and
technical stakeholders are populated. Table: deal, value, dimensions
missing, sorted by value descending.

## Sample data

`assets/sample-transcript.txt` — synthetic technical discovery call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
