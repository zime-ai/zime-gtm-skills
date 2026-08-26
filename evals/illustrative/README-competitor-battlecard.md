# Illustrative self-authored run: `competitor-battlecard`

Same mechanism, same caveat as the rest of this batch
(`evals/illustrative/README.md`). Shape C (document-writer) — gold is a
**reference battlecard**, graded by section-level diff (named competitor,
framing, claims with confidence tags, rep counters, and what went
unanswered).

## Result

Full grader output: `runs/competitor-battlecard-demo-verdict.md`. Skill's
raw output: `runs/competitor-battlecard-demo-output.md`.

| Metric | Result |
|---|---|
| Planted trap 1 (hedged API-access claim kept tentative, not smoothed) | Passed |
| Planted trap 2 (API-access claim placed in "left unanswered," not marked addressed) | Passed |
| Setup-timeline claim + rep counter | Correct, matches gold |
| Extra "cheaper/same-features" claim (gold folded into framing, skill promoted to its own claim) | Defensible restructuring, not an error |
| Hallucinations / outside knowledge of real RouteIQ | 0 |

## Reading this honestly

Clean pass on both planted traps. This brief stacked two failure modes on
the same line (the hedged API-access claim) — smoothing the hedge into
confident language, or letting the rep's nearby counter to a *different*
claim get credited against it — and the skill avoided both: the hedge
stayed hedged, and "left unanswered" only ever contains what was actually
never addressed. The one structural difference from gold (promoting the
"cheaper, same features" line from section 2's framing into its own
tagged claim in section 3) is more thorough than gold's own structure,
not wrong — the claim is real, correctly hedged, and genuinely never
countered either. Zero hallucinated facts about the named competitor, in
keeping with the skill's hard zero-outside-knowledge rule.

## Reproducing this

```bash
mkdir -p /tmp/cb-run/.claude/skills
cp -r skills/competitor-battlecard /tmp/cb-run/.claude/skills/
cp evals/illustrative/transcripts/competitor-battlecard-demo.txt /tmp/cb-run/transcript.txt
( cd /tmp/cb-run && claude -p "run competitor-battlecard on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/cb-grade
cp /tmp/cb-run/<output> /tmp/cb-grade/output.md
cp evals/illustrative/transcripts/competitor-battlecard-demo.txt /tmp/cb-grade/transcript.txt
cp evals/illustrative/gold/competitor-battlecard-demo.md /tmp/cb-grade/gold.md
( cd /tmp/cb-grade && claude -p "<grading prompt, see runs/competitor-battlecard-demo-verdict.md>" --dangerously-skip-permissions )
```
