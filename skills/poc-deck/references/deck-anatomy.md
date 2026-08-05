# Deck anatomy

`assets/template.pptx` has 28 slides: the 26 from the Astra POC-review deck,
plus 2 ported from the TrueFoundry pre-POC deck (KPI funnel at slide 9, the
3-week POV plan at slide 20). Two deck types share this one template —
`drop_slides` in the spec removes whichever tail doesn't apply.

| # | Slide | Varies | Fixed |
|---|---|---|---|
| 1 | Title | `CLIENT`, `CLIENT_SHORT` | layout, subtitle copy |
| 2 | "What does {{CHAMPION_FIRST}} want to drive?" | `CHAMPION_FIRST`, `CHAMPION_GOAL` (verbatim) | initiative chip catalogue |
| 3 | Current blockers (fixed at 3) | `BLOCKER_1..3_{TITLE,DESC}` | "CURRENT BLOCKERS" label, numbering |
| 4 | Root cause | `INITIATIVE_NAME`, `RUBRIC_NAME`, `ROOT_CAUSE_1..2` | "×10+ products..." framing |
| 5 | Impact / risk tiles (fixed at 4) | `RISK_HEADLINE`, `RISK_1..4_{LABEL,STAT,DESC}` | tile layout |
| 6 | Champion quote + immediate needs (fixed at 5; **optional** — drop for decks with no champion quote yet) | `CHAMPION_QUOTE`, `CHAMPION_TITLE`, `NEED_1..5_{TITLE,DESC}` | — |
| 7 | "You have two options. Pick one" | — | fully fixed |
| 8 | Introducing | `STEP1_SUBTITLE`, `STEP2_TITLE` | "Step 1 - Build your best practices" |
| 9 | KPI funnel (ported from TrueFoundry; **pre-POC decks only**, drop otherwise) | `CLIENT_TOOLS`, `KPI_*_LINE` | "You have data & insights..." |
| 10 | Step 1 diagram | `NEED_5_TITLE` (reused) | mostly fixed — v1 doesn't tokenize the rest, see Known limitations |
| 11 | Step 2 — operationalized per persona | `METRIC_PRODUCTIVITY`, `METRIC_TIME_SAVED`, `METRIC_HEADCOUNT_SAVED`, `METRIC_WIN_RATE` (fixed at 4 metric slots) | persona rows, "no new tool" line |
| 12 | Initiative catalogue by function | — | fully fixed (identical in both source decks) |
| 13 | Cost of inaction / ROI (**POC-review decks**; TrueFoundry's alternate TODAY→ZIME→OUTCOME framing lives on slide 9 instead) | `ROI_HEADLINE_STAT`, `ROI_HEADLINE_DESC` | "Cost of Inaction" label |
| 14 | How the partnership works | — | fully fixed (identical wording in both source decks, only client name via `CLIENT`) |
| 15 | HP proof (3rd-party case study) | — | fully fixed |
| 16 | Referenceable customers + founder bio | — | fully fixed |
| 17 | Commercials (fixed at 2 line items — see Known limitations) | `ACV_TOTAL`, `ACV_TOTAL_LINE`, `LINE_1_{LABEL,PRICE,DESC}`, `LINE_2_{LABEL,PRICE,DESC}` | "Term / 12 months", "Payment / Annual upfront · Net 30" |
| 18 | Zime pricing (Ignition/Execute/Consumption) | — | fully fixed, identical in both source decks |
| 19 | Next steps (fixed at 4 slots) | `STEP_1..4_TASK`, `STEP_3_LINK`, `STEP_4_LINK`, `STEP_ETA_TBC` | — |
| 20 | 3-week POV plan (ported from TrueFoundry; **pre-POC decks only**, drop for POC-review decks) | `POV_W1..3_TASK1..2_{TITLE,DESC}`, `POV_OUTCOME_1..2` | "POV: Let Us Show You Results" |
| 21 | Their stack vs Zime | `CLIENT_SHORT_UPPER`, `STACK_TOOL_1`, `STACK_TOOL_2` | table rows, "Our secret sauce" footer |
| 22 | Build vs. buy | — | fully fixed |
| 23–25 | Demo divider + 2 product-screen mocks | — | **out of scope** — these are illustrative screenshots, not filled by the skill (see SKILL.md) |
| 26 | Supplement divider | — | fixed |
| 27 | FAINT rubric appendix | — | fixed methodology; drop if the chosen initiative isn't qualification |
| 28 | Why not just prompt Claude | — | fully fixed |

## Known limitations

- **Slide 10 diagram** — only `NEED_5_TITLE` is tokenized (it happens to
  repeat verbatim from slide 6 in both source decks). The rest of the
  diagram's box labels ("Sales Strategy", "MQLs", "Commercials and Terms")
  are left fixed rather than guessed at; if a deck needs different diagram
  inputs, edit the template directly.
- **Commercials — 2 line items max.** The Astra deck (the template's base)
  only ever used 2 pricing lines. TrueFoundry's deck had a 3rd (a one-time
  integration fee). Adding a removable `LINE_3` slot means duplicating a
  shape group in the template — not done for v1. A deck needing a 3rd line
  today requires a manual edit to `template.pptx` in PowerPoint/Slides.
- **Demo screens (slides 23–24) are never filled.** They're illustrative
  product mocks with example deal names. The skill fills copy; it does not
  regenerate screenshots.
- **Formatting collapse on multi-run paragraphs.** If a paragraph containing
  a token has mixed formatting across runs (e.g. part bold, part not),
  filling collapses it to the first run's formatting. None of the current
  tokens hit this, but a future template edit could introduce it — check
  `tokens.py` output visually after any template change.
