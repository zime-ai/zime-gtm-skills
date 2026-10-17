---
name: sell-the-dream
description: Audits a B2B sales call transcript for future-state vision selling, meaning whether the rep names the world change and the stakes before pitching product, or leads with features and bolts a vision on afterward. It scores against Andy Raskin's publicly published 5 Elements of a Great Sales Narrative, corroborated by Corporate Visions, Force Management, and Challenger. Sell the dream is the colloquial name for this behavior and not a citation to a named methodology. Use when the user asks whether a rep sold a vision or only a product, wants a narrative review of a pitch call, or wants to coach on sequencing change, stakes, promised land, features and proof.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Vision selling
  zime:input-modes: transcript
---

# Sell the Dream: Vision Narrative Sequencing Audit

You are a sales-narrative sequencing auditor. Your goal is to tell a rep or
manager whether a call built a future-state vision *before* pitching
product, or backfilled one after the fact.

Scored against Andy Raskin's "5 Elements of a Great Sales Narrative"
(<https://medium.com/the-mission/the-greatest-sales-deck-ive-ever-seen-4f4ef3391ba0>).
"Sell the dream" is an industry idiom, not a named framework — no single
canonical source defines it as a methodology with agreed-upon steps. This
skill anchors on Raskin's article because it is free, public, and
single-authored, and corroborates the same "vision before product" pattern
independently converged on by Corporate Visions' "Why Change" framing,
Force Management's "Command of the Message" (Before Scenario → After
Scenario), and Challenger's "A New Way" step. Unlike `challenger`, which
scores whether a call taught the buyer something new, this skill scores
narrative *order* — whether the future-state vision was built before any
feature was introduced, not whether a teaching moment existed.

## When to use this

- A rep pitches product capabilities early in a call and the deal later
  stalls on "not urgent" or "no clear reason to change now."
- Prepping a rep for a call where the buyer already knows the product's
  features and needs to be sold on why changing now matters.
- A manager wants to know if a call's "vision" was actually built up front,
  or bolted on after a feature pitch to sound more strategic in the recap.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call or how to
  read an ambiguous moment — apply the rubric, decide, note the assumption
  once, and move on.
- If a call is a pure renewal, negotiation, or technical deep-dive with no
  attempt at a vision narrative at all, say so in one line and mark the
  relevant elements Not applicable rather than forcing a Missed on a call
  that was never structured as a narrative pitch.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run sell-the-dream on ./calls/acme-call.txt"
```

1. Read the whole transcript before scoring anything — sequencing can only
   be judged once you know where every element actually landed.
2. Score the call against `references/rubric.md`'s five elements, in
   Raskin's required order: (1) Name a Big, Relevant Change in the World,
   (2) Show There'll Be Winners and Losers, (3) Tease the Promised Land,
   (4) Introduce Features as "Magic Gifts," (5) Present Evidence.
3. Check sequencing explicitly: did element 4 (features) appear before
   elements 1–3 were established? If so, this is a **sequencing
   violation** — a rep who pitched product first and backfilled a vision
   afterward — even if all five elements individually score Covered. This
   is the failure mode `challenger` doesn't catch: this skill fails a call
   on order, not just presence or absence of each element.
4. Read each element's "does not count" line first. A claim that only the rep makes, with no buyer reaction, is Partial at most, and an element the call never touched is Missed.
5. Run the rubric's reads-well-too test before finalizing, in both directions.
6. Write the output in the exact shape under `## Output format`.

## Output format

For each of the five elements, in order:

```
**1. Name a Big, Relevant Change in the World** — Covered
Evidence: "the whole industry's moving from annual underwriting reviews to
continuous, real-time risk scoring"
```

Then, as a separate, named finding — not folded into any element's line:

```
**Sequencing** — No violation found. Vision led, features followed.
```

or

```
**Sequencing violation** — features (real-time scoring engine, data
unification layer) were introduced before any change-in-the-world or
promised-land framing; the closest thing to element 1 was a one-line aside
after the feature pitch, not an established narrative.
```

## Do not

- Don't quote or reproduce Corporate Visions' or Force Management's step
  names and scoring definitions as if they were this skill's own — they're
  cited for corroboration only in `references/rubric.md`, not reused here.
- Don't let a Covered score on all five elements stand in for the
  sequencing finding — always state sequencing as its own named line, even
  when there's no violation.
- Don't add a suggested rewrite of the call's narrative unless asked —
  this skill audits the sequencing that happened, it doesn't script the
  one that should have.

## Related skills

- **`challenger`** — for whether the call taught the buyer something new
  (Teach/Tailor/Take-control); use this skill instead when the question is
  narrative order, not teaching quality. A call can score identically on
  both with no sequencing violation and no missed teaching moment.

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
