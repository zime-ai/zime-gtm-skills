# Illustrative self-authored run: `improve-demo`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**seven-dimension scorecard**, graded by per-dimension agreement plus a
planted-trap check.

## Result

Full grader output: `runs/improve-demo-demo-verdict.md`. Skill's raw
output: `runs/improve-demo-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 6/7 exact match |
| Trap (a quiet transcript with one sharp question ≠ auto-Missed engagement) | Passed |
| Hallucinations | 0 confirmed, but flagged as suspicious — see below |

## Reading this honestly

The planted trap passed cleanly — the run correctly scored engagement
Covered on the strength of one specific, non-generic question rather than
marking it Missed because most of the transcript was minimal
acknowledgments. But dimension 6 (success criteria reconfirmed) is a real
miss: gold calls this Missed because the demo never circles back to a
measurable success metric, only the general priority. The run scored it
Covered instead, reasoning that answering the shift-overlap question
counts as reconfirming success — that conflates "addressed the stated
pain point" with "reconfirmed a specific success criterion," which the
rubric treats as distinct.

The grader also flagged this as more than an isolated scoring slip: the
two quotes the run cites to justify dimension 6 aren't in gold's evidence
set, and the grader couldn't check them against a transcript (none was in
its grading directory) — checked directly against the source transcript
here, both quotes are genuine and verbatim. So the underlying evidence
wasn't fabricated, but the run did stretch legitimate transcript detail to
support the wrong dimension's verdict, which is worth knowing even though
it clears the stricter "hallucination" bar.
