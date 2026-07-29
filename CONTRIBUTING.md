# Contributing

This repo is small and opinionated by design — see the [Agent Skills
specification](https://raw.githubusercontent.com/agentskills/agentskills/main/docs/specification.mdx)
for the format every skill here follows.

## Ways to help

- **New motion rubrics** — a new skill for a motion not yet covered (see the
  README's skill table for what's missing). Open an issue first with the
  motion and the dimensions you'd propose, so the shape gets agreed before
  you write the whole thing.
- **Rubric corrections** — if a skill's rubric got something wrong or missed
  a dimension that matters, open an issue with the transcript excerpt that
  shows the miss. This is the single most useful kind of contribution.
- **New input format support** — a transcript format the current skills
  don't parse cleanly.

## Skill requirements

Every skill must:

- Live at `skills/<skill-name>/`, with `name` in `SKILL.md`'s frontmatter
  exactly matching the directory name (kebab-case, `[a-z0-9-]` only)
- Have a `description` that states both what it does and when to use it
- Keep `SKILL.md` under 500 lines
- Keep any `references/`, `scripts/`, `assets/` files one level deep — no
  nested reference chains
- Pass `skills-ref validate skills/<skill-name>` (this runs in CI on every PR)
- Ship with a synthetic or fully anonymized sample file in `assets/` so the
  skill is runnable with nothing of the contributor's own

## Sample data

If your PR includes a sample transcript, deal export, or any other example
file: it must be synthetic or fully anonymized. Do not submit a real call
transcript or CRM export, even with names removed — anonymization of free
text is easy to get wrong, and this repo is public.

## AI-assisted contributions

If you used an AI assistant to help write a rubric or skill, disclose it in
the PR description — same norm as the upstream Agent Skills spec repo.
