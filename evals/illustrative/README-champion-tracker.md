# Illustrative self-authored run: `champion-tracker`

Same mechanism, same caveat as `meddicc`/`challenger`/`deal-risk-digest`
(`evals/illustrative/README.md`). **This one is weaker than the other
three on the self-authorship axis**: I wrote `champion-tracker`'s own
rubric (PR #26), so there is no "best-effort blinding" claim to make at
all here — this run tests the mechanism, not independence, more plainly
than any of the others.

This is Shape C (document-writer) — gold is a **reference action ledger**
(a document a human would have produced, Tier 0's shape), graded by
row-by-row diff (present/missing/wrong-tag/extra), not by findings recall.
The transcripts deliberately use different names/company than the skill's
own bundled `assets/sample-call-*.txt` fixture to avoid re-testing a
scenario the skill was already built and graded against — see
`BRIEF-champion-tracker.md`.

## Result

Full grader output: `runs/champion-tracker-demo-verdict.md`. Skill's raw
output: `runs/champion-tracker-demo-output.md`.

| Metric | Result |
|---|---|
| Gold rows present, correctly tagged | 7/7, 0 wrong-tag |
| Extra rows beyond gold | 4 (3 legitimate additional Sentiment rows, 1 overreach) |
| The planted trap (stated intention ≠ Action) | Passed on the call-1 occurrence |
| Champion read | Correct (Marisol sole candidate, Callum correctly excluded) |
| Trend | Correct ("strengthening," same underlying reasoning as gold) |
| Hallucinations | 0 |

## Reading this honestly

The one real finding: the skill passed the planted trap where I expected
it (call 1's "I want to get this in front of our finance lead sometime
soon"), but then **failed the identical trap shape later, un-planted, on
its own** — it tagged "she's asked me to bring a formal proposal to next
month's budget review" as Action, when that's a future task Marisol was
asked to do, not something she'd done yet. Same failure mode the rubric
warns against, just not the specific sentence I built the trap around.
That's a more convincing signal than passing a single planted trap would
have been on its own — it suggests the failure mode generalizes past the
one sentence I anticipated, though still from one transcript, one grader,
one author throughout.

## Reproducing this

Same pattern as the other illustrative runs, running the skill against
both `champion-tracker-demo-call-1.txt` and `champion-tracker-demo-call-2.txt`
together (`claude -p "/champion-tracker ./call1.txt ./call2.txt" --dangerously-skip-permissions`),
then grading in a separate isolated dir containing only the real output +
both transcripts + `gold/champion-tracker-demo.md` — never `SKILL.md`.
