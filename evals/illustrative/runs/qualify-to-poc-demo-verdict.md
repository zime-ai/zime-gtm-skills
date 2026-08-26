## Grading: qualify-to-poc-demo output vs gold

**Per-dimension agreement: 5/5 exact match**

| Dim | Gold | Output | Match |
|---|---|---|---|
| Success criteria | Covered | Covered | ✓ |
| Technical scope | Covered | Covered | ✓ |
| Stakeholders | Partial | Partial | ✓ |
| Timeline/exit | Covered | Covered | ✓ |
| Resourcing | Missed | Missed | ✓ |

**Trap 1 (independent gates, no "Go" halo from 3 Covered dims): PASSED**
Quote: `"No-go" (Needs one more call) — Resourcing missed and end-of-pilot decision-maker unnamed. Rep already flagged both open (...) — pilot shouldn't start Monday til both close.`
Names both gaps as blocking, doesn't blend toward positive verdict.

**Trap 2 (resourcing "someone on our side" ≠ Covered/Partial): PASSED**
Quote: `**5. Resourcing confirmed — Missed** Evidence: "Someone on our side will handle it, I'm sure we'll figure it out once it's running" — no named person, no bandwidth confirmed`
Correctly scored Missed, didn't infer a named owner.

**Hallucinated evidence check:** none. Checked transcript directly — quote at line 16 of output ("I'll follow up on who signs off at the end, and who's actually doing the hands-on work") matches transcript lines 39-40 verbatim. "confirmed by prospect" (dim 2) is a fair paraphrase of Ops Manager's line 16 ("Right, returns is a separate project for us anyway"), not fabricated.

**Verdict:** Clean pass. All five dimension scores match gold exactly, both planted traps avoided — output correctly isolates Resourcing/Stakeholders as blocking gates rather than averaging toward "Go," and correctly refuses to credit the vague "someone on our side" line as a real owner. Slightly terser than gold (no explicit "independent gates, not blended readiness score" framing) but the substance and verdict land identically. No fabricated quotes.
