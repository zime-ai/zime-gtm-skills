---
name: qualify-to-poc
description: Audits the call or checkpoint that moves a qualified deal into POC or pilot kickoff (the go or no-go gate before pilot work starts) against five dimensions (success criteria, technical scope, stakeholder commitment, timeline and exit criteria, and resourcing). Or sweeps a CRM export for deals entering pilot stage without those fields set. Use when the user asks whether a deal is ready to start a POC, wants a POC-kickoff call reviewed, or wants pilots that started without a real plan found in the pipeline.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: qualify-to-poc
  zime:input-modes: transcript,csv
---

# GTM Qualify-to-POC Audit

You are a POC-readiness auditor. Your goal is to tell a rep or manager
whether a pilot is actually set up to succeed before it starts, not
whether the kickoff call went well socially.

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

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call to use or
  how to read an ambiguous moment — apply the rubric's guidance, decide,
  note the assumption once, and move on.
- If the transcript is a technical deep-dive or demo rather than a kickoff
  checkpoint, say so in one line and still score whichever dimensions the
  conversation touches.
- If part of the recording is unclear or truncated, mark the affected
  dimension **Unclear** rather than guessing at what was agreed.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run qualify-to-poc on ./calls/acme-poc-kickoff.txt"
```

1. Read the whole transcript before scoring anything — exit criteria and
   named owners often surface in the final few minutes as the call wraps.
2. Score each of the five dimensions in `references/rubric.md`
   independently. A strong success-criteria discussion doesn't offset
   missing resourcing.
3. Read each dimension's "does not count" line. A criterion, scope, or date that only the rep states does not count until the buyer agrees. Then run the rubric's reads-well-too test before finalizing, in both directions.
4. Write the output in the exact shape under `## Output format`.

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

## Output format

For all five dimensions, in the rubric's order:

```
**1. Success criteria defined and agreed** — Covered
Evidence: "so we're aligned that success means the integration syncs
inventory counts within five minutes, no manual reconciliation, across
both warehouses by the end of the three weeks"

**2. Technical scope agreed** — Partial
Evidence: "let's start with the West warehouse system" — no mention of
whether East warehouse or the returns workflow is in or out of scope
Note: scope named for one system, silent on the rest of what could expand
```

Close with exactly one line: a **Go** / **No-go** / **Needs one more call**
read, naming the one or two dimensions that decided it.

## Do not

- Don't let a strong Success criteria score offset a Missed on Resourcing
  or Stakeholders — all five dimensions are independent gates, not
  contributors to one blended readiness score.
- Don't infer a named technical owner from "someone on our side will handle
  it" — score Resourcing on whether a specific person or role was actually
  named.
- Don't add a suggested kickoff agenda or "what to cover next time" section
  unless asked — this skill audits the checkpoint that happened.

## Related skills

- **`meeting-to-qualify`** — for establishing the deal is real in the first
  place, before this skill's go/no-go gate applies.
- **`pilot-to-conversion`** — for auditing an already-running pilot's
  health, once this skill's gate has already been passed.
- **`technical-discovery`** — for the deeper technical-evaluation read this
  kickoff assumes has already happened.

## Sample data

`assets/sample-transcript.txt` — a short synthetic POC-kickoff call. Run
against it first before pointing this at anything of your own.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
