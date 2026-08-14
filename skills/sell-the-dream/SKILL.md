---
name: sell-the-dream
description: Audits a B2B sales call transcript for future-state vision selling — does the rep name the world change and stakes before pitching product, or lead with features and bolt a "vision" on afterward. Scored against Andy Raskin's publicly published "5 Elements of a Great Sales Narrative," corroborated by Corporate Visions, Force Management, and Challenger's convergent "vision before product" pattern. "Sell the dream" is the colloquial name for this behavior, not a citation to a named methodology. Use when a rep pitches features early and a deal stalls on "not urgent," or when a manager wants to know if a call's vision narrative landed before the product did, not just whether a vision was mentioned at all.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Vision selling
  zime:input-modes: transcript
---

# Sell the Dream: Vision Narrative Sequencing Audit

Audits whether a sales call builds a future-state vision *before* pitching
product, using Andy Raskin's "5 Elements of a Great Sales Narrative"
(<https://medium.com/the-mission/the-greatest-sales-deck-ive-ever-seen-4f4ef3391ba0>)
as the scoring rubric. "Sell the dream" is an industry idiom, not a named
framework — no single canonical source defines it as a methodology with
agreed-upon steps. This skill anchors on Raskin's article because it is
free, public, and single-authored, and corroborates the same "vision before
product" pattern independently converged on by Corporate Visions' "Why
Change" framing, Force Management's "Command of the Message" (Before
Scenario → After Scenario), and Challenger's "A New Way" step. Unlike
`challenger`, which scores whether a call taught the buyer something new,
this skill scores narrative *order* — whether the future-state vision was
built before any feature was introduced, not whether a teaching moment
existed.

## When to use this

- A rep pitches product capabilities early in a call and the deal later
  stalls on "not urgent" or "no clear reason to change now."
- Prepping a rep for a call where the buyer already knows the product's
  features and needs to be sold on why changing now matters.
- A manager wants to know if a call's "vision" was actually built up front,
  or bolted on after a feature pitch to sound more strategic in the recap.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run sell-the-dream on ./calls/acme-call.txt"
```

Read the transcript, then score it against `references/rubric.md`'s five
elements, in Raskin's required order:

1. Name a Big, Relevant Change in the World
2. Show There'll Be Winners and Losers
3. Tease the Promised Land
4. Introduce Features as "Magic Gifts" for Overcoming Obstacles to the
   Promised Land
5. Present Evidence that You Can Make the Story Come True

For each element, output:

- **Status** — Covered / Partial / Missed / Not applicable to this call
- **Evidence** — a direct quote from the transcript
- **Note** — one line, only if Partial or Missed

Then check **sequencing** explicitly: did element 4 (features) appear
before elements 1–3 (change, stakes, promised land) were established? If
so, flag it as a **sequencing violation** — a rep who pitched product first
and backfilled a "vision" afterward — even if all five elements
individually score Covered. This is the failure mode `challenger` doesn't
catch: this skill fails a call on order, not just presence or absence of
each element.

Close with the **single sequencing observation**: either "vision led,
features followed" (the pattern this skill is designed to reward) or a
named quote showing where the order broke.

## Sample data

`assets/sample-transcript.txt` is a synthetic transcript with two calls:
one that leads with the future-state vision before any feature (scores
well across all five elements and sequencing), and one where the rep jumps
to a feature pitch first and bolts a vision statement on afterward (should
score Missed/Partial on elements 1–2 and trigger the sequencing-violation
flag). Run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
