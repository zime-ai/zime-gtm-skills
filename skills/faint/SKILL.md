---
name: faint
description: Audits a B2B sales call transcript against the FAINT qualification framework (Funds, Authority, Interest, Need, Timing), or sweeps a CRM export for deals missing FAINT fields. Use when a prospect hasn't articulated a clear need yet but shows financial capacity and curiosity, or when deciding whether a demand-driven lead is worth advancing before a formal need is on record.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: FAINT
  zime:input-modes: transcript,csv
---

# FAINT Qualification Audit

Audits a sales conversation against the five FAINT criteria. FAINT departs
from `bant` in one deliberate way: it scores Interest ahead of Need, and
reads Funds as general financial capacity rather than an allocated budget.
It's built for prospects who haven't stated a need yet, or don't have
budget set aside, but who show real financial capacity and can be made
curious. Use `bant` instead once a prospect has already named a specific
problem — FAINT is for the call before that, where the rep's job is to
generate interest, not confirm an existing one.

## When to use this

- A lead came in through outbound or a campaign with no stated problem, and
  the question is whether they're worth continuing to work rather than
  whether they're already sold.
- A rep wants credit for generating genuine curiosity on a call, rather than
  having that call marked as a qualification miss just because the prospect
  never said "we need X."
- RevOps wants to sweep a pipeline export for demand-driven leads sitting
  in "Qualified" that never actually had FAINT covered.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run faint on ./calls/acme-call.txt"
```

Read the transcript, then score it against each criterion in
`references/rubric.md`. For every criterion, output:

- **Status** — Covered / Partial / Missed
- **Evidence** — a direct quote from the transcript
- **Note** — one line, only if Partial or Missed

Score Need last, and read it against what Interest already established on
the call — see the "Interest before Need" section of the rubric before
marking Need Missed on a call where genuine curiosity was clearly built.

Close with the **single biggest qualification risk** if this deal were
forecast today, and what call or action would close it.

### CSV mode (`.csv`)

```
claude "run faint on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality claim — say so explicitly. For
each deal row, check whether fields corresponding to the five FAINT
criteria are present and non-trivial. Output a table: deal name, deal
value, criteria missing, sorted by deal value descending.

## Sample data

`assets/sample-transcript.txt` is a synthetic outbound discovery call — run
the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
