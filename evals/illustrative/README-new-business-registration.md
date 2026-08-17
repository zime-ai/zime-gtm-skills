# Illustrative self-authored run: `new-business-registration`

Same mechanism and same caveat as the `deal-risk-digest`/`meddicc` runs
(`evals/illustrative/README.md`) — same author behind brief, CSV, gold,
and grading prompt; real isolation only between the skill-run process and
the grading process; **not Tier 3, not evidence of real-world accuracy.**

This is Shape B (CSV structural sweep) — the skill audits each registration
row for completeness against six rubric dimensions (entity/domain,
dedup check, source, ICP fit, support request, expiry window). Because the
rubric is deterministic (presence/absence only, no point-scoring ambiguity),
the gold file here is computed fact, not judgment — but the skill did
introduce one judgment call the rubric doesn't explicitly ask for.

## Result

Full grader output: `runs/new-business-registration-demo-verdict.md`. Skill's
raw output: `runs/new-business-registration-demo-output.md`.

| Metric | Result |
|---|---|
| Row-level accuracy (all 8 registrations, dimensions missing) | 6/8 fully correct, 1/8 sloppy-but-right (Rapid Fulfillment — right conclusion, wrong mechanics), 1/8 wrong (Legacy Systems) |
| Traps passed (5 constructed traps) | 3/5 clean (Coastal domain, Metropolitan entity, Frontier dedup), 1/5 flawed (Rapid all-6 logic), 1/5 failed (Legacy expiry) |
| Hallucinations | 0 invented data; 1 dimension-count error (splits "entity + domain" into 7 items while claiming 6); 2 scope overreaches ("clean, approve" framing and remediation actions beyond audit scope) |
| Clean rows (Acme, TechFlow, Valley) | Correct |
| Maximum-miss row (Rapid Fulfillment) | Correct result (all 6 missing), muddled execution (enumerates 7 items) |
| Domain-missing trap (Coastal) | Correct |
| Entity-missing trap (Metropolitan) | Correct |
| Blank-dedup trap (Frontier) | Correct |
| **Past-expiry trap (Legacy Systems)** | **Failed** — flagged expiry as "stale/invalid" when rubric says past date still counts as set |

## Reading this honestly

Six rows perfect, one half-right, one wrong. The two failures center on expiry-date handling: the skill introduced a temporal validity check ("is the expiry in the future?") that the rubric doesn't require or mention. The rubric asks "is there a defined validity window or expiry date" — presence, not temporal validity. This is a clear scope overreach with one concrete victim (Legacy Systems row), and a logic mismatch in the Rapid row (splitting one composite dimension into two separate line items). The skill also edged toward approval/remediation language ("Clean, approve," "Send back," "run dedup check before approving") that's beyond a completeness audit's scope. Two data-point lessons: the skill conflates completeness with temporal validity for expiry dates, and it tends toward judgment/action language beyond what a pure structural audit covers.

## Reproducing this

Same pattern as other illustrative runs:
```bash
# 1. Run the skill in isolation
mkdir -p /tmp/new-business-registration-run/.claude/skills
cp -r skills/new-business-registration /tmp/new-business-registration-run/.claude/skills/
cp evals/illustrative/artifacts/new-business-registration-demo.csv /tmp/new-business-registration-run/registrations.csv
( cd /tmp/new-business-registration-run && claude -p "/new-business-registration ./registrations.csv" --dangerously-skip-permissions )

# 2. Grade in a separate isolated dir — never expose SKILL.md to this process
mkdir -p /tmp/new-business-registration-grade
cp /tmp/new-business-registration-run/<output> /tmp/new-business-registration-grade/output.md
cp evals/illustrative/artifacts/new-business-registration-demo.csv /tmp/new-business-registration-grade/registrations.csv
cp evals/illustrative/gold/new-business-registration-demo.md /tmp/new-business-registration-grade/gold.md
( cd /tmp/new-business-registration-grade && claude -p "You are grading an eval. Compare OUTPUT.md against GOLD.md for the input CSV. Report row-by-row accuracy on dimension-missing findings, whether the five constructed traps were passed, and any hallucinations (claims not grounded in the CSV or beyond the rubric's scope). Be precise and skeptical." --dangerously-skip-permissions )
```
