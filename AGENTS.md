# AGENTS.md

Guidelines for AI agents working in this repository.

## Repository overview

Open-source [Agent Skills](https://agentskills.io/specification.md) that
audit sales call transcripts and CRM exports against per-GTM-motion rubrics.
No Zime product coupling — every skill runs standalone: no API keys, no
gating, no data leaves the user's machine. Skills install to
`.agents/skills/` (the cross-agent standard) and also work under
`.claude/skills/`.

- **Name**: zime-gtm-skills
- **GitHub**: [zime-ai/zime-gtm-skills](https://github.com/zime-ai/zime-gtm-skills)
- **Maintained by**: [Zime](https://zime.ai)
- **License**: MIT

## Repository structure

```
zime-gtm-skills/
├── skills/
│   └── skill-name/
│       ├── SKILL.md          # required
│       ├── references/       # optional — the rubric lives here
│       ├── assets/           # optional — synthetic sample transcript/CSV
│       └── evals/            # optional — evals.json, declarative for now
├── validate-skills.sh         # local, zero-dep frontmatter/layout check
├── CONTRIBUTING.md
├── MAINTAINING.md              # process + decisions, for picking this repo back up
├── LICENSE
└── README.md
```

## Frontmatter contract

| Field | Required | Constraints |
|---|---|---|
| `name` | yes | 1–64 chars, lowercase `[a-z0-9-]`, must equal the parent directory name |
| `description` | yes | 1–1024 chars; state both *what* the skill does and *when* to use it |
| `license` | no | defaults to MIT |
| `metadata` | no | free-form; this repo uses `zime:category` and `zime:input-modes` |

`SKILL.md` stays under 500 lines — move detail into `references/`.
`references/`, `scripts/`, `assets/`, `evals/` are one level deep, no nested
reference chains.

## Validate

```bash
./validate-skills.sh                        # local, seconds, zero deps
```

CI additionally runs the upstream spec's `skills-ref validate` on every PR,
pinned to a commit (see `.github/workflows/validate.yml`) since it isn't
published to PyPI.

## The two hard content rules

1. **Every finding in a transcript-mode audit cites a quote or timestamp.**
   An uncited finding doesn't ship — this is the trust bar the whole repo is
   built on.
2. **Never copy Zime's internal checklist question text into a rubric.**
   Rubrics are written fresh, in this repo, from scratch. See
   `MAINTAINING.md` for the authoring process and how this gets enforced.

## Evals

Each skill may carry `evals/evals.json` — declarative test cases (prompt +
sample file + expected assertions). They are not run in CI yet; see
`MAINTAINING.md`'s deferred-work list. Treat them as the source of truth for
"does this skill actually work," not the `skills-ref`/`validate-skills.sh`
structural checks, which only catch frontmatter and layout errors.
