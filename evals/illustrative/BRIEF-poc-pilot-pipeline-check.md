# Brief: poc-pilot-pipeline-check-demo CSV

Same discipline as the pipeline briefs: decide the row roster and each
row's intended flag *before* writing values into the sheet, per
`references/rubric.md`'s six-check rubric (deterministic — the gold file
is an exact computed fact, not judgment).

Reference date for every relative date below: **2026-08-17** (the date
this brief was authored).

## Deliberate construction (per row, decided before the sheet)

- **Rows 1-2 — clean, must pass all checks (0 flags)**: the rubric's own
  "reads-well-too" check requires at least two such rows in any sample —
  written exit criteria, a conversion date or end date, an executive
  sponsor, and (if live) recorded usage.
- **Row 3 — no exit criteria only (1 flag)**: exit_criteria column is
  empty, everything else clean. Tests flag #1 in isolation.
- **Row 4 — maximum flags (3 flags)**: no exit criteria (flag #1), no
  conversion date and no poc_end_date (flag #2), and no sponsor (flag
  #4). The clearest possible Flagged deal.
- **Row 5 — past its own end date with no decision (1 flag)**: poc_end_date
  is in the past (2026-07-10, before today 2026-08-17), deal still in
  POC/pilot stage, decision field empty. Tests flag #3.
- **Row 6 — no executive sponsor (1 flag)**: sponsor column is empty, tests
  flag #4 in isolation.
- **Row 7 — live POC with no usage evidence (1 flag)**: poc_status=live,
  usage column is empty. Tests flag #5 (applies only if column exists and
  POC is live).
- **Row 8 — open-ended POC (1 flag)**: poc_start_date older than median
  POC duration, no poc_end_date. Median computed from rows 1-3, 5-7 with
  both dates: (92 + 118 + 90 + 61 + 92 + 92) / 6 = 92 days. Start date
  2026-05-01 (108 days old) exceeds this. Tests flag #6.
- **Row 9 — trap: no conversion_date but HAS poc_end_date (should be
  CLEAN)**: The rubric for flag #2 is explicit — *both* columns must be
  empty. Having an end date means this row should NOT flag on #2, even
  though conversion_date is blank. Tests that the condition is AND, not
  either/or.

## Expected final flags (computed by hand from the rubric)

| Deal | Flags | Count |
|---|---|---|
| Acme Corp | none | 0 |
| Globex Inc | none | 0 |
| Zenith Solutions | no exit criteria | 1 |
| Quantum Systems | no exit criteria, no conversion date, no sponsor | 3 |
| NeoTech Corp | past end date, no decision | 1 |
| Zenith Analytics | no sponsor | 1 |
| Prism Industries | live but no usage | 1 |
| Stellar Labs | open-ended (no end date, old start) | 1 |
| API Gateway Pro | none | 0 |

Closing lines expected: **"6 of 9 deals in POC/pilot flagged"**, and the
single most common flag across the 6 flagged deals is **no written exit
criteria**, appearing on 2 of them (Zenith Solutions, Quantum Systems) —
note that the next-most-common flags (no sponsor, past end date, no usage,
open-ended) each appear once.

## The traps (findings a correct run must get right)

1. **Quantum Systems must be flagged on three separate issues**, not
   collapsed into one. The rubric defines each check independently.
2. **NeoTech's past end date triggers only because decision is empty AND
   the deal is still in POC/pilot stage.** If either condition were false
   (decision filled, or deal moved out of POC stage), the flag would not
   fire. Test proper AND logic.
3. **Row 9 (API Gateway) must NOT flag on "no conversion_date"** even
   though conversion_date is empty — it has a poc_end_date, so flag #2's
   "both empty" condition is false. Tests that the check requires both
   columns to be absent, not just one.
4. **Prism Industries' usage flag (#5) applies only because poc_status=live
   and the usage column exists.** If poc_status were something else or if
   the column were missing entirely, this would be Unknown, not Flagged.
5. **Stellar Labs' open-ended flag (#6) uses the actual median computed
   from the sample, not a hardcoded number.** The median is 92 days
   (2026-05-17 is the cutoff date); Stellar's 2026-05-01 start date
   exceeds that by 16 days.

## Not present: reporting any of these is a hallucination

- Any flag on Acme Corp, Globex Inc, or API Gateway Pro (all clean).
- A flag not in the six defined in the rubric.
- Any inferred date, name, or role not present in the CSV cell.
- A claim that any column was missing — every column used by the rubric is
  present in this sheet.
- A "median POC duration" claim that is not the actual computed median from
  rows with both start and end dates present.
