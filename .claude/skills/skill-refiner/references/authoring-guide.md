# Authoring guide (Mode A)

Condensed from the installed `skill-creator` skill's proven conventions,
plus what actually mattered across real `zime-gtm-skills` skills — not
skill-creator's full surface (its trigger-eval + benchmark-viewer tooling
is a separate concern; Mode B here covers the refinement half instead).

## Frontmatter contract

- `name`: must match the skill's directory name exactly, lowercase,
  hyphen-separated.
- `description`: states both **what** the skill does and **when** to use
  it, in one or two sentences. This is the only thing that decides whether
  the skill fires — vague ("helps with documents") loses to specific
  ("fills the fixed X template from pasted Y, flagging every field it
  can't fill").
- `disable-model-invocation: true` only if the skill should never
  auto-trigger from conversation — e.g. it produces a specific, opinionated
  artifact that shouldn't fire on a passing mention.

## Structure: progressive disclosure

`SKILL.md` itself should be short enough to read in one sitting — every
invocation loads it in full. Anything not needed on *every* run (detailed
field-by-field rules, edge-case tables, worked examples, a full template)
goes in `references/*.md`, loaded only when that step needs it. A `SKILL.md`
over ~150 lines is a signal something belongs in a reference instead.

## Steps, not prose

Numbered steps, each with an explicit **Done when** condition — a
verifiable checkpoint, not "make sure it's good." Weak checkpoints ("output
looks reasonable") force the model to guess when a step is finished; strong
ones ("every field has either evidenced content or an unknown marker, none
silently blank") let it self-check.

## Density matches real samples, not report style

If the skill fills a template, its output density should match how a human
actually fills that template — fragments, not paragraphs; no restating the
field label; no preamble ("Based on the transcript, it appears that...").
Look at a real filled example before writing generation rules, not after.

## Grounding discipline for any extraction/audit skill

- Every filled field traces to a specific source; every field without
  evidence gets an explicit unknown marker, never silently blank and never
  a plausible-sounding guess. A confident fabrication is worse than a
  visible gap — the reader trusts it without checking.
- If a field commonly gets confused with an adjacent one (this recurs:
  "who NOT to engage" vs. "what NOT to say" being cross-filled, a status
  value duplicated in two places that then disagree), write the
  disambiguation into the reference explicitly — don't rely on the model
  inferring it correctly every time.

## Chat-response discipline

The chat-side reply after generation is a **gap summary**, not a
description of the doc. Echoing/restating the generated content in chat is
pure duplication — the doc is the deliverable. State: file paths, what's
missing and why, whether any human input is still needed. Nothing else.

## First test case is part of authoring, not an afterthought

A skill isn't done at "the frontmatter validates." `scripts/new_case.sh
<skill> <case>` scaffolds a workspace case; a real (or realistic synthetic)
input plus a hand-authored expected output, run through Mode B once, is
what actually proves the skill works — not just that it's well-formed.
