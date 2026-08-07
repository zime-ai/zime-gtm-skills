---
name: bant
description: Audits a B2B sales call transcript against the BANT qualification framework (Budget, Authority, Need, Timeline), or sweeps a CRM export for deals missing BANT fields. Use when qualifying an early-stage lead, deciding whether to advance a deal past a first call, or checking a pipeline export for unqualified opportunities.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: BANT
  zime:input-modes: transcript,csv
---

# BANT Qualification Audit

Audits a sales conversation against the four BANT criteria. Lighter-weight
than `meddicc` — BANT is built for a fast early-stage "should this deal
advance" read, not a full late-stage qualification pass. Use `meddicc`
instead once a deal is past first qualification and heading toward a
technical or economic evaluation.

## When to use this

- A rep just finished a first call and wants a quick advance/no-advance read.
- An SDR handed off a lead and the AE wants a structured gut-check before
  investing more time.
- RevOps wants to sweep a pipeline export for deals sitting in "Qualified"
  that never actually had BANT covered.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run bant on ./calls/first-call.txt"
```

Read the transcript, then score it against each criterion in
`references/rubric.md`. For every criterion, output:

- **Status** — Covered / Partial / Missed
- **Evidence** — a direct quote from the transcript, or mark **Unclear**
  rather than guess
- **Note** — one line, only if Partial or Missed

Close with a single **Advance / Advance with a specific follow-up question /
Do not advance yet** call, and the one thing that would change your answer.

### CSV mode (`.csv`)

```
claude "run bant on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality claim — say so explicitly. For
each deal row, check whether fields for Budget, Authority, Need, and
Timeline are present and non-trivial. Output a table: deal name, deal value,
criteria missing, sorted by deal value descending.

## Sample data

`assets/sample-transcript.txt` is a synthetic first qualification call — run
the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
