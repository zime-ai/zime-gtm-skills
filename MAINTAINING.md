# Maintaining this repo

Read this before touching the rubrics or repo structure. It's written so a
fresh Claude Code session started in this repo can pick the work up with no
other context. Sanitized for a public repo: no credentials, no hostnames, no
internal question text. It describes the *process*, not the source.

## What this is

Open-source, standalone Agent Skills for GTM call-audit motions. **This is
not a lead funnel.** No gating, no API-key path, no product coupling to
Zime's paid product, no conversion mechanics anywhere in a skill's output.
Value stands alone; goodwill and credibility are the return. This is the
decision most likely to get quietly walked back later under commercial
pressure. Don't.

Persona: a RevOps engineer, or an engineer working on behalf of a sales
team, at a mid-market/enterprise company. Comfortable with a terminal and a
repo, not going to wire live CRM credentials into a third-party skill
(security review kills that path). Skills operate on **local files the user
already has**: call transcripts and CRM exports, never a live connection.

## The rubric-authoring flow

Each skill's rubric is grounded in Zime's internal initiative/checklist
taxonomy: customer-visible checklist question text (see "The IP boundary"
below for what's still off-limits), pruned down to the items distinctive to
that motion, then written up fresh as a full rubric dimension — what it is,
what good coverage looks like, what a miss looks like. The prose framing is
never copy-pasted from an internal scoring guide.

## The IP boundary, and how it's enforced

**Hard rule: never expose anything that isn't already customer-visible in
the Zime product.** Checklist titles and question text are customer-visible
and are permitted. What stays out:

- Internal scoring weights, thresholds, or model configuration
- Customer names, account details, or any per-account data
- Anything from an internal scoring guide, prompt, or eval that isn't shown
  to a Zime customer today

Before any rubric change goes public, check it against that boundary, not
against a "does this echo a checklist title" test — that test is gone now
that checklist text itself is allowed.

## Sample-transcript rules

Every skill ships a sample under `assets/` so it's runnable cold, with no
data of the user's own. Rules for any sample file (transcript or CSV):

- **Synthetic or fully anonymized.** Never a real call or export, even with
  names stripped: anonymizing free text is easy to get wrong.
- Transcripts carry a `[Synthetic transcript for demo purposes only — no
  real company or person]` header line.
- Deliberately mixed quality: a sample that covers everything perfectly
  gives an eval nothing to find. Show some Covered, some Partial/Missed.

## The two hard content rules

1. **Every finding in a transcript-mode audit cites a quote or timestamp.**
   An uncited finding is worse than none: it's untrustworthy the first time
   it's wrong, which is the fastest way to kill adoption of a tool like this.
2. **Never expose anything that isn't already customer-visible in the Zime
   product**: see the IP boundary section above.

## Two dimensions: stage, initiative

Skills cover two axes, both ordinary skills in a flat `skills/`, no nesting:

- **Stage** and **initiative**. `zime:dimension` in frontmatter is `stage`
  or `initiative`. The 11 original skills are stage skills; `meddicc`,
  `bant`, `pain-finder`, `next-step-commitment`, `meddpicc`, `faint`,
  `sandler`, and `challenger` are initiative skills that run at any stage.
- Do **not** nest skills under `skills/stage/` or `skills/initiative/`
  directories. It was considered and rejected. The Agent Skills spec pins
  `name` to the directory name, `validate-skills.sh` and the pinned
  `skills-ref` CI validator both iterate `skills/*/`, and the README's
  `cp -r skills/* .agents/skills/` install line would copy the nesting dirs
  as if they were skills themselves.
- This 20-skill set is a deliberate proof-set, not the full catalogue — see
  `ROADMAP.md` for what's built and what's next. Expand it the same way the
  first 4 initiative skills were built.

## Verification state, honestly

- **Structural validation**: all 20 skills pass `./validate-skills.sh`
  (which now also checks `zime:dimension` is present/valid, and that any
  `evals/evals.json` parses and uses `expectations`, not `assertions`) and
  the pinned `skills-ref validate` in CI.
- **Functional validation**: only `deep-discovery` has actually been run
  end-to-end against its sample transcript and had its output read for
  correctness. The other 19 have evals written (see below) but have not
  been manually run.
- **CSV mode**: has never been exercised on any skill. A shared synthetic
  pipeline export exists at `skills/deep-discovery/assets/sample-pipeline.csv`.
- **CI-catches-a-broken-PR test**: fixed. `tests/run-checks-tests.sh` runs
  `validate-skills.sh`, `scripts/check-docs-sync.sh`, and
  `scripts/scan-content.py` against scratch fixtures with a deliberately
  mismatched `name`/directory, missing frontmatter fields, an un-ignored
  private data dir, a leaked home path, an injection pattern, and more —
  asserting the real script fails with the right message, not just that it
  exists. Wired into `.github/workflows/validate.yml` as its own step.
- **Vertical overlay demo (Tier 2)**: paused, not run. Was scoped as running
  `pain-finder` with no vertical named vs. `vertical: cybersecurity` named
  and confirming the output's vocabulary/framing actually changes. Blocked
  on `vertical-context` returning from its own branch after domain review —
  see "Two dimensions" above.
- **Gold-label insight recall (Tier 3)**: not started. Blocked on a human
  (not the rubric author) gold-labeling sample transcripts. See `EVALS.md`
  for the full methodology and why this tier can't be automated.

`skills/*/evals/evals.json` exist for all 20 skills, using `expectations`
(not `assertions`) with skill-root-relative `files` paths. Every eval carries
at least one expectation a format-compliant-but-shallow output would fail,
per `EVALS.md`'s falsifying-expectation rule. They remain declarative, not
run in CI.

Full eval methodology, the format-vs-insight distinction, and the tier
structure now live in `EVALS.md`. Read that before adding or changing any
eval, not just this section.

## Deferred work (on hold by decision, not forgotten)

- **`npx skills add` support**: the Claude Code plugin path
  (`.claude-plugin/plugin.json` + `marketplace.json`) already ships; this
  alternate install path is still deferred.
- **Running the evals in CI**: turn `evals/evals.json` from a spec into an
  actual check, likely by invoking each skill against its eval prompts with
  a small harness and comparing against the expectations.
- **The `vertical-context` skill** (a third axis: industry reference packs
  for cybersecurity, healthcare, fintech, loaded by other skills on request)
  was pulled off `main` before public launch — it never got the
  domain-expert review its own "Status: unreviewed" line called for, and a
  public repo isn't the place to let that sit unresolved. It lives on the
  `vertical-context` branch, snapshotted at the point of removal, with a
  draft PR open against this repo tracking its return once reviewed.
- **`VERSIONS.md` + per-skill `metadata.version`**: only worth the
  bookkeeping once there are installed users who need to detect updates.
- **Auto-regenerating the README's skill table** from the `SKILL.md`
  frontmatter (the reference repo this was adapted from has a
  `sync-skills.js` for this): not worth it yet at 20 skills; the
  `<!-- SKILLS:START/END -->` markers are already in place for whenever it is.

## Building skills at scale

For building several skills at once instead of one Claude Code session at a
time. Three pieces, each doing one job:

### Worktree-per-skill

Use the installed `using-git-worktrees` skill (`obra/superpowers`) to isolate
each skill-in-progress in its own git worktree and branch. It handles the
mechanics (directory, branch, isolation check), but it doesn't know this
repo's rules, which still apply regardless of worktree tooling:

- No `Co-Authored-By: Claude` trailer, ever.
- No commit under a Claude-attributed identity.

`scripts/pr-prep.sh <worktree-path> "<PR title>"` enforces both, runs
`./validate-skills.sh` against the worktree, then pushes the branch and opens
the PR directly. See "Who runs git commands" below for what Claude may and
may not do past that point. Run it from the main checkout once a worktree's
skill work is done.

One worktree per skill being built. 3-5 concurrent is the practical ceiling:
past that, review becomes the bottleneck, not the building.

### Create → validate → iterate, with real stop conditions

Not a new custom loop, a documented procedure chaining what already exists,
with explicit stop conditions instead of ad hoc judgment each time:

1. Draft the skill (a Claude Code session, in its own worktree).
2. Deterministic gate: `./validate-skills.sh` (frontmatter, line count,
   layout).
3. Deterministic gate, if the skill ships `evals/evals.json`:
   `python3 <skill-creator>/scripts/run_eval.py --eval-set skills/<name>/evals/evals.json --skill-path skills/<name>`
   (see `EVALS.md`).
4. **Independent verification, not self-grading**: a fresh-context Claude
   session reads the rubric against this file's IP-boundary rule and the two
   hard content rules. This is the step the gates above can't do: judging
   rubric quality and IP-safety needs a model, not a test runner, and the
   model that wrote the rubric must not be the one that clears it.
5. Hard iteration cap: **3 revision passes** per skill. On the 4th failure,
   stop and hand to the maintainer rather than continuing. A loop that lets
   the model keep "trying again" past a small cap is exactly the runaway
   pattern to avoid.
6. Only after steps 2-4 pass: `scripts/pr-prep.sh`.

What this is **not**: a CI job, unattended, or something that merges without
review. It's the same manual flow already run for `deep-discovery` (the one
skill actually run end-to-end, see "Verification state" above), made
repeatable. Running this loop unattended in CI, with no human anywhere in it,
is explicitly out of scope. It would need a much stronger verifier than "a
fresh Claude session reads it," since this repo's IP and evidence-citation
rules aren't mechanically checkable. Said plainly rather than implying more
autonomy than actually exists.

### PR-Agent

`.github/workflows/pr-agent.yml` runs [PR-Agent](https://github.com/The-PR-Agent/pr-agent)'s
`/review` automatically on every PR open/sync, via Claude
(`config.model: anthropic/claude-sonnet-5`). `auto_describe`/`auto_improve`
stay off on purpose: this repo already requires a filled-in PR template, and
the bot shouldn't overwrite what a contributor wrote; `/describe` and
`/improve` are still available as manual PR comments. Pinned to a release
commit SHA, not `@main`, same reasoning as `validate.yml`'s `skills-ref` pin:
bump deliberately by resolving the new tag's commit
(`gh api repos/The-PR-Agent/pr-agent/git/refs/tags/<tag> --jq '.object.sha'`).

This is a second, automated pass. It doesn't replace a maintainer's own
`/code-review`, and a real acceptance decision is still the maintainer's.

One-time setup the maintainer needs to do (needs repo admin, not just push):
add `ANTHROPIC_KEY` as a repo secret (Settings → Secrets and variables →
Actions), and since this is a public repo, confirm "Require approval for all
outside collaborators" is on for fork PRs, otherwise a malicious fork PR can
run the workflow against that secret unapproved.

Fork PRs never see the secret regardless (GitHub withholds it), so the job's
`if:` skips them outright rather than running and failing. See
`CONTRIBUTING.md` — fork PRs get maintainer review instead.

## Landing a skill on dev

"Building skills at scale" above covers writing and validating a skill.
Separately: every one of the README's several count/table surfaces has to be
updated by hand when a skill actually lands, or `dev` starts shipping a
stale README. `scripts/check-docs-sync.sh` (wired into CI and into
`scripts/pr-prep.sh`) catches a skipped step, but it doesn't do the step for
you — steps 2-6 below are hand-edits by design, not generated, since the
"Audits" column and the coverage-table cells are prose judgment calls, not
something derivable from frontmatter.

Skill branches PR into `dev`, not `main` — see "Releasing dev to main" below
for how `dev` reaches `main`.

1. Skill directory complete: `SKILL.md`, `references/`, `assets/`,
   `evals/evals.json`.
2. `README.md` — bump the skill count in all four places: the badge, the
   opening paragraph, "How these fit together," and the `<summary>` tag.
3. `README.md` — add a row inside `<!-- SKILLS:START -->`/`<!-- SKILLS:END -->`,
   under the right group (New business / Post-sale / Initiative (cross-stage)
   — matching the skill's `zime:category`), with a hand-written "Audits"
   summary and its input modes.
4. `README.md` — add a row to the "Coverage" table.
5. `README.md` — if it's a stage skill, place it in the mermaid diagram.
6. `ROADMAP.md` — check the skill's box under its phase-1 group.
   `check-docs-sync.sh`'s `roadmap-in-sync` rule fails the PR if this is
   skipped.
7. `./validate-skills.sh` && `./scripts/check-docs-sync.sh` — both must exit 0.
8. `scripts/pr-prep.sh <worktree-path> "<PR title>"` — re-runs both gates,
   pushes, opens the PR against `dev`. PR-Agent reviews automatically.
9. Merging to `dev` is still a human decision. Unchanged by any of the above.

## Releasing dev to main

`dev` is where skill PRs land; `main` only moves forward in batches, once a
release checklist has run. This is `main`'s only job: stay release-quality
so a `git clone` always gets something that's actually been checked as a
whole, not skill-by-skill drift.

The `gtm-release` skill (`.claude/skills/gtm-release/`, local-only, same as
the other batch-landing skills) operationalizes this: it re-derives all five
README count surfaces plus the GitHub repo description from what's actually
in `skills/` (not from what individual skill PRs claimed), runs all four
validators, adds the `CHANGELOG.md` entry, and opens the `dev` → `main` PR.
Same human-merge rule applies — see "Who runs git commands" below.

Run it whenever a batch of `dev`-landed skills is ready to ship, not on a
fixed cadence.

## Who runs git commands

Claude may run `git push` and `gh` directly for this repo (branches, PRs,
repo metadata) once the relevant safety gate has passed (`./validate-skills.sh`
at minimum; for skill content, the create-validate-iterate loop above). This
is narrower than it sounds: **merging a PR into `main` stays a human decision**
via PR review (`CONTRIBUTING.md` + the automated PR-Agent pass), not something
Claude does itself.

`git commit --author=` still applies, no `Co-Authored-By: Claude` trailer,
ever. `scripts/pr-prep.sh` enforces both mechanically before any push.

**Never push `internal_skills`.** It holds work that must not be public.
Branches are as world-readable as `main` on a public repo, so parking WIP on
a branch does not hide it. Keep it local only.
