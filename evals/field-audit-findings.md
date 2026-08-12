# Field-level audit — astra & truefoundry, post specificity-fix

Method: ran the current skill (post today's rule-consolidation edit) fresh
against `evals/transcripts/{astra,truefoundry}.txt`, diffed the output
directly against `evals/gt/sales-to-cs-handover/{astra,truefoundry}.md` by
hand. Deliberately skipped the promptfoo/judge-panel/Cohen's-kappa machinery
for this pass — a direct read of two ~220-line docs against their GT is
cheaper and gives more specific findings than 3 redundant LLM judge votes
would; reserve that heavier machinery for later-stage calibration once
there's enough labeled data to be worth automating. Full field-by-field
labels: `evals/labels/sales-to-cs-handover-{astra,truefoundry}.json`.

## Finding 1 — the specificity fix triggers inconsistently, not reliably

Today's `grounding-rules.md` edit ("Specificity survives compression")
generalized Fyno's two misses into one predicate. Re-tested fresh, not on
Fyno:

| Client | Number GT kept | Output kept it? |
|---|---|---|
| Astra | "~7 reps" (pilot cohort, §1 and team size, §2) | **No** — both fields dropped the number |
| Astra | "$99/user/month" (§1 commercial terms) | **No** — output wrote "no pricing discussed," contradicting GT |
| TrueFoundry | "7 generalists" (§2 team size) | Yes |
| TrueFoundry | "$99/user/month" (§1 commercial terms) | Yes |

The rule works roughly half the time on fields it wasn't written for. A
descriptive rule ("keep the number") is advice a model can still forget
under budget pressure; the skill's own Step 2 already solves an analogous
problem for placeholders with a mechanical re-scan ("re-scan the filled
template a second time... confirm every placeholder was actually
replaced"). Applying the same mechanical-check pattern to specificity, not
just description, is the fix — see below.

## Finding 2 — "Pilot cohort" is an ambiguous field (new, not from Fyno)

Both GT docs independently read "Pilot cohort" as **team headcount**:
Astra GT → "7 reps"; TrueFoundry GT → "7 generalists (Founders office)".
Both fresh runs independently read it as **account/deal count** instead:
Astra output → "minimum 10 deals... cohort selection pending"; TrueFoundry
output → "Top 10 high-revenue accounts... 21-day POC".

2-for-2 wrong in the same direction is not noise — the field label itself
doesn't disambiguate "who's piloting" from "what's being piloted," and
under-specification, not evidence-dropping, is the cause. This is a
different bug class than Finding 1 and was invisible from either single-GT
doc alone — the ambiguity only became visible by holding two clients up
against each other.

## Finding 3 — Economic-buyer stakeholder row silently missing (Astra)

Astra GT has an explicit row for the economic buyer ("Co-founder... yet to
engage"). Fresh Astra output has no such row at all — the fact that an
economic buyer is unidentified only surfaces in prose (Open Questions), not
as its own stakeholder-table row. `miss-prone-fields.md`'s existing role-
completeness rule already requires this ("Champion, Decision maker, and
Economic buyer each either name a person or read as explicitly
unidentified") — this is a re-confirmation that the rule doesn't reliably
fire, same shape as Finding 1: a described rule, not a mechanically
checked one.

## Finding 4 — company website: likely a sanctioned gap, not a bug

Both fresh runs return `TBC` for company website; both GT docs have the
real URL. `grounding-rules.md` already documents a near-identical case for
"What they do" (Astra's public-info note, explicitly flagged as "a manual
step the AE took outside this skill's scope"). Plausible the website
field in both GT docs got the same manual treatment. Not fixing this
without confirming — it's a scope question (should the skill be allowed a
narrow company-identity lookup exception?) for the elicitation session, not
a recall bug.

## Labeling note

`calibrate.py`'s schema (`present|missing|wrong|extra`) has no verdict for
"correctly and deliberately blank" — TrueFoundry §9 is blank in both GT and
output, by design (per `handover-template.md`'s own reconciliation note),
and got labeled `present` for lack of a better option. Flag if this schema
gap matters once more calibration is done — for now it's one field out of
15, not worth a schema change yet.

## Fixes applied from this pass

1. `SKILL.md` Step 2 — added a mechanical specificity re-scan, same pattern
   as the existing placeholder re-scan, so Finding 1 has a checklist step
   behind it instead of description alone.
2. `handover-template.md` / `grounding-rules.md` — disambiguated "Pilot
   cohort" as team headcount, not account/deal count (Finding 2).

Finding 3 (economic-buyer row) is already covered by an existing rule that
isn't firing reliably — same root cause as Finding 1, so the Step 2
mechanical re-scan should help it too; not adding a second, separate fix for
what's likely the same underlying gap.

## Honest limit

N=2 fresh runs. Finding 2 (pilot cohort) is well-evidenced — 2 independent
GT authors agree, 2 independent fresh runs agree, in opposite directions.
Findings 1 and 3 are single-run observations and could be sampling noise
from one generation; re-run after the fixes above to confirm they moved,
not just re-read once more.
