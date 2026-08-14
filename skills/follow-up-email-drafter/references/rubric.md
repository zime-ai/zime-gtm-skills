# Follow-up-email-drafter grounding rubric

Reuses `mutual-action-plan`'s `heard`/`inferred` distinction as the
internal check before drafting each line of the email. The difference
here: those tags never surface in the deliverable itself. The email is
customer-facing text, so the tags stay in the grounding notes section
below it.

## The check, per claim

For every concrete claim a drafted line would make — a next step, a date,
a recap of what was agreed, a specific number or name — ask:

1. **Was this actually said?** Find the line in the transcript. If you
   can't quote it, it isn't `heard`.
2. **Was it agreed, or just raised?** A prospect saying "we might look at
   X at some point" is not the same as "let's do X by Friday." The first
   is a hand-wave; the second is an agreement.
3. **Is there a real trigger?** A date, or an event with an obvious,
   checkable occurrence. "Soon," "at some point," "eventually," or "before
   the quarter closes" with nothing more specific fails this element.

## Tagging

- **`heard`** — the claim, and enough of its specifics (date, owner,
  scope), were actually said on the call as an agreed fact. Quote it.
- **`inferred`** — the claim is a reasonable next step given the call, but
  wasn't stated as an agreed fact, or is missing a date/owner/specific
  enough to state as fact. Quote the closest thing said.

## What to do with each tag when drafting

- `heard` → state it plainly in the email: "As discussed, I'll send the
  proposal over by Thursday."
- `inferred` → either:
  - Phrase it as the rep's own proposal, not a recap: "I'd suggest we
    loop in your security team early — happy to set that up whenever
    works." This is honest because it reads as the rep suggesting
    something, not recapping something agreed.
  - Or leave it out of the email entirely if it's too thin to even
    propose usefully.
  - Either way, list it in the grounding notes as something to confirm
    before sending — the rep may know context the transcript doesn't
    capture, and this is where they say so.

## The failure mode this guards against

A shallow drafter treats every next-step-shaped moment in a call the same
way and writes them all as agreed facts. The tell: a vague, hedged, or
one-sided moment ("we might," "at some point," "I'll have to check")
shows up in the email body as a stated commitment ("I'll get back to you
on X" or "we'll schedule Y for next week") with no hedge at all. That's
the exact case this rubric exists to catch — the moment must be caught at
the tagging step, downgraded to `inferred`, and drafted as a proposal or
dropped, not smoothed into a confident recap line.

## Nothing concrete to follow up on

If every substantive moment in the call comes back `inferred`, or the
call simply didn't produce a next step, don't draft an email that invents
one to fill the space. Say so, and draft the minimal honest version: a
short "great talking with you" recap of what was discussed, no fabricated
ask or date.
