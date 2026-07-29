---
name: onboarding-journey
description: Audits a new-customer onboarding call transcript against a rubric covering onboarding experience, sentiment, and early expansion signal, or sweeps a CRM export for onboarding accounts with no documented health signal. Use when reviewing an onboarding check-in call, or checking a new-customer list for onboardings going quiet.
license: MIT
metadata:
  zime:category: post-sale
  zime:input-modes: transcript,csv
---

# GTM Onboarding Journey Audit

Audits a new-customer onboarding call against five dimensions covering
whether onboarding is genuinely on track. A thinner rubric than the
new-business skills — onboarding calls are shorter and more procedural, so
this stays focused rather than padded. Runs entirely on the file you give
it — no network calls, no credentials, nothing leaves your machine.

## When to use this

- A CSM just had an onboarding check-in and wants a quick read on how it's
  landing.
- A CS lead wants to spot-check onboarding calls across a cohort.
- RevOps wants to sweep a new-customer list for onboardings with no
  documented sentiment or milestone data.

## Modes

Dispatch on the input file's extension.

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run onboarding-journey on ./calls/acme-onboarding.txt"
```

Score against `references/rubric.md`. Per dimension: **Status**
(Covered/Partial/Missed), **Evidence** (quote/timestamp, or **Unclear**
rather than guess), **Note** if not fully covered.

Close with an on-track / needs-attention read. Run the reads-well-too check
first.

### CSV mode (`.csv`)

```
claude "run onboarding-journey on ./exports/new-customers.csv"
```

Structural sweep only. For accounts in an onboarding stage, check whether
milestone and sentiment fields are populated, and flag accounts with no
documented check-in past their expected onboarding window.

## Sample data

`assets/sample-transcript.txt` — synthetic onboarding check-in call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
