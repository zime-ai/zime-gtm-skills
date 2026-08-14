# Competitor battlecard rubric

## The no-outside-knowledge rule

This skill has zero information about any competitor beyond what the
transcript says. Every sentence in the battlecard traces to a quote or
timestamp in the transcript in front of it — never to what the model
happens to know (or believe) about that competitor's real product,
pricing, market position, or actual weaknesses.

An unsourced competitor fact does not ship even if it happens to be true.
"TrackWell's mobile app is known to crash frequently" is a fabrication if
no one on the call said it, regardless of whether that claim is accurate in
the real world — this skill has no way to know that, and must not act like
it does. The only test for whether a line belongs in the battlecard is
"did someone say this on this call," never "is this true about the
competitor."

This also rules out filling gaps with generic competitive-selling
knowledge — no "competitors in this category typically underprice on
enterprise deals" type filler. If the transcript didn't say it, it isn't in
the card.

## No competitor named

If nothing in the transcript names a competitor or an alternative —
including "doing nothing"/sticking with the status quo, which counts as a
competitor per `meddicc`'s Competition dimension (what else the prospect is
evaluating, formally or informally, including doing nothing) — stop after
step 1 and say so plainly: no competitor was named on this call. Do not
invent a hypothetical competitive frame to complete the rest of the
template. A battlecard for a competitor nobody mentioned is exactly the
kind of fabrication this skill exists to prevent.

## Claim confidence test

Tag each claim in section 3 (what the buyer said the competitor does
better/differently) as **clear** or **tentative** — the same test
`win-loss-brief` uses for driver confidence:

- **Clear** — the buyer states the claim plainly and unhedged (a specific
  capability, a specific number, a direct comparison stated as fact).
- **Tentative** — the closest thing said is a hedge, a guess, secondhand
  information ("someone on our team said..."), or an unconfirmed aside.
  Quote it exactly as hedged. Do not smooth a tentative claim into
  confident language, and do not drop it just because it's uncertain —
  cite it as uncertain.

## Left unanswered

A claim belongs in section 5 only if the rep never addressed it anywhere
later in the same call — not just immediately after the buyer raised it.
Re-check the rest of the transcript before listing a claim as unanswered;
if the rep circles back to it later, it belongs in section 4 instead, not
section 5.

## Evidence rule

Every element in every section — the competitor mention, the framing, each
claim, each rebuttal, each unanswered item — cites its quote or timestamp.
An element with no cited evidence does not ship.

## Reads-well-too check

A call where the rep countered every claim the buyer raised should come
back with an explicit "rep addressed everything raised" in section 5, not
a manufactured gap to make the section look populated. Likewise, a call
with only one buyer claim about the competitor should produce a battlecard
with one claim in section 3, not padded with invented ones to look
thorough.
