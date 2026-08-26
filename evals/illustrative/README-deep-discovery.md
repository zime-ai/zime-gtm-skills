# Illustrative self-authored run: `deep-discovery`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**nine-dimension scorecard**, graded by per-dimension agreement plus two
planted-trap checks.

## Result

Full grader output: `runs/deep-discovery-demo-verdict.md`. Skill's raw
output: `runs/deep-discovery-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 7/9 exact match |
| Trap 1 (blunt "who else are you evaluating" — score content, not phrasing) | Passed |
| Trap 2 (procurement Missed on a $50k+ deal) | Passed |
| Hallucinations | 0 confirmed |

## Reading this honestly

Both planted traps passed cleanly — the run didn't ding the rep for asking
a blunt competitive question, and correctly flagged procurement as Missed
on a deal that plausibly crosses the CFO's approval threshold, exactly the
two things this brief was built to test. Where it fell short: gold marks
decision process and budget/timeline as **Partial** (CFO is aware but
hasn't confirmed alignment himself; budget is earmarked but no figure was
given), and the run flattened both to Covered, losing precisely the
nuance the rubric asks for. The run's own "reads-well-too" self-check
claimed "8/9 Covered" — its own count was wrong even by its own scoring,
let alone gold's actual 7/9. Net: trap-passing was solid, dimension-level
calibration leaned toward over-crediting ambiguous evidence.
