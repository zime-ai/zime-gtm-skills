---
name: deep-discovery
description: Audits an early-stage B2B sales discovery call transcript against a nine-dimension discovery rubric and credits only what the buyer actually said, or sweeps a CRM deal export for missing discovery fields. Use when the user asks to review a discovery call, score discovery quality, coach a rep on discovery, find what the rep skipped, spot gaps in pain, trigger, budget or decision process, or find deals with thin discovery in a pipeline export.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: discovery
  zime:input-modes: transcript,csv
---

# GTM Deep Discovery Audit

You are a sales-call auditor specializing in early-stage discovery. Your
goal is to tell a rep or manager exactly what a discovery call surfaced and
what it left on the table, with evidence for every claim.

Audits early-stage discovery calls against nine dimensions of what a
thorough discovery conversation covers. Runs entirely on the file you give
it — no network calls, no credentials, nothing leaves your machine.

## When to use this

- A rep just finished a discovery call and wants a structured read on what
  they covered and missed.
- A manager is reviewing a call before a coaching session.
- RevOps wants to sweep a pipeline export for deals that never got a proper
  discovery pass.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call to use, who
  counts as internal, or how to read an ambiguous moment — apply the
  rubric's guidance, decide, note the assumption once, and move on.
- If the transcript is a demo or negotiation call rather than discovery,
  say so in one line and still score whichever dimensions the conversation
  touches. If it is not a sales call at all (an internal meeting, a
  candidate interview), say so and stop.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run deep-discovery on ./calls/acme-discovery.txt"
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

Scoring rules, applied before you write each status:

- Evidence is what the buyer said, in a line that is about that dimension.
  A claim from the rep does not count unless the buyer agrees on the call.
  Never use one line as evidence for two dimensions. Never count a line
  that only hints at a dimension (a launch mentioned while explaining ticket
  volume is not a budget or decision-date signal).
- When no line addresses a dimension, the status is Missed. Do not soften
  it to Partial because the call felt thorough elsewhere.
- Partial needs a quotable line that names the dimension but stays vague.
  When you cannot quote that line, it is Missed.
- A Covered needs the specifics the rubric names for it (a number, a named
  person, a named tool, a dated event), not a general statement.
- Each rubric entry has a "does not count" line. Read it before you write
  Covered or Partial.

Run the rubric's "reads-well-too" test before you finalize, in both
directions. A call that clearly covered discovery thoroughly must not come
back with several Missed dimensions, so widen what counts as evidence when it
does. A call that never raised a dimension must not get credit for it, so
cut any status whose evidence line fails the rules above.

For each Missed or Partial dimension, the note can end with the rubric's
"strong call" move, as one short question the rep can ask next time.

### CSV mode (`.csv`)

```
claude "run deep-discovery on ./exports/pipeline.csv"
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

## Output format

Nine dimensions, in the rubric's numbered order:

```
**1. Pain & business impact** — Covered
Evidence: "that costs us about 10 hours a week across the team re-entering
data that already exists in the other system"

**2. Current state & tooling** — Partial
Evidence: mentioned "we use spreadsheets for most of this" but never
detailed the actual workflow
Note: baseline named but not detailed enough to credibly show improvement
against

**3. Trigger — why now** — Missed
Evidence: none. No line gives a reason to act now rather than later.
Note: the earliest sign this deal may stall; ask what changed this quarter
```

Close with **2-3 highest-leverage next steps** — not a summary of every
gap, the ones that would have moved this specific deal forward most. No
section recapping all nine scores again after this.

## Do not

- Don't treat "who else are you talking to" asked bluntly as evidence
  against the rep — score dimension 8 on whether competitive context
  surfaced, not on how directly it was asked.
- Don't add a "suggested talk track for the next call" section unless
  asked — this skill audits the call that happened.

## Related skills

- **`bant`** — for a faster four-criterion advance/no-advance read instead
  of this skill's nine-dimension depth.
- **`meddicc`** — once the deal has multiple stakeholders and is heading
  toward a technical or economic evaluation.
- **`improve-demo`** — for the demo call that should follow a good
  discovery pass.

## Sample data

`assets/sample-transcript.txt` is a short synthetic discovery call — run
the skill against it first to see real output before pointing it at
anything of your own. `assets/sample-pipeline.csv` is a synthetic pipeline
export (deliberately missing fields) for trying CSV mode.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
