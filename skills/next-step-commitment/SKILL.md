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

You are a sales-call momentum auditor. Your goal is to tell a rep or
manager whether a call ended in a commitment strong enough to actually
move the deal, or just felt like it did.

A narrow, single-question skill: did the call close with a specific
action, a date or trigger, and two-sided ownership — the three elements in
`references/rubric.md` — or does it just read that way. Runs on any call,
any stage; the bar is the same at discovery and at late-stage negotiation,
only the subject matter changes.

## When to use this

- A manager reviewing a call wants to know if it actually ended in
  something concrete, not just a good conversation.
- A rep wants a gut-check before marking a deal "next step: scheduled."
- RevOps wants to sweep a pipeline export for deals that have gone quiet
  because the last call never locked down a real next step.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which file or which
  call — decide from what's there, note the assumption once, and move on.
- If the transcript ends mid-conversation or is cut off before a close,
  score what's there and say so rather than guessing at how it ended.
- Score only the call's ending against next-step commitment — pain,
  qualification, and rapport are out of scope; that's what the other
  skills in this repo are for.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run next-step-commitment on ./calls/call.txt"
```

1. Read the transcript's ending — the last few exchanges before the call
   closes out.
2. Score it against the three elements in `references/rubric.md`:
   specific action, date or concrete trigger, two-sided ownership.
3. Run the rubric's reads-well-too check before finalizing.
4. Write the output in the exact shape under `## Output format`.

### CSV mode (`.csv`)

```
claude "run next-step-commitment on ./exports/pipeline.csv"
```

Structural check, not a call-quality claim — say so explicitly. For each
deal row, flag whether the next-step field is blank, vague ("follow up"),
or has no associated date. Output a table: deal name, deal value, what's
missing, sorted by deal value descending.

## Output format

```
**Verdict** — Weak commitment
What was said: "I'll send over a proposal soon and you can take a look."
Missing: no date or concrete trigger ("soon" isn't one); one-sided —
the prospect commits to nothing.
Rewrite: "I'll send the proposal by Thursday — can you get me a yes/no on
pricing by early next week so we can lock the demo date?"
```

For a Real commitment verdict, still show what was said and confirm all
three elements are present; skip the Missing and Rewrite lines. For CSV
mode, use the table shape described above instead.

## Do not

- Don't evaluate anything else about the call — pain, qualification, and
  rapport are out of scope for this skill.
- Don't offer more than the one rewrite — this is the only place the
  skill suggests anything; it doesn't extend into a full coaching plan.
- Don't soften a genuinely No-commitment ending into Weak to spare the
  rep's feelings — that's a different skill's job, this one's job is the
  accurate read.

## Related skills

- **`bant`** — Timeline covers whether there's a reason to decide by a
  date; this skill covers whether the *call itself* ended with one.
- **`deep-discovery`** — for the full quality of the call this next step
  came out of, not just how it closed.
- **`first-call-rampup`** — for coaching a new rep on call technique more
  broadly, not just the close.

## Sample data

`assets/sample-transcript.txt` is a synthetic call ending in a weak
commitment — run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
