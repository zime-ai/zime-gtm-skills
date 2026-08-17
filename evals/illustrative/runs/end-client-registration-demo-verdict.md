**Registration-level accuracy: 8/10 correct, 2/10 wrong**

| Reg | Gold | Output | Match? |
|---|---|---|---|
| REG-100 | clean | clean | ✓ |
| REG-101 | clean | clean | ✓ |
| REG-102 | flagged (Dim 1, partner_contact empty) | flagged, same evidence | ✓ |
| REG-103 | flagged (Dim 2, conflation) | flagged, same evidence | ✓ |
| REG-104 | flagged (Dim 4, conflict found) | flagged, correctly reads "conflict found not missing" | ✓ |
| REG-105 | flagged (Dim 5, permission not confirmed) | flagged, same evidence | ✓ |
| REG-106 | flagged (Dim 3, vague engagement_scope) | **listed clean** | ✗ miss |
| REG-107 | flagged (Dim 4 + Dim 6, two separate flags) | flagged, both fields named but bundled as one row | ✓ (partial, see trap 3) |
| REG-108 | flagged (Dim 7, expiry empty) | flagged, same evidence | ✓ |
| REG-109 | clean (boundary, valid) | **flagged** ("essentially already elapsed") | ✗ false positive |

Net: output's flagged set is {102,103,104,105,107,108,109} vs gold's {102,103,104,105,106,107,108}. Swapped REG-106 for REG-109 — count of 7 is coincidentally right, set is wrong.

**Trap handling: 3/5 pass, 2/5 fail**

1. REG-103 conflation caught correctly. **PASS**
2. REG-104 correctly reads "conflict found," not "check missing." **PASS**
3. REG-107 two independent dimensions (4 and 6) — output does name both fields but treats them as one bundled row/action, then in the closing summary lumps them into a single meta-bucket "missing required field" alongside Dim 1 and Dim 7. Gold requires these stay distinct dimensions. **FAIL** (methodological, not just cosmetic — corrupts the most-common-dimension count later)
4. REG-109 boundary case — gold explicitly says this must NOT be flagged, and explicitly calls out "near-expiry flag" as a named hallucination trap. Output flags it anyway. **FAIL** (this is the one gold flags hardest)
5. REG-102 vs REG-103 distinguished correctly, separate evidence. **PASS**

**Hallucinations: yes, one explicit, plus one omission**

- REG-109 flagged for "expiry window essentially already elapsed" / "renewal decision now" — this is the exact hallucination gold's "Not present" section calls out by name. Not grounded: the rubric dimension only checks a window exists, not its proximity.
- REG-106 dropped entirely (false negative) — engagement_scope "General support" (vague) never evaluated, called clean instead.
- No invented CSV values otherwise; the evidence quoted for genuine flags is accurate.

**Closing lines: count right, dimension claim wrong**

1. "7 of 10 registrations flagged" — **matches gold numerically**, but underlying set is wrong (see table above), so the correctness is accidental.
2. Most common flag dimension: gold says **Dimension 4 (Conflict check), 2 of 7 flagged rows** (REG-104, REG-107). Output says **"missing required field (contact/conflict check/commercial terms/expiry) — 4 of 7"** — this collapses Dim 1, Dim 4, Dim 6, Dim 7 into one artificial bucket, which is not how the rubric's dimensions work and directly contradicts gold's per-dimension framing. **FAIL**

**Summary:** output gets most individual flags right with good evidence, but fails two things gold specifically warns about: flagging REG-109 (explicit hallucination) and missing REG-106 (false negative), and its closing "most common dimension" claim is wrong because it merges four distinct rubric dimensions into one ad-hoc category instead of reporting per-dimension. Score: 8/10 registrations, 3/5 traps, closing lines half right (count yes, dimension no).
