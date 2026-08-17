Row-by-row check (CSV vs gold vs output):

| Deal | Gold flag | Output flag | Evidence match | Verdict |
|---|---|---|---|---|
| Sterling Corp | Clean | Clean | — | PASS |
| Pinnacle Tech | Clean | Clean | — | PASS |
| North Ridge Solutions | Flag #1, cs_owner empty | No CS/onboarding owner, cs_owner empty | match | PASS |
| Vantage Group | Flag #2, kickoff_date empty | No kickoff date, kickoff_date empty | match | PASS |
| Cascade Industries | Flag #3, contract_value empty | No signed value/term, contract_value empty | match | PASS |
| Apex Ventures | Flag #4, won_date future | Date inconsistency, won_date 2026-09-15 future | match | PASS |
| Horizon Logistics | Flag #5, contract_id empty | No signed-contract reference, contract_id empty | match | PASS |
| Zenith Partners | Flag #6a, owner empty (orphaned) | Orphaned record, owner empty | match, correctly not conflated with CS owner (present) | PASS |
| Nexus Financial | Flag #6b, probability 60% (orphaned) | Orphaned record, probability 60% | match, correctly not conflated with owner/CS owner (both present) | PASS |

All 9 rows correct on flag + evidence. No hallucinated flags, no phantom column ("value_reason"), no false close/won mismatch on Apex, no false owner-flag on North Ridge, no false check#4 on Cascade.

## Ordering fail

Gold ranks flagged deals in CSV row order (North Ridge, Vantage, Cascade, Apex, Horizon, Zenith, Nexus) — all tied at 1 flag each, so tiebreak preserves sheet order. Output instead groups by flag type: Zenith, Nexus (orphaned) first, then North Ridge, Vantage, Cascade, Apex, Horizon. Wrong rank order per rubric's "most flags first" spec — output invented a secondary sort (by flag category) gold doesn't call for.

## Closing lines

Line 1 exact match: "7 of 9 deals in Won pipeline flagged." Line 2 substantively correct (Orphaned record, 2 occurrences) but far thinner than gold's required detail — gold specifies it must lead "ahead of each other flag at 1 of 7 each," output omits that comparison. Content correct, completeness short of gold's exact line.

---

```
ROW_ACCURACY: 9/9 matched
CLEAN_DEALS: correct (Sterling, Pinnacle both Clean)
TRAP_TESTS: 8/8 (all trap rows identified and separated correctly)
HALLUCINATIONS: 0
CLOSING_LINES_CORRECT: no (line 2 missing detail: should explicitly compare count to other flags)
ORDERING_CORRECT: no (output groups by flag type instead of preserving CSV row order)
```

## Summary

- **Row-level accuracy**: 9/9 — every flag, every evidence cell matches exactly.
- **All 8 traps passed** — clean rows stay clean, each flag isolated correctly, no false positives.
- **Hallucinations**: 0 — no invented signals, no phantom columns, no inferred data.
- **Closing line 1**: Correct ("7 of 9 deals flagged").
- **Closing line 2**: Right flag type and count, but incomplete — should detail "ahead of other flags at 1 of 7 each."
- **Table ranking**: **Wrong** — skill grouped by flag type (Orphaned first, then others) instead of sorting by row/CSV order when all flagged deals have equal counts.

Overall: Perfect row-level detection, zero hallucinations, but two output-format violations — table ranking and closing-line detail.
