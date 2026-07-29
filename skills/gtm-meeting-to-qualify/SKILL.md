---
name: gtm-meeting-to-qualify
description: Audits a qualification call transcript to assess whether a deal is real — authority, budget plausibility, urgency, and fit — or sweeps a CRM export for deals never properly qualified. Use when deciding whether to invest further in a deal, reviewing a qualification call, or checking pipeline for unqualified deals inflating forecast.
license: MIT
metadata:
  zime:category: new-business
  zime:input-modes: transcript,csv
---

# GTM Meeting-to-Qualify Audit

Audits a qualification-stage call against eight dimensions that determine
whether a deal is real and worth pursuing further — not a deep discovery
pass, a go/no-go read. Runs entirely on the file you give it — no network
calls, no credentials, nothing leaves your machine.

## When to use this

- A rep just had a first or second call and needs a structured read on
  whether to keep investing time in this deal.
- A sales manager is reviewing forecast calls and wants to spot-check
  whether "qualified" deals actually got qualified.
- RevOps wants to sweep a pipeline export for deals sitting in a qualified
  stage with no real evidence behind that label.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run gtm-meeting-to-qualify on ./calls/acme-qualify.txt"
```

Score the call against each dimension in `references/rubric.md`. For every
dimension, output:

- **Status** — Covered / Partial / Missed
- **Evidence** — a direct quote or timestamp. If you can't point to a
  specific line, mark **Unclear** rather than guess.
- **Note** — one line, only if Partial or Missed

Close with a single **go / no-go / needs one more call** read, with the one
or two dimensions that decided it.

Before finalizing, run the reads-well-too check in `references/rubric.md` —
if a call that was clearly a strong, real deal still comes back mostly
Missed, the rubric is reading too strictly.

### CSV mode (`.csv`)

```
claude "run gtm-meeting-to-qualify on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality audit. For deals marked
"qualified" or past a qualification stage, check whether fields
corresponding to authority, budget, timeline, and urgency are populated and
non-trivial. Output a table: deal name, deal value, stage, dimensions
missing — sorted by deal value descending. State explicitly that this
checks whether fields were filled in, not whether the call itself was good.

## Sample data

`assets/sample-transcript.txt` — a short synthetic qualification call. Run
against it first before pointing this at anything of your own.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
