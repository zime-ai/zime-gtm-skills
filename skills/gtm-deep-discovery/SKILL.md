---
name: gtm-deep-discovery
description: Audits an early-stage B2B sales discovery call transcript against a discovery-quality rubric, or sweeps a CRM deal export for missing discovery fields. Use when reviewing a discovery/early-stage sales call, coaching a rep on discovery quality, or checking a pipeline export for deals with thin discovery.
license: MIT
metadata:
  zime:category: new-business
  zime:input-modes: transcript,csv
---

# GTM Deep Discovery Audit

Audits early-stage discovery calls against nine dimensions of what a
thorough discovery conversation covers. Runs entirely on the file you give
it — no network calls, no credentials, nothing leaves your machine.

## When to use this

- A rep just finished a discovery call and wants a structured read on what
  they covered and missed.
- A manager is reviewing a call before a coaching session.
- RevOps wants to sweep a pipeline export for deals that never got a proper
  discovery pass.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run gtm-deep-discovery on ./calls/acme-discovery.txt"
```

Read the transcript, then score the call against each dimension in
`references/rubric.md`. For every dimension, output:

- **Status** — Covered / Partial / Missed
- **Evidence** — a direct quote or timestamp from the transcript. If you
  cannot point to a specific line that justifies the status, mark the
  dimension **Unclear** instead of guessing — an uncited finding is worse
  than no finding, because it's untrustworthy the first time it's wrong.
- **Note** — one line, only if the status is Partial or Missed

Close with **2-3 highest-leverage next steps** — not a summary of every
gap, the ones that would have moved this specific deal forward most.

Run `references/rubric.md`'s "reads well too" check before finalizing: if a
transcript that clearly covered discovery thoroughly still comes back with
several Missed dimensions, the read is biased toward finding fault — widen
what counts as evidence before reporting.

### CSV mode (`.csv`)

```
claude "run gtm-deep-discovery on ./exports/pipeline.csv"
```

This is a **structural hygiene sweep**, not a call-quality audit — CRM
fields can't show whether a rep actually probed pain on a call, only
whether someone typed something into a field. Say this explicitly in the
output.

For each deal row, check whether fields corresponding to the rubric's
dimensions (pain/impact notes, decision process, budget, timeline,
competition) are present and non-trivial (not a single word, not a
placeholder). Output a table: deal name, deal value, dimensions missing,
sorted by deal value descending so the highest-value gaps surface first.

## Sample data

`assets/sample-transcript.txt` is a short synthetic discovery call — run
the skill against it first to see real output before pointing it at
anything of your own.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
