# Illustrative self-authored run: `win-loss-brief`

Same mechanism, same caveat as the rest of this batch
(`evals/illustrative/README.md`). Shape C (document-writer) — gold is a
**reference brief** (3 clear drivers, 1 tentative, 1 explicit non-driver),
graded by driver recall/precision and clear-vs-tentative tagging.

## Result

Full grader output: `runs/win-loss-brief-demo-verdict.md`. Skill's raw
output: `runs/win-loss-brief-demo-output.md`.

| Metric | Result |
|---|---|
| 3 clear drivers (competitive, champion loss, procurement) | All present, correct quotes and tags |
| Planted trap (hedge → must stay `tentative`, not upgraded) | Passed |
| Non-driver (well-received demo) forced in as a 4th clear driver | Not forced in as a scored driver, but placed as a labeled bullet inside the Drivers section rather than fully outside it |
| Hallucinations | 0 |

## Reading this honestly

Content is clean: all three real drivers correctly cited and tagged
clear, the hedge ("I don't know, maybe... I'm honestly not sure") stayed
tentative instead of getting upgraded into a confident fourth driver, and
nothing invented. The one nit — the grader's word, not a scoring
failure — is structural: the skill included the ruled-out demo feedback
as a bullet inside the "Drivers" section itself ("Technical fit — not a
driver (ruled out)") rather than keeping the section to only the 3-5
actual drivers the skill's own format calls for. The intent is clear from
the label, so it's not counted as a wrong driver, but it blurs the line
gold drew between "here are the drivers" and "here's something that
explicitly wasn't one."

## Reproducing this

```bash
mkdir -p /tmp/wlb-run/.claude/skills
cp -r skills/win-loss-brief /tmp/wlb-run/.claude/skills/
cp evals/illustrative/transcripts/win-loss-brief-demo.txt /tmp/wlb-run/transcript.txt
( cd /tmp/wlb-run && claude -p "run win-loss-brief on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/wlb-grade
cp /tmp/wlb-run/<output> /tmp/wlb-grade/output.md
cp evals/illustrative/transcripts/win-loss-brief-demo.txt /tmp/wlb-grade/transcript.txt
cp evals/illustrative/gold/win-loss-brief-demo.md /tmp/wlb-grade/gold.md
( cd /tmp/wlb-grade && claude -p "<grading prompt, see runs/win-loss-brief-demo-verdict.md>" --dangerously-skip-permissions )
```
