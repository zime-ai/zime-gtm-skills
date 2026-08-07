# Skill directory scaffold

Every skill in `skills/` is exactly this shape — four files, nothing else
at the top level (a fifth, `scripts/`, is allowed by the contract but no
current skill uses it). This is `skills/bant/` on `origin/main`, used as
the literal template since it's a clean example of the pattern.

```
skills/<name>/
├── SKILL.md
├── references/
│   └── rubric.md
├── assets/
│   └── sample-transcript.txt
└── evals/
    └── evals.json
```

`validate-skills.sh` warns (doesn't fail) on any subdirectory other than
`references|scripts|assets|evals` — so don't add a fifth directory without
a real reason, and don't be surprised if one shows up as a WARN.

## SKILL.md frontmatter — exact shape

```yaml
---
name: <matches the directory name exactly, kebab-case, [a-z0-9-]>
description: <one or two sentences stating both WHAT the skill audits and WHEN to use it. Not just "audits X" — the second half matters as much as the first, since this is also the trigger text.>
license: MIT
metadata:
  zime:category: new-business | post-sale | cross-stage
  zime:dimension: stage | initiative
  zime:input-modes: transcript | transcript,csv
---
```

Real example (`skills/bant/SKILL.md:1-11`):

```yaml
---
name: bant
description: Audits a B2B sales call transcript against the BANT qualification framework (Budget, Authority, Need, Timeline), or sweeps a CRM export for deals missing BANT fields. Use when qualifying an early-stage lead, deciding whether to advance a deal past a first call, or checking a pipeline export for unqualified opportunities.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: BANT
  zime:input-modes: transcript,csv
---
```

`zime:category` isn't part of `validate-skills.sh`'s hard-checked frontmatter
contract, but `check-docs-sync.sh`'s section-grouping check depends on it —
get it right the first time (see `doc-anchors.md`'s mapping table).

## SKILL.md body — the section headers every existing skill uses

Not every skill uses identically-named headers (`pain-finder` uses
`## How to run it` / `## Output` instead of `## Modes`), but the dominant
pattern across the 15 runnable skills is:

```markdown
# <Title>

<One paragraph: what this skill does, framed against neighboring skills if
relevant — e.g. "lighter-weight than meddicc" — so a reader picks the right
one.>

## When to use this

- <bullet: a concrete situation a rep/manager/RevOps person is actually in>
- <bullet>
- <bullet>

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

<how to invoke, what it scores against (reference `references/rubric.md`),
what the output format looks like — Status/Evidence/Note per dimension is
the house pattern>

### CSV mode (`.csv`)   <!-- omit this whole subsection if the skill is transcript-only -->

<structural hygiene sweep pattern: table of deal name/value/missing fields>

## Sample data

`assets/<filename>` is a synthetic <one-line description> — run the skill
against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
```

That closing "What this does not do" section is load-bearing house style —
every skill states plainly that it's local-only. Keep it verbatim unless
the skill genuinely does something different.

## `evals/evals.json` — required key names

```json
{
  "cases": [
    {
      "prompt": "...",
      "files": ["assets/sample-transcript.txt"],
      "expectations": ["..."]
    }
  ]
}
```

The key is **`expectations`**, never `assertions` — `validate-skills.sh`
greps for the literal string `"assertions"` and hard-fails if it finds it,
specifically to catch this mistake (it happened once already, across all
11 original skills, before this check existed).

## `assets/` — the hard rule

Synthetic or fully anonymized only. Never a real call transcript or CRM
export, even with names removed — anonymizing free text is easy to get
wrong, and this repo is public. If the user's draft skill came with a real
sample, generate a synthetic replacement rather than scrubbing the real one.
