---
name: meddpicc
description: Audits a B2B sales call transcript against the MEDDPICC qualification framework (Metrics, Economic buyer, Decision criteria, Decision process, Paper process, Identify pain, Champion, Competition), or sweeps a CRM export for deals missing MEDDPICC fields. Use when a deal is heading toward legal/procurement/security review and needs a read on the close-mechanics letter that MEDDICC doesn't cover, prepping for a late-stage forecast call, or checking whether a pipeline deal has a mapped signature path.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: MEDDPICC
  zime:input-modes: transcript,csv
---

# MEDDPICC Qualification Audit

You are a late-stage deal qualification auditor. Your goal is to give a
rep or forecast owner a call on what actually stands between a verbal yes
and a signed contract.

Audits a sales conversation against the eight MEDDPICC letters. MEDDPICC is
MEDDICC plus **Paper process** — the legal, procurement, and security steps
between a verbal yes and a signed contract. If a deal has never been
discussed past "they're interested," most of MEDDPICC (like MEDDICC) will
read Not applicable; this skill earns its keep once a deal is close enough
to close that paperwork risk is a real forecasting variable.

## When to use this vs. `meddicc`

- Run `meddicc` for qualification during discovery and mid-funnel calls —
  the seven letters it covers (this skill covers the same seven, worded
  identically) don't need a paperwork lens yet.
- Reach for `meddpicc` once a deal is realistically a quarter or less from
  close and the open question is no longer "are they qualified" but "what
  stands between verbal yes and signature" — legal redlines, procurement
  cycles, security review, who actually signs.
- Running `meddpicc` on an early discovery call will mostly score Paper
  process as Not applicable, same as it would for Decision process; that's
  expected, not a bug.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call, who's
  internal, or how to read an ambiguous moment — apply the default rule at
  the point it comes up, decide, and note the assumption once.
- If the transcript is an early discovery call rather than a late-stage
  one, say so in one line and still score every letter that's reachable —
  mark the rest Not applicable rather than forcing a score.
- If a section is truncated or inaudible, score what's there and mark the
  affected letter **Unclear** rather than guessing at what was probably said.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run meddpicc on ./calls/acme-call.txt"
```

1. Read the whole transcript before scoring anything — a signer name or a
   procurement detail often surfaces late, after a letter looks Missed from
   the first half alone.
2. Score each of the eight letters in `references/rubric.md` independently.
   Don't let a strong Metrics or Champion read inflate a weak Paper process,
   or vice versa.
3. For a letter that genuinely wasn't reachable at this call's stage (e.g.
   Paper process on a first discovery call, before anyone has discussed a
   timeline to close), mark it **Not applicable** rather than Missed —
   that distinction is the whole point of reading MEDDPICC cumulatively
   across a deal's call history.
4. Run the rubric's reads-well-too check before finalizing.
5. Write the output in the exact shape under `## Output format`.

### CSV mode (`.csv`)

```
claude "run meddpicc on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality claim — say so explicitly. For
each deal row, check whether fields corresponding to the eight letters are
present and non-trivial (not blank, not a placeholder), including a Paper
process field (signer, contract stage, security-review status). Output a
table: deal name, deal value, letters missing, sorted by deal value
descending.

## Output format

For every letter, in this order — Metrics, Economic buyer, Decision
criteria, Decision process, Paper process, Identify pain, Champion,
Competition:

```
**Paper process** — Missed
Evidence: "I haven't thought that far ahead... I couldn't tell you who or
how long that usually takes"
Note: no procurement process identified, no legal contact named, no signer
confirmed, despite the deal being three weeks past verbal approval
```

Then close with exactly one line naming the **single biggest qualification
risk** if this deal were forecast today, and the one call or action that
would close it:

> **Biggest risk: [letter]** — because [the specific gap, not a generic
> label], and here's what would close it: [specific next action].

If Paper process is the weakest letter, name the specific gap (no named
signer, no procurement timeline, security review never raised) rather than
a generic "paperwork risk" line. No recap section repeating all eight
scores again after this — the call above is the deliverable.

## Do not

- Don't average or blend the eight letters into a single "qualification
  score" — MEDDPICC stays eight separate reads, not one number.
- Don't score a letter Missed when it was genuinely unreachable at this
  call's stage — use Not applicable, and don't let having eight letters
  push the read toward finding fault on ones the call couldn't have covered.
- Don't infer Economic buyer or Champion from title or sentiment alone — a
  champion has to be shown doing something (looping in a stakeholder,
  flagging a legal contact), not just saying positive things.
- Don't add a "recommended next email" or talk-track section unless asked —
  this skill's job stops at naming the biggest risk and the action that
  closes it.

## Related skills

- **`meddicc`** — the same seven letters without Paper process, for
  discovery and mid-funnel calls where paperwork mechanics aren't yet the
  open question.
- **`bant`** — a faster four-criterion advance/no-advance read for an
  early-stage call, well before MEDDPICC's late-stage lens applies.
- **`deep-discovery`** — for auditing the discovery call itself rather than
  the close mechanics of a deal already past qualification.

## Sample data

`assets/sample-transcript.txt` is a synthetic late-stage call where
paperwork, not qualification, is the open risk — run the skill against it
first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
