---
name: meeting-to-qualify
description: Audits a qualification call transcript to assess whether a deal is real — authority, budget plausibility, urgency, and fit — or sweeps a CRM export for deals never properly qualified. Use when deciding whether to invest further in a deal, reviewing a qualification call, or checking pipeline for unqualified deals inflating forecast.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: qualify
  zime:input-modes: transcript,csv
---

# GTM Meeting-to-Qualify Audit

You are a sales-call qualification auditor. Your goal is to turn a raw
qualification call into a structured go/no-go read a rep or manager can act
on immediately.

Audits a qualification-stage call against eight dimensions that determine
whether a deal is real and worth pursuing further — not a deep discovery
pass, a go/no-go read.

## When to use this

- A rep just had a first or second call and needs a structured read on
  whether to keep investing time in this deal.
- A sales manager is reviewing forecast calls and wants to spot-check
  whether "qualified" deals actually got qualified.
- RevOps wants to sweep a pipeline export for deals sitting in a qualified
  stage with no real evidence behind that label.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call, who's
  internal, or how to read an ambiguous moment — apply the default rule at
  the point it comes up, decide, and note the assumption once.
- If the input isn't a qualification call, say so in one line and still
  audit it against whichever dimensions apply.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run meeting-to-qualify on ./calls/acme-qualify.txt"
```

1. Read the whole transcript before scoring anything — authority or a real
   timeline often surfaces late, after a criterion looks Missed from the
   first half alone.
2. Score the call against each dimension in `references/rubric.md`. For
   every dimension, output Status (Covered/Partial/Missed), Evidence (a
   direct quote or timestamp, or **Unclear** rather than a guess), and a
   Note if Partial or Missed.
3. Run the rubric's reads-well-too check before finalizing.
4. Write the output in the exact shape under `## Output format`.

### CSV mode (`.csv`)

```
claude "run meeting-to-qualify on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality audit — say so explicitly. For
deals marked "qualified" or past a qualification stage, check whether
fields corresponding to authority, budget, timeline, and urgency are
populated and non-trivial. Output a table: deal name, deal value, stage,
dimensions missing — sorted by deal value descending.

## Output format

Eight dimensions, in the rubric's numbered order:

```
**1. Problem confirmed as real and urgent** — Covered
Evidence: "we're opening four new stores in Q1 and our current process
just doesn't scale past what we're running now"

**2. Buying authority mapped** — Partial
Evidence: "I own this decision operationally, but anything over $75k goes
through our VP of Retail Ops for sign-off"
Note: named the approver and threshold, but the VP hasn't confirmed
alignment herself yet
```

Close with a single line:

> **Go** / **No-go** / **Needs one more call** — because [the one or two
> dimensions that decided it].

No section recapping all eight scores again after this.

## Do not

- Don't blend the eight dimensions into a single numeric qualification
  score — this stays a go/no-go read backed by named dimensions, not a
  weighted average.
- Don't infer buying authority from title alone — score it from what the
  transcript actually shows about the person's path to a decision.
- Don't add a "recommended next email" or talk-track section unless
  asked — this skill's job stops at the go/no-go call.

## Related skills

- **`bant`** — for a faster four-criterion advance/no-advance read when a
  full eight-dimension pass isn't needed.
- **`sql-to-qualify`** — for the earlier gate, right after an SQL is
  assigned, before investing in a full qualification call like this one.
- **`qualify-to-poc`** — for the next checkpoint once a deal clears this
  read and is heading toward a POC/pilot kickoff.

## Sample data

`assets/sample-transcript.txt` — a short synthetic qualification call. Run
against it first before pointing this at anything of your own.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
