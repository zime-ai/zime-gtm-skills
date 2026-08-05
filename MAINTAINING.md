# Maintaining this repo

Read this before touching the rubrics or repo structure — written so a fresh
Claude Code session started in this repo can pick the work up with no other
context. Sanitized for a public repo: no credentials, no hostnames, no
internal question text. It describes the *process*, not the source.

## What this is

Open-source, standalone Agent Skills for GTM call-audit motions. **This is
not a lead funnel.** No gating, no API-key path, no product coupling to
Zime's paid product, no conversion mechanics anywhere in a skill's output.
Value stands alone; goodwill and credibility are the return. This is the
decision most likely to get quietly walked back later under commercial
pressure — don't.

Persona: a RevOps engineer, or an engineer working on behalf of a sales
team, at a mid-market/enterprise company. Comfortable with a terminal and a
repo, not going to wire live CRM credentials into a third-party skill
(security review kills that path). Skills operate on **local files the user
already has** — call transcripts and CRM exports — never a live connection.

## The rubric-authoring flow

Each skill's rubric is grounded in Zime's internal initiative/checklist
taxonomy (curated call-quality question sets, refined across many real
client engagements) but that taxonomy is Zime IP. The repeatable process for
turning it into a public rubric, without shipping the IP itself:

1. Pull the target motion's checklist **titles only** (not question text)
   from the internal taxonomy, read-only.
2. Drop titles that recur across most motions (~10 generic-core titles:
   things like general feedback capture, active-listening notes, call
   summary, next-meeting logistics, objection logging, action items) —
   these make every motion look the same and add no distinguishing content.
   Keep them only where genuinely load-bearing for that specific motion.
3. Keep the **distinctive** titles — the ones specific to this motion.
4. **Re-author each surviving title into a fresh rubric dimension**, written
   from scratch in this repo: what the dimension is, what good coverage
   looks like, what a miss looks like. Titles are a seed list only — no
   internal question text is ever copied in.
5. Drop junk/orphaned entries.

## The IP boundary, and how it's enforced

**Hard rule: never copy Zime's internal curated checklist question text into
a rubric.** Before any rubric change goes public, grep the repo for verbatim
or near-verbatim matches against internal checklist titles. Rename any hit.

Five headings were already renamed for exactly this reason during the
initial build, because they matched an internal checklist title too closely
even though the surrounding prose was original: a churn-prevention heading
(now "Value delivered, in the customer's own words"), a pilot-to-conversion
heading (now "Setup experience so far"), a negotiation-closing heading (now
"Reaction to pricing"), another negotiation-closing heading (now "Procurement
process is moving"), and an upsell-expansion heading (now "The expansion ask
is concrete"). One near-match — "Onboarding experience quality" in
onboarding-journey — was judged acceptable and left as-is: it's the skill's
own inherent subject matter, not curated phrasing lifted from the taxonomy.
Use that same judgment call for future renames: does the heading name the
skill's actual subject, or does it echo curated phrasing?

## Sample-transcript rules

Every skill ships a sample under `assets/` so it's runnable cold, with no
data of the user's own. Rules for any sample file (transcript or CSV):

- **Synthetic or fully anonymized.** Never a real call or export, even with
  names stripped — anonymizing free text is easy to get wrong.
- Transcripts carry a `[Synthetic transcript for demo purposes only — no
  real company or person]` header line.
- Deliberately mixed quality — a sample that covers everything perfectly
  gives an eval nothing to find. Show some Covered, some Partial/Missed.

## The two hard content rules

1. **Every finding in a transcript-mode audit cites a quote or timestamp.**
   An uncited finding is worse than none — it's untrustworthy the first time
   it's wrong, which is the fastest way to kill adoption of a tool like this.
2. **Never copy Zime's internal checklist question text** — see the IP
   boundary section above.

## Three dimensions: stage, initiative, vertical

Skills cover three axes, but they compose as an **overlay**, not a matrix:

- **Stage** and **initiative** are both ordinary skills in a flat `skills/`
  — no nesting. `zime:dimension` in frontmatter is `stage` or `initiative`.
  The 11 original skills are stage skills; `meddicc`, `bant`, `pain-finder`,
  and `next-step-commitment` are initiative skills that run at any stage.
- **Vertical** is not a skill per industry — it's one skill,
  `skills/vertical-context/`, holding one reference pack per industry
  (`references/{cybersecurity,healthcare,fintech}.md`). Any stage or
  initiative skill can load a pack when a vertical is named. This keeps the
  cost `skills + verticals`, not `skills × verticals` — adding a fourth
  vertical means one new file, not re-authoring 15 skills.
- Do **not** nest skills under `skills/stage/` or `skills/initiative/`
  directories — it was considered and rejected. The Agent Skills spec pins
  `name` to the directory name, `validate-skills.sh` and the pinned
  `skills-ref` CI validator both iterate `skills/*/`, and the README's
  `cp -r skills/* .agents/skills/` install line would copy the nesting dirs
  as if they were skills themselves.
- The vertical packs are **unreviewed** — authored from general domain
  knowledge, not checked against a domain expert or real call data. Say so
  in the pack itself (each carries a "Status: unreviewed" line) rather than
  implying they were vetted.
- Zime's internal taxonomy has 31 initiatives. 15 are covered once the 11
  stage skills (each named after and scoped to one initiative) are counted
  alongside the 4 initiative skills. The other 16 — mostly named
  methodologies (MEDDPICC, FAINT, Sandler, Challenger, Sell the Dream, SQL to
  Qualify, Persona-based discovery, POC success, and others) — are not
  built. This was a deliberate proof-set decision, not an oversight; expand
  it the same way the first 4 were built (Part 2 of the restructure plan).

## Verification state — honestly

- **Structural validation**: all 16 skills pass `./validate-skills.sh`
  (which now also checks `zime:dimension` is present/valid, and that any
  `evals/evals.json` parses and uses `expectations`, not `assertions`) and
  the pinned `skills-ref validate` in CI.
- **Functional validation**: only `deep-discovery` has actually been run
  end-to-end against its sample transcript and had its output read for
  correctness. The other 15 have evals written (see below) but have not
  been manually run.
- **CSV mode**: has never been exercised on any skill. A shared synthetic
  pipeline export exists at `skills/deep-discovery/assets/sample-pipeline.csv`.
- **CI-catches-a-broken-PR test**: never actually run — nobody has opened a
  PR with a deliberately mismatched `name`/directory to confirm the workflow
  fails rather than passing vacuously.
- **Vertical demo (Tier 2)**: not yet run — running `pain-finder` against the
  same transcript with no vertical named vs. `vertical: cybersecurity` named,
  and confirming the output's vocabulary/framing actually changes, is the
  check that the overlay isn't decorative. See `EVALS.md`.
- **Gold-label insight recall (Tier 3)**: not started. Blocked on a human
  (not the rubric author) gold-labeling 3 transcripts, one per vertical. See
  `EVALS.md` for the full methodology and why this tier can't be automated.

`skills/*/evals/evals.json` exist for all 16 skills. Schema was fixed this
pass — they previously used `assertions` (the harness reads `expectations`)
and repo-root-relative `files` paths (the harness wants skill-root-relative),
so **none of the original 11 had ever actually been runnable** before now.
Every eval also now carries at least one expectation a
format-compliant-but-shallow output would fail, per `EVALS.md`'s
falsifying-expectation rule. They remain declarative — not run in CI.

Full eval methodology, the format-vs-insight distinction, and the tier
structure now live in `EVALS.md` — read that before adding or changing any
eval, not just this section.

## Deferred work (on hold by decision, not forgotten)

- **Plugin manifest + distribution** — reversed at public launch.
  `.claude-plugin/plugin.json` + `marketplace.json` now ship (`/plugin
  marketplace add zime-ai/zime-gtm-skills`). The original reasoning (wait
  for organic traction) held while the repo was private; a launch-day repo
  needs a one-line install path more than it needs to wait. `npx skills add`
  support is still deferred.
- **Running the evals in CI** — turn `evals/evals.json` from a spec into an
  actual check, likely by invoking each skill against its eval prompts with
  a small harness and comparing against the expectations.
- **The other 16 initiative skills** — see "Three dimensions" above.
- **Domain-expert review of the 3 vertical packs** — the "vertical jargon
  check" scoped for this pass and explicitly deferred.
- **`VERSIONS.md` + per-skill `metadata.version`** — only worth the
  bookkeeping once there are installed users who need to detect updates.
- **Auto-regenerating the README's skill table** from the `SKILL.md`
  frontmatter (the reference repo this was adapted from has a
  `sync-skills.js` for this) — not worth it yet at 16 skills; the
  `<!-- SKILLS:START/END -->` markers are already in place for whenever it is.

## Building skills at scale

For building several skills at once instead of one Claude Code session at a
time. Three pieces, each doing one job:

### Worktree-per-skill

Use the installed `using-git-worktrees` skill (`obra/superpowers`) to isolate
each skill-in-progress in its own git worktree and branch. It handles the
mechanics — directory, branch, isolation check — but it doesn't know this
repo's rules, which still apply regardless of worktree tooling:

- No `Co-Authored-By: Claude` trailer, ever.
- Claude never runs `git push` or `gh` — see "Who runs git commands" below.

`scripts/pr-prep.sh <worktree-path> "<PR title>"` enforces both, plus runs
`./validate-skills.sh` against the worktree, before writing (never running) a
push/PR script. Run it from the main checkout once a worktree's skill work is
done.

One worktree per skill being built. 3-5 concurrent is the practical ceiling —
past that, review becomes the bottleneck, not the building.

### Create → validate → iterate, with real stop conditions

Not a new custom loop — a documented procedure chaining what already exists,
with explicit stop conditions instead of ad hoc judgment each time:

1. Draft the skill (a Claude Code session, in its own worktree).
2. Deterministic gate: `./validate-skills.sh` — frontmatter, line count,
   layout.
3. Deterministic gate, if the skill ships `evals/evals.json`:
   `python3 <skill-creator>/scripts/run_eval.py --eval-set skills/<name>/evals/evals.json --skill-path skills/<name>`
   (see `EVALS.md`).
4. **Independent verification, not self-grading** — a fresh-context Claude
   session reads the rubric against this file's IP-boundary rule and the two
   hard content rules. This is the step the gates above can't do: judging
   rubric quality and IP-safety needs a model, not a test runner, and the
   model that wrote the rubric must not be the one that clears it.
5. Hard iteration cap: **3 revision passes** per skill. On the 4th failure,
   stop and hand to the maintainer rather than continuing — a loop that lets
   the model keep "trying again" past a small cap is exactly the runaway
   pattern to avoid.
6. Only after steps 2-4 pass: `scripts/pr-prep.sh`.

What this is **not**: a CI job, unattended, or something that merges without
review. It's the same manual flow already run for `deep-discovery` (the one
skill actually run end-to-end — see "Verification state" above), made
repeatable. Running this loop unattended in CI, with no human anywhere in it,
is explicitly out of scope — it would need a much stronger verifier than "a
fresh Claude session reads it," since this repo's IP and evidence-citation
rules aren't mechanically checkable. Said plainly rather than implying more
autonomy than actually exists.

### PR-Agent

`.github/workflows/pr-agent.yml` runs [PR-Agent](https://github.com/The-PR-Agent/pr-agent)'s
`/review` automatically on every PR open/sync, via Claude
(`config.model: anthropic/claude-sonnet-5`). `auto_describe`/`auto_improve`
stay off on purpose — this repo already requires a filled-in PR template, and
the bot shouldn't overwrite what a contributor wrote; `/describe` and
`/improve` are still available as manual PR comments. Pinned to a release
commit SHA, not `@main`, same reasoning as `validate.yml`'s `skills-ref` pin —
bump deliberately by resolving the new tag's commit
(`gh api repos/The-PR-Agent/pr-agent/git/refs/tags/<tag> --jq '.object.sha'`).

This is a second, automated pass — it doesn't replace a maintainer's own
`/code-review`, and a real acceptance decision is still the maintainer's.

One-time setup the maintainer needs to do (needs repo admin, not just push):
add `ANTHROPIC_KEY` as a repo secret (Settings → Secrets and variables →
Actions), and since this is a public repo, confirm "Require approval for all
outside collaborators" is on for fork PRs — otherwise a malicious fork PR can
run the workflow against that secret unapproved.

## Who runs git commands

Repo creation, `git push`, and any `gh` invocation (setting description,
topics, etc.) stay with the maintainer. Claude prepares and stages files and
hands over the exact commands to run. Read-only inspection (`gh repo view`,
`gh auth status`) is fine to run directly.

**Never push `internal_skills`.** It holds work that must not be public
(the build/launch plan, product-coupled skill drafts, internal decks) —
branches are as world-readable as `main` on a public repo, so parking WIP on
a branch does not hide it. Keep it local only.
