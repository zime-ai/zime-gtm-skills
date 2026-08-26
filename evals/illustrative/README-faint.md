# Illustrative self-authored run: `faint`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**ranked five-criterion scorecard**, graded by per-criterion agreement and
a hallucination check.

## Result

Full grader output: `runs/faint-demo-verdict.md`. Skill's raw output:
`runs/faint-demo-output.md`.

| Metric | Result |
|---|---|
| Per-criterion agreement with gold | 5/5 exact match |
| Trap 1 (Authority — title alone must not read as Covered) | Passed |
| Trap 2 (un-surfaced Need must not disqualify the advance call given strong Interest) | Passed |
| Hallucinations | 0 |

## Reading this honestly

Clean pass, both planted traps caught. The Authority read correctly
distinguished the "Ops Lead" title's day-to-day influence from a real
path to final sign-off, scoring Partial on exactly the evidence gold
expected. The Need read applied FAINT's own premise correctly — un-stated
need on a call where Interest is genuinely strong reads as "not yet
surfaced," not a disqualifying miss, and the advance call stayed
"Advance" with a concrete follow-up question rather than downgrading to
"do not advance" over the missing Need. One data point, one grader, but
on the specific inversion FAINT is built around (Interest ahead of Need),
this run applied the rule correctly rather than defaulting to the more
familiar BANT logic of treating an unstated need as disqualifying.

## Reproducing this

```bash
mkdir -p /tmp/faint-run/.claude/skills
cp -r skills/faint /tmp/faint-run/.claude/skills/
cp evals/illustrative/transcripts/faint-demo.txt /tmp/faint-run/transcript.txt
( cd /tmp/faint-run && claude -p "run faint on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/faint-grade
cp /tmp/faint-run/<output> /tmp/faint-grade/output.md
cp evals/illustrative/transcripts/faint-demo.txt /tmp/faint-grade/transcript.txt
cp evals/illustrative/gold/faint-demo.md /tmp/faint-grade/gold.md
( cd /tmp/faint-grade && claude -p "<grading prompt, see runs/faint-demo-verdict.md>" --dangerously-skip-permissions )
```
