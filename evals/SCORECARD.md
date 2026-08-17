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
(this Claude session) behind each skill's brief, transcript, gold label,
and grading prompt — a demonstration of the isolated-run/isolated-grade
mechanism, not third-party or human-verified evidence. This section grows
by adding correlated anecdotes from one author/model, not independent
proof — see each run's own README for full caveats before reading its
number as more than that.

| Skill | Recall | Hallucinations | Out-of-rubric finding | Dimension agreement | Notes |
|---|---|---|---|---|---|
| `meddicc` | 4/4 | 0 (1 soft overstatement) | No credit — folded into a rubric bucket | 4/7 | See `evals/illustrative/README.md` |
| `challenger` | 4/4 | 0 | Full credit — surfaced as its own finding | 2/3 comparable | Gold guessed a rubric dimension the skill doesn't score — flagged as a gold-construction mismatch, not a skill defect. See `evals/illustrative/README-challenger.md` |

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
