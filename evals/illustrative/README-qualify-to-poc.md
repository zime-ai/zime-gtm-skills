# Illustrative self-authored run: `qualify-to-poc`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**five-dimension scorecard plus a go/no-go close**, graded by
per-dimension agreement plus two planted-trap checks.

## Result

Full grader output: `runs/qualify-to-poc-demo-verdict.md`. Skill's raw
output: `runs/qualify-to-poc-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 5/5 exact match |
| Trap 1 (three Covered dims don't offset Missed Resourcing — independent gates) | Passed |
| Trap 2 ("someone on our side will handle it" ≠ real resourcing) | Passed |
| Hallucinations | 0 |

## Reading this honestly

Full clean pass. All five dimension scores matched gold exactly, and both
planted traps landed correctly — the run didn't let three strong Covered
dimensions pull the close toward "Go," and it correctly refused to credit
the rubric's own example of vague resourcing language as a named owner.
The close call itself came through a little muddled in wording ("No-go
(Needs one more call)" — two labels in one line rather than picking one),
but the underlying reasoning and named blocking dimensions match gold.
