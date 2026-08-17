# Gold label: poc-pilot-pipeline-check-demo.csv

Computed by hand from `references/rubric.md`'s six-check rubric and
`evals/illustrative/BRIEF-poc-pilot-pipeline-check.md`'s construction,
against today = 2026-08-17. This rubric is deterministic — every cell
below is a fact, not a judgment call.

## Expected flagged deals (in ranked order: most flags first, then by deal value desc)

| Deal | Flags | Evidence | Suggested action |
|---|---|---|---|
| Quantum Systems | 3 | exit_criteria=(empty); poc_end_date=(empty) AND conversion_date=(empty); sponsor=(empty) | Define exit criteria, set a conversion target date, assign an executive sponsor before proceeding |
| NeoTech Corp | 1 | poc_end_date=2026-07-10 is in the past; deal still in POC/pilot stage with no decision recorded | Resolve POC outcome or move deal out of POC stage |
| Zenith Analytics | 1 | sponsor=(empty) | Assign an executive sponsor to unblock escalation decisions |
| Stellar Labs | 1 | poc_start_date=2026-05-01 (108 days old, exceeds median duration of 92 days); no poc_end_date set | Set an end date for this POC or it will drift indefinitely |
| Zenith Solutions | 1 | exit_criteria=(empty) | Document success criteria before continuing |
| Prism Industries | 1 | poc_status=live but usage=(empty) | Record usage evidence (adoption, seat counts, feature use) or re-assess live status |

## Expected clean deals (in ranked order: by deal value desc)

| Deal | Evidence |
|---|---|
| Globex Inc | All checks pass |
| Acme Corp | All checks pass |
| API Gateway Pro | All checks pass (poc_end_date is present, so flag #2 does not fire despite empty conversion_date) |

## Summary

**6 of 9 deals in POC/pilot flagged.**

**Most common flag across flagged deals: no written exit criteria** (appears on 2 of 6 flagged: Quantum Systems, Zenith Solutions). All other flags (no sponsor, past end date, no usage, open-ended) appear once each.

## The traps (findings a correct run must get right)

1. **Quantum Systems has three separate flags**, not one umbrella "broken deal"
   flag — each check in the rubric fires independently.
2. **NeoTech's past-end-date flag requires both conditions**: poc_end_date
   in the past AND decision field empty AND deal still in POC/pilot stage.
   Proper AND logic, not either/or.
3. **API Gateway Pro must be Clean on flag #2** even though conversion_date
   is empty, because poc_end_date is not empty — the rule is "both columns
   empty," not "either column empty." This tests understanding of the
   condition's exact wording.
4. **Prism Industries' usage flag (#5) fires because poc_status=live and
   the usage column exists and is empty** — the flag applies only under
   those conditions. If either condition were false, result would be
   Unknown or Clean.
5. **Stellar Labs' open-ended flag (#6) uses the actual computed median
   POC duration.** The median of rows 1, 2, 3, 5, 6, 7 (those with both
   start and end dates):
   - Row 1: 2026-09-05 - 2026-06-05 = 92 days
   - Row 2: 2026-09-10 - 2026-05-15 = 118 days
   - Row 3: 2026-09-30 - 2026-07-01 = 90 days
   - Row 5: 2026-07-10 - 2026-05-10 = 61 days
   - Row 6: 2026-09-10 - (empty start date) = skip, no start date
   - Row 7: 2026-10-10 - 2026-07-10 = 92 days
   
   Sorted: 61, 90, 92, 92, 118 — median = 92 days.
   Cutoff: 2026-08-17 - 92 days = 2026-05-17.
   Stellar's start date (2026-05-01) is before 2026-05-17, so it flags.

## Not present: reporting any of these is a hallucination

- Any flag on Acme Corp, Globex Inc, or API Gateway Pro — all three must
  be Clean.
- A flag not in the six defined in the rubric (no exit criteria, no
  conversion date, past end date, no sponsor, no usage, open-ended).
- Any inferred date, status, or name not present in the CSV cell.
- A claim that any column was missing — every column needed by the rubric
  is present in this sheet.
- Incorrect median calculation or a hardcoded number instead of the
  computed median for the open-ended check.
