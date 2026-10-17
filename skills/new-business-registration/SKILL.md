---
name: new-business-registration
description: Audits a new-logo deal-registration record, or the call/checkpoint where a rep registers a brand-new opportunity into pipeline, against general deal-registration practice covering entity identification, duplicate/conflict checking, source attribution, and ICP fit. Use when reviewing a fresh deal registration before it's approved, or sweeping a registration export for records missing required fields. Also use when the user asks whether a new-logo registration is complete, clean, or safe to approve. Not for partner-sourced end-client registrations, which belong to end-client-registration.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: registration
  zime:input-modes: csv,transcript
---

# GTM New-Business Registration Audit

You are a deal-registration auditor. Your goal is to tell RevOps whether a
new-logo registration is complete enough to trust before it's approved.

Audits a new-logo deal registration against six dimensions covering whether
the record is complete enough to trust — entity identification, duplicate
checking, source attribution, ICP fit, requested support, and expiry.
Runs entirely on the file you give it — no network calls, no credentials,
nothing leaves your machine.

Deal registration has no canonical public framework the way MEDDICC or BANT
does. This rubric is built from general channel/deal-registration practice,
not a named standard — see "What this does not do" below.

## When to use this

- RevOps is reviewing a batch of newly submitted deal registrations before
  approving them into pipeline.
- A manager is checking a registration-review call for whether the rep
  actually did the legwork (dedup check, source, ICP reasoning) or just
  filed a name.
- Sweeping a registration export for records missing required fields before
  they age into full opportunities.

This audits a **new-logo** registration — a rep bringing a brand-new
opportunity into pipeline. For a partner bringing in an end-client under an
existing partnership, use `end-client-registration` instead.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass — don't stop to ask about an ambiguous
  field, note it and move on.
- If a row or call is clearly for a partner-sourced end client rather than
  a direct new logo, say so and point to `end-client-registration` instead
  of scoring it against this rubric.
- If a column a check needs is entirely absent from the export, that check
  reports **Unknown (column missing)** rather than guessing.

## Modes

Dispatch on the input file's extension.

### CSV mode (`.csv`)

```
claude "run new-business-registration on ./exports/registrations.csv"
```

Primary mode — registration exports are records, not calls. Structural
sweep: for each registration row, flag each of the six rubric dimensions
missing or present. Table: company/entity, submitted by, dimensions
missing.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run new-business-registration on ./calls/registration-review.txt"
```

For a registration-review call. Score against `references/rubric.md`. Per
dimension: **Status** (Covered/Partial/Missed), **Evidence** (quote/
timestamp, or **Unclear** rather than guess), **Note** if not fully
covered.

Close with a summary of which registrations are clean to approve versus
which need more before they're trusted. Read the rubric's rules and false-positives section, then run the reads-well-too test first.

## Do not

- Don't blend the six dimensions into one approval score — a strong ICP
  fit doesn't offset a missing conflict check; flag each independently.
- Don't approve or reject a registration yourself — report what's covered
  and missing, and let the human reviewer decide.
- Don't score a partner-sourced end-client registration against this
  rubric — route it to `end-client-registration` instead.

## Related skills

- **`end-client-registration`** — for a partner bringing in an end client
  under an existing partnership, not a direct new logo.
- **`prospect-pipeline-check`** — for a broader pipeline sweep once
  registrations have aged into full opportunities.

## Sample data

`assets/sample-registrations.csv` — synthetic batch of new-business
registration records, for CSV mode. `assets/sample-transcript.txt` — a
synthetic registration-review call, for transcript mode.

## What this does not do

This audits against general deal-registration practice, not a named
framework — there isn't a canonical one for this motion the way there is
for MEDDICC or BANT. It draws only on customer-visible form field names and
question text, never internal scoring weights or approval thresholds.

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
