---
name: mutual-action-plan
description: Writes a mutual action plan out of what was actually said on a call — milestones from today to signature, each with an owner on both sides and a date — or fills date/stage gaps from a CRM export row. Use when a rep needs a real MAP to send a prospect after a call, or a manager wants to check whether a deal's stated next steps actually hang together as a plan.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript,csv
---

# Mutual Action Plan

Writes a mutual action plan out of what was actually said on a call:
milestones from today to signature, each with an owner on both sides and a
date. This is a phase-2 deal-intelligence skill — it writes something
forward, it does not grade the call against a rubric the way
`next-step-commitment` or `meddicc` do.

## When to use this

- A rep just got off a call that covered next steps and wants a MAP to send
  the prospect, not a to-do list they invented themselves afterward.
- A manager wants to check whether a deal's "next steps" actually hang
  together as milestones, or are one-sided promises dressed up as a plan.
- RevOps wants to fill gaps in a deal's stage/date fields from what a call
  actually established, without overwriting what the CRM already has right.

## What makes a milestone real

Same three-part test `next-step-commitment` uses for a single commitment,
applied to every milestone in the plan:

1. **A specific action** — not "follow up," a named thing (a security
   review completed, a contract sent for signature, budget approved).
2. **A date or concrete trigger** — a calendar date or an event with an
   obvious, checkable occurrence, not "soon."
3. **Two-sided ownership** — someone on the account owns it too, not just
   the rep.

See `references/rubric.md` for the full test and how it maps to the
`heard` / `inferred` tags below.

## The evidence rule

Every milestone is tagged:

- **`heard`** — the milestone, its date, and its owners were actually said
  on the call; quote it.
- **`inferred`** — the milestone is a reasonable next step given what was
  discussed, but wasn't stated with enough of the three-part test present —
  the closest thing said is a hand-wave. Quote the closest thing said, and
  name which of the three elements is missing or assumed.

If every milestone in the plan comes back `inferred`, say so explicitly and
up front: an all-inferred plan is a finding about the call (nothing
concrete was locked down), not a plan a rep should send to a prospect as-is.

## Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run mutual-action-plan on ./calls/call.txt"
```

Read the transcript, then output a table of milestones from today to
signature, ordered chronologically:

- **Milestone** — the specific action
- **Owner (seller side)** and **Owner (prospect side)** — name or role;
  write "missing" if the call never assigned one
- **Target date**
- **Tag** — `heard` (with the quote) or `inferred` (with the closest quote
  and what's missing)

Close with a one-line summary: how many milestones are `heard` vs
`inferred`, and the all-inferred call-out above if it applies.

### CSV mode (`.csv`)

```
claude "run mutual-action-plan on ./exports/pipeline.csv"
```

Fills date/stage gaps in a deal row from what's in the CSV — a structural
check, not a call-quality claim, same disclaimer as
`next-step-commitment`'s CSV mode: say explicitly that this reads the
fields present, not what actually happened on any call. Flag rows missing
a next milestone, a date, or an owner.

## Sample data

`assets/sample-transcript.txt` is a synthetic call with a deliberately
mixed plan — run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
