# Illustrative self-authored run: `bant`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**ranked four-criterion scorecard**, graded by per-criterion agreement and
a hallucination check.

## Result

Full grader output: `runs/bant-demo-verdict.md`. Skill's raw output:
`runs/bant-demo-output.md`.

| Metric | Result |
|---|---|
| Per-criterion agreement with gold | 4/4 exact match |
| Planted trap (Authority — title/confidence alone must not read `Covered`) | Passed |
| Advance-call rationale consistency with its own Authority score | Partial mismatch |
| Hallucinations | 0 |

## Reading this honestly

All four criterion scores matched gold, including the planted trap — the
Director's confident tone and evaluation ownership correctly stayed at
Partial rather than Covered once the named $25K approval threshold and
managing-partner sign-off surfaced. The one real finding is a consistency
gap between the per-criterion score and the closing recommendation: the
skill scored Authority Partial but then framed it as "a credible path to
sign-off" in the advance-call line and only flagged Timeline for
follow-up, effectively treating the Authority gap it had just identified
as settled. Not a hallucination and not a wrong score, but the kind of
drift where a correct per-criterion read doesn't fully carry through to
the one line a rep would actually act on.

## Reproducing this

```bash
mkdir -p /tmp/bant-run/.claude/skills
cp -r skills/bant /tmp/bant-run/.claude/skills/
cp evals/illustrative/transcripts/bant-demo.txt /tmp/bant-run/transcript.txt
( cd /tmp/bant-run && claude -p "run bant on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/bant-grade
cp /tmp/bant-run/<output> /tmp/bant-grade/output.md
cp evals/illustrative/transcripts/bant-demo.txt /tmp/bant-grade/transcript.txt
cp evals/illustrative/gold/bant-demo.md /tmp/bant-grade/gold.md
( cd /tmp/bant-grade && claude -p "<grading prompt, see runs/bant-demo-verdict.md>" --dangerously-skip-permissions )
```
