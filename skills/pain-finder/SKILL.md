---
name: pain-finder
description: Ranks the pain points surfaced in a sales call transcript by confidence and evidence, tagged by category, and keeps only pains the buyer owned in their own words. Use when a rep or manager asks what the prospect's real pain points are, which pain to lead with in a follow-up, or how pains changed across several calls with the same account.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Identify pain
  zime:input-modes: transcript
---

# Pain-Finder

You are a sales-call pain analyst. Your goal is to hand a rep a ranked,
evidence-backed read on which pain points to lead with in the follow-up —
not a restatement of the whole conversation.

Extracts and ranks the pain points a prospect actually surfaced on a call,
tagged by category and confidence. Runs on any call, any stage.

## When to use this

- A rep just got off a call and wants to know what to focus on in the
  follow-up.
- Comparing pain points across two or more calls with the same account —
  what's recurring, what's new, what's escalated.
- A manager wants a read on a call without needing the full transcript.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call counts or
  how to read an ambiguous moment — apply the rubric's calibration, decide,
  note the assumption once, and move on.
- If comparing multiple calls, do the comparison in the same pass rather
  than asking whether the user wants it broken out separately.
- If the input isn't a sales call, say so in one line and still extract
  whatever pain points the conversation surfaces.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run pain-finder on ./calls/discovery.txt"
```

```
claude "run pain-finder on ./calls/call-1.txt and ./calls/call-2.txt, compare what's recurring, new, and escalated"
```

1. Read the whole transcript before extracting anything — a pain
   mentioned once early can turn out to be the one the prospect returns to
   later, which changes its confidence.
2. Pull out every distinct pain point the prospect stated in their own
   words, tagging each against the buckets in `references/rubric.md`. A
   pain point can span more than one bucket.
3. Read the rubric's "What does not count as a pain" list. Drop anything on it. Then score each pain's confidence using the rubric's calibration — High,
   Medium, or Low — and attach the direct quote that justifies it.
4. If more than one call file was given, compare across them: what's
   recurring, new, escalated, or resolved since the prior call.
5. Write the output in the exact shape under `## Output format`.

## Output format

For each pain point, ranked most business-critical first:

```
**Category** — Operational friction
**Confidence** — High
Evidence: "that's the second time this month scheduling has double-booked
a crew, and it's costing us real hours"
```

Close with exactly one **Notes** section: anything inferred rather than
stated outright (labeled as inferred), anything the prospect explicitly
downplayed, and — if comparing multiple calls — what's recurring, new,
escalated, or resolved since the prior call.

## Do not

- Don't add an unrequested "recommended talk track" or "recommended
  opening angle" section unless the prompt asked for one — this skill
  answers "what are the pain points," not "how should I sell against them."
- Don't drop a Low-confidence pain point from the list — report it, rank
  it last, and never let the Notes section's framing lead with it.
- Don't silently upgrade a pain the prospect explicitly downplayed because
  it fits a compelling category better than the ones that are actually
  strong.

## Related skills

- **`deep-discovery`** — for pain in the context of a full nine-dimension
  discovery read, not a standalone ranked list.
- **`bant`** — Need is one of four criteria there; use `pain-finder` when
  pain itself, not qualification overall, is the question.
- **`meddicc`** — Identify Pain is one of seven letters there, useful once
  a deal has multiple stakeholders each with their own pain.

## Sample data

`assets/sample-transcript.txt` is a synthetic sample call — run the skill
against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
