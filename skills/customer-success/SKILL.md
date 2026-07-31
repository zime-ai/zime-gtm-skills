---
name: customer-success
description: Audits a periodic QBR or account health-review call transcript against a rubric covering value delivered, usage breadth, open issues, and forward alignment, or sweeps a CRM export for accounts overdue for a health review. Use when reviewing a QBR or ongoing health check-in, distinct from a renewal-risk-triggered or expansion-triggered conversation.
license: MIT
metadata:
  zime:category: post-sale
  zime:dimension: stage
  zime:stage: post-sale-review
  zime:input-modes: transcript,csv
---

# GTM Customer Success Audit

Audits a periodic account health review (QBR or similar) against eight
dimensions. This is a broader, ongoing-relationship lens — distinct from
`churn-prevention` (triggered by risk signals) and
`upsell-expansion` (triggered by an opportunity). Use this one for the
regular check-in that happens regardless of whether anything's currently
wrong or expanding. Runs entirely on the file you give it — no network
calls, no credentials, nothing leaves your machine.

## When to use this

- A CSM is prepping for or reviewing a QBR and wants a structured read.
- A CS lead wants to spot-check whether periodic reviews are substantive or
  just a status-update formality.
- RevOps wants to sweep for accounts overdue for a health review.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run customer-success on ./calls/acme-qbr.txt"
```

Score against `references/rubric.md`. Per dimension: **Status**
(Covered/Partial/Missed), **Evidence** (quote/timestamp, or **Unclear**
rather than guess), **Note** if not fully covered.

Close with a one-line overall account read and the single most useful
follow-up action. Run the reads-well-too check first.

### CSV mode (`.csv`)

```
claude "run customer-success on ./exports/accounts.csv"
```

Structural sweep only. Check whether accounts have a health-review field
populated within a reasonable window (e.g. last 90 days) and flag those
that don't, sorted by ARR descending.

## Sample data

`assets/sample-transcript.txt` — synthetic QBR call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
