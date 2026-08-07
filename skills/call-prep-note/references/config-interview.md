# Config interview

Runs once, the first time this skill is used in a working directory with no
`prep-note-config.md` present. Ask all of these in one message, not one at a
time — the goal is a single round trip, not a wizard. Say up front that this
writes a local file the user can hand-edit later.

## Questions

1. **Your company's email domain(s)** — so internal-only calls can be
   detected (everyone on this domain = internal, no note).
2. **Deal stages you use**, in order, if you track a pipeline. If none, say
   so — the skill falls back to the generic ladder in `stage-criteria.md`.
3. **Exit criteria per stage** — for each stage named above, what has to be
   true to call it "won" and move to the next. Skippable per stage; unanswered
   stages fall back to the generic ladder's criteria for that position.
4. **Post-close/account milestones**, if relevant (health, expansion,
   renewal) — only ask if the user does CS/expansion motions, not pure new
   logo sales.
5. **One-line ICP** — who the buyer usually is, for framing "who this call is
   for."

If the user has a CRM connected (see `SKILL.md` step 2), offer to read stage
names off it instead of asking, and only ask for exit criteria (a CRM has
stage names, never exit criteria).

## Writing the file

Write `prep-note-config.md` to the **current working directory** (not the
skill directory — this is per-user, per-workspace data, and an installed
plugin's own files get overwritten on update). Plain markdown, human-editable,
roughly:

```markdown
# Prep note config

Domain(s): acme.com
CRM: none | hubspot | salesforce | ...

## Deal stages
1. Discovery — exit: pain confirmed, DM named, next step booked
2. Evaluation — exit: success criteria written, POC owner named
3. Negotiation — exit: pricing agreed, signer named

## Account milestones (post-close)
Health — no red usage/sentiment signal since last call
Expansion — named path with owner and date

## ICP
Series B-D SaaS, buyer is VP Sales or RevOps lead
```

If the user skips a section entirely, omit it from the file rather than
writing a placeholder — an absent section means "fall back to
`stage-criteria.md` for this."

## Re-running

If the user later says their stages changed, offer to re-run this interview
and overwrite the file — don't silently drift from it.
