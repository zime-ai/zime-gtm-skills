# zime-gtm-skills — build plan

Not public yet. Goal: grow this repo from 16 skills to roughly 55, across the
three dimensions it already claims (deal stage, initiative, industry vertical),
add a new category of skills modeled on Zime's in-product AMA feature, then
launch it publicly as the one-stop GTM skills repo. (The count moved from an
initial ~45 once the real initiative list and AMA roster replaced earlier
placeholder estimates — see "Target shape" below.)

## Why this order

**The repo overclaims today.** `README.md` says "Eleven skills" — there are 16.
The coverage matrix marks 13 skills as industry-adaptive; only 3 actually load
industry context in their instructions. The evals doc points at a trigger-test
file that doesn't exist. Only one skill has ever been run end to end. The
spreadsheet-input path has never been tried on any skill. Scaling on top of this
triples the debt, and a public launch is exactly when someone checks.

**The new category is a different shape.** All 16 current skills grade a call
against a rubric — status, evidence, note. Call prep, deal highlights, WBR
reports, and handover to customer success *write something forward* instead —
a finished document, not a scorecard. New output format, new way of citing
evidence, new kind of test. Needs proving on two skills before the rest of
that roster gets built on it.

**Why ~55 and not more.** The 60-skill marketing-skills repo has 42.5k stars.
The 206-skill GTM repo has 31. Depth in a bounded domain outperforms breadth —
~55 is where the actual initiative list and AMA roster land, not a number
picked in advance.

## Decisions

| Question | Decision |
|---|---|
| Audience | Open-source GTM community first. Every skill must work standalone — paste a transcript, get output, no setup required. |
| Positioning | Competence only. Maintainer credit, no calls-to-action, no product mentions inside any skill's output. |
| Verticals | Two: cybersecurity/infosec and healthcare. Drop the started fintech pack — better to go deep on two than thin on three. |
| Vertical model | Overlay, not separate skills. Industry packs are shared reference files any skill can load; adding a vertical is one new file, not new skills. |
| New spine | Add a company-profile skill (who we sell to, what we sell, competitors) that other skills can read. No skill currently has this context. |
| Quality gate | Automated checks on every skill; a person spot-checks a sample per batch, not every skill individually. |
| Install | Keep clone-only for now; add one-line install options at launch. |
| CRM integration | Named goal, not solved now — see "Open, not solved" below. |

## Target shape

```
16  today
17  + company-profile skill                         (Phase 0)
19  + 2 skills proving the new category              (Phase 1)
36  + 17 remaining sales-framework skills            (Phase 2)
55  + 19 remaining new-category skills                (Phase 3)
55  0 new — deepen the 2 industry packs               (Phase 4)
55  0 new — public launch                             (Phase 5)
```

Moved from ~45 to ~55 once the real initiative list (below) and a fuller
new-category roster replaced the earlier placeholder counts. The number isn't
the goal — coverage of real use cases is — but the batch sizes in Phase 2/3
change because of it, so it's worth stating plainly rather than quietly
letting the plan drift.

Skills stay flat under `skills/<name>/` — no nesting by dimension. Nesting
breaks the install command and the name-must-match-directory rule already in
place.

### New-category roster (21, up from 14)

Source: Zime's in-product AMA / CRO Twin surface. `Prep notes, global agent`
and `Deal AMA, global agent` are real, named agents there — cross-deal in
scope, not tied to one call or one deal, so they get their own group instead
of folding into seller-facing. `(proposed)` rows are mine, not confirmed
against the real surface — added because a GTM skills repo should cover this
ground and the roster had gaps. Each needs an explicit accept/cut decision in
Phase 3 before it gets built.

| Group | Skills |
|---|---|
| Seller-facing, single deal | call-prep, deal-highlights, mutual-action-plan, exec-briefing, champion-tracker, competitor-battlecard, follow-up-email-drafter (proposed) |
| Manager rituals | wbr-report-generator, forecast-review, pipeline-review, deal-risk-digest, win-loss-brief, stuck-deal-digest (proposed), rep-ramp-status-digest (proposed) |
| Cross-deal, global | zime-prep-notes-global-agent, global-deal-ama-agent, objection-pattern-digest (proposed), competitive-loss-digest (proposed) |
| Handoffs | sales-to-cs-handover, renewal-prep, coaching-plan |

### Remaining framework batch — grounded in the real initiative list (17)

Pulled from `.tmp/playbook-initiatives-and-checklists.md` (Playbook Builder
prod data, 31 initiatives, titles only — no checklist question content, same
IP line the repo already holds). 13 of 31 are already covered, one-to-one, by
existing skills. This corrects an earlier assumption in this plan: `SQL to
Qualify` and `POC success` do **not** fold into `meeting-to-qualify` /
`pilot-to-conversion` — the real list confirms they're distinct, unbuilt
initiatives. No dedup needed. The remaining 17 (of 30 real entries — one
`test` row excluded as junk data):

| Group | Initiatives to build |
|---|---|
| Qualification frameworks | FAINT, MEDDPICC, Sandler, Challenger, Sell the Dream, SQL to Qualify, Qualify to POC |
| Discovery | Persona based discovery |
| POC / pilot | POC success, Deal category: POC/Pilot |
| Deal-category pipeline sweeps | Deal category: Evaluation, Deal category: Prospect, Deal category: Negotiation, Deal category: Qualify, Deal category: Won |
| Deal registration | Deal registration, Deal registration (End Clients) |

The five deal-category entries are a different shape from the rest — a
CRM-export sweep against deals sitting in that pipeline stage, not a
call-audit. Confirm the existing spreadsheet-input path covers them rather
than forcing them into the call-transcript template.

### Already built, for reference (13 of 31 real initiatives)

MEDDICC, Technical discovery, Deep discovery, Customer success, Improve Demo,
Churn Prevention, Pilot to conversion, Upsell & Expansion, Meeting to qualify,
BANT, Onboarding Journey, First call rampup, Negotiation & Closing.

---

## Phase 0 — Fix what's already there (blocking)

No new skills. Nothing else starts until this is done, because it's the one
pass that touches every existing skill.

1. Correct the skill count and the vertical-adaptive claims in `README.md`,
   `EVALS.md`, `MAINTAINING.md` so they match what's actually implemented.
2. Write one shared paragraph for "how a skill loads industry context," add it
   everywhere it should apply, add the matching metadata flag. The matrix then
   reflects reality instead of intent.
3. Build the company-profile skill (`skills/revenue-context/`), same loading
   pattern as the industry packs.
4. Write the missing trigger-test file (`evals/trigger-set.json`) — short
   prompts checking the right skill fires, weighted toward near-misses (several
   skills already sound like "review this call").
5. Run both existing automated checks (format compliance, and the trigger test)
   across all 17 skills for the first time. Record the results.
6. Run the spreadsheet-input path once, on one skill, and fix what breaks.
7. Extend `validate-skills.sh` to catch what it currently misses: broken file
   references inside a skill's test file, a missing rubric file, a missing
   synthetic-data disclaimer on sample transcripts.

**Done when:** the validator passes with zero errors, both checks have real
recorded numbers, and every claim in the docs matches something that actually
exists in the repo.

## Phase 1 — Prove the new category (2 skills)

Build `call-prep` and `sales-to-cs-handover`. Deliberately the widest spread in
the roster — one reads several past calls and prepares the next one, one reads
a whole won deal and writes across a team boundary. If one format survives
both, it survives the other twelve.

Write up the settled format as a template — output shape, how evidence gets
cited in prose instead of a table, how multiple calls as input get declared, how
the company-profile and industry-pack context load. Every later skill in this
category follows it exactly.

**Done when:** both skills run end to end on made-up input, a person reads both
outputs and would actually send them, and the template is written down
somewhere the next batch can follow without re-deciding it.

## Phase 2 — Fill out the remaining frameworks (17 skills)

Highest volume, lowest risk — this format is already proven across 13 existing
skills. Build the 17 real, unbuilt initiatives listed above against that same
template. No dedup needed — confirmed against the real list, not guessed.

The five deal-category entries (Evaluation, Prospect, Negotiation, Qualify,
Won) are a different shape: a spreadsheet sweep against deals sitting in that
pipeline stage, not a call-audit. Confirm the spreadsheet-input path from
Phase 0 covers them before forcing them into the call template.

**The line we don't cross:** a framework's own public terminology (MEDDICC's
own letters, BANT's own words) is fine to use. Copying our internal
call-checklist question text is not — every new skill gets checked for this
before it merges. Initiative *names* themselves (Sandler, Challenger, and the
rest) are fine to use verbatim; they're the framework's own name.

**Done when:** validator passes, both automated checks run clean, and a person
has read a sample of the batch.

## Phase 3 — Finish the new category (19 skills)

The rest of the roster above, against the Phase 1 template. Includes the
cross-deal, global group (prep notes and deal AMA global agents) — a third
shape worth confirming here: not single-call, not single-deal, but reading
across a whole book of business. The proposed skills each need an explicit
accept-or-cut decision before they're built, not after. A few need the
spreadsheet-input path tested in Phase 0 — they work better against a full deal
list than a single call.

**Done when:** same gate as Phase 2, sample of the batch, every proposed skill
has a recorded decision.

## Phase 4 — Deepen two industries (0 new skills)

1. Remove the started fintech pack and every reference to it.
2. Grow the cybersecurity and healthcare packs from a rough first draft to
   something someone who actually sells into those industries has reviewed.
3. Run the same call through a skill twice — generic, then with the industry
   named — and confirm the output actually reads differently. If it doesn't,
   the pack is decoration.
4. Get 1-2 real (or realistic, human-reviewed) example calls per industry,
   graded by someone who didn't write the skill's rubric — the only number that
   proves the skill finds what a person would find, not just that it's
   formatted correctly.

## Phase 5 — Launch

1. Add one-line install options alongside the current clone-and-copy path.
2. Set repo topics and description around what the skills actually do
   (revenue operations, sales enablement, call intelligence) — not generic
   growth-hacking terms that bring the wrong audience.
3. Launch channels, roughly in order of expected return:
   - Our own site — the one channel where the audience is already looking for
     this. Link it from a resources page, not a footer, and track that link on
     its own.
   - RevOps and sales communities (Slack groups, relevant subreddits).
   - A public "show and tell" post framed on what the skills find, not the
     tooling.
   - Sales/RevOps-focused newsletters — not general developer or
     growth-marketing lists.
   - Product listing sites, framed as a working toolkit.
4. Track click-through from the repo to us as its own number from day one.
   Stars measure developer interest only — don't let that number stand in for
   the one that actually matters.
5. Link both directions: the repo points at our site, our site points at the
   repo.

---

## Open, not solved

**Live CRM connection (Salesforce, HubSpot).** Several skills would be
materially better with live deal data instead of a pasted call or exported
file. Real, and on the roadmap — not solved in this plan. The constraint
whoever picks it up should hold: every skill keeps working with zero
credentials, on a pasted transcript or exported file. A live connection is
always optional, never required, and the repo never stores a login. This
slightly narrows an existing promise in every skill's instructions ("no CRM
connection" becomes "no credentials required") — a deliberate, small edit, not
a reversal of it.

**Human-graded examples.** Phase 4 needs 1-2 calls per industry graded by
someone who didn't write that skill's rubric. Until that exists, every skill
reports "follows the right format" only, and says so plainly rather than
implying it's been checked for accuracy.

---

## Standing rules

- Sample data is always made up or fully anonymized, and says so on its face.
- Every finding a skill reports in call-review mode has to point to an exact
  quote — no exceptions.
- Repo creation and any public push stay with the maintainer.
- No AI-tool attribution in commit history.
