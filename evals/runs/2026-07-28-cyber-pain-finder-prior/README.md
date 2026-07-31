# Prior run: cyber-pain-finder benchmark (2026-07-28)

A skill-creator benchmark run against an early, unpublished draft of what
became the `pain-finder` initiative skill, specialized for cybersecurity.
Kept here as a prior data point, not as the repo's evidence base.

## What's here

- `iteration-1/benchmark.json`, `iteration-1/benchmark.md` — the raw
  `with_skill` vs `without_skill` results
- `review.html` — the skill-creator eval-review viewer for this run

## Result

| Metric | with_skill | without_skill |
|---|---|---|
| Pass rate | 1.00 | 0.51 |
| Time | 75.9s avg | 57.7s avg |
| Tokens | 36,369 avg | 31,456 avg |

## Why this is not cited as the repo's evidence

1. **Not reproducible.** The skill draft and the three call transcripts used
   (two Meridian Freight Logistics calls, one Northgate Health Partners call)
   were not retained — the prompts embedded them inline in a remote session
   that no longer exists. Nobody can re-run this.
2. **Measures format, not insight.** Of the 5 expectations in eval 1, four
   check *shape* — explicit category tags present, a confidence line present,
   direct quotes present, no unrequested extra section. Only one checks
   *substance* (correctly downgrading a secondary signal). The benchmark's
   own analyzer notes said as much: "the underlying model already does a
   strong job at finding pain points even without the skill — the biggest,
   most consistent gap is structural." So this result supports "the skill
   enforces a consistent, scope-disciplined format," not "the skill finds
   better insight than an unaided model."
3. **Self-eval bias.** Rubric, transcripts, expectations, executor, and
   grader were all the same model family with no independent gold label. See
   `EVALS.md` for how the repo's current eval methodology avoids this.

The `pain-finder` initiative skill in `skills/pain-finder/` is a from-scratch
rebuild, vertical-aware via `skills/vertical-context/`, evaluated under the
methodology in `EVALS.md` — not a continuation of this run.
