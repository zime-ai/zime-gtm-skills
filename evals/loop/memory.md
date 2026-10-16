# Loop memory

Durable notes for the improvement loop. The agent reads this first and appends to it.
Ideas that failed are listed so they are never retried. One entry per line.

## Findings that shape the work

- 2026-10-16 deep-discovery: pasting the rubric into a plain prompt gave most of the gain over the bare model (83% to 90% exact). The rest of SKILL.md added about one point.
- 2026-10-16 deep-discovery: all variants credited dimensions the call never raised. Rules that require evidence to be about that dimension, forbid softening Missed to Partial, and add a Missed example raised dev-bank exact from 0.909 to 0.995 and clean single-fact flips from 6 of 24 to 22 of 24.
- 2026-10-16 test design: modules in a planted bank must not hint at each other. A hint is a leak, and the model was right to credit it. `leak_audit()` in `evals/synth/deep_discovery.py` checks this.
- 2026-10-16 eval runs must use `--setting-sources project`, or personal hooks and output styles change the skill's output.

## Failed ideas (do not retry)

(none yet)
