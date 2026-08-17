# Illustrative self-authored run: `poc-pilot-pipeline-check`

Same mechanism and same caveat as the `meddicc`/`challenger`/`deal-risk-digest` runs
(`evals/illustrative/README.md`) — same author behind brief, CSV, gold,
and grading prompt; real isolation only between the skill-run process and
the grading process; **not Tier 3, not evidence of real-world accuracy.**

This is Shape B (CSV pipeline-sweep) — the second proof that the gold
template adapts to pipeline-wide checks. Because `poc-pilot-pipeline-check`'s rubric is a deterministic flag system (`references/rubric.md`), the gold file here is a computed fact, not a judgment call.

## Result

Full grader output: `runs/poc-pilot-pipeline-check-demo-verdict.md`. Skill's raw output:
`runs/poc-pilot-pipeline-check-demo-output.md`.

| Metric | Result |
|---|---|
| Row-level accuracy (flag status, all 9 deals) | 6/9 |
| Zenith Analytics (no-sponsor flag) | Missed — output omitted from list |
| Stellar Labs (open-ended flag) | Correct; BUT also added bogus "no conversion date" flag |
| Ranking / tiebreak (deals sorted by flag count, then value) | Broken — Stellar Labs bumped to rank 2 by extra flag; Zenith Analytics missing; NeoTech(85k) below Zenith Solutions(45k) |
| Closing line 1 ("N of M deals flagged") | **Wrong** — output says 5 of 9, gold says 6 of 9 |
| Closing line 2 ("most common flag") | **Wrong** — output says "tie" (no-exit-criteria and no-conversion-date, 2 each); gold says no-exit-criteria only (2 of 6) |
| Traps passed (5 constructed traps) | 5/5 — all trap logic correct; errors are outside trap scope |
| Hallucinations | 1 outright (Stellar's extra flag); no invented names/dates/statuses |

## Reading this honestly

The skill passed all five constructed trap tests (Quantum's 3 separate flags,
NeoTech's AND-logic, API Gateway's both-empty rule, Prism's live-status
requirement, Stellar's actual median), proving the core rubric logic works
correctly. But it failed on two separate issues both outside the trap set:

1. Zenith Analytics (no sponsor) was completely omitted from the flagged deals list,
   treated as clean despite the rubric's no-sponsor flag firing.
2. Stellar Labs got an extra "no conversion date" flag that doesn't exist in
   gold — the deal has a poc_end_date, so flag #2's "both columns empty"
   condition should be false.

Both errors happen to the same deal or its absence, not to the rubric's core
logic. The closing lines are wrong as a consequence: count is off by one
(5 vs 6), and the "most common flag" claim is a fabricated tie, real only
because of Stellar's extra flag. One sample; treat as one data point about
failure modes, not a verdict on real-world accuracy.

## Reproducing this

```bash
# 1. Run the skill in isolation
mkdir -p /tmp/poc-pilot-pipeline-check-run/.claude/skills
cp -r skills/poc-pilot-pipeline-check /tmp/poc-pilot-pipeline-check-run/.claude/skills/
cp evals/illustrative/artifacts/poc-pilot-pipeline-check-demo.csv /tmp/poc-pilot-pipeline-check-run/pipeline.csv
( cd /tmp/poc-pilot-pipeline-check-run && claude -p "/poc-pilot-pipeline-check ./pipeline.csv" --dangerously-skip-permissions )

# 2. Grade in a separate isolated dir — never expose SKILL.md, BRIEF.md to this process
mkdir -p /tmp/poc-pilot-pipeline-check-grade
cp <skill_output> /tmp/poc-pilot-pipeline-check-grade/output.md
cp evals/illustrative/artifacts/poc-pilot-pipeline-check-demo.csv /tmp/poc-pilot-pipeline-check-grade/pipeline.csv
cp evals/illustrative/gold/poc-pilot-pipeline-check-demo.md /tmp/poc-pilot-pipeline-check-grade/gold.md
( cd /tmp/poc-pilot-pipeline-check-grade && claude -p "<grading prompt, see runs/poc-pilot-pipeline-check-demo-verdict.md's own framing>" --dangerously-skip-permissions )
```
