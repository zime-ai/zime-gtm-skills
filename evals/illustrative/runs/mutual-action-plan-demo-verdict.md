## Row-by-row comparison

**Gold #1 (security questionnaire, heard)** → output row 1, tagged **heard**, quotes match. Correct. Output adds calendar date "Fri 2026-08-28" — not stated in transcript (only "Friday"), a computed addition beyond source text.

**Gold #2 (budget sign-off, inferred — the trap)** → output row 4, tagged **inferred**. **Trap passed.** Reasoning matches gold almost verbatim (no date, vague "moving", single-sided owner).

**Gold #3 (live demo, inferred)** → output row 5, tagged **inferred**. Correct, matches gold reasoning (vague date, no prospect-side owner).

**Gold #4 (MSA send + procurement loop-in, single heard row)** → output **splits this into two rows**:
- row 2: MSA send, tagged **inferred**, owner (prospect) marked *missing*
- row 3: procurement review, tagged **heard**, owner Sam

This split is not clearly defensible. Transcript line is one utterance: "I'll get the redlined MSA over to you by Wednesday so Sam has something concrete to start with" — Sam is named as owner right in that sentence, tied to the MSA action. Output row 2 discards that link and marks owner missing to justify downgrading to inferred, while row 3 reuses Sam for the separate procurement-review claim. Net effect: gold's one clean `heard` milestone becomes one `inferred` + one `heard` in output — an artificial downgrade, not a neutral restructuring. Flag as a tagging error, not just alternate splitting.

Output dates for this row also invented beyond transcript: "Wed 2026-09-02" and "end of next week (~2026-09-04)" — transcript only says "Wednesday" and "end of next week," no calendar dates given.

## Hallucination check
No invented names, dollar figures, or contract terms — Priya Okafor, Sam, Renata Fisk all grounded. No fabricated milestones. The only issue is invented **calendar dates** (2026-08-28, 2026-09-02, ~2026-09-04) computed from the stated call date but not literally present in transcript — minor over-specification, not fabricated facts, but diverges from gold's practice of keeping dates as stated ("Friday", "Wednesday").

## Verdict table

| Check | Result |
|---|---|
| Gold rows present | 4/4 (row 4 split into 2, content still covered) |
| Correctly tagged | 3/4 clean; 1/4 (MSA+procurement) mis-split, downgrades a heard fact to inferred |
| Trap (budget sign-off → inferred) | **Passed** |
| Hallucinated milestones/names | None |
| Invented specificity | 3 calendar dates computed, not stated in transcript |

**Overall:** solid run. Trap caught correctly, no fabricated entities. Main defect: splitting gold's single MSA/procurement milestone into two rows strips Sam as owner from the MSA row, manufacturing an `inferred` tag where the transcript actually supports `heard` (same sentence names both the date and the owner). Also over-specifies exact calendar dates beyond what the call stated. Not a failing run, but not a clean pass either — one tag is defensibly wrong.
