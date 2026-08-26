# Illustrative self-authored run: `next-step-commitment`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**single verdict against the three-part test**, graded on whether the
verdict and the specific missing elements match. Different scenario than
the skill's own bundled `assets/sample-transcript.txt`.

## Result

Full grader output: `runs/next-step-commitment-demo-verdict.md`. Skill's
raw output: `runs/next-step-commitment-demo-output.md`.

| Metric | Result |
|---|---|
| Planted trap (must not score `Real commitment`) | Passed — scored `No commitment` |
| Missing element 1 (specific action) | Correctly identified |
| Missing element 2 (exact date/trigger) | Correctly identified |
| Missing element 3 (two-sided ownership) | Correctly identified |
| Hallucinations | 0 |

## Reading this honestly

Clean pass. This brief's trap stacked a forward-sounding phrase ("let's
keep this moving") with a date-shaped word ("next week") specifically to
see whether the skill would pattern-match on momentum-sounding language
instead of checking the three required elements individually. It didn't
— all three were correctly identified as absent, the verdict landed on
`No commitment` (gold accepted either `Weak` or `No commitment`, only
`Real` was the failure mode), and the one-sided nature of the exchange
(only the rep proposed the follow-up) was caught explicitly. One
transcript, one grader, but on the specific failure mode this narrow
three-element skill exists to catch, this run applied the test rather
than the surface pattern.

## Reproducing this

```bash
mkdir -p /tmp/nsc-run/.claude/skills
cp -r skills/next-step-commitment /tmp/nsc-run/.claude/skills/
cp evals/illustrative/transcripts/next-step-commitment-demo.txt /tmp/nsc-run/transcript.txt
( cd /tmp/nsc-run && claude -p "run next-step-commitment on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/nsc-grade
cp /tmp/nsc-run/<output> /tmp/nsc-grade/output.md
cp evals/illustrative/transcripts/next-step-commitment-demo.txt /tmp/nsc-grade/transcript.txt
cp evals/illustrative/gold/next-step-commitment-demo.md /tmp/nsc-grade/gold.md
( cd /tmp/nsc-grade && claude -p "<grading prompt, see runs/next-step-commitment-demo-verdict.md>" --dangerously-skip-permissions )
```
