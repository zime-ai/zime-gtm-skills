# Rule ledger — `sales-to-cs-handover`

Every normative statement in `SKILL.md` and its four `references/*.md`,
tagged with origin and the **swap test**: can this rule be stated without
naming a specific client, industry, tool, person, or dollar figure? The test
itself is not new — `miss-prone-fields.md`'s persona table already applies it
informally ("could this sentence be copy-pasted onto a different stakeholder
at a different company without changing a word?"). This ledger promotes it
from a persona-only check to the acceptance test for every rule in the skill.

Origin codes: **G** = general principle, sample-independent. **A** =
Astra-sourced. **T** = TrueFoundry-sourced. **F** = Fyno-sourced. A rule can
have more than one origin tag if more than one sample independently produced
it (stronger evidence it generalizes).

Verdict: **PASS** = rule survives the swap test as written. **PASS (ex)** =
rule passes; a worked example beside it names a real client, but the example
is clearly marked as illustration, not part of the rule. **FLAG** = the rule
itself (not just an example) encodes something specific to ≤2 samples that
has not been checked against a third. **FAIL** = rule cannot be restated
without the specific — memorization, not a rule.

## SKILL.md

| # | Rule | Origin | Verdict | Note |
|---|---|---|---|---|
| S1 | Inventory sources: label, date, participants, type | G | PASS | Structural to any transcript-driven skill |
| S2 | Undated source → literal `undated`, never guess from file order | G | PASS | |
| S3 | Field-by-field walk, not source-by-source | G | PASS | Correct as a completeness guarantee; **this is also the structural blind spot** — a field-driven walk only finds what a cell asks for. Not a swap-test failure, but flagged in the plan as the thing workstream C (query-driven pass) exists to fix |
| S4 | Never fill from web search/prior knowledge/plausible guess; unknown marker instead | G | PASS | Core anti-hallucination rule, the skill's spine |
| S5 | Re-scan filled template for any remaining `{placeholder}` | G | PASS | |
| S6 | Five miss-prone areas (client context, roster, role completeness, persona test, answered≠closed, risk derivation) run explicitly every time | G | PASS | Confirmed independently by "a blind test run and the person who does this by hand" — two independent sources agreeing is closer to real signal than one doc |
| S7 | Acceptance checklist: check only with direct evidence, else short reason | G | PASS | |
| S8 | Open gaps: human-only fields vs. transcript gaps, kept separate | G | PASS | The human-only field *list itself* (Handover by/to, CS Owner, dates, Drive folder, Sales Deck, POC sheet link) is structural to the template's own form, not derived from deal content — low overfitting risk even though it traces to A+T |
| S9 | Ask only if unresolved AND load-bearing; cap 5 questions; confined to 4 named areas | G | FLAG | The "5" and "4 areas" caps are arbitrary round numbers, not derived from a measured failure rate. Not sample-specific (no client's number), but also not validated — flag for revisit once B's elicitation session surfaces how many the expert actually needs |
| S10 | Appendix renders only on explicit tribal-knowledge walkthrough evidence, else fully omitted | G/T | PASS (ex) | Rule is general; TrueFoundry (Juhi) is where the pattern was observed, but the rule doesn't name her — SKILL.md's own inline example ("here's how I spot an upsell") is already an invented generic phrase, not a real quote |
| S11 | Step 8 filename convention, delegate docx render, emit gap summary only | G | PASS | Mechanical |

## `references/grounding-rules.md`

| # | Rule | Origin | Verdict | Note |
|---|---|---|---|---|
| G1 | Unknown-marker table (`TBC`/`TBD`/`TBA`/etc.) — pick the one that names *why* | G | PASS | Markers themselves are the template's own vocabulary, not sample-derived |
| G2 | Never invent a marker outside the list | G | PASS | |
| G3 | Literal, not prescriptive — stay sourced; pair a gap with a one-line CS next-step, don't infer a fact | G | PASS (ex) | Rule and its swap-test-passing restatement are general; the worked example ("No numeric exit criteria discussed — Rohit prioritized...") is Fyno-specific and explicitly marked as illustration |
| G4 | "What they do" (§2): source only from pasted transcripts, never web search | G | PASS (ex) | Astra's public-info exception is *explicitly called out as not a path this skill takes on its own* — the file already does its own swap-test failure-handling correctly here. Good pattern to replicate elsewhere |
| G5 | "ROI they are targeting" (§5): label Zime's own benchmark numbers as Zime's claim, not client commitment | G | PASS (ex) | |
| G6 | Artifact/link fields: use "requested, not yet received/granted" over bare `TBC` when discussed-but-undelivered | G | PASS (ex) | |
| G7 | Human-only fields never filled, never asked for | G | PASS | See S8 |
| G8 | Acceptance checklist: never check from assumption a normal deal would have this by now | G | PASS | |
| G9 | Citation rule: coarse call-level link from raw transcript, finer per-item link from insight export, one citation per fact, fail-safe defaults to no marker over a broken one | G | PASS | Thorough and self-guarding already — the fail-safe section explicitly rules out constructing/guessing a URL from a pattern seen elsewhere, which is itself an anti-overfitting rule applied to citations specifically |
| G10 | Numeric/dated claims: traceable to a specific call; disagreement → most recent value, name the discrepancy inline | G | PASS | |
| G11 | **Keep the number, don't paraphrase into a duration** (added from Fyno feedback) | F→G | PASS (ex) | Rule is stated as a general predicate (a stated quantity gets carried as a number, not converted to qualitative/duration phrasing); Fyno's "~1,000 calls vs. 10-15" is the worked example. **Candidate for consolidation** — see rule-ledger action item below |
| G12 | §9 objections: answered is not closed, only explicit withdrawal removes it | G | PASS | |
| G13 | Word budget table: ~5-30 / ~35-60 / ~8-25 words per field shape | A+T | FLAG | The numeric bounds themselves are measured off exactly two documents ("Astra's Primary pain cell is 27 words; TrueFoundry's is 34"). Passes the swap test as a *category* (no client named), but the specific numbers have an N of 2 behind them — a third sample could show these bounds are too tight or too loose. Don't touch until D produces field-length data from a third client |
| G14 | §2 motion/tools describe the *client's* org, not Zime's proposed process — watch for same-call conflation | G | PASS | |
| G15 | §4 Primary pain (problem, client's words) vs. Key hooks (capability that resolved it) — don't conflate | G | PASS | |
| G16 | Trim connective prose first when over budget; never cut a stated number or named account first (added from Fyno feedback) | F→G | PASS | Already general as written — protects G11/M1 from being undone by G13 |
| G17 | §10/appendix: grounded only, no filler sentence without a specific line behind it | G | PASS | |

## `references/miss-prone-fields.md`

| # | Rule | Origin | Verdict | Note |
|---|---|---|---|---|
| M1 | **Named-account anecdotes as evidence for an already-derived risk/objection** (added from Fyno feedback) | F→G | PASS (ex) | Rule generalized as written (any named-account story tied to an existing risk hit gets carried as evidence); DCB Bank/Federal Bank is the worked example. Same consolidation candidate as G11 |
| M2 | Risk checklist: 8 standing conditions (unsigned paper, unengaged EB, single-threaded, unmet asks, deferred-but-assumed commitments, undated milestones, unfinalized commercials, new-to-systems stakeholder) | G | PASS | Generic GTM risk patterns, not client-specific; independently plausible without any sample. Lowest overfitting risk in the file |
| M3 | A checklist hit requires the sources to actually show the condition — absence of a topic is not evidence of the risk | G | PASS | |
| M4 | Persona table: Motivation = personal want sourced to what the person said; CS posture = behavioral instruction, not a mood adjective | G | PASS (ex) | The four worked rows are literally Astra/TrueFoundry stakeholders and their real tools (Fireflies, pentesting) — file explicitly flags this: "copy the *structure*... not the tool names or domain... which are specific to that deal." Already self-aware; the swap test given inline ("could this be copy-pasted onto a different stakeholder... without changing a word?") is the model for every other table in this ledger |
| M5 | §8 differentiation test (focus-first vs. first-interaction vs. do-not vs. chase) | G | PASS | |
| M6 | Insight-export routing map (Objections→§9, Action Items→§7/§8 by owner, Commitments→§4, Important points routed by content) | G | PASS | Describes a source *type* (Zime insight export), not a client — applies identically regardless of which client's export it is |
| M7 | Export severity tags are a hint, not a substitute for the derivation checklist | G | PASS | |

## `references/handover-template.md`

| # | Rule | Origin | Verdict | Note |
|---|---|---|---|---|
| H1 | Template structure itself (10 numbered sections + checklist + appendix) | A+T | FLAG | The *shape* of the form is fixed by Zime's actual process document, not something this skill invented from 2 samples — lower risk than it looks, since the form predates the skill. Still worth confirming with the expert in B whether any section is dead weight (see B's field-triage question) |
| H2 | "{current ops contacts}" templatized from literal "AV and Sajan" in both samples | A+T | PASS | Already correctly de-biased — explicit reconciliation note explains why (rotation changes, not a per-deal fact) |
| H3 | "Playbook resources" checklist item — TrueFoundry-only in the two samples, kept as a superset union | T | FLAG | Explicitly justified in-file as "not a per-deal quirk," but that justification hasn't been checked against a client where playbook resources genuinely don't apply — could still be a TrueFoundry-shaped assumption that every client has prior playbooks to hand over |
| H4 | §9 may legitimately stay blank if no distinct "why this could fail" narrative surfaced — not automatically a gap | A+T | PASS | Correctly framed as an absence-is-not-failure rule, matching M3's logic |

## `references/docx-layout.md`

Out of scope for this ledger — styling/rendering only, no content-extraction
judgment, so no overfitting-to-content risk. It carries its own honesty flag
already ("hex values read off the live template by eye... not sourced from
an official brand kit... confirm next time someone reviews a render") which
is the same discipline this ledger is applying to content rules.

## Summary

| Verdict | Count |
|---|---|
| PASS (rule and example both generalize) | 26 |
| PASS (ex) (rule generalizes, example is client-specific by design) | 11 |
| FLAG (unvalidated against a 3rd sample) | 4 — S9 (question caps), G13 (word-budget numbers), H1 (template shape), H3 (playbook checklist item) |
| FAIL (unrestatable without the specific) | 0 |

**Zero outright memorization** — every rule survives being stated without a
client name. That is a real, checkable claim about the skill's current
state, distinct from "the skill is unbiased": a rule can pass the swap test
and still be *wrong* because it was only ever tested against 2-3 samples
(the FLAG rows). The swap test catches memorization; it does not and cannot
catch a generalization that happens to be false. Only more labeled data
(workstream D) or expert correction (workstream B) catches that.

## Consolidation action taken

G11 (numbers) and M1 (named accounts) are two instances of one underlying
principle — specificity survives compression, generality is what gets cut —
identified from the Fyno failure pattern (see the plan's "Root cause,
restated"). Rather than leave them as two separate client-shaped rules,
`grounding-rules.md` now states the general predicate once and points G11/M1
at it as instances. See that file's new "Specificity survives compression"
section.
