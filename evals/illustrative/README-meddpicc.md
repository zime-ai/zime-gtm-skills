# Illustrative self-authored run: `meddpicc`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**ranked eight-letter scorecard**, graded by per-letter agreement and a
hallucination check, same shape as `meddicc`/`challenger`.

## Result

Full grader output: `runs/meddpicc-demo-verdict.md`. Skill's raw output:
`runs/meddpicc-demo-output.md`.

| Metric | Result |
|---|---|
| Per-letter agreement with gold | 4/8 exact match |
| Trap 1 (Paper process — should be `Partial`, not `Covered`) | Avoided the lenient failure, but overshot to `Missed` — one notch too strict |
| Trap 2 (Champion — should be `Missed`, not `Covered`) | Avoided the lenient failure, but landed on `Partial` — one notch too lenient |
| Hallucinations | 0 |

## Reading this honestly

Neither planted trap failed the way it was designed to fail — the run
never called Paper process Covered just because "legal" was named, and
never called Champion Covered from Dana's enthusiasm alone. But it also
didn't land on gold's exact answer for either: Paper process went one
notch too strict (`Missed`, when legal-as-named-function meets gold's own
`Partial` bar), and Champion went one notch too lenient (`Partial`, when
the rubric's explicit rule — a champion has to be shown doing something,
not just saying positive things — calls for `Missed` on enthusiasm with
zero action). Two more disagreements appeared on letters the brief didn't
even trap (Economic buyer downgraded to `Partial`, Competition upgraded
to `Partial`), split in opposite directions from each other too. Reading
across `meddicc`'s original finding (leans toward false confidence over
reporting ambiguity) and this run, the more consistent signal isn't a
directional bias — it's that MEDDPICC's eight-letter boundary lines are
where the skill is least precise, even when it avoids the worst failure
mode on each one.

## Reproducing this

```bash
mkdir -p /tmp/mp-run/.claude/skills
cp -r skills/meddpicc /tmp/mp-run/.claude/skills/
cp evals/illustrative/transcripts/meddpicc-demo.txt /tmp/mp-run/transcript.txt
( cd /tmp/mp-run && claude -p "run meddpicc on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/mp-grade
cp /tmp/mp-run/<output> /tmp/mp-grade/output.md
cp evals/illustrative/transcripts/meddpicc-demo.txt /tmp/mp-grade/transcript.txt
cp evals/illustrative/gold/meddpicc-demo.md /tmp/mp-grade/gold.md
( cd /tmp/mp-grade && claude -p "<grading prompt, see runs/meddpicc-demo-verdict.md>" --dangerously-skip-permissions )
```
