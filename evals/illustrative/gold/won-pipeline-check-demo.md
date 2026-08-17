# Gold label: won-pipeline-check-demo.csv, scored against `won-pipeline-check`

Computed by hand from `references/rubric.md`'s exact six-check system and
`evals/illustrative/BRIEF-won-pipeline-check.md`'s construction, against
today = 2026-08-17. This rubric is deterministic — every check below is a
fact, not a judgment call, unlike the transcript-audit gold files.

## Expected ranked table (flagged deals first, most flags first)

| Rank | Deal | Flags | Evidence | Suggested action |
|---|---|---|---|---|
| 1 | North Ridge Solutions | Flag #1 | cs_owner = (empty) | Assign CS owner before kickoff |
| 2 | Vantage Group | Flag #2 | kickoff_date = (empty) | Schedule kickoff immediately |
| 3 | Cascade Industries | Flag #3 | contract_value = (empty) | Obtain signed contract value and term |
| 4 | Apex Ventures | Flag #4 | won_date = 2026-09-15 (future) | Correct won date — cannot be after today |
| 5 | Horizon Logistics | Flag #5 | contract_id = (empty) | Link signed contract or order form |
| 6 | Zenith Partners | Flag #6 | owner = (empty) | Assign deal owner to the record |
| 7 | Nexus Financial | Flag #6 | probability = 60% on Closed Won | Update probability to 100% — CRM state mismatch |

Expected closing lines:
- **"7 of 9 deals in Won pipeline flagged"** (rows 3-9; rows 1-2 are clean)
- **Most common flag across them: Flag #6 (orphaned record)**, appearing
  2 of 7 flagged deals (Zenith, Nexus) — ahead of each other flag at 1 of 7
  each (Flags 1, 2, 3, 4, 5 appear one time each).

## The traps (findings a correct run must get right)

1. **Sterling and Pinnacle must NOT be flagged on any check.** Both are
   structurally clean: real owner, CS owner, kickoff date, consistent dates,
   contract value equals deal value (no reason needed), contract ID, 100%
   probability. The "reads-well-too" check requires them to return Clean — if
   they flag, the rubric is being applied too strictly.

2. **North Ridge's missing CS owner is the only flag** — it still has a deal
   owner (James Wilson), so check #6 (no deal owner at all) does not fire.
   The flag is strictly on the empty CS owner field (check #1).

3. **Vantage's empty kickoff_date triggers check #2 only**, not check #3 or
   #6. Contract value is present and equals deal value, probability is 100%,
   and a deal owner exists.

4. **Cascade's empty contract_value triggers check #3 only** — contract_term
   is filled in (12 months), but the absence of contract_value is sufficient
   to flag per "contract value or contract term field is empty" (it doesn't
   require both to be empty). Deal value is 35000, but without contract_value
   present, there's no evidence the contract matched the quote.

5. **Apex's future won_date (2026-09-15, nine days after 2026-08-17) triggers
   check #4 only.** Close date and won date match, so there's no
   close-date/won-date disagreement. Created date (2026-07-01) is before
   won_date, so it doesn't violate the "won before created" rule. The only
   violation is the future-date check.

6. **Horizon's empty contract_id triggers check #5 only** — all other handoff
   fields are present, dates are consistent (close = won = 2026-07-15),
   probability is 100%, both owners assigned.

7. **Zenith's empty owner (deal owner, not CS owner) triggers check #6a** —
   the row has no deal owner at all, per the "no deal owner at all" clause
   of check #6. CS owner is present (Nicole Brown), but that's not a
   substitute for deal owner. Probability is 100%, so the probability clause
   doesn't fire.

8. **Nexus's 60% probability triggers check #6b** — it has both deal owner
   and CS owner, kickoff date, complete contract data, and consistent dates.
   The 60% probability on a Closed Won row indicates the CRM state is
   incomplete: the deal won but someone forgot to update the probability
   from its original forecast value. This is the "orphaned record" signal —
   a post-win CRM housekeeping miss.

## Not present: reporting any of these is a hallucination

- Any flag on Sterling or Pinnacle (both are clean per the reads-well-too
  check).
- A claim that North Ridge has check #6 flagged (has deal owner, has 100%
  probability).
- A claim that Cascade has check #4 flagged (dates are consistent: created
  2026-01-10, close 2026-02-28, won 2026-02-28 — close = won, both after
  created).
- A claim that Apex has a close-date/won-date mismatch (both are 2026-09-15).
- A claim that Zenith's check #1 (no CS owner) is flagged separately from
  check #6 (the row *has* a CS owner — Nicole Brown — so check #1 is clean,
  only check #6 fires because owner/deal owner is empty).
- Any "value mismatch flagged without reason" on rows 1, 2, 3, 4, 6, 7, 8, or
  9 — none have contract_value ≠ deal_value; only Cascade has a missing
  contract_value entirely.
- A claim that the "value_reason" column is missing (it is not present in
  the CSV, but this does not cause all rows to report Unknown — the column's
  absence only matters for the contract-value-mismatch half of check #3,
  which doesn't apply to any row that has all required data).
- Any total count other than 9 rows in scope, or any mention of out-of-scope
  rows (all 9 rows have stage = "Closed Won").
