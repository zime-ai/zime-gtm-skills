# Skill eval framework (Tier 0)

Gap diff of a skill's output against hand-written ground truth, run through
[promptfoo](https://www.promptfoo.dev/) so it scales past one-off manual
testing: a real dataset of cases, self-consistency judge sampling, and
run-over-run score diffing. See `EVALS.md` for how this fits the repo's other
three eval tiers.

## Run it

```bash
evals/framework/eval.sh <skill>                       # all cases for that skill
evals/framework/eval.sh <skill> --case astra-poc-deck  # one case
evals/framework/eval.sh <skill> --judges 5             # more judge samples
evals/framework/eval.sh <skill> --baseline             # promote this run to the baseline
evals/framework/eval.sh <skill> --learn                # also run the LEARN stage after
```

Output lands in `evals/runs/<timestamp>/`: `results.json`/`.csv` (promptfoo's
native output, structured, diffable), `gaps-<skill>-<case>.md` (human-readable
per-field verdicts), `verdicts/` (every judge sample's raw JSON, for audit and
for `calibrate.py`), and `feedback.md` (seeded template — add your notes before
running `--learn`).

## The three stages, and why they're isolated

| Stage | Script | Sees | Does NOT see |
|---|---|---|---|
| RUN | `run_skill.sh` (promptfoo provider) | the one skill, its transcript | ground truth, other skills, repo root |
| GAP | `judge.py` (promptfoo assertion) | output + ground truth + transcript | `SKILL.md` — judges the artifact, not the author's intent |
| LEARN | `learn.sh` | `gaps-*.md` + your `feedback.md` + `SKILL.md`/references | the transcript, the generated output |

Each stage runs in its own scratch dir under `/tmp/skill-eval-*`, copied fresh
every run. This is the whole point: the same context that writes a skill's
rubric shouldn't grade whether the rubric worked.

## The judge, honestly

`judge.py` runs N (`--judges`, default 3) independent `claude -p` sessions per
case, majority-votes each ground-truth field, and reports the vote spread
(`LOW_AGREEMENT` fields are flagged, not averaged away). It also shuffles the
ground truth's field order per sample — the applicable analogue of a judge
position-swap, since this is pointwise reference grading, not pairwise A/B.

**What this does and doesn't fix, per the research:** multi-sampling one
model family reduces *variance* (random scatter). It does nothing for
*systematic bias* — if every sample shares the same priors, sampling it more
just measures the bias more precisely. There are no third-party API keys in
this environment, so a real cross-family judge panel isn't available; this is
a known, accepted limitation, not an oversight. The mitigation that *is*
available: `calibrate.py` computes Cohen's kappa between the judge's majority
verdict and a hand-labeled set, so you can see — and re-tune the rubric
against — wherever the judge systematically disagrees with a human.

```bash
python3 evals/framework/calibrate.py <skill> <case> evals/runs/<timestamp>
```

Requires `evals/labels/<skill>-<case>.json`: `{"field name": "present|missing|wrong|extra", ...}`,
~10+ fields hand-labeled by you (ideally not the person who wrote the skill).
Run it whenever you add a case, and whenever `judge.py`'s `JUDGE_PROMPT_TEMPLATE`
or `RUBRIC_VERSION` changes — a judge/rubric swap is a calibration event, not a
free pass.

## Run log and amendments ledger

Every `eval.sh` run appends one row per case to `evals/runs.jsonl`
(gitignored, private -- see "Data privacy" below): skill, case, rubric
version, judges, and the four `namedScores`. `evals/framework/status.sh`
reads it and prints, per skill, the last run's `field_recall` and the delta
vs. the previous run for that skill. Not a 7d/30d trend table -- there isn't
enough run history yet for one to mean anything.

`--learn` also seeds `evals/amendments.jsonl` (gitignored) with one `pending`
row per proposal in `learnings.md`. Decide on one with:

```bash
evals/framework/amend.sh A-001 applied "tightened quote-per-finding rule"
evals/framework/amend.sh A-002 rejected "not a rubric issue, judge miscounted"
```

Both are appends, latest row per id wins, no rewrite path. The next
`--learn` run reads the ledger and won't re-propose anything already
`applied` or `rejected` for that skill. When a proposal ships, the fix
commit for the skill references the amendment id
(`fix(pain-finder): require a quote per finding -- amendment A-014`) --
the commit log is the public, sanitized record; no client evidence crosses
into it.

## Adding a case

1. Drop a transcript at `evals/transcripts/<name>.txt`.
2. Hand-author ground truth at `evals/gt/<name>--<skill>.<ext>` (real human
   work — see `evals/gt/README.md`, never a previous model run).
3. Add one entry to `evals/cases/<skill>.yaml` — copy the pattern in
   `evals/cases.example.yaml` (repo root, public).
4. New cases should cover more than happy-path transcripts — the literature
   this framework is built on specifically calls out missing-context,
   ambiguous, and adversarial-phrasing cases as where regressions actually
   hide. Tag the case's `metadata.tier` accordingly.

## What's deliberately not built

- No `without_skill` baseline arm — the value of comparing against no-skill
  output is granted, but it's a maintainer-run procedure
  (see `MAINTAINING.md`), not part of this loop.
- No cross-family judge panel — see "The judge, honestly" above.
- No CI job — `EVALS.md` already decided evals stay out of CI.

## Data privacy

`evals/transcripts/`, `evals/gt/`, `evals/cases/`, `evals/labels/`,
`evals/baseline-*.json`, `evals/runs/*` (except the one pre-existing public
demo run), `evals/runs.jsonl`, and `evals/amendments.jsonl` are all
gitignored — real client names, deal details, and rubric-fix proposals
derived from them live in several of these. Only `evals/framework/*`,
`evals/promptfooconfig.yaml`, and `evals/cases.example.yaml` are public.
`./validate-skills.sh` checks the `.gitignore` entries are still in place.
