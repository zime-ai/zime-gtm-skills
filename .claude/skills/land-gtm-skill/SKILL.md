---
name: land-gtm-skill
description: Walks through landing a new GTM audit skill on zime-gtm-skills' main branch — worktree, scaffold, validators, the full README/repo-description count bump, and opening the PR via pr-prep.sh. Use whenever the user wants to add, build, or land a new skill in the zime-gtm-skills repo specifically ("add a skill to zime-gtm-skills", "land skill X on main", "help me turn this draft into a zime-gtm-skills skill"), whether starting from scratch or from an existing draft SKILL.md. Do NOT use this for editing an existing skill already in skills/, or for GTM skill work in a different repo.
---

# Landing a skill on zime-gtm-skills

This operationalizes `MAINTAINING.md`'s "Building skills at scale" and
"Landing a skill on main" sections so nothing gets skipped. The single
biggest failure mode this skill exists to prevent: bumping the skill count
in the four README places but forgetting the GitHub repo description — a
fifth surface no script checks, and the exact gap that slipped through once
already.

Read `references/doc-anchors.md` before touching `README.md` — it has the
literal grep patterns `scripts/check-docs-sync.sh` matches against, so edits
land right the first time instead of getting caught by the validator and
redone. Read `references/scaffold-template.md` before writing a new skill's
files — it's the exact shape `skills/bant/` and every other skill use.

## 0. Confirm you're in the right place, on the right base

This whole procedure assumes the `zime-gtm-skills` repo and `main` as the
base. Check both before doing anything:

```bash
git remote get-url origin   # expect .../zime-gtm-skills.git
git fetch origin -q
```

If the current checkout is on a branch other than `main` (this repo has run
sessions on `internal_skills` before, which deliberately strips the public
skill catalog), don't read `README.md`/`AGENTS.md`/`MAINTAINING.md` from the
working tree — read them via `git show origin/main:<path>` instead, or the
counts and rules you're working from will be wrong. The worktree you create
in the next step branches off `origin/main` regardless of what the main
checkout currently has checked out.

## 1. Worktree

```bash
git worktree add ../zime-gtm-skills-<name> -b add-<name> main
```

One worktree per skill. If the user already has a draft `SKILL.md`
somewhere (Downloads, another doc), read it now — you're about to
restructure it, not just move it: repo skills push detail into
`references/`, keep `SKILL.md` under 500 lines, and never contain hardcoded
personal identities, real client names, or content that isn't already
customer-visible in the Zime product (see `AGENTS.md`'s "The two hard
content rules"). Flag anything that violates those rather than shipping it
as-is — this has come up before and the fix each time was to ask the user
how to adjust, not silently drop or silently keep the violating content.

## 2. Scaffold the skill directory

Follow `references/scaffold-template.md` exactly. Four files, nothing else
at the top level of `skills/<name>/`:

- `SKILL.md` — frontmatter (`name` matching the directory exactly,
  `description` stating both what and when, `metadata.zime:category`,
  `metadata.zime:dimension` of `stage` or `initiative`, `zime:input-modes`)
  plus the run procedure.
- `references/rubric.md` — the actual scoring criteria.
- `assets/sample-transcript.txt` (or similar) — synthetic or fully
  anonymized. Never a real transcript or CRM export, even with names
  scrubbed — anonymizing free text reliably misses something, and this
  repo is public.
- `evals/evals.json` — declarative test cases using the key
  `expectations`, never `assertions` (`validate-skills.sh` fails on the
  wrong key name).

A skill with `zime:dimension: stage` or `initiative` **must** ship both
`assets/` and `evals/evals.json`, or `validate-skills.sh`'s
`sample-required` rule fails it — this isn't optional the way it once was
prose-only advice; it's an enforced check now.

## 3. Validate before touching the README

```bash
cd ../zime-gtm-skills-<name>
./validate-skills.sh
```

Fix everything it reports before moving on — there's no point editing the
README against a skill that doesn't even pass its own frontmatter contract
yet.

## 4. Update the README — all five count surfaces, in order

Read `references/doc-anchors.md` for the exact regex each of these must
match. In `README.md`:

1. **Badge** — `skills-N-blue` in the shields.io URL near the top.
2. **Opening paragraph** — "`here. N [Agent Skills](https://agentskills.io)`".
3. **"How these fit together"** — `N skills: M stage motions ... K
   cross-stage initiative skills`. The validator only checks the first
   number (`N`) against the actual directory count — **the `M` and `K`
   sub-counts are not checked by anything and must be hand-verified**: if
   the new skill is a stage skill, `M` goes up by one; if initiative, `K`
   does.
4. **`<summary>` tag** — `<summary>N skills across ...</summary>` right
   above the skills table.
5. **GitHub repo description** — not in any file, so no script catches it.
   Run:
   ```bash
   gh repo edit zime-ai/zime-gtm-skills --description "Build your own sales-call review tooling: N open Agent Skills that audit call transcripts and CRM exports against GTM rubrics, citing a quote for every finding. Local, no credentials."
   ```
   Only touch the number — keep the rest of the sentence exactly as it is
   unless the user has separately asked to change the pitch itself.

Then, still in `README.md`:

6. **Table row** inside `<!-- SKILLS:START -->`/`<!-- SKILLS:END -->`,
   under the section matching the skill's `zime:category` (see the mapping
   table in `references/doc-anchors.md`), format
   `` | [name](skills/name/) | <hand-written Audits summary> | <input modes> | ``.
   The "Audits" column is prose judgment, not derived from anything — write
   the one line that actually tells a reader what the skill catches.
7. **Coverage table row** — `` | `name` | <stage or n/a> | <initiative or n/a> | ``.
   Skip this step entirely if `zime:dimension: vertical-context`.
8. **Mermaid diagram** — only if it's a stage skill, place it in the
   flowchart in the right position in the deal lifecycle.

## 5. Check off MAINTAINING.md

If the skill was listed under `MAINTAINING.md`'s "Deferred work" section,
strike that line now that it's landing.

## 6. Validate again — this time the doc-sync check

```bash
./scripts/check-docs-sync.sh
```

This is what actually catches a missed anchor from step 4 or a missing row
from step 6/7 — treat any FAIL here as something to fix, not something to
explain away. It cannot catch the mermaid diagram, the repo description, or
the stage-motion sub-counts (see step 4) — those stay on you.

## 7. Content scan

```bash
python3 scripts/scan-content.py
```

Catches home paths, injection patterns, hidden unicode, and (if a local
`.private/client-denylist.txt` exists) denylisted client names. A skip
message for `no-client-names` when that file is absent is expected, not a
failure — it means the rule has nothing to check against locally, not that
it passed.

## 8. Ship it

Write the real PR description to `.tmp/pr-description-add-<name>.txt` in
the **main checkout**, not the worktree — one physical line per
paragraph/bullet, however long, since GitHub renders a single `\n` in a PR
body as a hard line break, not a soft wrap. Then, from the main checkout:

```bash
./scripts/pr-prep.sh ../zime-gtm-skills-<name> "Add <name> skill"
```

This re-runs all three validators, checks for a Claude co-author trailer or
Claude-looking commit author (hard-blocks either), and only then pushes the
branch and opens the PR. The first run will fail on purpose if the PR body
file doesn't exist yet — it writes a placeholder and stops so you fill it
in for real.

**Stop here.** Merging the PR into `main` is always a human decision — see
`MAINTAINING.md`'s "Who runs git commands." Report the PR URL and don't
merge it, don't ask to merge it, regardless of how clean the checks are.
