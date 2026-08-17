# Illustrative self-authored run: `deal-risk-digest`

Same mechanism and same caveat as the `meddicc`/`challenger` runs
(`evals/illustrative/README.md`) — same author behind brief, CSV, gold,
and grading prompt; real isolation only between the skill-run process and
the grading process; **not Tier 3, not evidence of real-world accuracy.**

This is Shape B (CSV pipeline-sweep) — the first proof that the gold
template adapts to a deterministic, row-scored skill rather than a
transcript-audit rubric. Because `deal-risk-digest`'s rubric is an exact
point system (`references/rubric.md`), the gold file here is a computed
fact, not a judgment call — this run has much less room for reasonable
disagreement than `meddicc`/`challenger`'s did.

## Result

Full grader output: `runs/deal-risk-digest-demo-verdict.md`. Skill's raw
output: `runs/deal-risk-digest-demo-output.md`.

| Metric | Result |
|---|---|
| Row-level accuracy (points + tier, all 9 deals) | 9/9 |
| Ranking / tiebreak (three-way point tie sorted by value) | Correct |
| Traps passed (5 constructed traps — stale-but-fine, early-pipeline, empty-contacts-counts, tiebreak, exact-3pt boundary) | 5/5 |
| Hallucinations | 0 |
| Closing line 1 ("N of M deals High risk") | Correct (2 of 9) |
| Closing line 2 ("most common signal") | **Wrong** — output said "past-due close date paired with low probability" (2 of 6 flagged deals); the actual most common signal is blank/vague next step (4 of 6) |

## Reading this honestly

Every row-level score, every trap, and the ranking were exactly right —
strong evidence the skill applies its own deterministic rubric correctly
per-row. But the one aggregate/summary statistic it had to compute across
rows (which signal is most common) came out wrong, and confidently stated
as if correct, with no hedge. That's a meaningfully different failure mode
than `meddicc`/`challenger`'s pattern (resolving ambiguity toward more
confidence) — this is a plain counting error on an otherwise perfect run,
not an ambiguity-resolution bias. One sample; treat as one data point, not
a verdict on the skill.

## Reproducing this

Same pattern as the other illustrative runs, using
`evals/illustrative/artifacts/deal-risk-digest-demo.csv` as the input
instead of a transcript, and pointing the skill at it as
`claude -p "/deal-risk-digest ./pipeline.csv" --dangerously-skip-permissions`.
Grading scratch dir contains only the skill's real output + the CSV +
`gold/deal-risk-digest-demo.md` — never `SKILL.md`.
