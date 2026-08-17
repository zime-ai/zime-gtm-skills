Grade: OUTPUT.md vs GOLD.md, pipeline.csv (9 rows).

## Row-level table

| Deal | Gold Flags | Output Flags | Match |
|---|---|---|---|
| Quantum Systems | 3 | 3 | Yes |
| NeoTech Corp | 1 | 1 | Yes |
| Zenith Analytics | 1 (no sponsor) | 0 — omitted, treated clean | **No** |
| Stellar Labs | 1 (open-ended only) | 2 (added "no conversion date") | **No** |
| Zenith Solutions | 1 | 1 | Yes |
| Prism Industries | 1 | 1 | Yes |
| Globex Inc | 0 | 0 | Yes |
| Acme Corp | 0 | 0 | Yes |
| API Gateway Pro | 0 | 0 | Yes |

6/9 deal rows correct. 2 wrong.

## Flag count accuracy
Gold: 6 of 9 flagged. Output: 5 of 9 flagged. **Wrong** — Output dropped Zenith Analytics entirely (no-sponsor flag missed), so total off by one.

## Ranking check
Gold order (flags desc, tie broken by deal value desc): Quantum(3) > NeoTech(1,85k) > Zenith Analytics(1,65k) > Stellar Labs(1,55k) > Zenith Solutions(1,45k) > Prism(1,35k).

Output order: Quantum(3) > Stellar Labs(2) > Zenith Solutions(1) > NeoTech(1) > Prism(1).

**Wrong.** Stellar Labs bumped to rank 2 only because of its bogus extra flag. Zenith Analytics missing from list entirely. NeoTech(85k) ranked below Zenith Solutions(45k) — value-tiebreak also broken.

## Most common flag (closing line)
Gold: "no written exit criteria" — 2/6 (Quantum, Zenith Solutions), all others once each, no tie.
Output: "tie between 'no written exit criteria' and 'no conversion date' (2 deals each)."

**Wrong.** Tie is fabricated — only exists because Output wrongly gave Stellar Labs a "no conversion date" flag.

## Closing line 1 (count flagged)
Gold: 6 of 9. Output: 5 of 9. **Wrong.**

## Trap assessment (5 traps)

| # | Trap | Result |
|---|---|---|
| 1 | Quantum = 3 separate flags, not one umbrella | **Pass** |
| 2 | NeoTech past-end-date needs AND logic (date past + decision empty + stage POC/pilot) | **Pass** |
| 3 | API Gateway Pro stays Clean (poc_end_date present despite empty conversion_date) | **Pass** |
| 4 | Prism usage flag fires only under poc_status=live AND usage empty | **Pass** |
| 5 | Stellar open-ended uses computed median (92 days), not hardcoded | **Pass** (median = 92, matches gold, correct cutoff, correct flag fires) |

All 5 constructed traps passed. Errors are outside the trap set: the Zenith Analytics omission and the spurious Stellar Labs "no conversion date" flag.

## Hallucinations
- **Stellar Labs "no conversion date" flag**: not in gold, not consistent with gold's own rubric application (gold explicitly gives Stellar only the open-ended flag). This is an extra, ungrounded flag.
- Median duration inputs list slightly off (Zenith Solutions=91 vs gold's 90) but final median (92) still matches — cosmetic, not a hallucination that changes output.
- No other invented dates/names/statuses found. Opening scope line ("9 of 9 rows in POC/Pilot") is accurate.

## Summary score
**6/9 row-level correct, 2 wrong** (Zenith Analytics false negative, Stellar Labs false-positive extra flag). Both closing-line checks fail (count 5 vs 6, tie claim fabricated). Ranking broken as downstream consequence. All 5 designed traps passed cleanly — errors are real but outside trap coverage.

**Grade: FAIL** (closing-line accuracy is explicit rubric check; both closing lines wrong).
