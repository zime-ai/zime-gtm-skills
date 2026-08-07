# Changelog

All notable changes to this repo are documented here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.0] — Initial public release

16 Agent Skills across two axes — deal stage and cross-stage initiative —
each auditing a transcript or CRM export against a GTM rubric with a quote
or timestamp behind every finding.

**Stage** (11): `deep-discovery`, `meeting-to-qualify`, `technical-discovery`,
`improve-demo`, `pilot-to-conversion`, `negotiation-closing`,
`first-call-rampup`, `onboarding-journey`, `customer-success`,
`churn-prevention`, `upsell-expansion`.

**Initiative** (5): `meddicc`, `bant`, `pain-finder`, `next-step-commitment`,
`adoption-leaderboard`.

A third axis, `vertical-context` (industry reference packs for
cybersecurity, healthcare, fintech), was built but held back from this
release pending domain-expert review — see the `vertical-context` branch.

Also ships:
- `validate-skills.sh`, `scripts/check-docs-sync.sh`,
  `scripts/scan-content.py` — zero-dependency local checks, all three run in
  CI on every PR, backed by a fixture test suite (`tests/run-checks-tests.sh`)
  that proves each one actually catches what it claims to.
- A Claude Code plugin (`/plugin marketplace add zime-ai/zime-gtm-skills`),
  alongside clone-and-copy and git-submodule install paths.
- `EVALS.md`'s three-tier eval methodology, and a worked example
  (`evals/runs/2026-07-28-cyber-pain-finder-prior/`) comparing a skill-aided
  run against an unaided one.
- `CONTRIBUTING.md` / `MAINTAINING.md` documenting the full skill-authoring,
  review, and landing process, and the IP boundary on what's fair to draw
  from Zime's own product.
