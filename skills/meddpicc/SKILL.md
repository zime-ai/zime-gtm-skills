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

Audits a sales conversation against the eight MEDDPICC letters. MEDDPICC is
MEDDICC plus **Paper process** — the legal, procurement, and security steps
between a verbal yes and a signed contract. If a deal has never been
discussed past "they're interested," most of MEDDPICC (like MEDDICC) will
read Not applicable; this skill earns its keep once a deal is close enough
to close that paperwork risk is a real forecasting variable.

## When to use this vs. `meddicc`

Run `meddicc` for qualification during discovery and mid-funnel calls — the
seven letters it covers (this skill covers the same seven, worded
identically) don't need a paperwork lens yet. Reach for `meddpicc` instead
once a deal is realistically a quarter or less from close and the open
question is no longer "are they qualified" but "what stands between verbal
yes and signature" — legal redlines, procurement cycles, security review,
who actually signs. Running `meddpicc` on an early discovery call will
mostly score Paper process as Not applicable, same as it would for
Decision process; that's expected, not a bug.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run meddpicc on ./calls/acme-call.txt"
```

Read the transcript, then score it against each letter in
`references/rubric.md`. For every letter, output:

- **Status** — Covered / Partial / Missed / Not applicable to this call
- **Evidence** — a direct quote from the transcript. If a letter genuinely
  wasn't addressable on this specific call (e.g. Paper process on a first
  discovery call, before anyone has discussed timelines to close), say
  **Not applicable** rather than scoring it Missed.
- **Note** — one line, only if Partial or Missed

Close with the **single biggest qualification risk** if this deal were
forecast today, and what call or action would close it. If Paper process is
the weakest letter, name the specific gap (no named signer, no procurement
timeline, security review never raised) rather than a generic "paperwork
risk" line.

### CSV mode (`.csv`)

```
claude "run meddpicc on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality claim — say so explicitly. For
each deal row, check whether fields corresponding to the eight letters are
present and non-trivial, including a Paper process field (signer, contract
stage, security-review status). Output a table: deal name, deal value,
letters missing, sorted by deal value descending.

## Sample data

`assets/sample-transcript.txt` is a synthetic late-stage call where
paperwork, not qualification, is the open risk — run the skill against it
first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
