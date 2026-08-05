# Evals

How this repo tests whether its skills actually work, and, just as
important, what these evals can and cannot prove.

## The problem with evaluating this kind of skill

Every skill here follows the same loop: read a call, apply a rubric, report
findings. The natural way to test that is to write a transcript, write
expectations, run the skill, and grade the output. But if the same person
(or the same model) writes the rubric, the transcript, and the expectations,
a 100% pass rate proves nothing: the transcript was written to contain
exactly what the rubric hunts for.

A prior benchmark run against an early `pain-finder` draft (kept at
`evals/runs/2026-07-28-cyber-pain-finder-prior/`, see its own README) showed
`1.0` vs `0.51` pass rate with/without the skill. Read closely, 4 of its 5
expectations checked *format* (was a category tag present, was a confidence
line present, was a quote present) and only one checked substance. The
benchmark's own analyzer said as much: the underlying model already finds
pain points well unaided; the skill's main contribution was structural
consistency. That's a real result, but "the skill enforces a consistent
format" and "the skill finds better insight" are different claims, and
blending them into one number overstates the second.

This repo reports them separately, on purpose.

## Two metrics, never blended into one number

- **Format compliance**: did the output follow the rubric's structure and
  stay in scope (right sections, evidence cited, no unrequested extra
  content). Automated, no human required. High-with-skill /
  low-without-skill is expected and is a real, if modest, claim.
- **Insight recall / precision**: of the pain points, gaps, or risks a
  human expert would flag on this call, how many did the skill find
  (recall), and of what it reported, how much was actually real (precision;
  the inverse of precision is roughly the hallucination rate). This is the
  number that survives a skeptical read, and it requires a human-authored
  gold label, see below.

## Three tiers, plus a Tier 0 for document-writing skills

Skills like `poc-deck` and `sales-to-cs-handover` don't audit a call, they
write a document forward from one. Tiers 1-3 above still apply, but the
fastest and cheapest signal for these is a direct diff against a real filled
example — see **Tier 0** below, and run it first.

### Tier 0 — Gap diff vs ground truth (isolated, mostly automated)

`evals/framework/eval.sh <skill>` runs the loop via promptfoo — a real dataset
of cases (`evals/cases/*.yaml`), not a one-off transcript, with structured,
diffable scores (`results.json`/`.csv`) instead of prose you re-read by eye.
Full detail in `evals/framework/README.md`; the shape:

1. **RUN** (`run_skill.sh`, a promptfoo provider) — isolated scratch dir, only
   the skill + its transcript. Produces the output artifact.
2. **GAP** (`judge.py`, a promptfoo assertion) — separate isolated scratch
   dir per judge sample, only the output + ground truth (`evals/gt/`) +
   transcript, never `SKILL.md`. **N independent judge samples** (default 3)
   majority-vote each ground-truth field as present/missing/wrong/extra, with
   ground-truth field order shuffled per sample (the applicable analogue of a
   judge position-swap here). Every "missing" is further tagged derivable
   (in the transcript, so a real skill bug) or not (an input limit). Splits
   across judges are flagged `LOW_AGREEMENT`, not averaged away. A free
   mechanical check — unresolved TBC/TBD/TBA markers — is reported as its own
   score, separate from the model-judged diff, so a format regression can't
   hide inside an insight number.
3. **LEARN** (`learn.sh`, `--learn` flag) — separate isolated scratch dir,
   only the run's `gaps-*.md` + your `feedback.md` + the skill's own
   `SKILL.md`/references. Writes ranked, gap-cited fixes to `learnings.md`.
   Never edits the skill itself — you apply what's useful.

**Honest limit on the judge panel:** multi-sampling one model family fixes
*variance*, not *systematic bias* — every sample shares the same priors, so
sampling more just measures the bias more precisely. A real cross-family panel
needs third-party API keys this environment doesn't have. The mitigation that
*is* built: `evals/framework/calibrate.py` computes Cohen's kappa between the
judge's majority verdict and a hand-labeled set, so a rubric drift is visible
and fixable rather than silently trusted. Run it whenever a case is added or
the judge rubric changes.

Every artifact lands in `evals/runs/<timestamp>/` as a plain file (session
logs, `verdicts/`, `results.json` included), not chat-only. Requires ground
truth in `evals/gt/` first — see `evals/gt/README.md`.

### Tier 1: trigger evals (automated)

Does the *right* skill fire for a given prompt? With 16 skills now in the
repo, several with overlapping descriptions (`deep-discovery` vs
`technical-discovery` vs `pain-finder` vs `meddicc` can all sound like "audit
this call"), description collision is a real risk that no amount of rubric
quality fixes. Run via `skill-creator`'s `scripts/run_eval.py` against an
`evals/trigger-set.json` of prompts labeled `should_trigger` true/false per
skill.

### Tier 2: format compliance (automated)

The `with_skill` vs `without_skill` benchmark loop, using each skill's
`evals/evals.json`. Reported explicitly as "consistency and scope
discipline," never as "quality" or "insight."

### Tier 3: insight recall vs. human gold labels (requires a human, once)

The only tier that answers "did it find what an expert would find." For a
gold transcript, a human (not the rubric author, ideally) marks:

```markdown
## Findings a human expert marked (ranked)
1. <finding>: must be found. Quote: "<quote>"
## The one a weak rep misses
<finding>: skill gets credit only if it surfaces this
## Dimensions that legitimately do not apply
<dimension>: correct behavior is to say so, not force it in
## Not present: reporting any of these is a hallucination
<plausible-but-absent finding>
```

Scored as recall (found ÷ marked) and precision (in-gold ÷ reported). This
cost is paid **once per transcript**, not once per run. The same gold
transcript can be re-scored every time a rubric changes.

## Where a human is genuinely required, and where not

Required, no automated substitute exists:

- **Gold labels** (above): without them there's no recall denominator and
  every number is self-referential.
- **Blind transcript authorship.** A gold transcript must be written from a
  persona/situation brief, without reference to the rubric it will be
  scored against. It must contain at least one real pain that maps to no
  rubric bucket, and omit at least one dimension the rubric expects to see.
  If the rubric author writes the transcript, the result gets discarded.
- **At least one falsifying expectation per eval.** Every eval in this repo
  carries an expectation that a format-compliant-but-shallow output would
  fail: the guard against a benchmark that's 4-of-5 format checks.

Not required, do not spend time here:

- Trigger evals, schema/layout validation, format-compliance grading,
  `without_skill` baseline runs, benchmark aggregation, HTML report
  generation. All of this runs unattended.

## Reproducing a run

```bash
# Tier 0 (gap diff vs ground truth), document-writing skills:
evals/framework/eval.sh <skill>                       # all cases for that skill
evals/framework/eval.sh <skill> --baseline --learn     # promote to baseline, then LEARN
python3 evals/framework/calibrate.py <skill> <case> evals/runs/<timestamp>  # judge-vs-human kappa

# Tier 1 (trigger), any skill — run_eval.py is trigger-only, a different
# schema/script from the one below:
python3 <skill-creator>/scripts/run_eval.py \
  --eval-set evals/trigger-set.json \
  --skill-path skills/<name>

# Tier 2 (format compliance) is a subagent procedure, not a script — see
# skill-creator's SKILL.md, "Running and evaluating test cases". It spawns
# with_skill/without_skill agents against each skill's evals/evals.json,
# grades via agents/grader.md into grading.json, then:
python3 <skill-creator>/scripts/aggregate_benchmark.py <run-dir> > benchmark.json
python3 <skill-creator>/eval-viewer/generate_review.py evals/runs/<timestamp>
```

`<skill-creator>` is whatever local install of Anthropic's `skill-creator`
skill you have. This repo doesn't vendor it, since it's tooling for
authoring/testing skills, not itself a GTM skill.

## Current coverage, honestly

| Tier | Status |
|---|---|
| Tier 0 (gap diff) | Framework built (`evals/framework/`, promptfoo-backed); `astra` cases wired for both `poc-deck` and `sales-to-cs-handover`. No calibration labels yet — judge-vs-human kappa unrun |
| Tier 1 (trigger) | `evals/trigger-set.json` written (17 cases); not yet run. Structurally impossible for `sales-to-cs-handover` — `disable-model-invocation: true` |
| Tier 2 (format) | Only the prior, non-reproducible `pain-finder` draft run (see above). None of the 16 shipped skills have been benchmarked yet — the `evals/evals.json` schema bug (`assertions` vs `expectations`, wrong file paths) blocked every one of them until this pass |
| Tier 3 (gold-label insight) | Not started. Blocked on 3 gold-labeled transcripts (one per vertical: cybersecurity, healthcare, fintech), by design done by a human, not the rubric author |

CSV mode has never been exercised on any skill. The intentionally-broken-
frontmatter CI test has never been run. See `MAINTAINING.md`'s "Verification
state" for the full picture, kept in sync with this file.

Evals are declarative and are not run in CI. That is a decision, not an
oversight. Say so plainly rather than implying enforcement that doesn't
exist yet.
