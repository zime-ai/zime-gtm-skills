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

- **Plugin manifest + distribution** (`.claude-plugin/plugin.json` +
  `marketplace.json`, `npx skills add` support, `/plugin marketplace add`)
  — explicitly held back. Do this once the repo has some organic traction
  worth distributing, not before.
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

## Who runs git commands

Repo creation, `git push`, and any `gh` invocation (setting description,
topics, etc.) stay with the maintainer. Claude prepares and stages files and
hands over the exact commands to run. Read-only inspection (`gh repo view`,
`gh auth status`) is fine to run directly.
