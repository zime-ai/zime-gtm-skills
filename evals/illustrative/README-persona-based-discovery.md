# Illustrative self-authored run: `persona-based-discovery`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**five-dimension scorecard for a single persona**, graded by per-dimension
agreement plus two planted-trap checks.

## Result

Full grader output: `runs/persona-based-discovery-demo-verdict.md`. Skill's
raw output: `runs/persona-based-discovery-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 5/5 exact match |
| Trap 1 (don't infer persona from title alone — "Director" ≠ economic buyer) | Passed |
| Trap 2 (single persona present — no penalty for absent personas) | Passed |
| Hallucinations | 0 |

## Reading this honestly

Clean pass. The run correctly read past the misleading "Director of IT"
title to the technical-evaluator role Riley actually described, and scored
all five dimensions against that read rather than assuming budget
authority from the title. It also correctly scored only the one persona
present, with no fabricated or penalized second-persona section. The
grader flagged one rigor nit — the run's evidence for dimensions 3 and 4
is mapped slightly differently than gold's (which quote backs which
dimension), and dimension 4's supporting quote is paraphrased rather than
lifted verbatim — but both are defensible alternate readings of the same
transcript, not a correctness failure.
