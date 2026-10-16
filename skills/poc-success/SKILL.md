---
name: poc-success
description: Audits a POC or pilot exit review (did the pilot meet its agreed success criteria, and is the decision documented with evidence and sign-off), or sweeps a CRM export for deals past their POC end date with no recorded outcome. Use when a pilot has just wrapped and the user asks whether it genuinely passed, wants an exit review audited, or wants POCs that ran out the clock with no written outcome found in the pipeline.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: POC/pilot exit
  zime:input-modes: transcript,csv
---

# GTM POC/Pilot Exit Review

You are a POC exit auditor. Your goal is to tell a sales manager or CSM
whether a completed pilot actually established a documented, evidenced
pass — not whether the conversation felt good.

Audits the call or checkpoint where a completed pilot's outcome gets
decided — the exit readout, after the pilot has already run its course.
Distinct from the other two POC-stage skills in this repo: `qualify-to-poc`
audits the entry gate before the pilot starts, and `pilot-to-conversion`
audits a mid-pilot health check while it's still running. `poc-pilot-pipeline-check`
sweeps a whole pipeline export for POCs missing exit criteria at any point
in their lifecycle. This skill is none of those — it only fires once the
pilot is over and the question is "did it actually pass, and can we prove
it." Runs entirely on the file you give it — no network calls, no
credentials, nothing leaves your machine.

## When to use this

- A pilot just finished and a rep or CSM wants a structured read on whether
  the exit call actually established a pass, not just a good vibe.
- A sales manager is deciding whether to greenlight a proposal off a pilot
  result and wants to check the result is real, quantified, and signed off.
- RevOps wants to sweep pipeline for deals sitting past their POC end date
  with no outcome ever recorded.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which file or whether
  a borderline quote counts — decide from the transcript, note it once in
  the output, and move on.
- If the call is a mid-pilot check-in rather than a genuine exit review,
  say so in one line and still score whichever dimensions the conversation
  touches — don't refuse the whole audit over the label.
- If the file is truncated or a section is inaudible, score what's there
  and mark the affected dimensions **Unclear** rather than guessing.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run poc-success on ./calls/acme-poc-exit.txt"
```

Score the call against each dimension in `references/rubric.md`. For every
dimension, output:

- **Status** — Covered / Partial / Missed
- **Evidence** — a direct quote or timestamp. If you can't point to a
  specific line, mark **Unclear** rather than guess.
- **Note** — one line, only if Partial or Missed

Close with a single **pass / fail / inconclusive** read on the pilot, with
the one or two dimensions that decided it.

Before finalizing, read the rubric's "Rules and false positives" section and run the reads-well-too test in `references/rubric.md` —
if a call that was clearly a well-run, genuinely successful exit still
comes back mostly Missed, the rubric is reading too strictly.

### CSV mode (`.csv`)

```
claude "run poc-success on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality audit. For deals whose POC/pilot
end date has already passed, check whether an outcome field (result,
won/lost reason, exit status, or similar) is populated and non-trivial.
Output a table: deal name, deal value, POC end date, days past end date,
outcome field status — sorted by deal value descending. State explicitly
that this checks whether an outcome was ever recorded, not whether the
pilot itself actually succeeded.

## Do not

- Don't blend the eight dimensions into one overall score — a strong result
  doesn't offset a missing sponsor sign-off; each stands on its own.
- Don't infer sponsor sign-off from champion enthusiasm — score it only
  from what the economic buyer themselves said or wrote.
- Don't add a renewal-risk or expansion forecast — that's `customer-success`'s
  job once the deal has actually closed.

## Related skills

- **`qualify-to-poc`** — audits the entry gate before the pilot starts, not
  the exit.
- **`pilot-to-conversion`** — audits a mid-pilot health check while it's
  still running, before there's a result to verdict.
- **`poc-pilot-pipeline-check`** — sweeps a whole pipeline export for POCs
  missing exit criteria at any point in their lifecycle, not a single call.

## Sample data

`assets/sample-transcript.txt` — a short synthetic POC-exit call. Run
against it first before pointing this at anything of your own.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
