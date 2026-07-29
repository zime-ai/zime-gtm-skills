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

## Verification state — honestly

- **Structural validation**: all 11 skills pass `./validate-skills.sh` and
  the pinned `skills-ref validate` in CI.
- **Functional validation**: only `deep-discovery` has actually been run
  end-to-end against its sample transcript and had its output read for
  correctness. The other 10 have evals written (see below) but have not
  been manually run.
- **CSV mode**: has never been exercised on any of the 11 skills. A shared
  synthetic pipeline export exists at
  `skills/deep-discovery/assets/sample-pipeline.csv` for this.
- **CI-catches-a-broken-PR test**: never actually run — i.e. nobody has
  opened a PR with a deliberately mismatched `name`/directory to confirm the
  workflow fails rather than passing vacuously.

`skills/*/evals/evals.json` exist for all 11 skills (3 cases each: sample
transcript, a "reads-well-too" negative case, and CSV mode or — for
`first-call-rampup`, which is transcript-only — a decline-CSV case). They are
**declarative only right now**, not run in CI. Running them is the top item
below.

## Deferred work (on hold by decision, not forgotten)

- **Plugin manifest + distribution** (`.claude-plugin/plugin.json` +
  `marketplace.json`, `npx skills add` support, `/plugin marketplace add`)
  — explicitly held back. Do this once the repo has some organic traction
  worth distributing, not before.
- **Running the evals in CI** — turn `evals/evals.json` from a spec into an
  actual check, likely by invoking each skill against its eval prompts with
  a small harness and comparing against the assertions.
- **`VERSIONS.md` + per-skill `metadata.version`** — only worth the
  bookkeeping once there are installed users who need to detect updates.
- **Auto-regenerating the README's skill table** from the `SKILL.md`
  frontmatter (the reference repo this was adapted from has a
  `sync-skills.js` for this) — not worth it yet at 11 skills; the
  `<!-- SKILLS:START/END -->` markers are already in place for whenever it is.

## Who runs git commands

Repo creation, `git push`, and any `gh` invocation (setting description,
topics, etc.) stay with the maintainer. Claude prepares and stages files and
hands over the exact commands to run. Read-only inspection (`gh repo view`,
`gh auth status`) is fine to run directly.
