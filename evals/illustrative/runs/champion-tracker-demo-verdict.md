## Row diff (gold 7 rows)

| Gold row | Match in output |
|---|---|
| Marisol c1 finance-lead intent → Sentiment | PRESENT, correct tag |
| Marisol c2 "looped in finance lead" → Action | PRESENT |
| Marisol c2 pushback → Action | PRESENT |
| Marisol c2 security call → Action | PRESENT |
| Callum c1 "exactly what we need" → Sentiment | PRESENT |
| Callum c1 "telling everyone on floor" → Sentiment | PRESENT |
| Callum c2 "glad this is finally moving" → Sentiment | PRESENT |

All 7 present, all tags right. 0 wrong-tag.

## Extra rows (not in gold)

1. Marisol c1 "Let me think about timing..." → Sentiment — legit, real quote, correct tag.
2. Callum c1 "really hope this happens" → Sentiment — legit.
3. Callum c2 "we're all rooting for it" → Sentiment — legit.
4. Marisol c2 "asked me to bring a formal proposal to next month's budget review" → tagged **Action** ("driving formal internal process") — **overreach**. Quote describes finance lead's ask for a future proposal, not a completed act yet — same stated-intention-not-yet-done shape as the call-1 trap. Should be Sentiment/plan, not Action. This also inflates output's own champion-read count to "4 Action rows" vs gold's 3.

## Trap check
Call-1 finance-lead line correctly tagged Sentiment. Trap passed. But output failed an equivalent trap later in call 2 (the formal-proposal line), same failure mode gold warns against.

## Champion read
Marisol sole candidate, Callum correctly excluded, zero Action rows for Callum. Correct in substance despite inflated Action count (4 vs true 3).

## Trend
"Strengthening," same underlying logic (call 1 = plan only, call 2 = real actions). Correct, though restated with one extra (wrong) action padding the count.

## Hallucination check vs gold's "Not present" list
No third contact, no invented dollar figures/competitor, no fabricated date beyond "Thursday," no Callum Action row. Clean — nothing invented outside the transcripts. The formal-proposal issue is a **mis-tag**, not a hallucinated fact.

---

ROWS_PRESENT: 7/7
ROWS_WRONG_TAG: 0
EXTRA_ROWS: 4 (3 legitimate / 1 overreach)
TRAP_PASSED: yes
CHAMPION_READ_CORRECT: yes
TREND_CORRECT: yes
HALLUCINATIONS: 0
