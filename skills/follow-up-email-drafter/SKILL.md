---
name: follow-up-email-drafter
description: Drafts the customer-facing follow-up email a rep sends after a sales call, grounding every recap, next step, and date in what was actually said, plus a separate grounding-notes section flagging which lines are heard-verbatim versus a proposal the rep should confirm before sending. Use right after a call when a rep wants a first-draft follow-up instead of writing one from scratch, or when a manager wants to sanity-check a drafted email against the transcript before it goes out.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript
---

# Follow-Up Email Drafter

Drafts the actual follow-up email a rep sends after a call — subject line
and body, ready to send. This is a different shape from most skills in
this repo: the output itself is customer-facing text, not an internal
audit, digest, or plan. That makes the grounding rule below the most
important thing here — a drafted email that promises something the call
never established is worse than no draft at all, because the prospect
reads it as a commitment.

Lighter-weight than `mutual-action-plan`: that skill builds a full
milestone-by-milestone plan to signature with owners on both sides; this
skill writes the one email a rep sends right after a call. Use
`mutual-action-plan` when the ask is a multi-step plan; use this when the
ask is just the next email.

## When to use this

- A rep just got off a call and wants a first-draft follow-up email
  instead of writing one from scratch or copy-pasting notes.
- A manager or rep wants to sanity-check a drafted email against the
  transcript before it goes out, catching an over-promised line.
- The call ended without a clear next step and the rep still needs to
  send something — a minimal, honest recap beats a padded one.

## The grounding rule

Before drafting each line, run `mutual-action-plan`'s internal check: is
this claim `heard` (actually said on the call — quote it) or `inferred`
(a reasonable next step, but not stated with a date, owner, or as an
agreed fact)? See `references/rubric.md` for the full test.

- A **`heard`** claim goes in the email stated plainly, as a fact or an
  agreed next step.
- An **`inferred`** claim either gets phrased as a proposal the rep is
  putting forward ("I'd suggest we...", "Would it help if...") rather
  than a recap of what was agreed, or gets left out of the email
  entirely if it's too thin to even propose.
- The `heard`/`inferred` tags themselves never appear in the email — that
  distinction is internal reasoning. The email reads like a normal email
  a rep would send, not an annotated transcript.

Never invent a next step, number, date, or name that the call didn't at
least gesture toward.

## Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run follow-up-email-drafter on ./calls/call.txt"
```

Read the transcript, then output two parts:

1. **The drafted email** — subject line + body. Professional, not
   robotic. Recaps what was discussed; confirms next steps only if they
   were actually agreed. Proposed (not-yet-agreed) items are phrased as
   suggestions, not recaps.
2. **Grounding notes** (below the email, not part of it) — one line per
   concrete claim in the draft:
   - `Heard` — the quote from the transcript it traces to.
   - `Proposed` — flagged as something the rep should confirm is actually
     wanted before sending, since the call didn't lock it down.

If the call ended with nothing concrete to follow up on, say so directly
and draft a minimal "great talking with you, here's a quick recap" email
instead of padding it with invented asks.

## Sample data

`assets/sample-transcript.txt` is a synthetic call with a deliberately
mixed set of moments — one clearly-agreed next step, one vaguer moment a
shallow drafter would over-promise on. Run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond
the current session. It reads the file(s) you point it at and nothing
else. It never invents a next step the call didn't at least gesture
toward, and never fabricates a specific number, date, or name not present
in the transcript.
