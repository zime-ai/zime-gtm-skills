# Illustrative self-authored run: `technical-discovery`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**seven-dimension scorecard**, graded by per-dimension agreement plus a
planted-trap check.

## Result

Full grader output: `runs/technical-discovery-demo-verdict.md`. Skill's
raw output: `runs/technical-discovery-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 7/7 exact match |
| Trap (business-buyer enthusiasm ≠ named technical stakeholder) | Passed |
| Hallucinations | 0 |

## Reading this honestly

Full clean pass — every dimension matched gold, and the planted trap
landed with sharper reasoning than gold even asked for: the run correctly
scored "technical stakeholders identified" as Missed off Casey's
enthusiasm ("I don't think we need to overthink who's involved"), and
went further by explicitly distinguishing Jamie's later-named resourcing
role from an actual technical-evaluator role — a distinction the rubric
implies but the gold reference didn't spell out as explicitly. Closing
read matched gold's two deciding gaps (technical stakeholders, success
metrics) exactly.
