---
name: pain-finder
description: Ranks the pain points surfaced in a sales call transcript by confidence and evidence, tagged by category, and optionally specialized for a named industry vertical. Use when a rep wants to know what a prospect's real pain points are and which to lead with in a follow-up, or when comparing pain points across multiple calls with the same account.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Identify pain
  zime:vertical-aware: true
  zime:input-modes: transcript
---

# Pain-Finder

Extracts and ranks the pain points a prospect actually surfaced on a call —
not a restatement of the whole conversation, a ranked, evidence-backed read
on what to lead with. Runs on any call, any stage. This is the skill that
demonstrates the **vertical** dimension: the taxonomy below is generic by
default, and sharpens when a `skills/vertical-context/` pack is loaded.

## When to use this

- A rep just got off a call and wants to know what to focus on in the
  follow-up.
- Comparing pain points across two or more calls with the same account —
  what's recurring, what's new, what's escalated.
- A manager wants a read on a call without needing the full transcript.

## How to run it

```
claude "run pain-finder on ./calls/discovery.txt"
```

If comparing multiple calls with the same account:

```
claude "run pain-finder on ./calls/call-1.txt and ./calls/call-2.txt, compare what's recurring, new, and escalated"
```

To specialize for a vertical:

```
claude "run pain-finder on ./calls/discovery.txt, vertical: cybersecurity"
```

When a vertical is named, read the matching pack in
`skills/vertical-context/references/<vertical>.md` first — it supplies the
category taxonomy variant, domain vocabulary, and priors for that industry.
**The pack sharpens categories and priors. It never invents a finding the
transcript doesn't support, and it never suppresses a real quote just
because it doesn't fit a category.** If no vertical is named, use the
generic taxonomy in `references/rubric.md`.

## Output

For each pain point, in ranked order (most business-critical first):

- **Category** — one of the taxonomy's buckets (generic or vertical-specific)
- **Confidence** — High / Medium / Low, with one line on why. A pain
  mentioned once in passing and downplayed by the prospect is Low, not High.
- **Evidence** — a direct quote. No pain point without one.

Close with a **Notes** section: anything inferred rather than stated
outright (label it as such), anything the prospect explicitly downplayed,
and — if comparing multiple calls — what's recurring, new, escalated, or
resolved since the prior call.

Do **not** add an unrequested "recommended talk track" or "recommended
opening angle" section unless the prompt asked for one — this skill answers
"what are the pain points," not "how should I sell against them."

## Sample data

`assets/sample-transcript.txt` is a synthetic generic-vertical call — run
the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
