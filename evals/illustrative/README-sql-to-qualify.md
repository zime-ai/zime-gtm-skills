# Illustrative self-authored run: `sql-to-qualify`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**five-dimension scorecard plus an advance/disqualify close**, graded by
per-dimension agreement plus two planted-trap checks.

## Result

Full grader output: `runs/sql-to-qualify-demo-verdict.md`. Skill's raw
output: `runs/sql-to-qualify-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold (incl. close) | 5/6 exact match |
| Trap 1 (form-fill story ≠ pain restated in the prospect's own words) | Passed |
| Trap 2 (competitive dimension scored on whether asked, not on a named competitor) | Passed |
| Hallucinations | 0 |

## Reading this honestly

Both planted traps passed cleanly — the run correctly refused to credit
Morgan's vague "someone forwarded it to me" as real pain, and correctly
scored competitive awareness Covered because the question was asked and
answered, even though the answer was "not yet." The close call matched
gold exactly. The one dimension mismatch — contact reachability, which
gold reads as Covered and the run downgraded to Partial over Morgan
lacking personal budget authority — is a stricter, defensible read, not
one of the planted traps, and not a rubric violation.
