# Illustrative self-authored run: `mutual-action-plan`

Same mechanism, same caveat as the other Shape C runs
(`evals/illustrative/README.md`, `README-champion-tracker.md`). Brief,
transcript, gold, and grading prompt all authored by the same session
that helped build this repo — not Tier 3, not third-party evidence.

This is Shape C (document-writer): gold is a **reference milestone plan**,
graded by row/tag diff against the skill's own three-part test (a named
action, a date or checkable trigger, two-sided ownership) — not by
findings recall.

## Result

Full grader output: `runs/mutual-action-plan-demo-verdict.md`. Skill's raw
output: `runs/mutual-action-plan-demo-output.md`.

| Metric | Result |
|---|---|
| Gold rows present | 4/4 (one gold row split into two by the skill) |
| Correctly tagged | 3/4 clean; 1/4 mis-split |
| Planted trap ("budget sign-off moving" → must be `inferred`) | Passed |
| Hallucinated milestones/names | 0 |
| Invented specificity | 3 exact calendar dates computed from a stated call date, where the transcript only ever said "Friday" / "Wednesday" / "end of next week" |

## Reading this honestly

The planted trap passed cleanly — the vague "I'll get budget sign-off
moving" line was correctly tagged `inferred`, not inflated into a
commitment. The real finding is on a milestone the brief didn't plant a
trap on: the transcript's MSA-and-procurement line ("I'll get the
redlined MSA over to you by Wednesday so Sam has something concrete to
start with") names both the date and the prospect-side owner (Sam) in one
sentence. The skill split this into two rows and, in doing so, stripped
Sam as owner from the MSA-send row — manufacturing an `inferred` tag on a
milestone the same sentence supports as `heard`. Net effect: a real
commitment reads slightly less locked-down than the call actually
supports. Separately, the skill computed exact calendar dates ("Wed
2026-09-02") the transcript never stated, which isn't wrong exactly but
is more precision than the source supports — worth watching since the
skill's own rule is "don't invent," and a fabricated date is closer to
that line than a vague trigger is.

## Reproducing this

```bash
mkdir -p /tmp/map-run/.claude/skills
cp -r skills/mutual-action-plan /tmp/map-run/.claude/skills/
cp evals/illustrative/transcripts/mutual-action-plan-demo.txt /tmp/map-run/transcript.txt
( cd /tmp/map-run && claude -p "run mutual-action-plan on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/map-grade
cp /tmp/map-run/<output> /tmp/map-grade/output.md
cp evals/illustrative/transcripts/mutual-action-plan-demo.txt /tmp/map-grade/transcript.txt
cp evals/illustrative/gold/mutual-action-plan-demo.md /tmp/map-grade/gold.md
( cd /tmp/map-grade && claude -p "<grading prompt, see runs/mutual-action-plan-demo-verdict.md>" --dangerously-skip-permissions )
```
