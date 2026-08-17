# Brief: champion-tracker-demo transcripts

**Honesty note stronger than the other two runs**: I wrote
`champion-tracker`'s own rubric (PR #26) — there is no meaningful
blinding here at all, even the "best-effort" kind claimed for
`meddicc`/`challenger`. Treat this run as the weakest of the three on the
self-authorship axis, not just tied with them.

**Avoiding the skill's own bundled fixture on purpose.** The skill's own
`assets/sample-call-*.txt` already tests a near-identical shape (a
plan-vs-done trap on a "flag this to procurement next week" line,
contacts named Priya/Devon, company "Cascade Freight"). Reusing that
fixture would just re-run a scenario the skill was already built and
graded against, not a fresh test — so this brief uses a different
company, different names, and different specific actions, even though the
underlying pattern being tested (stated plan ≠ completed action) is
structurally the same idea.

## Situation

Two calls, ~3 weeks apart: a mid-market manufacturing company ("Kestrel
Tooling") evaluating a quality-inspection platform. Two named buyer-side
contacts across both calls.

## Deliberate construction — gold here is a reference action ledger
(Shape C: document-writer, not a rubric grade)

- **Marisol Vance (Ops Director)** — trend must read **strengthening**:
  - Call 1: says something plan-shaped, not yet done ("I'll get this in
    front of our finance lead sometime soon") — must tag **Sentiment**,
    not Action, since nothing had happened yet.
  - Call 2: reports having actually done it (finance lead looped in,
    pushed back on a competing internal priority in a meeting the rep
    wasn't in), plus a second independent action.

- **Callum Reeve (Plant Supervisor)** — enthusiastic in both calls, never
  crosses into action in either. Every row Sentiment. Not the headline
  finding this time (Marisol's genuine trend is) — tests whether the
  skill still tags Callum correctly as a secondary thread rather than
  promoting him to champion or dropping him from the ledger entirely.

- **The trap**: a stated future intention ("I'll get this in front of...
  sometime soon") must never be tagged Action just because it sounds
  proactive — only a call where the action is reported as already done
  counts, per the skill's own Champion definition (doing something, not
  saying something).
