# zime-gtm-skills

[![Skills](https://img.shields.io/badge/skills-41-blue)](skills/)
[![validate](https://github.com/zime-ai/zime-gtm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/zime-ai/zime-gtm-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE)
[![Agent Skills spec](https://img.shields.io/badge/spec-agentskills.io-informational)](https://agentskills.io)
[![Zime](https://img.shields.io/badge/by-zime.ai-000000)](https://zime.ai)

If you're building call-review or deal-inspection tooling in-house, start
here. 41 [Agent Skills](https://agentskills.io) that audit sales call
transcripts and CRM exports against GTM rubrics: one file in, one
evidence-cited audit out. Runs locally, no credentials, no data leaves your
machine. Works with Claude Code, Cursor, Windsurf, OpenAI Codex, or any agent
that reads the Agent Skills spec.

Two axes: **deal stage** (discovery through renewal) and **initiative**
(MEDDICC, BANT, pain identification: frameworks that run at any stage).

The rule every skill here is built on: **an uncited finding doesn't ship.**
Every dimension a skill marks Covered, Partial, or Missed points at a direct
quote or timestamp from the transcript in front of it, never a plausible
guess dressed up as a finding.

MIT, no gating, no telemetry, no lead capture. Fork it, rewrite the rubrics
for your motion, ship it internally: that's the intended use. Built and
maintained by [Zime](https://zime.ai); we'd rather hand over the rubrics than
argue anyone out of building.

**Contributions welcome**: see [CONTRIBUTING.md](CONTRIBUTING.md). Found a
bug or have a question? [Open an issue](https://github.com/zime-ai/zime-gtm-skills/issues).

- [See it work](#see-it-work)
- [Quick install](#quick-install)
- [How these fit together](#how-these-fit-together)
- [Coverage: two dimensions, not one](#coverage-two-dimensions-not-one)
- [Where this stops](#where-this-stops)
- [Available skills](#available-skills)
- [Repository structure](#repository-structure)
- [FAQ](#faq)
- [Installation](#installation)
- [Built by Zime](#built-by-zime)
- [License](#license)

## See it work

Same synthetic call, same model, two ways: a plain "review this call"
prompt with no skill, and `deep-discovery` against
`skills/deep-discovery/assets/sample-transcript.txt`.

<details>
<summary><b>Without the skill</b>: unaided, prompted "review this discovery call"</summary>

```
Discovery call feedback — Northwind x Vendor Co:

Strong:
- Quantified pain: 8-10 hrs/week dispatcher time chasing exceptions.
- Got compelling event: lost account last quarter + board-mandated
  ops review this quarter.
- Got economic buyer + threshold: CFO approves anything over $40k/year.

Gaps:
1. No next step. Call ends on rapport with zero concrete action.
2. Budget not probed directly — got the approval threshold, not the
   actual budget range.
3. Timeline vague — "before Q3 planning" never pinned to a date.
```

No structure that repeats across calls, no consistent evidence format,
findings and gaps interleaved with commentary.
</details>

<details open>
<summary><b>With <code>deep-discovery</code></b></summary>

```
1. Pain & business impact — Covered
   "spends probably 8-10 hours a week just chasing down exception
   statuses"

2. Current state & tooling — Covered
   "Dispatchers log exceptions in a shared spreadsheet"

3. Trigger — why now — Covered
   "we lost a mid-size account last quarter over a missed exception,
   and our board asked for a logistics-ops review this quarter"

[... 4. Desired outcome, 5. Decision process — both Covered, trimmed ...]

6. Budget & timeline — Partial
   CFO approval threshold ($40k) surfaced, but that's an approval
   gate, not deal-specific budget. No explicit decision-date beyond
   "before Q3 planning."

7. Procurement & buying path — Covered
   "anything touching our TMS goes through a security review with
   our IT director. Usually takes about three weeks"

[... 8. Competitive landscape, 9. Rapport — both Covered, trimmed ...]

Reads-well-too check: 8/9 Covered, 1 Partial, zero Missed — matches a
call that clearly covered discovery well. No fault-finding bias here.

Highest-leverage next steps:
1. Nail a real budget number, not just the approval gate.
2. Pin a hard decision date, not "before Q3 planning."
```

Same nine dimensions, every run: a rep gets the same read whoever's on
the call, and every Missed or Partial is falsifiable against the transcript
next to it.
</details>

Run it yourself, nothing of your own required:

```bash
git clone https://github.com/zime-ai/zime-gtm-skills.git
cd zime-gtm-skills
claude "run deep-discovery on skills/deep-discovery/assets/sample-transcript.txt"
```

## Quick install

```bash
# Claude Code plugin (recommended)
/plugin marketplace add zime-ai/zime-gtm-skills
/plugin install gtm-skills@zime-gtm-skills
```

```bash
# or clone and copy into any agent that reads the Agent Skills format
git clone https://github.com/zime-ai/zime-gtm-skills.git
cp -r zime-gtm-skills/skills/* .agents/skills/
```

See [Installation](#installation) below for the submodule option and the
`.claude/skills/` vs `.agents/skills/` distinction.

## How these fit together

41 skills: 23 stage motions laid out across the deal lifecycle, 10
cross-stage initiative skills, and 8 deal-intelligence skills that write
something forward — a plan, a digest, a drafted email — instead of grading
a call.

```
New business

┌────────────────┐     ┌────────────────┐     ┌────────────────────┐
│ sql-to-qualify │ ──▶ │ deep-discovery │ ──▶ │ meeting-to-qualify │
└────────────────┘     └────────────────┘     └────────────────────┘
                                                         │
                                                         ▼
┌─────────────────────┐     ┌──────────────┐     ┌────────────────┐
│ technical-discovery │ ◀── │ improve-demo │ ◀── │ qualify-to-poc │
└─────────────────────┘     └──────────────┘     └────────────────┘
           │
           ▼
┌─────────────────────┐     ┌─────────────┐     ┌─────────────────────┐
│ pilot-to-conversion │ ──▶ │ poc-success │ ──▶ │ negotiation-closing │
└─────────────────────┘     └─────────────┘     └─────────────────────┘
                                                           │
                                                           ▼

                                                     Post-sale

                                                ┌────────────────────┐     ┌──────────────────┐
                                                │ onboarding-journey │ ──▶ │ customer-success │
                                                └────────────────────┘     └──────────────────┘

Runs alongside, not in the chain:
  • persona-based-discovery — persona-adapted lens on discovery
  • first-call-rampup       — coaching, at any stage
  • churn-prevention        — renewal risk, post-sale
  • upsell-expansion        — expansion opportunity, post-sale
```

Unlike some agent-skill collections, there's no foundational context skill
every other one depends on, and no required order. Each skill is independent:
one call transcript (or CRM export) in, one evidence-cited audit out.

## Coverage: two dimensions, not one

**Stage** and **initiative** are both skills: a flat set, no nesting.

| | Stage | Initiative |
|---|---|---|
| `new-business-registration` | Registration | n/a |
| `end-client-registration` | Registration | n/a |
| `sql-to-qualify` | SQL to qualify | n/a |
| `deep-discovery` | Discovery | n/a |
| `persona-based-discovery` | Discovery | n/a |
| `meeting-to-qualify` | Qualify | n/a |
| `technical-discovery` | Technical discovery | n/a |
| `improve-demo` | Demo | n/a |
| `qualify-to-poc` | Qualify to POC | n/a |
| `pilot-to-conversion` | Pilot | n/a |
| `poc-success` | POC/pilot exit | n/a |
| `negotiation-closing` | Negotiation | n/a |
| `prospect-pipeline-check` | Prospect pipeline | n/a |
| `qualify-pipeline-check` | Qualify pipeline | n/a |
| `evaluation-pipeline-check` | Evaluation pipeline | n/a |
| `poc-pilot-pipeline-check` | POC/pilot pipeline | n/a |
| `negotiation-pipeline-check` | Negotiation pipeline | n/a |
| `won-pipeline-check` | Won pipeline | n/a |
| `first-call-rampup` | Any (coaching) | n/a |
| `onboarding-journey` | Onboarding | n/a |
| `customer-success` | Post-sale review | n/a |
| `churn-prevention` | Renewal risk | n/a |
| `upsell-expansion` | Expansion | n/a |
| `meddicc` | Any | MEDDICC |
| `meddpicc` | Any | MEDDPICC |
| `faint` | Any (early) | FAINT |
| `sandler` | Any | Sandler Submarine |
| `challenger` | Any | Challenger Sale |
| `bant` | Any (early) | BANT |
| `pain-finder` | Any | Identify pain |
| `next-step-commitment` | Any | Next step commitment |
| `adoption-leaderboard` | Any (post-sale) | Behavior adoption |
| `sell-the-dream` | Any | Vision selling |

**A third class, not in this table: deal intelligence.** The 8
`mutual-action-plan`/`deal-risk-digest`/`deal-highlights`/
`follow-up-email-drafter`/`win-loss-brief`/`executive-briefing`/
`champion-tracker`/`competitor-battlecard` skills don't grade a call
against a rubric — they write something forward, so a Stage/Initiative
pair doesn't fit them. See the "Deal intelligence" group in
[Available skills](#available-skills) instead.

**Roadmap.** Other named methodologies and motions aren't built yet.
See [ROADMAP.md](ROADMAP.md), or
[contribute one](CONTRIBUTING.md).

## Where this stops

Everything here runs on one file, in one session, with no memory. That's a
design ceiling, and it's worth knowing before you build on it:

- **One call at a time.** You point a skill at a transcript. Auditing every
  call an org makes, as it happens, is a pipeline problem, not a rubric
  problem.
- **Snapshot, not trend.** Each run is independent. Nothing here tracks the
  same rubric across a rep's quarter, a team, or a pipeline over time.
- **Reads exports, never writes back.** A CRM `.csv` goes in. Nothing updates
  a deal record or feeds a forecast.
- **Rubrics are hand-written, not calibrated.** These dimensions come from
  experience and community correction, not from regression against your own
  won/lost data. A sound default, not a model fit to your motion.
- **No rep or manager surface.** This is an engineer running a command.
  Assignment, coaching loops, adoption tracking are out of scope.

Past that ceiling you're building a platform, not a skill, and that's a much
larger piece of work. It's the problem [Zime](https://zime.ai) works on.

## Available skills

<details open>
<summary>41 skills across new business, post-sale, cross-stage initiative, and deal intelligence</summary>

<!-- SKILLS:START -->
**New business**

| Skill | Audits | Input |
|---|---|---|
| [new-business-registration](skills/new-business-registration/) | A new-logo deal-registration record for completeness — entity identification, duplicate/conflict check, source attribution, ICP fit, expiry window | CRM export (`.csv`) or transcript |
| [end-client-registration](skills/end-client-registration/) | A partner/reseller's end-client deal registration — partner identity, end-client entity kept distinct, engagement scope, conflict check against direct pipeline, permission to engage, commercial terms, expiry | CRM export (`.csv`) or transcript |
| [sql-to-qualify](skills/sql-to-qualify/) | Whether a freshly-assigned SQL is a real opportunity — right contact, pain in their own words, rough budget/urgency fit, competitive awareness, concrete next meeting | transcript or CRM export |
| [deep-discovery](skills/deep-discovery/) | Early-stage discovery call quality — pain, trigger, decision process, budget/timeline, procurement, competition, rapport | transcript (`.txt`/`.vtt`/`.json`/`.md`) or CRM export (`.csv`) |
| [persona-based-discovery](skills/persona-based-discovery/) | Whether a discovery call was actually tailored to the buyer persona in the room — role ID, pain framing, proof points, objection handling, next step | transcript or CRM export |
| [meeting-to-qualify](skills/meeting-to-qualify/) | Whether a deal is real — authority, budget plausibility, urgency, fit, competitive situation, concrete next step | transcript or CRM export |
| [technical-discovery](skills/technical-discovery/) | Whether a POC is set up to succeed — current stack, future-state fit, scope clarity, technical stakeholders, resourcing | transcript or CRM export |
| [improve-demo](skills/improve-demo/) | Demo quality — tailoring, stakeholder presence, engagement, competitive differentiation, clear next step | transcript or CRM export |
| [qualify-to-poc](skills/qualify-to-poc/) | Whether a POC kickoff is set up to succeed before it starts — success criteria, technical scope, stakeholder commitment, timeline/exit criteria, resourcing | transcript or CRM export |
| [pilot-to-conversion](skills/pilot-to-conversion/) | Pilot/POC health — plan alignment, technical readiness, user engagement, results against criteria, conversion path | transcript or CRM export |
| [poc-success](skills/poc-success/) | A completed POC/pilot's exit review — each success criterion verdict-ed with evidence, end-user validation, sponsor sign-off, production-readiness blockers, commercial next step | transcript or CRM export |
| [negotiation-closing](skills/negotiation-closing/) | Late-stage deal momentum — pricing reaction, procurement progress, contracting awareness, closure timeline | transcript or CRM export |
| [first-call-rampup](skills/first-call-rampup/) | New-rep foundational technique — opening, open-ended questioning, pain uncovering, pitch clarity, rapport | transcript only |
| [prospect-pipeline-check](skills/prospect-pipeline-check/) | A prospect-stage pipeline export for deals with no two-way engagement — no reply, no meeting held, single-threaded and unanswered, aged with no activity | CRM export (`.csv`) or connector |
| [qualify-pipeline-check](skills/qualify-pipeline-check/) | A pipeline export for deals advanced past Qualify with no economic buyer, stated pain, budget signal, next step, or a close date that fits the procurement cycle | CRM export (`.csv`) or connector |
| [evaluation-pipeline-check](skills/evaluation-pipeline-check/) | A pipeline export for technical evaluations running with no success criteria, technical champion, or end date — plus evaluations running long or stalled against the export's own norms | CRM export (`.csv`) or connector |
| [poc-pilot-pipeline-check](skills/poc-pilot-pipeline-check/) | A pipeline export for POCs and pilots with no written exit criteria, conversion date, or executive sponsor, and POCs already past their own end date | CRM export (`.csv`) or connector |
| [negotiation-pipeline-check](skills/negotiation-pipeline-check/) | A pipeline export for negotiation-stage deals with no paper process started, no approver on a discount, no named signer, or a close date that has already slipped | CRM export (`.csv`) or connector |
| [won-pipeline-check](skills/won-pipeline-check/) | A closed-won export for missing handoff data — CS owner, kickoff date, signed value/term, contract reference — and won/close date inconsistencies | CRM export (`.csv`) or connector |

**Post-sale**

| Skill | Audits | Input |
|---|---|---|
| [onboarding-journey](skills/onboarding-journey/) | New-customer onboarding health — setup experience, sentiment, engagement, milestone clarity | transcript or CRM export |
| [customer-success](skills/customer-success/) | Periodic QBR/health-review depth — value vs. original goals, usage breadth, issue resolution, strategic alignment | transcript or CRM export |
| [churn-prevention](skills/churn-prevention/) | Renewal risk — value realization, usage depth, champion strength, sentiment, service friction | transcript or CRM export |
| [upsell-expansion](skills/upsell-expansion/) | Expansion readiness — account health check first, opportunity clarity, champion strength, strategic alignment | transcript or CRM export |

**Initiative (cross-stage)**

| Skill | Audits | Input |
|---|---|---|
| [meddicc](skills/meddicc/) | MEDDICC coverage — Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion, Competition | transcript or CRM export |
| [meddpicc](skills/meddpicc/) | MEDDPICC coverage — MEDDICC plus Paper Process: legal/procurement/security review, signature path, redlines | transcript or CRM export |
| [faint](skills/faint/) | FAINT coverage — Funds, Authority, Interest, Need, Timing, for buyers with no articulated need yet | transcript or CRM export |
| [sandler](skills/sandler/) | Sandler Submarine coverage — bonding & rapport, up-front contract, pain, budget, decision, fulfillment, post-sell | transcript or CRM export |
| [challenger](skills/challenger/) | Challenger Sale coverage — teach, tailor, take control, and the commercial-teaching pitch arc | transcript or CRM export |
| [bant](skills/bant/) | BANT coverage — Budget, Authority, Need, Timeline — lighter-weight, early-stage qualification | transcript or CRM export |
| [pain-finder](skills/pain-finder/) | Ranked pain points with confidence and evidence | transcript |
| [next-step-commitment](skills/next-step-commitment/) | Whether a call ended in a real, dated, two-sided commitment vs. a vague "we'll circle back" | transcript or CRM export |
| [adoption-leaderboard](skills/adoption-leaderboard/) | Ranks reps by adoption of five fixed winning behaviors (rapport, upsell signals, renewal risk, customer experience, value realization) across recent calls, lowest first | transcript or connector |
| [sell-the-dream](skills/sell-the-dream/) | Whether a call builds a future-state vision before pitching product, scored against Andy Raskin's "5 Elements of a Great Sales Narrative" and flagged for feature-first sequencing violations | transcript |

**Deal intelligence**

| Skill | Audits | Input |
|---|---|---|
| [mutual-action-plan](skills/mutual-action-plan/) | Writes a mutual action plan from a call — milestones from today to signature, each with an owner on both sides and a date, tagged `heard` or `inferred` | transcript or CRM export |
| [deal-risk-digest](skills/deal-risk-digest/) | Ranks a whole pipeline export by risk — past-due close date against low probability, stage age, vague next step, single-threaded contact | CRM export (`.csv`) |
| [deal-highlights](skills/deal-highlights/) | Writes a short highlights digest of one call — a commitment, an objection, a buying signal, a competitive mention, a risk — each cited with its quote | transcript |
| [follow-up-email-drafter](skills/follow-up-email-drafter/) | Drafts the follow-up email a rep sends after a call, grounded in what was heard vs. proposed, with grounding notes flagging which lines to confirm before sending | transcript |
| [win-loss-brief](skills/win-loss-brief/) | Writes a brief on why one closed deal was won or lost — outcome plus 3-5 cited drivers, each tagged clear or tentative | transcript or CRM export |
| [executive-briefing](skills/executive-briefing/) | Writes the short brief a rep sends upward on one deal — snapshot, status, risk, and the ask — each claim cited to a quote or a CSV column/cell | transcript or CRM export |
| [champion-tracker](skills/champion-tracker/) | Builds a cited action ledger of who's actually acting like a champion across a deal's calls vs. who's just enthusiastic, and reads the trend | transcript |
| [competitor-battlecard](skills/competitor-battlecard/) | Writes a battlecard for the competitor a buyer actually named on a call — their framing, the rep's counter, and what went unanswered, citing only the transcript | transcript |
<!-- SKILLS:END -->

</details>

All 23 stage motions are covered; the initiative set is 10 skills today.
New skills welcome, see [CONTRIBUTING.md](CONTRIBUTING.md). For how these
are tested, and what that testing can and can't prove, see
[EVALS.md](EVALS.md).

## Repository structure

```
zime-gtm-skills/
├── .claude-plugin/
│   ├── marketplace.json       # /plugin marketplace add zime-ai/zime-gtm-skills
│   └── plugin.json
├── skills/
│   └── skill-name/
│       ├── SKILL.md          # required
│       ├── references/       # optional, the rubric lives here
│       ├── assets/           # synthetic sample transcript/CSV
│       └── evals/            # declarative evals.json
├── validate-skills.sh         # local, zero-dep frontmatter/layout check
├── scripts/                    # check-docs-sync.sh, scan-content.py, pr-prep.sh
├── tests/                      # fixture tests for the validators above
├── evals/                       # eval methodology assets, see EVALS.md
├── CONTRIBUTING.md
├── MAINTAINING.md              # process + decisions, for picking this repo back up
├── ROADMAP.md                  # what's built, what's next
├── LICENSE
└── README.md
```

## FAQ

**Do I need an API key or any credentials?** No. Every skill is a markdown
rubric your agent reads and applies to a file you already have. Nothing
here calls out to a service, and nothing you feed a skill leaves your
machine beyond whatever your agent's own model call already sends.

**My agent isn't picking up the skill.** Claude Code reads
`.claude/skills/`, not `.agents/skills/` — if you installed via Option 2 or
3 below for Claude Code specifically, copy (or symlink) into `.claude/skills/`
instead. For other agents, confirm they read the
[Agent Skills spec](https://agentskills.io) format and that the skill
directory is where that agent expects it.

**A skill's output doesn't look right.** If it's the rubric itself — a
missed dimension, a wrong classification — that's the most useful kind of
issue, see [CONTRIBUTING.md](CONTRIBUTING.md#ways-to-help). If it's install
or tooling breaking, [open a bug report](https://github.com/zime-ai/zime-gtm-skills/issues/new/choose).

## Installation

### Option 1: Claude Code plugin

```bash
/plugin marketplace add zime-ai/zime-gtm-skills
/plugin install gtm-skills@zime-gtm-skills
```

### Option 2: Clone and copy

```bash
git clone https://github.com/zime-ai/zime-gtm-skills.git
cp -r zime-gtm-skills/skills/* .agents/skills/
```

Or copy just the one skill you want: `cp -r zime-gtm-skills/skills/deep-discovery .agents/skills/`.

> [!TIP]
> Claude Code reads `.claude/skills/`, not `.agents/skills/` — see the
> [FAQ](#faq) if your agent isn't picking the skill up.

### Option 3: Git submodule

```bash
git submodule add https://github.com/zime-ai/zime-gtm-skills.git .agents/zime-gtm-skills
```

Update later with `git submodule update --remote`.

## Built by Zime

[Zime](https://zime.ai) builds sales-call analytics; this repo is the
rubric layer we'd rather hand over than gatekeep. If it's useful, a star
helps other GTM/RevOps teams find it. Business inquiries: support@zime.ai.

## License

MIT, see [LICENSE](LICENSE).

Maintained by [Zime](https://zime.ai).
