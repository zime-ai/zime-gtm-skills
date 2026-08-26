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

You are a sales-call qualification auditor. Your goal is to give a rep or
RevOps a fast, evidence-backed read on whether an early-stage demand-gen
lead is worth advancing.

Audits a sales conversation against the five FAINT criteria. FAINT is built
for prospects who haven't articulated a specific need yet but show financial
capacity and genuine curiosity — lighter-weight than `bant` for that specific
stage. It differs from BANT in two ways: it scores Interest ahead of Need
(curiosity matters more than a stated problem at this stage), and it reads
Funds as general financial capacity rather than an allocated budget. Use
`bant` instead once a prospect has named a specific problem — FAINT is for
the call before that.

## When to use this

- A lead came in through outbound or a campaign with no stated problem, and
  the question is whether they're worth continuing to work rather than
  whether they're already sold.
- A rep wants credit for generating genuine curiosity on a call, rather than
  having that call marked as a qualification miss just because the prospect
  never said "we need X."
- RevOps wants to sweep a pipeline export for demand-driven leads sitting
  in "Qualified" that never actually had FAINT covered.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which file or whether a
  borderline quote counts — decide from the transcript, note the call once
  in the output, and move on.
- If the transcript is a demo, renewal, or support call rather than a first
  outbound discovery, say so in one line and still score whichever FAINT
  criteria the conversation happens to touch.
- If the file is truncated or a section is inaudible/unclear, score what's
  there and mark the affected criterion **Unclear** rather than guessing at
  what was probably said. Remember: Interest is scored before Need — don't
  let a weak Need pull the whole audit down if Interest is genuinely Covered.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run faint on ./calls/outbound-call.txt"
```

1. Read the whole transcript before scoring anything — a Funds signal or a
   Timing trigger often surfaces late, after the criterion looks Missed from
   the first half alone.
2. Score each of the five criteria in `references/rubric.md` independently.
   Don't let strong Interest inflate a weak Funds, or vice versa.
3. Run the rubric's reads-well-too check before finalizing.
4. Write the output in the exact shape under `## Output format`.

### CSV mode (`.csv`)

```
claude "run faint on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality claim — say so explicitly. For
each deal row, check whether fields corresponding to the five FAINT
criteria are present and non-trivial (not blank, not a placeholder like
"TBD"). Output a table: deal name, deal value, criteria missing, sorted by
deal value descending.

## Output format

For every criterion, in this order — Funds, Authority, Interest, Need, Timing:

```
**Funds** — Covered
Evidence: "We're not tight on cash, if it was worth it we could probably just fold it into the ops tooling spend"

**Authority** — Partial
Evidence: "I'd bring it to my director if we ever got serious about it"
Note: influencer with a real path to decision-maker, not the final approver
```

Then close with exactly one line:

> **Advance** / **Advance with a follow-up on [criterion]** / **Do not
> advance yet** — because [the one signal that drove this call], and here's
> the one question that would change it: [specific follow-up].

No recap section repeating all five scores again after this — the call
above is the deliverable, not a summary of it.

## Do not

- Don't blend the five letters into a single "qualification score" — FAINT
  stays five separate reads, not one number.
- Don't infer Authority from title alone ("Ops Lead" isn't automatically the
  economic buyer) — score it from what the transcript actually shows about
  their path to a decision.
- Don't treat "no stated Need" as a disqualifying miss if Interest is
  genuinely Covered — that's the whole premise of FAINT. When Interest is
  strong, frame Need as "not yet surfaced" and name the call that would
  surface it.
- Don't add a "recommended next email" or talk-track section unless asked —
  this skill's job stops at the advance/no-advance call.

## Related skills

- **`bant`** — once a prospect has named a specific problem, BANT's four
  criteria replace FAINT's five for a faster early-stage read.
- **`meddicc`** — once a deal is past first qualification and multiple
  stakeholders are in play, MEDDICC's seven letters replace both BANT and
  FAINT.
- **`sandler`** — for a different qualification lens (buyer's motivation
  and reluctance, not just their stated problem).

## Sample data

`assets/sample-transcript.txt` is a synthetic outbound discovery call — run
the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
