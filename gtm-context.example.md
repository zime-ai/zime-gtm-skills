# GTM context

Copy this file to `.agents/gtm-context.md` (or `.claude/gtm-context.md`) and
fill it in with your own company's details. Every skill in this repo reads
whichever of those two paths exists, once, before it does anything else —
no flag, no config. Delete any section that doesn't apply; a skill treats a
missing section the same as a missing file and falls back to asking (or to
its own generic default) only for what this file doesn't answer.

This file is never committed or read by anything except the skill at run
time — both paths above are already gitignored in this repo.

## Company & product

- **Company name:**
- **Product, one sentence:**
- **Pricing model** (seat-based, usage-based, flat, tiered — whatever a
  rubric would need to judge if a discount or a deal size is normal):

## Ideal customer profile

- **Target company size / segment:**
- **Target buyer persona(s) / titles:**
- **Common disqualifiers** (company traits that mean this isn't a fit,
  regardless of budget or interest):

## Named competitors

List the competitors your reps actually run into, so a skill recognizes a
name instead of treating every mention as generic. One line each:

- **Competitor name** — how they're usually positioned against you (cheaper,
  more features, incumbent, category leader, etc.)

## Internal terminology

Only fill this in where your team's own words differ from a skill's
generic defaults — a skill assumes the generic term until told otherwise.

- **Deal stage names**, if they differ from generic ones a skill might
  assume (e.g. your "Technical Validation" stage instead of "POC"):
- **Team/role names**, if not just "AE", "SE", "CSM" (e.g. what you call a
  solutions engineer or a customer success rep internally):
- **Any other shorthand** a rep would use on a call that an outsider (or a
  skill with no context) wouldn't otherwise recognize:
