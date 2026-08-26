## Grading: poc-success

**Per-dimension agreement (gold has 7 numbered dimensions + 1 close verdict):**

| # | Dimension | Gold | Output | Match |
|---|---|---|---|---|
| 1 | Criteria verdict-ed individually | Covered | Covered | ✅ |
| 2 | Quantified vs baseline | Covered | Covered | ✅ |
| 3 | End-user validation | Covered | Covered | ✅ |
| 4 | Sponsor sign-off | Missed | Missed | ✅ |
| 5 | Blockers surfaced | Covered | Covered | ✅ |
| 6 | Commercial next step | Covered | **Partial** | ❌ |
| 7 | What wasn't delivered | Covered | Covered | ✅ |
| Close | inconclusive | inconclusive | inconclusive | ✅ |

**Score: 7/8 exact matches** (6/7 core dimensions + close verdict correct; dimension 6 diverges).

**Planted trap — PASSED.** Output line: `4. **Sponsor sign-off** — Missed. Champion speaks for VP ("I know she'll be fine with it"), no VP statement obtained.` Skill correctly refuses to credit champion's secondhand enthusiasm as sign-off, matching gold's required Missed verdict and rubric's "Do not" rule.

**Possible hallucination.** Output cites `Casey correctly flags: "I'll want that in writing."` — this exact quote does not appear anywhere in brief.md or gold.md's cited evidence. No transcript file exists in this grading directory to verify it against source, so it's unconfirmed — flag as possible fabricated/unverifiable quote rather than confirmed hallucination.

**Dimension 6 divergence.** Gold treats commercial-next-step as fully Covered (owner = rep, date-anchored trigger = SOC 2 close). Output downgrades to Partial, reasoning no hard date is attached to the redline itself. This is a stricter, defensible read, not a rubric violation — just disagreement with gold's leniency, not a planted trap.

**Verdict:** Strong output. Nails the one thing the brief was actually testing — resisting the sponsor-sign-off trap — and lands on the correct overall "inconclusive" close for the right reason. Loses one clean dimension match by being stricter than gold on the commercial-next-step criterion (arguably reasonable, not wrong), and carries one quote that can't be verified against a transcript in this directory. Net: trap passed, close call correct, minor scoring drift on one dimension.
