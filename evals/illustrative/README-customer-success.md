# Illustrative self-authored run: `customer-success`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is an
**eight-dimension scorecard**, graded by per-dimension agreement plus a
planted-trap check.

## Result

Full grader output: `runs/customer-success-demo-verdict.md`. Skill's raw
output: `runs/customer-success-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 8/8 exact match |
| Trap (a single missed dimension isn't blended away by seven strong ones) | Passed |
| Hallucinations | 0 |

## Reading this honestly

Full clean pass. Every dimension matched gold, including the deliberately
missed stakeholder-breadth dimension, and the closing summary named that
gap explicitly as a standing risk rather than folding it into an overall
positive read — exactly what the planted trap was testing for. The run's
one added touch (suggesting an "ops lead" as a candidate second
stakeholder) is speculative framing consistent with gold's own similar
suggestion, not an asserted fact from the transcript.
