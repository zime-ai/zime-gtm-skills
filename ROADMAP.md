# Roadmap

What's shipped and what's next, organized the way the playbook already
tracks GTM motions. Distribution/go-to-market planning is deliberately not
here — see `MAINTAINING.md` for process, not promotion.

`scripts/check-docs-sync.sh`'s `roadmap-in-sync` rule keeps this file honest:
every `skills/<name>/` directory must have a matching `- [x] <name>` line
below, and no checked line may name a directory that doesn't exist. When you
land a skill, check its box in the same PR — don't leave that for later.

`sell-the-dream` has no canonical single-source framework behind the name
(unlike meddicc/bant/faint) — needs scoping before it's buildable, pulled
from the batch that shipped the other two qualification gaps below.

## Phase 1 — Initiative & stage skills

Every framework and deal motion the playbook tracks today.

**Qualification**
- [x] meddicc
- [x] bant
- [x] meddpicc
- [x] faint
- [x] sandler
- [x] challenger
- [ ] sell-the-dream
- [x] sql-to-qualify
- [x] qualify-to-poc

**Discovery**
- [x] deep-discovery
- [x] technical-discovery
- [x] meeting-to-qualify
- [x] persona-based-discovery

**Demo**
- [x] improve-demo

**POC & pilot**
- [x] pilot-to-conversion
- [ ] poc-success

**Negotiation & closing**
- [x] negotiation-closing

**Deal-stage pipeline checks** (work from an exported deal list, not a single call)
- [x] evaluation-pipeline-check
- [x] prospect-pipeline-check
- [x] qualify-pipeline-check
- [x] negotiation-pipeline-check
- [x] poc-pilot-pipeline-check
- [x] won-pipeline-check

**Deal registration**
- [ ] new-business-registration
- [ ] end-client-registration

**Post-sale**
- [x] onboarding-journey
- [x] customer-success
- [x] churn-prevention
- [x] upsell-expansion

**Rep enablement**
- [x] first-call-rampup

**Not tied to one stage**
- [x] pain-finder
- [x] next-step-commitment
- [x] adoption-leaderboard

## Phase 2 — Deal intelligence skills

A different class from phase 1: instead of grading a call against a rubric,
these write something forward — prep notes, a report, a handoff — from one
call, one deal, or a whole book of business. Every skill in this group works
standalone; CRM connector access is optional and used only when already
there.

**Seller-facing, single deal**
- [ ] call-prep
- [ ] deal-highlights
- [ ] mutual-action-plan
- [ ] executive-briefing
- [ ] champion-tracker
- [ ] competitor-battlecard
- [ ] follow-up-email-drafter

**Manager & leader rituals**
- [ ] wbr-report-generator
- [ ] forecast-review
- [ ] pipeline-review
- [ ] deal-risk-digest
- [ ] win-loss-brief
- [ ] stuck-deal-digest
- [ ] rep-ramp-status-digest

**Cross-deal, global** (read across a whole book of business, not one call)
- [ ] prep-notes-global-agent
- [ ] deal-ama-global-agent
- [ ] objection-pattern-digest
- [ ] competitive-loss-digest

**Handoffs**
- [ ] handover-to-customer-success
- [ ] renewal-prep
- [ ] coaching-plan

## Phase 3 — Vertical packs

The skills above don't change; a vertical pack is buyer titles, compliance
drivers, and vocabulary that any skill can load on request. One pack, once
written well, works across every skill that loads it. Both need a review by
someone who actually sells into that industry before either is called done.

- [ ] cybersecurity pack
- [ ] healthcare pack

## Phase 4 — Other GTM skills

Motions already tracked but not yet built, plus general GTM practice adapted
from how other public skill collections cover this ground — so the repo has
something for every GTM function, not sales calls alone. A starting list,
worth a second look before any of it gets built.

**Partner & channel**
- [ ] channel-partner-engagement
- [ ] partner-potential
- [ ] partner-sentiment
- [ ] ideal-channel-partner-profile
- [ ] partner-decision-authority
- [ ] partner-competition-landscape
- [ ] partner-pain-points
- [ ] partner-business-review

**Pricing & deal desk**
- [ ] deal-desk-approval-brief
- [ ] discount-pattern-digest

**Account & territory**
- [ ] account-plan-generator
- [ ] territory-summary

**Customer proof**
- [ ] reference-case-study-drafter
- [ ] client-testimonial-finder

**General GTM practice**
- [ ] prospecting-sequence-builder
- [ ] cold-outreach-drafter
- [ ] competitor-teardown
- [ ] customer-research-synthesis
- [ ] revops-process-audit
- [ ] referral-program-builder
- [ ] win-back-offer-generator
- [ ] sales-enablement-library-audit

**Marketing & content**
- [ ] seo-audit
- [ ] content-strategy
- [ ] cold-email-sequences
- [ ] ad-copy-generator
- [ ] social-content-drafter
- [ ] landing-page-copy
- [ ] email-newsletter-drafter
- [ ] launch-announcement-writer
