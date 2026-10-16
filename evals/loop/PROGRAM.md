# Improvement loop: program

This file tells the agent how to run one iteration of the skill-improvement loop.
The owner edits this file. The agent never edits it.

Design sources:

- Karpathy's autoresearch: a `program.md` file, keep or discard on one metric, git as
  the frontier, never stop.
- "AutoResearch at Production Scale": prevent, persist, redirect.
- The ECC `loop-design-check` skill: a goal a machine can check, an independent judge,
  damping.
- The SkillsBench and SWE-Skills-Bench studies: compact skills win, and skills can hurt.

## The goal, in terms a script can check

Raise the held-out score of one skill per iteration, and never lower anything else.

- Measure: planted-fact exact accuracy from `scripts/referee.py`. The answer key is true
  by construction, so no model gives an opinion.
- If the referee prints `ACCEPT`, accept the change. Otherwise reject it. The referee
  is a script, and its result outranks your own view.
- A change that scores the same but makes the skill shorter or simpler also counts as
  an improvement. A change that adds many lines for a tiny gain does not.

## What you can and cannot touch

You can edit only `skills/<target>/SKILL.md` and `skills/<target>/references/*`.
Never edit these, even to fix a bug you think you found:

- `evals/framework/`, `evals/synth/`, `scripts/referee.py`, `scripts/loop_iteration.sh`,
  `evals/loop/baseline.json`, `evals/loop/state/` except `hypothesis.txt`
- `evals/loop/PROGRAM.md`, `.github/`, `MAINTAINING.md`, `EVALS.md`, `.gitignore`
- Any held-out bank, any answer key, any run output under `evals/runs/`

If one of those looks wrong, write the problem in `evals/loop/escalations.md` and stop
the iteration. The evaluator is locked on purpose: agents change the evaluator in about
half of unlocked runs.

## One iteration

1. Read `evals/loop/memory.md` and `evals/loop/state/rejects.tsv` first. They list ideas
   that failed. If an idea is listed, do not retry it.
2. Read the last 20 rows of `evals/loop/state/results.tsv`, if it exists.
3. Pick the target: the skill with the lowest recorded score that has a planted bank
   listed in `scripts/referee.py`. If no such skill exists, do not edit a skill. Your
   task is then to write a new planted bank for the next skill.
4. Write one hypothesis in one sentence: which failure it fixes and why. Use the dev
   bank failures that the referee prints. You never see the held-out bank. You see only
   its aggregate numbers.
5. Make one change. Keep `SKILL.md` under 500 lines. Prefer a rule or one worked
   example over more prose. Cite a public source for any change to rubric content.
6. Write your one-sentence hypothesis to `evals/loop/state/hypothesis.txt`. Do not run
   the referee and do not use git. You have no shell. The runner script does both.
7. The runner runs `scripts/referee.py`. On `ACCEPT` it commits on a branch named
   `loop/<target>-<date>` and opens a pull request to `dev`. On `REJECT` it restores
   `skills/` and logs your hypothesis and the numbers to `state/rejects.tsv`.
8. Stop. The next iteration starts with a fresh context. Do not carry plans in your
   head. If you learned something the next run needs, add it to `memory.md`.

## Redirect when stuck

If the last 5 rows show no accepted change, or the best held-out score moved by less
than 8% relative, change strategy before retrying. Try a different failure class, a
shorter version of the skill, or adding a worked example. Write the new direction in
`memory.md`. Do not ask the owner for this.

## Ask the owner only for these

Write to `evals/loop/escalations.md` and stop. Do not ask about anything else.

- Spend reaches 80% of any cap (`JUDGE_CAP_USD`, `JUDGE_RUN_CAP_USD`).
- The referee, the key files, or the validator fail on a clean checkout of `dev`.
- A change touches private data, a credential, a release, a public post, or any
  file outside the allowed list.
- A planted canary or a held-out score is perfect. That is evidence of cheating or a
  leak, not of success.
- Three accepted changes in a row later reverted by the nightly guard.
- Any step that needs a human judgment about whether a skill's goal is right.

## Hard rules

- Every Claude subagent uses Haiku 5.5. This author step is the only Sonnet use.
- Judges use `z-ai/glm-5.3-flash` with the spend caps in `evals/framework/judge.py`.
- No Claude attribution lines in any commit or pull request.
- Never use private Zime transcripts, customer names, or anything not already public.
- The kill switch is the file `~/.config/gtm-loop/STOP`. If it exists, do nothing.
