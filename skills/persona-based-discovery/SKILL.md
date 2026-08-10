---
name: persona-based-discovery
description: Audits whether a discovery call's questions and framing were actually tailored to the specific buyer persona in the room (technical evaluator, economic buyer, end user, etc.), or sweeps a CRM export for deals with no persona/role data attached to contacts. Use when checking that a rep adapted to who they were talking to rather than running a one-size-fits-all script, or when reviewing a pipeline export for deals missing contact-role fields.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: discovery
  zime:input-modes: transcript,csv
---

# GTM Persona-Based Discovery Audit

Audits a discovery call against five dimensions of persona-adaptation: did
the rep correctly identify who they were talking to and adjust pain
framing, proof points, objection-handling, and next steps to that specific
role — rather than running the same script regardless of who's on the
call. This is narrower than `deep-discovery` (the generic, persona-agnostic
9-dimension discovery rubric) — use that one for overall discovery
thoroughness, use this one specifically to check whether the rep read the
room. Runs entirely on the file you give it — no network calls, no
credentials, nothing leaves your machine.

## When to use this

- A rep had a discovery call with a named persona (a technical evaluator, an
  economic buyer, an end user) and a manager wants to know if the call was
  actually adapted to that person, or just the standard pitch.
- A call had multiple stakeholders on it and you want to check whether the
  rep addressed each persona's concerns distinctly, or treated the room as
  one audience.
- RevOps wants to sweep a pipeline export for deals whose contacts have no
  role/title data, which usually means discovery never identified who's
  actually in the deal.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run persona-based-discovery on ./calls/acme-discovery.txt"
```

First identify who was on the call and what persona each speaker maps to
(technical evaluator, economic buyer, end user, champion, etc.) — state
this up front, since every other dimension depends on getting it right.
Then score the call against each dimension in `references/rubric.md`. For
every dimension, output:

- **Status** — Covered / Partial / Missed
- **Evidence** — a direct quote or timestamp tying the finding to a specific
  persona on the call. If you cannot point to a specific line, mark the
  dimension **Unclear** rather than guessing.
- **Note** — one line, only if the status is Partial or Missed

If the call only had one persona in the room, say so and score the
dimensions against that one persona rather than penalizing the call for
not covering personas that were never present.

Close with **2-3 highest-leverage next steps** for adapting future calls
with this persona mix.

### CSV mode (`.csv`)

```
claude "run persona-based-discovery on ./exports/pipeline.csv"
```

This is a **structural hygiene sweep**, not a call-quality audit — a CRM
export can only show whether contact role/title data was ever captured, not
whether a rep actually adapted to it on a call. Say this explicitly in the
output.

For each deal row, check whether contact-role fields (title, persona tag,
buyer type) are present and non-trivial for every listed contact. Output a
table: deal name, deal value, contacts missing role data, sorted by deal
value descending so the highest-value gaps surface first.

## Sample data

`assets/sample-transcript.txt` is a short synthetic discovery call with a
technical evaluator and an economic buyer both on the line — run the skill
against it first. `assets/sample-pipeline.csv` is a synthetic pipeline
export (deliberately missing contact-role data) for trying CSV mode.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
