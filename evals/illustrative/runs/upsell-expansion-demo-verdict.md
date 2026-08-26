## Grading: upsell-expansion

**Dimension-by-dimension vs gold** (8 total):

| # | Gold | Output | Match? |
|---|------|--------|--------|
| 1 | Missed | Partial | ✗ (invented third status, not binary rubric) |
| 2 | Covered | Covered | ✓ |
| 3 | Missed | Missed | ✓ |
| 4 | Missed | Missed | ✓ |
| 5 | Covered | Covered | ✓ |
| 6 | Covered | Covered | ✓ |
| 7 | Covered | Covered | ✓ |
| 8 | Covered | Covered | ✓ |

**7/8 exact match.** Close read matches: gold "Hold", output "Hold, conditional" — same call.

**Trap 1 (gate, don't average)** — PASSED. Output: *"Dim 1 unresolved: usage dip tied to admin departure, no coverage plan yet — expanding seats onto a team whose current admin function is unstaffed adds risk before that gap closes."* Explicitly holds despite 5/8 covered elsewhere, matching gold's gating logic.

**Trap 2 (enthusiasm ≠ champion strength)** — PASSED. Output: *"Enthusiasm only, no standing/advocacy answer. Question dodged."* Scored Missed, refused to credit "I'm really excited" as advocacy evidence — matches gold exactly.

**Hallucinated evidence:** None found in the quoted transcript lines — all quotes trace to transcript.txt. Two soft fabrications worth flagging though: "Question dodged" is an interpretive gloss (Sam did respond, just not with standing/intent — gold calls this "lacking any stated advocacy plan," output reframes as a dodge, slightly stronger claim than transcript supports) and the closing "Reads-well-too check: sanity-checked against a healthy-close pattern" invents a verification step with no basis in transcript or brief — process theater, not evidence, but not a rubric-scoring error either.

**Verdict:** Strong output — both planted traps passed cleanly, 7/8 dimensions and the Hold verdict match gold. Only real defect: dimension 1 uses a "Partial" status the rubric's binary Covered/Missed schema doesn't have, softening what gold scores flatly as Missed — a labeling deviation, not a reasoning failure, since the prose still correctly treats it as unresolved and gates the close on it. Minor invented "sanity-check" step at the end is unnecessary noise but harmless.
