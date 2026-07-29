---
name: first-call-rampup
description: Audits a new rep's early sales call transcript against a foundational-skills rubric covering opening, open-ended questioning, pain uncovering, and pitch delivery. Use when coaching a newly ramped rep, reviewing their first calls, or building a rep-development plan from real call evidence.
license: MIT
metadata:
  zime:category: new-business
  zime:input-modes: transcript
---

# GTM First-Call Rampup Audit

Audits an early-tenure rep's call against six foundational skills —
coaching-flavored, not deal-outcome-flavored. Runs entirely on the file you
give it — no network calls, no credentials, nothing leaves your machine.

## When to use this

- A manager is reviewing a new rep's early calls to build a coaching plan.
- A new rep wants a structured self-check before their next call.
- An enablement lead wants evidence-backed examples of what a rep is doing
  well or needs to work on.

## Modes

Transcript only (`.txt`, `.vtt`, `.json`, `.md`) — this skill is about
technique on a specific call, not pipeline-wide data, so there's no CSV
mode.

```
claude "run first-call-rampup on ./calls/new-rep-call-1.txt"
```

Score against `references/rubric.md`. Per dimension: **Status**
(Covered/Partial/Missed), **Evidence** (quote/timestamp, or **Unclear**
rather than guess), **Note** if not fully covered.

Close with **one specific thing to work on before the next call** — not a
list, the single highest-leverage one, framed as coaching, not a verdict.
Run the reads-well-too check first: coaching feedback that reads as
uniformly harsh is unlikely to be acted on.

## Sample data

`assets/sample-transcript.txt` — synthetic early-tenure rep call.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session.
