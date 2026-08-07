# Known pitfalls

Concrete lessons hit once while building/using this. Read before touching a
skill's `SKILL.md`/references.

## No fabrication

Refining toward a closer ground-truth match never means inventing content
the ground truth doesn't support. A GT's own genuine gaps (`TBC`, "requested,
not received," an unnamed stakeholder) are the correct target to reproduce,
not a defect to paper over. A skill that produces a plausible-but-invented
value to close a gap is worse after "refinement," not better.

## Root cause, not symptom

When the same mismatch shows up across more than one client's output, trace
it to the one shared instruction in `SKILL.md`/`references/` responsible and
fix it there — not a patch per case.

## A rendered document defaults to unstyled unless told otherwise

A skill that generates a `.docx`/`.pptx` and is only given *structural*
rendering intent ("this is a table," "this is bold") comes out plain
black-and-white even when the rendering tool fully supports colors, shading,
custom layout — nothing is blocking it, the instructions just never asked
for it. If a generated document visually doesn't resemble a
reference/branded sample, check whether the skill's layout reference
specifies concrete color/shading intent before assuming the tool is the
limitation. (Real example: `sales-to-cs-handover`'s `docx-layout.md` was
structure-only; adding explicit hex/shading/banner instructions fixed a
genuine visual mismatch against the live template.)

## Ground-truth section-format varies

Real ground truth in this workspace has shown up as markdown `## ` headers,
table-row section markers (`| N | Title |`), and JSON top-level keys. Don't
assume one shape when reading a GT file by hand — check which it actually is
before concluding a field is "missing."

## Parent-directory context inheritance is real

Claude Code walks parent directories past a git repo boundary for both
`CLAUDE.md` and `.claude/skills/` discovery — confirmed live: a session with
cwd inside a repo with no `.claude/skills/` of its own still inherited a
parent directory's `CLAUDE.md` and every skill under its `.claude/skills/`.
This is *why* the test tree (`Master_workspace/skill-testing/`) sits where it
does — `Master_workspace/` itself has no `CLAUDE.md`/`.claude/`, so booting
there only inherits `~/.claude` (global), nothing project-specific.

## `.claude/skills/*` symlinks can dangle

`sales-to-cs-handover` and `poc-deck` only exist on `zime-gtm-skills`' branch
`internal_skills`. If that repo is checked out to a different branch, the
symlinks in `skill-testing/.claude/skills/` point at nothing and `/<skill>`
won't resolve in the test instance. Check the branch before assuming the
skill itself is broken.

## Comparing `.pptx` output is structural, not visual

There's no libreoffice on this machine, so no slide can actually be
rendered to an image for a pixel comparison. `scripts/extract_pptx.py`
reads shape position/size, fill color, and font color/size/bold via
python-pptx instead — real signal for "wrong color" or "shifted box," but
it can't catch a purely visual defect that doesn't touch any of those
properties (e.g. two shapes overlapping despite both having individually
"correct" coordinates). If a `.pptx` comparison feels inconclusive, say so
rather than declaring a match the extractor genuinely can't see.

## The three skill locations are not interchangeable

`zime-gtm-skills/skills/*` (public product skills) and
`zime_repos/.claude/skills/*` (meta/tooling skills, skill-refiner's own home)
are both fine to read/edit. `~/.claude/skills/*` (the user's personal global
skills) is never touched by this skill, no exceptions — it's a different
person's tooling, not a GTM product skill.
