# POC/pilot exit rubric

Eight dimensions covering whether a completed pilot's exit review actually
established a documented, evidenced pass — not just a good conversation.

## Rules and false positives

Three rules apply to every dimension.

- **The buyer must say it.** Results, validation, and sign-off count only when the buyer or the end users say them. Results that only the rep reports score Missed. A champion who speaks for the whole team is not validation by end users.
- **Absence is a result.** A dimension that the call never touched is Missed. Do not credit it because the pilot felt successful.
- **Read the false-positive line before you write Covered.**

False positives to remove before you score:

- "It went well" or "the team is happy" with no criterion and no number.
- Early pilot feedback or a general user's praise. It is not adoption and not a verdict against a criterion.
- Benchmarks that the vendor set. The buyer's own baseline is the one that counts.
- Sign-off that the rep assumes because the champion seemed satisfied. Silence is not a yes.
- A gap that the rep calls minor and the buyer never accepted as minor.

A strong exit review has the sponsor say the pilot passed in their own words, has each criterion verdict-ed, and gives every open product gap an owner and a date.

## 1. Every success criterion verdict-ed individually

**What it is.** The success criteria agreed at kickoff — the specific
metrics, thresholds, and must-pass use cases — each get their own verdict:
met, not met, or unmeasured.

**Covered vs. a miss.** Covered looks like each criterion named at kickoff
getting its own line: "sub-2s query latency — met, averaged 1.4s"; "SSO
integration — not met, still pending." A miss looks like the call
collapsing everything into one blended "it went well" verdict that hides
which specific criteria actually passed.

**Weak:** "The pilot went really well overall, the team was happy." **Strong:**
"Of the four success criteria — latency, uptime, SSO, and report accuracy —
three passed and SSO did not; procurement flagged it as a blocker for
production."

## 2. Result quantified against a stated baseline

**What it is.** The result is a number compared against a baseline
measured before the pilot started, not an assertion of success.

**Covered vs. a miss.** Covered looks like "cut error rate from 12% to 5%,"
a before/after pair either side stated on the call. A miss looks like
"results were great" with no baseline or number ever named.

**Weak:** "Their team saw a big improvement." **Strong:** "Response time
dropped from an 18-hour average to under 4 hours, which the ops lead
confirmed against their own ticket log."

## 3. Validated by actual end users, not only the champion

**What it is.** The people who used the pilot day to day — not just the
champion who sponsored it — confirmed the result themselves.

**Covered vs. a miss.** Covered looks like a named end user's own quote or
a stated field-team validation step. A miss looks like the champion
speaking for the whole team with no one who touched the product weighing in.

**Weak:** "Our champion says the team loves it." **Strong:** "Three of the
five analysts who ran the pilot were on this call and each confirmed the
dashboard replaced their manual export."

## 4. Explicit sponsor / economic-buyer sign-off

**What it is.** The person who controls budget and the final decision has
explicitly signed off that the result counts as a pass — not implied,
delegated, or still pending.

**Covered vs. a miss.** Covered looks like the economic buyer's own
statement on the call or in writing that the pilot passed. A miss looks
like sign-off assumed because the champion seemed satisfied, or deferred to
"I'll check with my boss" with no follow-up confirmed.

**Weak:** "I think leadership will be fine with this." **Strong:** "Our VP
of Ops, who owns this budget, said on the call: 'this clears our bar, let's
talk contract.'"

## 5. Production-readiness blockers surfaced

**What it is.** Remaining blockers to going live — security review,
procurement, integration work — are named explicitly rather than left
unaddressed.

**Covered vs. a miss.** Covered looks like "security review is still
outstanding, expected to close in two weeks" stated plainly. A miss looks
like the call ending with no mention of what stands between this pilot and
a production rollout.

**Weak:** "We're basically ready to go." **Strong:** "The only open item is
a SOC 2 review their infosec team is running, targeted to close by the 15th."

## 6. Commercial next step named, with an owner and a date

**What it is.** A specific next step — a proposal, a contract review, a
renewal conversation — with a named owner and a date, not an open-ended
close.

**Covered vs. a miss.** Covered looks like "Legal will have the redlined
contract back to us by Friday, owned by their procurement lead." A miss
looks like "we'll follow up soon" with no owner or date attached.

**Weak:** "We'll circle back after the holidays." **Strong:** "Their CFO
committed to a signed PO by end of quarter, contingent on the SOC 2 review
above closing first."

## 7. What was NOT delivered, and whether that gap is fatal

**What it is.** What the pilot did not cover or did not deliver is named,
along with a plain statement of whether that gap kills the deal or is
acceptable to move past.

**Covered vs. a miss.** Covered looks like "we didn't test the bulk-import
path, and they said that's fine since they migrate manually anyway." A miss
looks like the scope that didn't get tested going unmentioned entirely.

**Weak:** "There's a little bit left to figure out." **Strong:** "Mobile
push notifications weren't in scope for this pilot; the prospect confirmed
that's a nice-to-have for phase two, not a blocker."

## 8. Reads-well-too test

Sanity-check against a pilot you know genuinely succeeded and was closed
out well. If it still comes back mostly Missed, loosen the read before
reporting.
