# zime-gtm-skills

[![Skills](https://img.shields.io/badge/skills-16-blue)](skills/)
[![validate](https://github.com/zime-ai/zime-gtm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/zime-ai/zime-gtm-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE)
[![Agent Skills spec](https://img.shields.io/badge/spec-agentskills.io-informational)](https://agentskills.io)
[![Zime](https://img.shields.io/badge/by-zime.ai-000000)](https://zime.ai)

If you're building call-review or deal-inspection tooling in-house, start
here. 16 [Agent Skills](https://agentskills.io) that audit sales call
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

Run it yourself:

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

16 skills: 11 stage motions laid out across the deal lifecycle and 5
cross-stage initiative skills.

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 65, "rankSpacing": 90, "padding": 20}, "themeVariables": {"fontSize": "20px"}}}%%
flowchart LR
    subgraph nb["New business"]
        direction LR
        dd[deep-discovery] --> mq[meeting-to-qualify]
        mq --> td[technical-discovery]
        td --> id[improve-demo]
        id --> pc[pilot-to-conversion]
        pc --> nc[negotiation-closing]
    end
    subgraph ps["Post-sale"]
        direction LR
        oj[onboarding-journey] --> cs[customer-success]
    end
    nb --> ps
    fcr["first-call-rampup, coaching at any stage"]
    cp["churn-prevention, renewal risk"]
    ue["upsell-expansion, expansion opportunity"]
    ps -.-> cp
    ps -.-> ue
```

Unlike some agent-skill collections, there's no foundational context skill
every other one depends on, and no required order. Each skill is independent:
one call transcript (or CRM export) in, one evidence-cited audit out.

## Coverage: two dimensions, not one

**Stage** and **initiative** are both skills: a flat set, no nesting.

| | Stage | Initiative |
|---|---|---|
| `deep-discovery` | Discovery | n/a |
| `meeting-to-qualify` | Qualify | n/a |
| `technical-discovery` | Technical discovery | n/a |
| `improve-demo` | Demo | n/a |
| `pilot-to-conversion` | Pilot | n/a |
| `negotiation-closing` | Negotiation | n/a |
| `first-call-rampup` | Any (coaching) | n/a |
| `onboarding-journey` | Onboarding | n/a |
| `customer-success` | Post-sale review | n/a |
| `churn-prevention` | Renewal risk | n/a |
| `upsell-expansion` | Expansion | n/a |
| `meddicc` | Any | MEDDICC |
| `bant` | Any (early) | BANT |
| `pain-finder` | Any | Identify pain |
| `next-step-commitment` | Any | Next step commitment |
| `adoption-leaderboard` | Any (post-sale) | Behavior adoption |

**Roadmap.** The named methodologies (MEDDPICC, FAINT, Sandler, Challenger,
Sell the Dream, and others) aren't built yet. See `MAINTAINING.md`'s
deferred work, or [contribute one](CONTRIBUTING.md).

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
<summary>16 skills across new business, post-sale, and cross-stage initiative</summary>

<!-- SKILLS:START -->
**New business**

| Skill | Audits | Input |
|---|---|---|
| [deep-discovery](skills/deep-discovery/) | Early-stage discovery call quality — pain, trigger, decision process, budget/timeline, procurement, competition, rapport | transcript (`.txt`/`.vtt`/`.json`/`.md`) or CRM export (`.csv`) |
| [meeting-to-qualify](skills/meeting-to-qualify/) | Whether a deal is real — authority, budget plausibility, urgency, fit, competitive situation, concrete next step | transcript or CRM export |
| [technical-discovery](skills/technical-discovery/) | Whether a POC is set up to succeed — current stack, future-state fit, scope clarity, technical stakeholders, resourcing | transcript or CRM export |
| [improve-demo](skills/improve-demo/) | Demo quality — tailoring, stakeholder presence, engagement, competitive differentiation, clear next step | transcript or CRM export |
| [pilot-to-conversion](skills/pilot-to-conversion/) | Pilot/POC health — plan alignment, technical readiness, user engagement, results against criteria, conversion path | transcript or CRM export |
| [negotiation-closing](skills/negotiation-closing/) | Late-stage deal momentum — pricing reaction, procurement progress, contracting awareness, closure timeline | transcript or CRM export |
| [first-call-rampup](skills/first-call-rampup/) | New-rep foundational technique — opening, open-ended questioning, pain uncovering, pitch clarity, rapport | transcript only |

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
| [bant](skills/bant/) | BANT coverage — Budget, Authority, Need, Timeline — lighter-weight, early-stage qualification | transcript or CRM export |
| [pain-finder](skills/pain-finder/) | Ranked pain points with confidence and evidence | transcript |
| [next-step-commitment](skills/next-step-commitment/) | Whether a call ended in a real, dated, two-sided commitment vs. a vague "we'll circle back" | transcript or CRM export |
| [adoption-leaderboard](skills/adoption-leaderboard/) | Ranks reps by adoption of five fixed winning behaviors (rapport, upsell signals, renewal risk, customer experience, value realization) across recent calls, lowest first | transcript or connector |
<!-- SKILLS:END -->

</details>

All 11 stage motions are covered; the initiative set is five skills today.
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
