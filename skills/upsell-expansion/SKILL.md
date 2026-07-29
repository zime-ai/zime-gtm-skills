---
name: upsell-expansion
description: Audits an expansion/upsell call transcript against a rubric covering opportunity clarity, champion strength, renewal health, and strategic alignment, or sweeps a CRM export for expansion opportunities missing a health check. Use when reviewing an upsell or expansion conversation, or checking an account list for expansion pushes that skipped a renewal-health check first.
license: MIT
metadata:
  zime:category: post-sale
  zime:input-modes: transcript,csv
---

# GTM Upsell & Expansion Audit

Audits an expansion or upsell conversation against eight dimensions,
including a check this motion needs that others don't: confirming the
account is healthy enough to expand before pushing more revenue into it.
Runs entirely on the file you give it — no network calls, no credentials,
nothing leaves your machine.

## When to use this

- An AM or CSM just had an expansion conversation and wants a structured
  read before building a proposal.
- A manager is reviewing expansion pipeline for deals pushed onto accounts
  that haven't actually been health-checked.
- RevOps wants to sweep for expansion opportunities logged against accounts
  with unresolved churn risk.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run upsell-expansion on ./calls/acme-expansion.txt"
```

Score against `references/rubric.md`. Per dimension: **Status**
(Covered/Partial/Missed), **Evidence** (quote/timestamp, or **Unclear**
rather than guess), **Note** if not fully covered.

**Check dimension 1 (account health) first, explicitly.** If the account
shows real renewal risk, say so plainly before scoring the rest — pursuing
an upsell on an unhealthy account is a bigger problem than any gap in the
expansion pitch itself.

Close with a go/hold read on the expansion push. Run the reads-well-too
check first.

### CSV mode (`.csv`)

```
claude "run upsell-expansion on ./exports/accounts.csv"
```

Structural sweep only. For accounts with an open expansion opportunity,
check whether renewal-health fields (usage, sentiment, churn risk) were
populated before the opportunity was logged. Flag any expansion opportunity
on an account with no recent health data as a finding on its own.

## Sample data

`assets/sample-transcript.txt` — synthetic expansion call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
