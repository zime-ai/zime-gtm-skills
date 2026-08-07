---
name: call-prep-note
description: Generate a pre-call sales prep note (hook, win condition, 3 moves, watch-outs) for one upcoming meeting from pasted call transcripts and, if connected, a CRM. Use whenever asked to "prep me for", "prep note for", "get ready for my call with", or similar, naming a specific customer/prospect meeting. Not for bulk/scheduled generation across many meetings, and not a transcript summarizer — it produces a forward-looking action note, not a recap.
metadata:
  zime:category: gtm
  zime:dimension: initiative
  zime:input-modes: [transcript, crm-mcp]
---

# Call prep note

Produces the same 4-part note shape Zime's own hosted product outputs — Hook,
Win condition, Your 3 moves, Watch out for — from whatever the user actually
has: pasted transcripts, an optional connected CRM, and their own stage
definitions. No hosted backend, no API keys, nothing leaves this session.

Read `references/note-format.md` before generating — it's the full output
contract (word caps, citation rule, the internal-call suppression case) and
is not repeated here.

## Step 1 — Config: load or interview

Check the current working directory for `prep-note-config.md`.

- **Present:** read it, use its domain(s)/stages/exit-criteria/milestones for
  everything below. Never re-ask.
- **Absent:** run the interview in `references/config-interview.md` once, write
  the file, then continue with this request using what was just gathered. If
  the user clearly wants to skip setup right now ("just do it," "skip that"),
  proceed using `references/stage-criteria.md`'s generic ladder instead —
  don't block the note on the interview.

## Step 2 — Gather what's available

1. **Transcript(s).** Use whatever the user pasted or pointed at for this
   account/deal. If more than one, note each one's date and attendee list —
   needed for the ranking rule below.
2. **CRM, if connected.** Check whether any currently-available tool looks
   CRM-shaped (deals/opportunities, contacts, accounts/companies — by
   capability, not by a specific server name; don't hardcode a vendor). If one
   exists, pull the deal/account: stage, close date, contact titles. If none is
   connected, or a call errors, continue without it — never block or ask the
   user to go connect one.
3. **The ask itself.** Which meeting, and anything the user already said about
   it (stage, stakes, who's attending).

**Internal-call check, before anything else generates:** if every named
attendee shares the user's own email domain, or the user describes it as
personal/1:1 with no external party, stop here — skip straight to
`note-format.md`'s suppression line and output nothing else.

## Step 3 — Rank past calls, if more than one transcript

Same rule the hosted product uses, applied to whatever transcripts exist
rather than to calendar history: tag each past call `attendee_overlap` (every
external attendee on it is also on today's call) > `partial_attendee_overlap`
(some overlap) > `unit_overlap` (same account/deal, no shared attendees).
Weight the highest tag most — it's what makes the note specific to today's
people, not generic to the account. The most recent `attendee_overlap` call is
"the last call" for the hook and Watch out for.

## Step 4 — Decide what's missing, ask at most 3 questions

Pick the 1–3 facts that would most change the note — usually from: current
stage (if no CRM and no config states it), who specifically is on today's call
and their role, what outcome the rep needs from this call, or a live objection
hinted at but not detailed in the transcript. Ask them together, once. If the
user doesn't answer or says to proceed anyway, generate with what exists —
never refuse and never loop back for more.

This intentionally departs from a batch/no-human deployment of this same
concept: there's a person here to ask, so ask, briefly, then commit to
generating.

## Step 5 — Generate

Follow `references/note-format.md` exactly for structure, word caps, the
numbering rule for the 3 moves, and the citation rule. Pull the moves' source
material from, in order: a live objection worth resolving today, then the
current stage's exit criteria (from config or `stage-criteria.md`'s fallback),
then any visible decision/timeline gap. Print the note and stop — no preamble,
no "here's your prep note," no explanation of what was fetched.

## What "done" looks like

A note that is Hook, then `🎯 **Win condition:**`, then exactly 3 numbered
moves, then a short "Watch out for" — or, for an internal call, the single
suppression line and nothing else. Every claim about what was said in a past
call carries a citation; forward-looking moves and the win condition do not
need one.
