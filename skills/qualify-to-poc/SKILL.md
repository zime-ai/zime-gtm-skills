---
name: qualify-to-poc
description: Audits the call/checkpoint that moves a qualified deal into POC/pilot kickoff — the go/no-go gate before pilot work starts — against five dimensions covering success criteria, technical scope, stakeholder commitment, timeline/exit criteria, and resourcing. Or sweeps a CRM export for deals entering pilot stage without those fields set. Use when deciding whether a deal is actually ready to start a POC, reviewing a POC-kickoff call, or checking pipeline for pilots that started without a real plan.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: qualify-to-poc
  zime:input-modes: transcript,csv
---

# GTM Qualify-to-POC Audit

Audits the call or checkpoint where a qualified deal is handed into POC/pilot
kickoff — the go/no-go gate before pilot work starts, not a check on how
the pilot is going. Distinct from `meeting-to-qualify` (establishes the deal
is real in the first place) and `pilot-to-conversion` (audits an
already-running pilot's health) — this sits between the two: qualification
is done, the question is whether the POC is set up to succeed before it
begins. Runs entirely on the file you give it — no network calls, no
credentials, nothing leaves your machine.

## When to use this

- A rep just had a POC-kickoff call and wants a structured read on whether
  the pilot is actually set up to succeed, or is starting on hope.
- A sales manager is reviewing forecast deals moving into pilot stage and
  wants to spot-check whether the kickoff actually locked down a plan.
- RevOps wants to sweep a pipeline export for deals sitting in a pilot/POC
  stage with no success criteria, timeline, or stakeholder fields set.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run qualify-to-poc on ./calls/acme-poc-kickoff.txt"
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
if a call that was clearly a well-run kickoff still comes back mostly
Missed, the rubric is reading too strictly.

### CSV mode (`.csv`)

```
claude "run qualify-to-poc on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality audit. For deals marked as
entering or in a pilot/POC stage, check whether fields corresponding to
success criteria, technical scope, stakeholders, timeline/exit criteria, and
resourcing are populated and non-trivial. Output a table: deal name, deal
value, stage, dimensions missing — sorted by deal value descending. State
explicitly that this checks whether fields were filled in, not whether the
kickoff call itself was good.

## Sample data

`assets/sample-transcript.txt` — a short synthetic POC-kickoff call. Run
against it first before pointing this at anything of your own.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
