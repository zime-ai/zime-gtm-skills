# zime-gtm-skills

Open-source Claude Code Skills, GTM call-audit focused. No Zime product
coupling — every skill here runs standalone, no API keys, no gating.

## Conventions

- One skill per directory under `skills/`, kebab-case, `name` in frontmatter
  must equal the directory name.
- `SKILL.md` stays under 500 lines; move detail into `references/`.
- Every skill ships a synthetic sample in `assets/` so it's runnable cold.
- Transcript-mode outputs must cite a quote or timestamp per finding — an
  uncited finding doesn't ship. This is the trust bar the whole repo is
  built on.
- Never copy Zime's internal checklist question text into a skill's rubric.
  Rubrics here are written fresh, in this repo, from scratch.

## Adding a skill

See `CONTRIBUTING.md` for the process. Validate locally before opening a PR:

```bash
skills-ref validate skills/<skill-name>
```
