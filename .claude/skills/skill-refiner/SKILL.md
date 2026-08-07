---
name: skill-refiner
description: Build a new Claude Code skill from scratch, or compare an existing skill's real output against hand-authored ground truth and fix the skill. Use when the user wants to draft a new SKILL.md, or says a skill's output doesn't match a sample/reference doc, wants a skill "refined"/"tuned" against real examples, or asks to grade a skill's output against ground truth.
---

Read `references/known-pitfalls.md` before touching anything — concrete
lessons already hit once, don't re-hit them.

## Hard rules — apply in both modes, no exceptions

1. **No fabrication.** A GT's own genuine gaps (`TBC`, "requested, not
   received," an unnamed stakeholder) are the correct target to reproduce,
   not a defect to paper over.
2. **Root cause, not symptom.** The same mismatch across more than one
   client traces to one shared instruction — fix it there, not per case.
3. `~/.claude/skills/*` (the user's personal global skills) is never edited
   by this skill. `zime-gtm-skills/skills/*` and
   `zime_repos/.claude/skills/*` are the only valid targets.

## Mode A — Build a new skill

Full conventions in `references/authoring-guide.md`. Short version:

1. Capture intent: what does this skill do, on what input, producing what
   output — ask until this is concrete, don't guess.
2. Draft `SKILL.md`: minimal frontmatter (`name` matching the directory,
   `description` stating both what and when), numbered steps each ending in
   an explicit **Done when** condition, density matching real filled
   examples — not speculative flexibility no one asked for.
3. Push anything not needed on every invocation into `references/` —
   progressive disclosure. `SKILL.md` itself should read short.
4. Hand off to Mode B for the first real-input pass before considering the
   skill done.

## Mode B — Compare real output against ground truth, fix the skill

No scripts, no ledger. The user runs the skill themselves in the test
instance (`Master_workspace/skill-testing/<skill>/<client>/`) — a fresh
Claude Code boot, so it's a real execution, not a scripted one-shot. I
compare the result to hand-authored ground truth and edit the skill.

### 0. Ingest a sample input

The user hands me a sample input by pointing at a file path already on
disk (a transcript, a doc, whatever the skill takes) — not by pasting it
into chat. My job:

1. Work out `<skill>` and `<client>` from context (which skill this is a
   sample for, whose deal/data it is). Ask if either is genuinely
   ambiguous — don't ask if it's obvious from the conversation or the
   filename.
2. If `Master_workspace/skill-testing/<skill>/<client>/` doesn't exist yet,
   create it: `mkdir -p input output`, symlink `.claude -> ../../.claude`
   (same pattern as the existing leaves — this is what makes `/<skill>`
   resolve when the user boots Claude there). If the skill has no entry
   yet in `skill-testing/.claude/skills/`, add that symlink too, pointing
   at its real source.
3. Copy the file into `input/`, keeping its original name.
4. Tell the user the leaf folder is ready and what command to run there
   (step 1) — don't wait to be asked.

Ground truth is separate and can arrive later — don't block scaffolding
the input on having GT in hand.

### 1. Run

User: `cd Master_workspace/skill-testing/<skill>/<client>`, boot `claude`,
run `/<skill> input/<file>`, save whatever it produces into `output/`.
User tells me it's done.

### 2. Compare

I read `skill-testing/<skill>/<client>/output/*` against
`zime-gtm-skills/evals/gt/<skill>/<client>.<ext>` (ground truth — never
touched by the user's run, lives outside the test tree entirely; if it
doesn't exist yet, say so and stop here rather than comparing against
nothing). I state plainly: what matched, what didn't and why (root cause,
not just "field X was wrong"), what in the GT is itself a genuine gap (not
a defect to fix).

**For a `.pptx` GT/output pair** (e.g. `poc-deck`): a deck can't be read as
text directly. Run `scripts/extract_pptx.py <file.pptx>` on both GT and
output — it dumps every slide's shapes to JSON (text/runs, position in
inches, fill color, font color/size/bold), and I diff the two JSONs. This
is structural conformity only, not a rendered image (no libreoffice on
this machine) — it catches "wrong color," "shifted box," "missing
text/slide," but not a purely visual issue that doesn't touch any of
those properties (e.g. two boxes overlapping despite both having "correct"
coordinates). Say so explicitly if a mismatch might be layout-only and
outside what this can see.

### 3. Fix

If there's a real skill bug, I edit `SKILL.md`/references at the shared
root cause — surgical, not a rewrite — and say what changed and why.

### 4. Repeat

Back to step 1 with the same client (or the next one) until remaining gaps
are all genuine, non-derivable GT gaps — not until every field is filled.

**Ground truth locations** (already restructured per-skill this session,
gitignored, never lives inside `skill-testing/`):

```
zime-gtm-skills/evals/gt/
  sales-to-cs-handover/astra.md, truefoundry.md
  poc-deck/astra.json
```

**No automated scoring.** There's no `field_recall` number, no run-over-run
delta — I read the diff and say what I see. Traded away deliberately for
fewer moving parts; if that turns out wrong, say so and it comes back.

## Reporting back

Never claim a match that isn't real to make a pass look more finished than
it is. State the current gap plainly, even if it's "still wrong on 3 of 9
fields."
