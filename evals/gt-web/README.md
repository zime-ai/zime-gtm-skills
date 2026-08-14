# Web-harvested ground truth

Tier 0/3's other ground-truth source (`evals/gt/`) is hand-authored, one
human at a time — this repo has none of that labor available. This
directory is the alternative: **a real named expert's already-published
critique of a real call**, used as ground truth instead of a synthetic
transcript a human here hand-labeled. Nobody in this repo writes the
answer key; a third party already did, in public, before this repo asked
any question of it.

This only covers what public call-coaching content exists for: stage-motion
skills (discovery, demo, objection handling, qualification, closing —
`meddicc`, `challenger`, `deep-discovery`, `pain-finder`, `sandler`, and
similar). Deal-intelligence/writer skills (`champion-tracker`,
`mutual-action-plan`, `executive-briefing`, and the rest of that class) have
no public teardown equivalent — there is no `SOURCES.md` row for them, and
none should be manufactured. `evals/SCORECARD.md` lists those skills under
"No public ground truth available" rather than forcing a number.

## What counts as a source

A harvested source must have, checked before it's used, not after:

- A **real named human coach or org** as author — not an anonymous forum
  post, not AI-generated "expert roundup" content.
- A **publish date**.
- A **transcript or verbatim call excerpt** the critique is actually about,
  not a critique of a hypothetical or paraphrased scenario.
- **Specific, quoted findings** — enough to ground at least one rubric
  dimension of the skill it's mapped to.

## Extraction discipline

Pull the coach's findings as **direct quotes only**. Do not paraphrase what
they "really meant" or extrapolate a verdict they didn't state — that
extrapolation is exactly the kind of interpretation a rubric author's own
bias would otherwise launder into "ground truth." If a source's critique
doesn't explicitly address a rubric dimension, that dimension gets no
ground truth from this source — skip it, don't infer it.

**The one bias point this mechanism does not remove, stated plainly:**
something still decides which sources qualify and which quote maps to
which rubric field, and that something is this repo's own tooling/agent,
not a second independent human. This is a materially different failure
mode than authoring both the transcript and the rubric (the source content
itself is genuinely third-party and checkable), but it is not zero-bias.
`SOURCES.md` exists so anyone can pull the URL and check the mapping
themselves — that's the actual mitigation, not a claim of neutrality.

## Layout

- `evals/gt-web/<source-slug>--<skill>.md` — the harvested excerpt/critique
  used as ground truth for one skill. **Gitignored** (copyright risk in
  redistributing a third party's published content wholesale, not a
  confidentiality concern like `evals/gt/`).
- `evals/gt-web/SOURCES.md` — **public**. One row per source: URL, author,
  org, date retrieved, skill, which rubric dimensions it grounds, and a
  one-line reason it qualifies. This is what makes a `SCORECARD.md` number
  checkable by someone with no access to this repo's private files.

## Running against this ground truth

`evals/framework/judge.py` reads ground truth from `evals/gt/` by default;
a case pointed at web-sourced GT instead sets `gt_dir: gt-web` in its
`evals/cases/<skill>.yaml` entry. Everything else in the Tier 0 loop
(`eval.sh`, isolated RUN/GAP scratch dirs, judge sampling) is unchanged —
see `evals/framework/README.md`.

`calibrate.py`'s Cohen's-kappa check compares the judge against a second
human labeler and has no such labeler for web-sourced GT — there is no
`evals/labels/<skill>-<case>.json` to calibrate against here, by
construction. `SCORECARD.md` states this as **N/A**, not skipped silently.
