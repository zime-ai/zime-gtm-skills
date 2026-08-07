---
name: next-step-commitment
description: Checks whether a sales call ended with a real, dated, mutually-owned next step versus a vague "we'll circle back." Use when reviewing whether a call actually moved a deal forward, coaching a rep on closing calls out properly, or sweeping a CRM export for deals stuck without a next step.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Next step commitment
  zime:input-modes: transcript,csv
---

# Next-Step-Commitment Audit

A narrow, single-question skill: did this call end with a commitment strong
enough to actually move the deal, or does it just feel like it did? Runs on
any call, any stage — the bar for what counts as a real commitment is the
same at discovery and at late-stage negotiation, only the subject matter
changes.

## When to use this

- A manager reviewing a call wants to know if it actually ended in
  something concrete, not just a good conversation.
- A rep wants a gut-check before marking a deal "next step: scheduled."
- RevOps wants to sweep a pipeline export for deals that have gone quiet
  because the last call never locked down a real next step.

## What counts as a real commitment

A next step passes only if it has **all three**:

1. **A specific action** — not "follow up" or "circle back," but a named
   thing that will happen (a demo, a proposal, an intro to a stakeholder, a
   signed document review).
2. **A date or concrete trigger** — a calendar date, or an event that will
   obviously occur ("once the security team responds"), not "soon" or
   "next quarter" with nothing more specific.
3. **Two-sided ownership** — the prospect commits to something too (showing
   up, looping in a stakeholder, reviewing a document), not just the rep
   promising to send something into the void.

## Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run next-step-commitment on ./calls/call.txt"
```

Read the transcript's ending, then output:

- **Verdict** — Real commitment / Weak commitment / No commitment
- **What was said**, quoted directly
- **Which of the three elements are missing**, if not a Real commitment
- **One concrete rewrite** of what the rep could have said to close the
  gap — this is the one place this skill offers a suggestion, since it's
  the entire point of running it

Do not evaluate anything else about the call — pain, qualification, rapport
are out of scope for this skill; that's what the other skills in this repo
are for.

### CSV mode (`.csv`)

```
claude "run next-step-commitment on ./exports/pipeline.csv"
```

Structural check, not a call-quality claim — say so explicitly. Flag rows
where the next-step field is blank, vague ("follow up"), or has no
associated date. Output a table sorted by deal value descending.

## Sample data

`assets/sample-transcript.txt` is a synthetic call ending in a weak
commitment — run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
