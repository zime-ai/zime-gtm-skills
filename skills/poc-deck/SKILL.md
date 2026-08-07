---
name: poc-deck
description: Build a client POC/proposal slide deck (.pptx) from discovery/POC call transcripts, the client's playbook, and a CRM export. Use when asked to build, draft, or update a POC deck, client proposal deck, or "the usual GTM deck" for a specific client.
metadata:
  zime:category: internal-gtm
---

# POC deck

Fills `assets/template.pptx` — a tokenized version of Zime's real POC decks
— with one client's specifics, and outputs a ready `.pptx`. Read
`references/deck-anatomy.md` before starting; it explains which slides vary
and which are fixed boilerplate you must never rewrite.

## 1. Pick the deck type

Ask if not stated:

- **Pre-POC proposal** — ends in the 3-week POV plan (slide 20) and the KPI
  funnel (slide 9). `drop_slides` should NOT include 9 or 20.
  `DECK_TITLE_LINE1`: `"Helping {{CLIENT}} Scale"`, `DECK_TITLE_LINE2`:
  `"Without Losing Context"`, `DECK_SUBTITLE`: `"Prepared for {{CLIENT}}  ·
  Confidential"` (repeats the slide's own footer — no cleaner source exists).
- **POC review / close** — ends in demo screens + next steps.
  `drop_slides: [9, 20]`. `DECK_TITLE_LINE1`: `"POC DAY 7 REVIEW"`,
  `DECK_TITLE_LINE2`: `"Building {{CLIENT_SHORT}}'s Sales Execution
  System"`, `DECK_SUBTITLE`: `"Based on past won deals and industry best
  practices"`.

The title slide (slide 1) is the one place fixed copy changes per deck
type — set the three tokens above per type, don't reuse one set for both.

Also drop slide 27 (FAINT rubric appendix) if the chosen initiative isn't
qualification — it's Zime's qualification-specific methodology, not generic.

## 2. Extract, in this order, citing sources as you go

1. **Champion** — name, title, and their goal **verbatim** from a
   transcript. Quote it, don't paraphrase, and note which call it's from.
   Set both `CHAMPION_FIRST` and `CHAMPION_FIRST_UPPER` (slide 6's header
   uses the uppercase form).
2. **Chosen initiative** — one from the catalogue on slide 12 (discovery,
   qualification, expansion, cross-sell, churn, POC success, ...). Drives
   `INITIATIVE_NAME`, `RUBRIC_NAME`, and the rubric appendix choice above.
3. **Blockers** (3, fixed) — each traceable to a specific transcript moment.
4. **Root cause** — whose head, which call recorder, whose strategy — where
   their best practices are locked today.
5. **Risk tiles** (4, fixed) — a stat + one-line consequence each. The stat
   comes from CRM math (show the arithmetic) or a number the client
   themselves stated on a call. **Neither available → `[[TBD: ...]]`, never
   invented.**
6. **Their stack** — actual call-recorder and CRM tool names, for the
   comparison table.
7. **ROI / cost of inaction** — arithmetic shown in a `notes` field alongside
   the spec, so a human can sanity-check it.
8. **Next steps** — owner and ETA per row, from the call's actually-agreed
   actions, not invented tasks.
9. **Commercials** — from the user's prompt if given. This is the one field
   set with no source in transcripts/playbook/CRM — if not given, every
   commercials token becomes `[[TBD: commercials not yet agreed]]`.

Full token-by-token source mapping: `references/token-reference.md`.
Fixed-copy voice rules: `references/copy-patterns.md`.

## 3. Hard rules

- Every client-specific claim traces to a quote, a CRM figure, or a stated
  user input. No invented numbers, no invented objections, no invented tool
  names.
- Champion goal and any quote are verbatim — same words as the transcript.
- Fixed boilerplate slides (see `copy-patterns.md`) are never rewritten to
  "fit the client."
- An unfilled token is a bug, not a style choice — `fill.py` hard-errors on
  it. A genuinely unknown value is `[[TBD: what's needed]]`, not a guess.

## 4. Run it

1. Write a `deck_spec.json` (schema and example in
   `scripts/fill.py`'s docstring and `examples/deck_spec.example.json`).
2. `python3 scripts/tokens.py` if unsure which tokens the template currently
   needs — it's the live source of truth, not this file.
3. `python3 scripts/fill.py deck_spec.json out.pptx`
4. Report every `[[TBD]]` fill.py prints at the end to the user before
   calling the deck done — those need a human to fill before it ships.

## Out of scope

Demo-screen screenshots (slides 23–24) and any redesign of the fixed
boilerplate — this skill fills copy, it does not regenerate visuals or
change the deck's design.
