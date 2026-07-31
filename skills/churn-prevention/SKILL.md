---
name: churn-prevention
description: Audits a renewal-risk or check-in call transcript against a churn/retention-signal rubric, or sweeps a CRM export for at-risk accounts missing renewal-risk data. Use when reviewing a customer check-in or QBR before a renewal, coaching a CSM on retention conversations, or scanning an account list for churn risk.
license: MIT
metadata:
  zime:category: post-sale
  zime:dimension: stage
  zime:stage: renewal-risk
  zime:input-modes: transcript,csv
---

# GTM Churn Prevention Audit

Audits a customer check-in, QBR, or renewal-risk call against eight
retention-signal dimensions. Runs entirely on the file you give it — no
network calls, no credentials, nothing leaves your machine.

## When to use this

- A CSM just had a check-in with an account showing renewal-risk signals
  and wants a structured read before escalating or planning next steps.
- A CS lead is reviewing a call before a QBR or renewal conversation.
- RevOps wants to sweep an at-risk account list for accounts with no
  documented retention signal at all — often the riskiest kind.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run churn-prevention on ./calls/acme-checkin.txt"
```

Score the call against each dimension in `references/rubric.md`. For every
dimension, output:

- **Status** — Covered / Partial / Missed
- **Evidence** — a direct quote or timestamp. Mark **Unclear** rather than
  guess if you can't point to a specific line.
- **Note** — one line, only if Partial or Missed

Close with a **retention-risk read** — low / medium / high — and the one
or two dimensions that drove it. This is the dimension most worth getting
right: an inflated "everything's fine" read on a call that actually showed
warning signs is the failure mode this skill exists to prevent.

Run the reads-well-too check in `references/rubric.md` before finalizing.

### CSV mode (`.csv`)

```
claude "run churn-prevention on ./exports/accounts.csv"
```

Structural hygiene sweep, not a call-quality audit. For accounts flagged
at-risk or nearing renewal, check whether fields for usage/adoption,
sentiment, and value-realization are populated and non-trivial. Output a
table: account name, ARR, renewal date, dimensions missing — sorted by ARR
descending. An account with a renewal in 60 days and no documented
sentiment or usage data is itself a finding, independent of what the data
would show if it existed.

## Sample data

`assets/sample-transcript.txt` — a short synthetic check-in call. Run
against it first before pointing this at anything of your own.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
