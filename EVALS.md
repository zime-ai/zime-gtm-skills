# Evals

How this repo tests whether its skills actually work, and — just as
important — what these evals can and cannot prove.

## The problem with evaluating this kind of skill

Every skill here follows the same loop: read a call, apply a rubric, report
findings. The natural way to test that is to write a transcript, write
expectations, run the skill, and grade the output. But if the same person
(or the same model) writes the rubric, the transcript, and the expectations,
a 100% pass rate proves nothing — the transcript was written to contain
exactly what the rubric hunts for.

A prior benchmark run against an early `pain-finder` draft (kept at
`evals/runs/2026-07-28-cyber-pain-finder-prior/`, see its own README) showed
`1.0` vs `0.51` pass rate with/without the skill. Read closely, 4 of its 5
expectations checked *format* — was a category tag present, was a confidence
line present, was a quote present — and only one checked substance. The
benchmark's own analyzer said as much: the underlying model already finds
pain points well unaided; the skill's main contribution was structural
consistency. That's a real result, but "the skill enforces a consistent
format" and "the skill finds better insight" are different claims, and
blending them into one number overstates the second.

This repo reports them separately, on purpose.

## Two metrics, never blended into one number

- **Format compliance** — did the output follow the rubric's structure and
  stay in scope (right sections, evidence cited, no unrequested extra
  content). Automated, no human required. High-with-skill /
  low-without-skill is expected and is a real, if modest, claim.
- **Insight recall / precision** — of the pain points, gaps, or risks a
  human expert would flag on this call, how many did the skill find
  (recall), and of what it reported, how much was actually real (precision;
  the inverse of precision is roughly the hallucination rate). This is the
  number that survives a skeptical read, and it requires a human-authored
  gold label — see below.

## Three tiers

### Tier 1 — Trigger evals (automated)

Does the *right* skill fire for a given prompt? With 16 skills now in the
repo — several with overlapping descriptions (`deep-discovery` vs
`technical-discovery` vs `pain-finder` vs `meddicc` can all sound like "audit
this call") — description collision is a real risk that no amount of rubric
quality fixes. Run via `skill-creator`'s `scripts/run_eval.py` against an
`evals/trigger-set.json` of prompts labeled `should_trigger` true/false per
skill.

### Tier 2 — Format compliance (automated)

The `with_skill` vs `without_skill` benchmark loop, using each skill's
`evals/evals.json`. Reported explicitly as "consistency and scope
discipline," never as "quality" or "insight."

### Tier 3 — Insight recall vs. human gold labels (requires a human, once)

The only tier that answers "did it find what an expert would find." For a
gold transcript, a human (not the rubric author, ideally) marks:

```markdown
## Findings a human expert marked (ranked)
1. <finding> — must be found. Quote: "<quote>"
## The one a weak rep misses
<finding> — skill gets credit only if it surfaces this
## Dimensions that legitimately do not apply
<dimension> — correct behavior is to say so, not force it in
## Not present — reporting any of these is a hallucination
<plausible-but-absent finding>
```

Scored as recall (found ÷ marked) and precision (in-gold ÷ reported). This
cost is paid **once per transcript**, not once per run — the same gold
transcript can be re-scored every time a rubric changes.

## Where a human is genuinely required — and where not

Required, no automated substitute exists:

- **Gold labels** (above) — without them there's no recall denominator and
  every number is self-referential.
- **Blind transcript authorship.** A gold transcript must be written from a
  persona/situation brief, without reference to the rubric it will be
  scored against. It must contain at least one real pain that maps to no
  rubric bucket, and omit at least one dimension the rubric expects to see.
  If the rubric author writes the transcript, the result gets discarded.
- **At least one falsifying expectation per eval.** Every eval in this repo
  carries an expectation that a format-compliant-but-shallow output would
  fail — the guard against a benchmark that's 4-of-5 format checks.

Not required, do not spend time here:

- Trigger evals, schema/layout validation, format-compliance grading,
  `without_skill` baseline runs, benchmark aggregation, HTML report
  generation. All of this runs unattended.

## Reproducing a run

```bash
# Tier 2 (format compliance), any skill:
python3 <skill-creator>/scripts/run_eval.py \
  --eval-set skills/<name>/evals/evals.json \
  --skill-path skills/<name>

# Aggregate a benchmark, and view it:
python3 <skill-creator>/scripts/aggregate_benchmark.py <run-dir> > benchmark.json
python3 <skill-creator>/eval-viewer/generate_review.py evals/runs/<timestamp>
```

`<skill-creator>` is whatever local install of Anthropic's `skill-creator`
skill you have — this repo doesn't vendor it, since it's tooling for
authoring/testing skills, not itself a GTM skill.

## Current coverage, honestly

| Tier | Status |
|---|---|
| Tier 1 (trigger) | Not yet run on any skill |
| Tier 2 (format) | Only the prior, non-reproducible `pain-finder` draft run (see above). None of the 16 shipped skills have been benchmarked yet — the `evals/evals.json` schema bug (`assertions` vs `expectations`, wrong file paths) blocked every one of them until this pass |
| Tier 3 (gold-label insight) | Not started. Blocked on 3 gold-labeled transcripts (one per vertical: cybersecurity, healthcare, fintech), by design done by a human, not the rubric author |

CSV mode has never been exercised on any skill. The intentionally-broken-
frontmatter CI test has never been run. See `MAINTAINING.md`'s "Verification
state" for the full picture, kept in sync with this file.

Evals are declarative and are not run in CI. That is a decision, not an
oversight — say so plainly rather than implying enforcement that doesn't
exist yet.
