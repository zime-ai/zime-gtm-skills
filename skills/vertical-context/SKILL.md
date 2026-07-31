---
name: vertical-context
description: Provides industry-vertical context packs (buyer titles, compliance drivers, domain vocabulary) that any other skill in this repo can load when a call is specialized for a named industry. Use when a stage or initiative skill is asked to analyze a call for a specific vertical (cybersecurity, healthcare, fintech), not as a skill to run on its own.
license: MIT
metadata:
  zime:category: cross-cutting
  zime:dimension: vertical-context
  zime:input-modes: none
---

# Vertical Context Packs

This is not a skill you run directly — it's a reference library other
skills load when a call is specialized for a named industry. It's the
answer to the **vertical** dimension: rather than one skill per
vertical-per-motion (which would mean re-authoring all 15 stage/initiative
skills for every new industry), any of them can load one of these packs and
apply it on top of their own rubric.

## Status: unreviewed

These three packs (`cybersecurity`, `healthcare`, `fintech`) were authored
from general domain knowledge, not verified against a domain expert or real
call data. A "vertical jargon check" was scoped for this pass and explicitly
not run yet — see `MAINTAINING.md`. Treat the vocabulary and priors as a
plausible starting draft, not validated fact, until someone with real
domain exposure signs off.

## The contract

A vertical pack may supply:

- Typical buyer titles and who actually holds signing authority
- Compliance / regulatory regimes that create urgency in this industry
- A specialized variant of the calling skill's category taxonomy
- Domain vocabulary a rep is expected to use or recognize
- Typical procurement shape and cycle length
- What a disqualifying signal looks like in this vertical

A vertical pack must **never**:

- Override what a transcript actually says — it supplies priors and
  vocabulary, not a substitute for evidence
- Let a calling skill report a finding without a direct quote, just because
  the pack made the finding plausible
- Suppress a real quote or pain point because it doesn't fit the pack's
  taxonomy — an out-of-taxonomy finding gets reported and flagged as such,
  not dropped

## How a calling skill uses this

1. If the user names a vertical (or one is otherwise evident), read
   `references/<vertical>.md`.
2. Use its vocabulary and category variant for framing and labeling.
3. Every finding still needs to trace back to the transcript in front of
   you. The pack changes how you describe what you find, not what counts as
   evidence.
4. If no vertical is named, the calling skill's own generic rubric applies
   unmodified.

## Available packs

- `references/cybersecurity.md`
- `references/healthcare.md`
- `references/fintech.md`

Each follows the same section order so a calling skill (or a person
comparing two verticals) can find the same thing in the same place across
packs.
