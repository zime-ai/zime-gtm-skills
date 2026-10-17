---
name: customer-success
description: Audits a periodic QBR or account health-review call transcript against an eight-dimension rubric (value delivered, usage breadth, open issues, enablement gaps, stakeholder breadth, strategic alignment, forward fit, next check-in) and credits only what the customer said, or sweeps a CRM export for accounts overdue for a health review. Use when the user asks to review a QBR or account health check-in, or asks whether a customer is really healthy, and not for a renewal-risk or expansion conversation.
license: MIT
metadata:
  zime:category: post-sale
  zime:dimension: stage
  zime:stage: post-sale-review
  zime:input-modes: transcript,csv
---

# GTM Customer Success Audit

You are a customer-success health-review auditor. Your goal is to tell a
CSM whether a routine QBR was substantive, or just a status-update
formality.

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

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass — don't stop to ask which call or
  whether a borderline quote counts.
- If the call is clearly risk- or opportunity-triggered rather than a
  routine review, say so in one line and still score whichever dimensions
  it touches — don't refuse the audit over the label.
- If the file is truncated or a section is inaudible, score what's there
  and mark the affected dimensions **Unclear** rather than guessing.

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
follow-up action. Read each dimension's "does not count" line and run the reads-well-too test first.

### CSV mode (`.csv`)

```
claude "run customer-success on ./exports/accounts.csv"
```

Structural sweep only. Check whether accounts have a health-review field
populated within a reasonable window (e.g. last 90 days) and flag those
that don't, sorted by ARR descending.

## Do not

- Don't blend the eight dimensions into one health score — good value
  delivery doesn't offset a single-point-of-contact risk; each stands on
  its own.
- Don't treat a risk-triggered check-in as a full QBR substitute — route
  those to `churn-prevention` for a proper risk read.
- Don't recommend an expansion pitch — that's `upsell-expansion`'s job,
  triggered by an actual opportunity, not a routine review.

## Related skills

- **`churn-prevention`** — for a risk-flagged check-in, a narrower and more
  urgent lens than this routine review.
- **`upsell-expansion`** — for an opportunity-triggered conversation.

## Sample data

`assets/sample-transcript.txt` — synthetic QBR call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
