# Illustrative self-authored run: `onboarding-journey`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**five-dimension scorecard**, graded by per-dimension agreement plus a
planted-trap check.

## Result

Full grader output: `runs/onboarding-journey-demo-verdict.md`. Skill's raw
output: `runs/onboarding-journey-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 5/5 exact match |
| Trap (full-call attendance ≠ active engagement) | Passed |
| Hallucinations | 0 |

## Reading this honestly

Full clean pass on substance — every dimension matched gold, and the
planted trap landed exactly right: the run explicitly cited the rubric's
active-participation rule to score engagement Missed despite Priya
attending the entire call. The one soft ding is stylistic rather than a
scoring error: the run's closing verdict hedges with "needs attention,
leaning on-track," which slightly waters down the unhedged "needs
attention" read gold intended — the brief specifically warns against
letting a solid setup timeline paper over the sentiment/engagement gaps,
and this hedge edges toward doing exactly that, even though the underlying
dimension scores didn't change.
