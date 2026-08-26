## Grading: persona-based-discovery

**Per-dimension agreement (5/5 exact match on verdict label):**

| Dim | Gold | Output | Match |
|---|---|---|---|
| 1 Persona ID | Covered | Covered | ✅ |
| 2 Pain framed | Covered | Covered | ✅ |
| 3 Proof point | Covered | Covered | ✅ (evidence choice differs, see below) |
| 4 Objections | Covered | Covered | ✅ (evidence choice differs, see below) |
| 5 Next step | Covered | Covered | ✅ |

Minor divergence, not a scoring miss: gold anchors dim3 (proof point) on retry-backoff mechanism and dim4 (objections) on SSO/SAML/OIDC exchange. Output flips it — SSO exchange used as dim3 evidence, "sticking point" question used as dim4 evidence, without re-quoting Morgan's actual SSO answer. Defensible alternate read, not wrong, but output's dim4 evidence is thinner (paraphrase "answers directly, doesn't deflect" instead of quoting the SAML/OIDC line).

**Trap 1 (title-vs-role mismatch) — PASSED.**
Quote, output.md line 1: "Single persona on call — Riley, Director of IT, self-identified as technical evaluator (budget sign-off sits with CIO, who's absent)."
Output never treats "Director" title as economic-buyer signal; explicitly scores off disclosed role.

**Trap 2 (no penalty for absent persona) — PASSED.**
Quote, output.md line 1: "Scoring dims 1-5 against Riley only, per rubric rule against penalizing absent personas."
No second-persona section exists; economic buyer only surfaces in forward-looking next-steps, not as a scored/missing dimension.

**Hallucinated evidence: none found.** Checked every quote against transcript (`persona-based-discovery-demo.txt`) — all verbatim and correctly attributed, including the extra Morgan line ("what's your role look like day to day...") that gold didn't quote but is genuinely in the transcript.

**Verdict:** Output matches gold on every dimension verdict and cleanly passes both planted traps, with slightly *more* transcript grounding than gold in places (dim1 quotes Morgan's question too, not just Riley's answer). Only weakness is a defensible re-mapping of which quote backs proof-point vs objection-handling, with dim4's supporting quote left paraphrased rather than lifted verbatim — a rigor nit, not a correctness failure. Strong pass overall.
