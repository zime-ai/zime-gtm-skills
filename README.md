# zime-gtm-skills

[![Skills](https://img.shields.io/badge/skills-16-blue)](skills/)
[![validate](https://github.com/zime-ai/zime-gtm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/zime-ai/zime-gtm-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE)
[![Agent Skills spec](https://img.shields.io/badge/spec-agentskills.io-informational)](https://agentskills.io)

Open-source [Agent Skills](https://agentskills.io) that audit sales call
transcripts and CRM exports against GTM rubrics, along three axes: **deal
stage** (discovery through renewal), **initiative** (MEDDICC, BANT, pain
identification, and more — qualification frameworks that run at any stage),
and **vertical** (industry context packs that specialize any skill's output
for cybersecurity, healthcare, or fintech). Runs locally, no credentials, no
data leaves your machine. Works with Claude Code, Cursor, Windsurf, OpenAI
Codex, or any agent that supports the Agent Skills spec.

The rule every skill here is built on: **an uncited finding doesn't ship.**
Every dimension a skill marks Covered, Partial, or Missed points at a direct
quote or timestamp from the transcript in front of it — never a plausible
guess dressed up as a finding.

Built for RevOps engineers and sales engineers who want a structured second
opinion on call quality without wiring a live CRM connection into a
third-party tool. Standalone and community-maintained — no gating, no
product coupling, no lead capture. Built and maintained by
[Zime](https://zime.ai).

**Contributions welcome** — see [CONTRIBUTING.md](CONTRIBUTING.md). Found a
bug or have a question? [Open an issue](https://github.com/zime-ai/zime-gtm-skills/issues).

## See it work

Same synthetic call, same model, two ways: a plain "review this call"
prompt with no skill, and `deep-discovery` against
`skills/deep-discovery/assets/sample-transcript.txt`.

<details>
<summary><b>Without the skill</b> — unaided, prompted "review this discovery call"</summary>

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

Same nine dimensions, every run — a rep gets the same read whoever's on
the call, and every Missed or Partial is falsifiable against the transcript
next to it.
</details>

Run it yourself — nothing of your own required:

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

16 skills: 11 stage motions laid out across the deal lifecycle, 4 cross-stage
initiative skills, and 1 shared vertical-context pack loaded by the others.

```mermaid
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
    fcr["first-call-rampup — coaching, any stage"]
    cp["churn-prevention — renewal risk"]
    ue["upsell-expansion — expansion opportunity"]
    ps -.-> cp
    ps -.-> ue
```

Unlike some agent-skill collections, there's no foundational context skill
every other one depends on, and no required order. Each skill is independent:
one call transcript (or CRM export) in, one evidence-cited audit out.

## Why 16 skills, not 200+

Other GTM skill repos compete on breadth — hundreds of skills spanning
outbound, ABM, paid ads, tooling setup. This one stays inside one bounded
domain (auditing calls and deal data against rubrics) and spends the effort
there instead: an evidence-citation rule enforced in every skill, a vertical
overlay instead of a skill-per-industry multiplication, and an
[eval methodology](EVALS.md) that reports format compliance and insight
recall as two separate numbers on purpose, because blending them is how a
skill's benchmark ends up proving less than it claims. Depth in a bounded
domain over breadth across every GTM motion.

## Coverage: three dimensions, not one

**Stage** and **initiative** are both skills — a flat set, no nesting.
**Vertical** is different: it's shared context any stage or initiative skill
can load (`skills/vertical-context/`), rather than a separate skill per
industry. That keeps the cost additive (skills + verticals) instead of
multiplicative (skills × verticals).

| | Stage | Initiative | Vertical-aware |
|---|---|---|---|
| `deep-discovery` | Discovery | — | — |
| `meeting-to-qualify` | Qualify | — | — |
| `technical-discovery` | Technical discovery | — | — |
| `improve-demo` | Demo | — | — |
| `pilot-to-conversion` | Pilot | — | — |
| `negotiation-closing` | Negotiation | — | — |
| `first-call-rampup` | Any (coaching) | — | — |
| `onboarding-journey` | Onboarding | — | — |
| `customer-success` | Post-sale review | — | — |
| `churn-prevention` | Renewal risk | — | — |
| `upsell-expansion` | Expansion | — | — |
| `meddicc` | Any | MEDDICC | ✅ |
| `bant` | Any (early) | BANT | ✅ |
| `pain-finder` | Any | Identify pain | ✅ |
| `next-step-commitment` | Any | Next step commitment | — |

Vertical-aware today: 3 skills (`meddicc`, `bant`, `pain-finder`). Extending
the overlay to the 11 stage skills is tracked in `MAINTAINING.md` — not done
yet, stated plainly rather than implied.

Vertical packs available today: **cybersecurity, healthcare, fintech** —
see `skills/vertical-context/`. Unreviewed against a domain expert; see that
skill's status note.

**Known gap, stated plainly:** Zime's internal taxonomy tracks 31
initiatives. The 11 stage skills above double as initiative coverage (each
is named after and scoped to one), plus these 4 cross-stage initiative
skills — 15 of 31 covered. The other 16, mostly named methodologies
(MEDDPICC, FAINT, Sandler, Challenger, Sell the Dream, and others), aren't
built yet — see `MAINTAINING.md`'s deferred work.

## Available skills

<details open>
<summary>16 skills across new business, post-sale, cross-stage initiative, and vertical context</summary>

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
| [pain-finder](skills/pain-finder/) | Ranked pain points with confidence and evidence, optionally specialized by vertical | transcript |
| [next-step-commitment](skills/next-step-commitment/) | Whether a call ended in a real, dated, two-sided commitment vs. a vague "we'll circle back" | transcript or CRM export |

**Vertical context (not run directly — loaded by other skills)**

| Skill | Provides | Verticals |
|---|---|---|
| [vertical-context](skills/vertical-context/) | Buyer titles, compliance drivers, domain vocabulary, specialized pain taxonomy | cybersecurity, healthcare, fintech |
<!-- SKILLS:END -->

</details>

All 11 stage motions are covered; initiative coverage is a 4-skill proof set
(15 of 31 Zime initiatives total, once the 11 stage skills are counted — see
the coverage table above). New skills beyond these are welcome — see
[CONTRIBUTING.md](CONTRIBUTING.md). For how these are tested, and what that
testing can and can't prove, see [EVALS.md](EVALS.md).

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
> Claude Code reads `.claude/skills/`, not `.agents/skills/`. If you're
> installing for Claude Code specifically outside the plugin flow above,
> copy there instead (or symlink one to the other).

### Option 3: Git submodule

```bash
git submodule add https://github.com/zime-ai/zime-gtm-skills.git .agents/zime-gtm-skills
```

Update later with `git submodule update --remote`.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. Every skill reads the file you point it at and nothing
else.

## License

MIT — see [LICENSE](LICENSE).

Maintained by [Zime](https://zime.ai).
