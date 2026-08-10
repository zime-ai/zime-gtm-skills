# Changelog

All notable changes to this repo are documented here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [2.0.0] — 29 skills, ROADMAP.md, dev/main release flow

29 Agent Skills (up from 16 at 1.0.0), 20 stage + 9 initiative, plus the
process this repo now ships work through: `ROADMAP.md` tracks what's built
and what's next, work lands on `dev` and ships to `main` in batched,
fully-gated releases (this entry is the first one cut that way).

**New initiative skills** (4): `meddpicc`, `faint`, `sandler`, `challenger`.

**New stage skills** (9): `sql-to-qualify`, `qualify-to-poc`,
`persona-based-discovery`, and the deal-stage pipeline-check family —
`prospect-pipeline-check`, `qualify-pipeline-check`,
`evaluation-pipeline-check`, `poc-pilot-pipeline-check`,
`negotiation-pipeline-check`, `won-pipeline-check`. The pipeline-check six
are a new input class for this repo: no transcript mode, they read a `.csv`
deal export and flag deals that can't pass their own stage's exit test,
citing the column and cell value behind every flag.

Also ships:
- `ROADMAP.md` — every phase-1 skill tracked as a checkbox, machine-checked
  against `skills/*/` by `scripts/check-docs-sync.sh`'s `roadmap-in-sync`
  rule so this file can't silently drift the way this changelog once did.
- `dev` as the integration branch for skill PRs; `main` only moves in
  batched, fully-validated releases via the new `gtm-release` skill.
- `scripts/check-pr-diff-identity.py` — scans every PR's actual diff for the
  operator's own git identity or a home-directory path right after
  `gh pr create`, since the PR is already public by the time a pre-push gate
  could catch it.

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
- `EVALS.md`'s three-tier eval methodology, and a worked example comparing
  a skill-aided run against an unaided one.
- `CONTRIBUTING.md` / `MAINTAINING.md` documenting the full skill-authoring,
  review, and landing process, and the IP boundary on what's fair to draw
  from Zime's own product.
