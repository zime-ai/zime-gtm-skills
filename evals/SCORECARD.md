# Verification scorecard

The credibility artifact for this repo's evals — what's actually been
checked, against what, with a link to every source so none of this has to
be taken on faith. See `EVALS.md` for the tier definitions and
`evals/gt-web/README.md` / `evals/gt-web/SOURCES.md` for how web-sourced
ground truth works and what's been rejected and why.

## Tier 0/3 (accuracy vs. ground truth): no skill has a number yet

`evals/gt-web/`'s first harvest pass (2026-08-14) found **zero** qualifying
sources — see `evals/gt-web/SOURCES.md` for the full search record,
including a real, well-labeled dataset (Gong Research's "Call Playbook")
that was found and rejected because it's gated and proprietary-licensed,
not because it wasn't real. `evals/gt/`'s human-labeled path is also not
started — no human labeler is on staff. Neither path is faked to produce a
number; both are reported as not-yet-possible rather than skipped
silently.

| Skill | Tier 0/3 status |
|---|---|
| All 41 skills | No ground truth available (web harvest: 0 qualifying sources; human labeling: no labeler on staff) |

## Tier 1 (trigger evals): written, not run

`evals/trigger-set.json` has 16 cases, written when the repo had 16
skills — 25 skills added since have no trigger case. Framework
(`skill-creator`'s `run_eval.py`) exists; hasn't been executed against the
current set.

## Tier 2 (format compliance): schema-valid across all 41, unrun

Every skill has a schema-valid `evals/evals.json` (3 were fixed from a
nonstandard shape in this pass — see `MAINTAINING.md`'s "Verification
state"). 37 of 41 have at least one case with `files: []` — a described
scenario with no real sample file behind it, unrunnable even once a runner
is wired up. None have been run through the `with_skill`/`without_skill`
benchmark loop.

## Illustrative self-authored runs (not Tier 3)

**Not Tier 0/3 numbers, and not counted in the table above.** Same author
(this Claude session) behind each skill's brief, artifact, gold label, and
grading prompt — a demonstration of the isolated-run/isolated-grade
mechanism, not third-party or human-verified evidence. This section grows
by adding correlated anecdotes from one author/model, not independent
proof — see each run's own README for full caveats before reading its
number as more than that.

Transcript-audit skills (findings-recall shape):

| Skill | Recall | Hallucinations | Out-of-rubric finding | Dimension agreement | Notes |
|---|---|---|---|---|---|
| `meddicc` | 4/4 | 0 (1 soft overstatement) | No credit — folded into a rubric bucket | 4/7 | See `evals/illustrative/README.md` |
| `challenger` | 4/4 | 0 | Full credit — surfaced as its own finding | 2/3 comparable | Gold guessed a rubric dimension the skill doesn't score — flagged as a gold-construction mismatch, not a skill defect. See `evals/illustrative/README-challenger.md` |
| `meddpicc` | — | 0 | — | 4/8 exact match | Both planted traps (Paper process, Champion) avoided their designed lenient failure but missed gold's exact answer in opposite directions — one too strict, one too lenient. See `evals/illustrative/README-meddpicc.md` |
| `faint` | — | 0 | — | 5/5 exact match | Clean pass — both planted traps (Authority from title alone, Need's absence given strong Interest) passed. See `evals/illustrative/README-faint.md` |
| `sandler` | — | 0 | — | 7/7 exact match | Clean pass — both planted traps (Pain from a symptom mention, Fulfillment from a hedged "I guess, sure") passed, sequencing violation named correctly. See `evals/illustrative/README-sandler.md` |
| `bant` | — | 0 | — | 4/4 exact match | All criteria matched gold including the planted Authority trap; closing advance-call line didn't carry the Authority-Partial finding through to its own follow-up recommendation. See `evals/illustrative/README-bant.md` |
| `pain-finder` | 4/4 pains recalled, correct order | 0 | — | — | Both planted traps passed — a downplayed pain stayed Low confidence, a thin pain was reported rather than dropped. Category labels reworded from gold but evidence/confidence/order all matched. See `evals/illustrative/README-pain-finder.md` |
| `next-step-commitment` | — | 0 | — | — | Single-verdict shape, not a scorecard. Planted trap (momentum-sounding language must not read as `Real commitment`) passed; verdict landed on `No commitment`, all 3 missing elements correctly named. See `evals/illustrative/README-next-step-commitment.md` |
| `sell-the-dream` | — | 0 | — | 4/5 exact match | Sequencing violation (feature pitched before vision) caught with correct root cause; one element score (`Missed` vs. gold's `Covered`) double-counted the same order problem the sequencing section already flags. See `evals/illustrative/README-sell-the-dream.md` |

CSV pipeline-sweep skills (row/ranking-accuracy shape):

| Skill | Row/finding accuracy | Hallucinations | Notes |
|---|---|---|---|
| `deal-risk-digest` (Shape B) | 9/9 rows, 5/5 traps, ranking correct | 0 | Row-level accuracy and ranking perfect; the one aggregate summary line ("most common signal") was wrong and stated with no hedge. See `evals/illustrative/README-deal-risk-digest.md` |
| `evaluation-pipeline-check` | 8/8 rows, 3/3 traps | 0 | Perfect row-level flags and both closing lines correct. See `evals/illustrative/README-evaluation-pipeline-check.md` |
| `negotiation-pipeline-check` | 10/10 rows | 0 | Perfect match against gold, including median-discount math and both closing lines. See `evals/illustrative/README-negotiation-pipeline-check.md` |
| `prospect-pipeline-check` | 8/8 rows, 5/5 traps | 0 | Perfect row-level flags and both closing lines correct. See `evals/illustrative/README-prospect-pipeline-check.md` |
| `qualify-pipeline-check` | 10/10 rows, 5/5 traps | 0 | Perfect row-level flags and both closing lines correct. See `evals/illustrative/README-qualify-pipeline-check.md` |
| `poc-pilot-pipeline-check` | 6/9 rows, 5/5 core-logic traps | 0 | One deal's flag omitted entirely, one spurious flag invented on another row; both closing lines wrong as a result. See `evals/illustrative/README-poc-pilot-pipeline-check.md` |
| `won-pipeline-check` | 9/9 rows, 8/8 traps | 0 | Every flag and evidence cell correct; table sort order and one closing line's phrasing were off. See `evals/illustrative/README-won-pipeline-check.md` |
| `end-client-registration` | 8/10 rows, 3/5 traps | 1 (unrubriced near-expiry concern) | One false negative (vague scope), one false positive (over-strict on expiry), aggregate line collapsed distinct dimensions. See `evals/illustrative/README-end-client-registration.md` |
| `new-business-registration` | 6/8 rows fully correct, 1 sloppy-but-right, 1 wrong | 0 | Introduced an unrubriced temporal-validity check on expiry dates the rubric doesn't ask for; also mild scope overreach into approval/remediation framing. See `evals/illustrative/README-new-business-registration.md` |

Document-writer skills (row/field-diff shape) — all 7 Shape C
deal-intelligence writers now have a run (`deal-risk-digest`, the 8th
deal-intelligence skill, is CSV-only and counted under Shape B above):

| Skill | Row accuracy | Extra rows | Hallucinations | Notes |
|---|---|---|---|---|
| `champion-tracker` (Shape C) | 7/7 gold rows, 0 wrong-tag | 4 (3 legit, 1 overreach) | 0 | Same author wrote this skill's own rubric — weakest blinding of the runs so far. Passed a planted stated-intention-vs-action trap, then failed the identical trap shape later, un-planted. See `evals/illustrative/README-champion-tracker.md` |
| `mutual-action-plan` | 3/4 gold rows correctly tagged (1 mis-split) | 0 | Planted "budget sign-off moving" trap passed (correctly `inferred`); un-planted defect: split one `heard` milestone into two rows and stripped the named owner from one half, manufacturing an `inferred` tag on a fact the same sentence supports as `heard`. Also invented exact calendar dates beyond what the call stated. See `evals/illustrative/README-mutual-action-plan.md` |
| `deal-highlights` | 6/6 gold items recalled, citations correct | 0 | Avoided the planted small-talk trap (dog/vacation) but failed the subtler planted trap: wrote a pure Tuesday/Wednesday scheduling exchange up as "Commitment (both)." One legit bonus item (a real rep-side commitment) also added. See `evals/illustrative/README-deal-highlights.md` |
| `follow-up-email-drafter` | Clean pass — email + grounding notes match gold claim-for-claim | 0 | Planted trap (an inferred ask promoted to an agreed fact) passed; `Heard`/`Proposed` tags never leaked into the email body. See `evals/illustrative/README-follow-up-email-drafter.md` |
| `win-loss-brief` | 3/3 clear drivers correct, hedge correctly kept tentative | 0 | Planted trap passed (hedge not upgraded to a confident driver); one structural nit — a ruled-out non-driver was listed as a bullet inside the Drivers section instead of fully outside it. See `evals/illustrative/README-win-loss-brief.md` |
| `executive-briefing` | Snapshot/risks/ask all correct | 0 | Planted trap passed (deal value correctly reported as not-stated, not estimated); un-planted defect: a buyer-stated close date ("before end of quarter") was headlined as "no firm date" before the correct quote followed — under-reported a fact that was actually said. See `evals/illustrative/README-executive-briefing.md` |
| `competitor-battlecard` | Clean pass — all 5 sections correct | 0 | Both planted traps passed (hedged claim kept tentative; correctly bucketed as left-unanswered rather than credited to a nearby but unrelated rep counter). See `evals/illustrative/README-competitor-battlecard.md` |

## Tier 0 framework: landed and runnable

`evals/framework/` (promptfoo-backed, isolated RUN/GAP/LEARN stages,
Cohen's-kappa calibration) is live on `dev` as of this pass. It has
existing cases wired for `sales-to-cs-handover`/`poc-deck` on a separate,
unmerged branch — not part of this repo's shipped 41 skills yet. The
mechanism works; it has nothing to grade the 41 shipped skills against
until either a source clears `evals/gt-web/`'s bar or a human labels
`evals/gt/`.

## What this scorecard is not claiming

- Not claiming any of the 41 skills produce accurate output — that's
  exactly the unproven claim this whole effort exists to either support or
  refute, and it remains unproven.
- Not claiming the harvest is exhausted — new call-coaching content
  publishes with transcripts occasionally; re-running the search
  periodically could still find something. `evals/gt-web/SOURCES.md`'s
  "First harvest pass" section is a snapshot, not a permanent verdict.
- Not claiming structural validation (`validate-skills.sh`, format checks)
  is equivalent to behavioral correctness — see `EVALS.md`'s "two metrics,
  never blended" doctrine. This scorecard is entirely about the metric
  structural checks can't reach.
