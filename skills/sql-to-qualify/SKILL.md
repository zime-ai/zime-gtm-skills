---
name: sql-to-qualify
description: Audits the first call after a sales-qualified lead (SQL) hand-off to check whether there's a real opportunity worth a rep's time — right contact, pain in the prospect's own words, rough budget/urgency fit, competitive awareness, and a concrete next meeting — or sweeps a CRM export for SQLs sitting untouched past this gate. Use right after an SQL is assigned and worked for the first time, before investing in a full qualification call.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: sql-to-qualify
  zime:input-modes: transcript,csv
---

# GTM SQL-to-Qualify Audit

Audits the call that decides whether a sales-qualified lead becomes a worked
opportunity — the gate before `meeting-to-qualify`, which assumes the deal
is already real and digs into authority/competition/next steps in depth.
This one asks the earlier question: is there even a real opportunity here,
or is the MQL/SQL label doing the work instead of the call. Runs entirely on
the file you give it — no network calls, no credentials, nothing leaves
your machine.

## When to use this

- A rep just worked a newly-assigned SQL for the first time and needs a
  read on whether it's worth pursuing past this call.
- A sales manager wants to spot-check whether reps are actually testing SQLs
  or just advancing every inbound lead on the strength of the form fill.
- RevOps wants to sweep a pipeline export for SQLs that have sat past this
  stage with no evidence the first call actually happened or landed.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run sql-to-qualify on ./calls/acme-sql.txt"
```

Score the call against each dimension in `references/rubric.md`. For every
dimension, output:

- **Status** — Covered / Partial / Missed
- **Evidence** — a direct quote or timestamp. If you can't point to a
  specific line, mark **Unclear** rather than guess.
- **Note** — one line, only if Partial or Missed

Close with a single **advance / disqualify / needs one more touch** read,
with the one or two dimensions that decided it.

Before finalizing, run the reads-well-too check in `references/rubric.md` —
if a call that was clearly a strong, real opportunity still comes back
mostly Missed, the rubric is reading too strictly.

### CSV mode (`.csv`)

```
claude "run sql-to-qualify on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality audit. For rows marked SQL or
past this stage, check whether fields corresponding to contact role, stated
pain, budget/urgency signal, and next-meeting date are populated and
non-trivial. Output a table: lead name, days since SQL, stage, dimensions
missing — sorted by days since SQL descending. State explicitly that this
checks whether fields were filled in, not whether the call itself was good.

## Sample data

`assets/sample-transcript.txt` — a short synthetic SQL follow-up call. Run
against it first before pointing this at anything of your own.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
