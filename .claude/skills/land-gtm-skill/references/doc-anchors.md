# README anchors `scripts/check-docs-sync.sh` actually checks

Pulled directly from the script, current as of the `sample-required` /
16-skill / two-dimension state of `main`. If the script's patterns change,
this file is out of date before this sentence is — treat the script itself
as the source of truth and update this table when it drifts.

## Count anchors (§1 — `check_count`)

Every one of these must contain the *same* number: the actual count of
`skills/*/` directories. The script extracts the **first** number it finds
in each match, so a line with more than one number (see row 3) only has its
first number checked.

| Surface | Exact regex | Example match on current README |
|---|---|---|
| Badge | `skills-[0-9]+-blue` | `skills-16-blue` |
| Opening paragraph | `here\. [0-9]+ \[Agent Skills\]` | `here. 16 [Agent Skills]` |
| "How these fit together" | `[0-9]+ skills: [0-9]+ stage motions` | `16 skills: 11 stage motions` — only the first `16` is checked; the `11` (and any "K cross-stage initiative skills" that follows in the same sentence) is **not verified by the script** |
| `<summary>` tag | `<summary>[0-9]+ skills across` | `<summary>16 skills across new business, post-sale, and cross-stage initiative</summary>` |

**Not covered by this script, and not covered by anything else either:**
- The GitHub repo description (`gh repo edit ... --description "..."`) —
  pure API metadata, no file to grep.
- The "N stage motions" / "K cross-stage initiative skills" sub-counts
  inside the "How these fit together" sentence — hand-verify these against
  the actual `zime:dimension: stage` vs `initiative` split.
- The mermaid flowchart's node list.

## Table row anchors (§2/§3 — missing/orphan rows)

Block extraction: everything between the literal markers
`<!-- SKILLS:START -->` and `<!-- SKILLS:END -->`.

Row shape required: `[skill-name](skills/skill-name/)` — link text and the
path segment must both be the bare skill name, and the trailing slash on
the path is required. Anything else and the skill silently doesn't count as
"present" even if a row exists.

## Section-grouping anchors (§5)

A group header is a markdown line that is bold text and *only* bold text —
`**Group Name**` on its own line, nothing else. The skill's `zime:category`
must map to the section it's actually listed under:

| `zime:category` | Expected section heading |
|---|---|
| `new-business` | `New business` |
| `post-sale` | `Post-sale` |
| `cross-stage` | `Initiative (cross-stage)` |
| `cross-cutting` | `Vertical context` |

An unrecognized `zime:category` value is silently skipped by this check
(the script can't tell you where it expected the row) — `validate-skills.sh`
won't catch that either since `zime:category` isn't part of its frontmatter
contract, so double check this by hand if the category is anything other
than the four above.

## Coverage table anchors (§4)

Block extraction: from the heading matching `## Coverage: [a-z]+ dimensions`
(currently "two dimensions", was "three dimensions" before vertical-context
was pulled) down to `## Where this stops`.

Row shape required: the skill name in backticks as the **first** cell,
e.g. `` | `bant` | Any (early) | BANT | ``.

Skipped entirely — no row required — if `zime:dimension: vertical-context`.
Every `stage` or `initiative` skill needs a row here or the check fails
naming exactly which skill and dimension is missing.

## `sample-required` (enforced in `validate-skills.sh`, not `check-docs-sync.sh`)

Any skill with `zime:dimension: stage` or `initiative` must have:
- `assets/` containing at least one file
- `evals/evals.json` that parses as valid JSON and uses the key
  `expectations` (not `assertions`)

`zime:dimension: vertical-context` skills are exempt — they're loaded by
other skills rather than run directly, so there's nothing to "sample" them
against.
