# Brief: new-business-registration-demo CSV

Same discipline as the other CSV briefs: decide each row's completeness
profile (which of the six rubric dimensions are present, which missing)
*before* writing values into the sheet, per `references/rubric.md`.

Reference date for every relative date below: **2026-08-17** (the date
this brief was authored). The expiry-date dimension checks whether a
validity window is set, regardless of whether it's future or past relative
to today.

## Deliberate construction (per row, decided before the sheet)

- **Rows 1-2 — clean, all six dimensions present**: legal entity and
  domain both filled; duplicate check run (Yes); source stated; ICP fit
  articulated; requested support specified; expiry date set. These are
  the rubric's "reads-well-too" anchors.
- **Row 3 — maximum missing (5 of 6 missing)**: only company name,
  submitted_by, and submitted_date present. Everything else blank.
- **Row 4 — trap: legal_entity filled, but domain missing.** Tests whether
  the rubric requires *both* entity AND domain identified, or either one
  counts. The rubric says "legal entity + domain identified" (the +
  suggests both), so missing domain should flag this dimension as missing.
- **Row 5 — trap: domain filled, legal_entity missing.** Mirrors Row 4
  from the opposite direction — tests the same + interpretation.
- **Row 6 — trap: duplicate_check_run = empty string.** Does an empty cell
  (vs. "No") count as "no evidence a check happened"? The rubric asks "was
  the account checked" — empty should mean "no evidence," same as "No".
- **Row 7 — clean row (all six dimensions).** Boundary test: can the skill
  find all six in a different row arrangement / value mix than rows 1-2.
- **Row 8 — trap: expiry_date is in the past (2026-07-01, before today
  2026-08-17).** Does "expiry / validity window set" count a past date as
  "set"? The rubric says "defined validity window or expiry date" — a
  past date is still defined/set, even if it's expired. Should NOT flag
  this dimension as missing.

## Expected completeness per row (computed by hand from the rubric)

| Company | Entity | Domain | DupCheck | Source | ICP Fit | Support | Expiry | Missing (expected) |
|---|---|---|---|---|---|---|---|---|
| Acme Logistics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | None (0/6) |
| TechFlow Systems | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | None (0/6) |
| Rapid Fulfillment | - | - | - | - | - | - | - | All 6 |
| Coastal Industries | ✓ | - | ✓ | ✓ | ✓ | ✓ | ✓ | Domain (1/6) |
| Metropolitan Finance | - | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Legal entity (1/6) |
| Frontier Retail | ✓ | ✓ | - | ✓ | ✓ | ✓ | ✓ | Duplicate check (1/6) |
| Valley Logistics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | None (0/6) |
| Legacy Systems | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (past) | None — expiry is set, even if past (0/6) |

Closing observation: the two clean rows and the maximum-miss row provide
clear anchors; the four trap rows test boundary conditions on the "entity +
domain" pair and expiry dating.
