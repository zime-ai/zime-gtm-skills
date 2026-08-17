# Brief: won-pipeline-check-demo CSV

Same discipline as the deal-risk-digest brief, adapted for the handoff-data
checks: decide the row roster and each row's flagged checks *before* writing
values into the sheet, per `references/rubric.md`'s exact six-check rubric (a
deterministic rubric, unlike transcript-audit skills — this lets the gold file
be exact rather than judgment-based).

Reference date for every relative date below: **2026-08-17** (the date
this brief was authored). The won-date-in-future check depends on this anchor.

## Deliberate construction (per row, decided before the sheet)

- **Rows 1-2 — clean, must pass all six checks**: the rubric's own
  "reads-well-too" check requires at least two such rows in any sample —
  a won deal with real CS owner, kickoff date, contract value=deal value
  (or differs with reason documented), consistent dates, contract ID,
  probability=100%. No flags at all on either row.
- **Row 3 — Flag #1 only (no CS owner)**: CS owner field is empty; all
  other fields present and clean. Tests check 1 in isolation.
- **Row 4 — Flag #2 only (no kickoff date)**: Kickoff date is empty; all
  other fields present and clean. Tests check 2 in isolation.
- **Row 5 — Flag #3 only (no signed value or term)**: Contract value is
  empty; term is filled in (or vice versa). Deal value is present but no
  contract value means check triggers. No value-reason field needed when
  contract value is missing — the absence itself is the flag. Tests check 3.
- **Row 6 — Flag #4 only (date inconsistency — future won date)**: Won date
  is 2026-09-15 (after 2026-08-17 reference date), making it in the future.
  Created date and close date are both before reference date and consistent
  with each other. Tests the "won date in future" branch of check 4.
- **Row 7 — Flag #5 only (no contract reference)**: Contract ID field is
  empty. All other fields complete and consistent. Tests check 5.
- **Row 8 — Flag #6a (orphaned record — no deal owner at all)**: Deal owner
  column is empty (not just CS owner, but the deal/account owner is absent).
  Probability is 100% (so the probability check would pass if owner existed).
  Tests the "no deal owner" half of check 6.
- **Row 9 — Flag #6b (orphaned record — probability not 100%)**: Deal owner
  and CS owner both present, kickoff date exists, but probability is still
  60% on a Closed Won row. This indicates the CRM was only half-updated
  post-win. Tests the "probability not 100%" half of check 6.

## Expected final flagging (computed by hand from the rubric, not guessed)

| Deal | Flags | Evidence |
|---|---|---|
| Sterling Corp | Clean | none |
| Pinnacle Tech | Clean | none |
| North Ridge Solutions | Flag #1 | cs_owner = (empty) |
| Vantage Group | Flag #2 | kickoff_date = (empty) |
| Cascade Industries | Flag #3 | contract_value = (empty) |
| Apex Ventures | Flag #4 | won_date = 2026-09-15 (future) |
| Horizon Logistics | Flag #5 | contract_id = (empty) |
| Zenith Partners | Flag #6 | owner = (empty) |
| Nexus Financial | Flag #6 | probability = 60% on Closed Won (orphaned CRM state) |

Closing lines expected: **"2 of 9 deals in Won pipeline flagged"** for the
count (rows 8-9 have flags; note that rows 1-2 are clean, rows 3-7 each have
exactly one flag, all in-scope), and the **single most common flag across all
flagged rows** is **Flag #6 (orphaned record)**, appearing 2 of 9 times
(Zenith, Nexus), ahead of each other flag at 1 time each.

Actually, wait — let me recalculate. The closing line says "N of M deals
flagged" — I need to count how many rows have at least one flag:
- Row 1 (Sterling): 0 flags
- Row 2 (Pinnacle): 0 flags
- Row 3 (North Ridge): 1 flag (#1)
- Row 4 (Vantage): 1 flag (#2)
- Row 5 (Cascade): 1 flag (#3)
- Row 6 (Apex): 1 flag (#4)
- Row 7 (Horizon): 1 flag (#5)
- Row 8 (Zenith): 1 flag (#6a)
- Row 9 (Nexus): 1 flag (#6b)

So 7 of 9 deals flagged (all except the two clean ones). The most common flag
is Flag #6 at 2/7 = 2 of the flagged deals.
