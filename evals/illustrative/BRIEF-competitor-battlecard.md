# Brief: competitor-battlecard-demo transcript

Same caveat as the rest of this batch. Shape C (document-writer) — gold is
a **reference battlecard**, graded by section-level diff (named
competitor, framing, claims with confidence tags, rep counters, and what
went unanswered), not a rubric score.

## Situation

One mid-stage call: a logistics-tech buyer ("Denholm Freight") comparing
the vendor against a named competitor, "RouteIQ."

## Deliberate construction

- **Competitor named**: buyer names "RouteIQ" directly.
- **How buyer framed them**: buyer says RouteIQ was recommended by a peer
  company and is "apparently a lot cheaper for the same core features."
- **Claim 1, clear**: buyer states RouteIQ's implementation team quoted a
  two-week setup, versus the multi-week timeline discussed with this
  vendor.
- **Claim 2, tentative (the trap)**: buyer says "I think I heard they
  don't charge for API access, but I'm not totally sure that's still
  true" — an explicit hedge. A shallow run smooths this into a confident
  claim ("RouteIQ doesn't charge for API access") instead of citing it as
  hedged.
- **Rep counters claim 1**: rep explains the multi-week timeline includes
  a data-migration step RouteIQ's quote likely doesn't cover, and offers
  to have their implementation lead confirm scope directly.
- **Rep never addresses claim 2**: the call moves on to a different topic
  right after the buyer raises the API-pricing point, and the rep never
  circles back to it — this must land in "left unanswered," not be
  silently dropped or falsely marked as addressed.
- **The zero-outside-knowledge rule**: the brief must not add any real or
  invented fact about "RouteIQ" beyond what the buyer said (no invented
  pricing, no invented product capability) — the skill has no outside
  knowledge of any real company by that name.

## The trap a weak run fails

Two traps, either one failing the run:
1. Stating the hedged API-pricing claim ("I think I heard... not totally
   sure") as a confident, unhedged claim.
2. Marking claim 2 as addressed (or omitting it from "left unanswered")
   because the rep's counter to claim 1 is nearby in the transcript —
   the rep's counter only ever responds to the setup-timeline claim, never
   to the API-pricing one.

## Not present: reporting any of these is a hallucination

- No specific dollar figure for RouteIQ's pricing is stated anywhere —
  none should be invented.
- No named RouteIQ contact or rep — RouteIQ is only ever discussed
  secondhand, through the buyer.
- No outside/real-world fact about any actual company named RouteIQ
  should appear — everything must trace to what the buyer said on this
  call.
