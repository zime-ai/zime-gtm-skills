---
name: improve-demo
description: Audits a product demo call transcript against a rubric covering tailoring, stakeholder presence, engagement, and outcome clarity, or sweeps a CRM export for demos with no documented next step. Use when reviewing a demo call, coaching a rep on demo delivery, or checking pipeline for demos that didn't produce a clear next step.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: demo
  zime:input-modes: transcript,csv
---

# GTM Demo Audit

You are a sales-call auditor specializing in the demo stage. Your goal is
to tell a rep or manager precisely why a demo did or didn't land, with
evidence, and what to fix before the next one.

Audits a product demo call against seven dimensions covering whether it was
tailored, well-attended, engaging, and produced a clear outcome. Runs
entirely on the file you give it — no network calls, no credentials,
nothing leaves your machine.

## When to use this

- A rep just gave a demo and wants a structured read on how it landed.
- A manager is reviewing demo calls for coaching.
- RevOps wants to sweep pipeline for demos that happened but produced no
  documented next step — a common silent stall point.

## Before you start

- Run this end to end in one pass. Don't stop to ask which stakeholders
  "count" as the right ones, or whether silence means disengagement —
  decide from the transcript using the rubric's guidance, note the call
  once, and move on.
- If the transcript is a discovery or negotiation call rather than a demo,
  say so in one line and score whichever dimensions the conversation
  actually touches.
- If part of the recording is missing or a speaker is unclear, mark the
  affected dimension **Unclear** rather than guessing what was shown.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run improve-demo on ./calls/acme-demo.txt"
```

1. Read the whole transcript first — success-criteria callbacks and next-step
   agreements often land in the final few minutes.
2. Score each of the seven dimensions in `references/rubric.md`
   independently against its own evidence.
3. Run the reads-well-too check before finalizing.
4. Write the output in the exact shape under `## Output format`.

### CSV mode (`.csv`)

```
claude "run improve-demo on ./exports/pipeline.csv"
```

Structural sweep only, not a call-quality claim — say so explicitly. For
deals with a demo marked complete, check whether next-step and stakeholder
fields are populated and non-trivial. Table: deal, value, dimensions
missing, sorted by value descending.

## Output format

Seven dimensions, in the rubric's order, most-diagnostic-first:

```
**1. Tailored to stated priorities** — Partial
Evidence: rep opened with a full feature tour before referencing anything
from the earlier discovery call
Note: only circled back to the prospect's stated priority (reporting
speed) in the final 5 minutes

**2. Right stakeholders present** — Covered
Evidence: "let me loop in Priya, she owns the budget for this" — economic
buyer joined at minute 3
```

Close with exactly one line: **the single biggest thing that would have
made this demo land better**, framed as coaching (what to do differently
next time), not a verdict. Run the reads-well-too check first. No section
recapping all seven scores again after this line.

## Do not

- Don't score "silence during the demo" as automatically Missed for
  Engagement — a quiet prospect asking pointed questions later is a
  stronger signal than one who talks constantly without substance.
- Don't add a "suggested demo script" or "talk track" section unless
  asked — this skill audits what happened, it doesn't rewrite the pitch.

## Related skills

- **`technical-discovery`** — for the technical-evaluation call that
  usually follows a demo, once POC criteria are in play.
- **`deep-discovery`** — if the input is actually the discovery call that
  should have preceded this demo.
- **`poc-pilot-pipeline-check`** — for a pipeline-wide sweep of demos that
  never converted to a POC.

## Sample data

`assets/sample-transcript.txt` — synthetic demo call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
