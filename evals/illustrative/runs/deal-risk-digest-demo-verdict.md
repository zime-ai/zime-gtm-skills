Row-level check (all 9 deals):

| Deal | Gold | Output | Match |
|---|---|---|---|
| Redstone | 6, High | 6, High | yes |
| Milltown | 3, High | 3, High | yes |
| Thistlebrook | 2, Medium | 2, Medium | yes |
| Bramblewood | 2, Medium | 2, Medium | yes |
| Palisade | 2, Medium | 2, Medium | yes |
| Northgate | 1, Medium | 1, Medium | yes |
| Harborline | 0, Low | 0, Low | yes |
| Cinderpine | 0, Low | 0, Low | yes |
| Ashworth | 0, Low | 0, Low | yes |

No mismatches. 9/9.

**Ranking.** Gold order: Redstone, Milltown, Thistlebrook, Bramblewood, Palisade, Northgate, Harborline, Cinderpine, Ashworth. Output order: identical, including tiebreak Thistlebrook(67k) > Bramblewood(51k) > Palisade(40k). Match.

**Traps:**

1. Ashworth stale-but-fine — gold: "must NOT be flagged." Output: "Low (0pts)... probability = 78% (past-due signal needs prob <50%, not triggered)." PASS.
2. Bramblewood early-pipeline — gold: 2pts must come only from stage age + vague next step, not probability/date. Output reasons: "stage age, vague next step" — no past-due claim. PASS.
3. Thistlebrook empty contacts = single-threaded — gold requires counting empty cell as signal. Output: "vague next step, single-threaded ... contacts = (empty)." PASS.
4. Three-way tie sorts by value descending — output shows Thistlebrook > Bramblewood > Palisade. PASS.
5. Milltown hits High at exactly 3pts, no second signal — output: "High (3pts) ... past-due & unlikely" only. PASS.

5/5 traps passed.

**Hallucination check.** No extra signal on Harborline/Cinderpine/Ashworth, no sixth signal type, no invented contact/next-step/date, no "missing column" claim (output explicitly says "all columns present, none missing" — correct). 0 hallucinations.

**Closing lines.**
- "2 of 9 deals rated High risk" — matches gold exactly. Correct.
- Most-common-signal line — gold: blank/vague next step, 4 of 6 (Redstone, Bramblewood, Thistlebrook, Palisade). Output: "past-due close date paired with low probability" — that signal fires on only 2 deals (Redstone, Milltown), not the most common one. Wrong.

---

```
ROW_ACCURACY: 9/9
RANKING_CORRECT: yes
TRAPS_PASSED: 5/5
HALLUCINATIONS: 0
CLOSING_LINES_CORRECT: no (second line wrong — output says "past-due close date paired with low probability", gold says "blank/vague next step", 4 of 6)
```
