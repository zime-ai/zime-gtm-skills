# zime-gtm-skills

Open-source [Agent Skills](https://agentskills.io) that audit sales call
transcripts and CRM exports against GTM rubrics, along three axes: **deal
stage** (discovery through renewal), **initiative** (MEDDICC, BANT, pain
identification, and more — qualification frameworks that run at any stage),
and **vertical** (industry context packs that specialize any skill's output
for cybersecurity, healthcare, or fintech). Runs locally, no credentials, no
data leaves your machine. Works with Claude Code, Cursor, Windsurf, OpenAI
Codex, or any agent that supports the Agent Skills spec.

Built for RevOps engineers and sales engineers who want a structured second
opinion on call quality without wiring a live CRM connection into a
third-party tool. Standalone and community-maintained — no gating, no
product coupling, no lead capture. Built and maintained by
[Zime](https://zime.ai).

**Contributions welcome** — see [CONTRIBUTING.md](CONTRIBUTING.md). Found a
bug or have a question? [Open an issue](https://github.com/zime-ai/zime-gtm-skills/issues).


## Quick start

```bash
git clone https://github.com/zime-ai/zime-gtm-skills.git
cd zime-gtm-skills
claude "run deep-discovery on skills/deep-discovery/assets/sample-transcript.txt"
```

That's a synthetic call bundled with the repo — nothing of yours required
to see real output. Expect a per-dimension audit like:

```
1. Pain & business impact — Covered
   "our lead dispatcher... spends probably 8-10 hours a week just
   chasing down exception statuses" (00:48)

2. Trigger — why now — Covered
   "we lost a mid-size account last quarter over a missed exception,
   and our board asked for a logistics-ops review this quarter" (01:30)

7. Procurement & buying path — Covered
   "anything touching our TMS goes through a security review with
   our IT director... about three weeks" (04:28)

Next steps:
- Confirm the $40k CFO threshold in writing before scoping a proposal
- Get the competing vendor's name — "felt built for a bigger company"
  is a usable wedge, worth understanding further
```

## How these fit together

Eleven skills, one per GTM motion, laid out across the deal lifecycle:

```
New business
────────────
deep-discovery → meeting-to-qualify → technical-discovery
    → improve-demo → pilot-to-conversion → negotiation-closing

    first-call-rampup   (coaching, any stage of a new rep's calls)

Post-sale
─────────
onboarding-journey → customer-success

    churn-prevention    (renewal risk)
    upsell-expansion    (expansion opportunity)
```

Unlike some agent-skill collections, there's no foundational context skill
every other one depends on, and no required order. Each skill is independent:
one call transcript (or CRM export) in, one evidence-cited audit out.

## Coverage: three dimensions, not one

**Stage** and **initiative** are both skills — a flat set, no nesting.
**Vertical** is different: it's shared context any stage or initiative skill
can load (`skills/vertical-context/`), rather than a separate skill per
industry. That keeps the cost additive (skills + verticals) instead of
multiplicative (skills × verticals).

| | Stage | Initiative | Vertical-aware |
|---|---|---|---|
| `deep-discovery` | Discovery | — | ✅ |
| `meeting-to-qualify` | Qualify | — | ✅ |
| `technical-discovery` | Technical discovery | — | ✅ |
| `improve-demo` | Demo | — | ✅ |
| `pilot-to-conversion` | Pilot | — | ✅ |
| `negotiation-closing` | Negotiation | — | ✅ |
| `first-call-rampup` | Any (coaching) | — | — |
| `onboarding-journey` | Onboarding | — | ✅ |
| `customer-success` | Post-sale review | — | ✅ |
| `churn-prevention` | Renewal risk | — | ✅ |
| `upsell-expansion` | Expansion | — | ✅ |
| `meddicc` | Any | MEDDICC | ✅ |
| `bant` | Any (early) | BANT | ✅ |
| `pain-finder` | Any | Identify pain | ✅ |
| `next-step-commitment` | Any | Next step commitment | — |

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

All 11 stage motions are covered; initiative coverage is a 4-skill proof set
(15 of 31 Zime initiatives total, once the 11 stage skills are counted — see
the coverage table above). New skills beyond these are welcome — see
[CONTRIBUTING.md](CONTRIBUTING.md). For how these are tested, and what that
testing can and can't prove, see [EVALS.md](EVALS.md).

## Installation

### Option 1: Clone and copy

```bash
git clone https://github.com/zime-ai/zime-gtm-skills.git
cp -r zime-gtm-skills/skills/* .agents/skills/
```

Or copy just the one skill you want: `cp -r zime-gtm-skills/skills/deep-discovery .agents/skills/`.

> [!TIP]
> Claude Code reads `.claude/skills/`, not `.agents/skills/`. If you're
> installing for Claude Code specifically, copy there instead (or symlink
> one to the other).

### Option 2: Git submodule

```bash
git submodule add https://github.com/zime-ai/zime-gtm-skills.git .agents/zime-gtm-skills
```

Update later with `git submodule update --remote`.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. Every skill reads the file you point it at and nothing
else. There's no npx installer or plugin marketplace listing (yet) — clone
or submodule for now.

## License

MIT — see [LICENSE](LICENSE).

Maintained by [Zime](https://zime.ai).
