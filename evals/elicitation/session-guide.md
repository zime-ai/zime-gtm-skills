# Elicitation session guide — sales-to-cs-handover framework extraction

One long live session with the teammate who holds the real handover
framework in his head. Method: Critical Decision Method (CDM), a
retrospective cognitive-task-analysis interview built for exactly this
problem — extracting an expert's decision cues without asking the expert to
describe his own process, which the literature is consistent experts
under-report when asked directly.¹

**Do not send this guide to him beforehand.** He should not prep, and should
not see the skill's current template/rules first — both anchor him to the
existing structure instead of his own. Record the session (Zime records
calls) — the recording is itself durable, reusable data, not a one-off.

## Before the session

Pick two real past deals he ran, together with him or from what's on file:

- **Deal A — went well.** A handover CS accepted cleanly, ideally one that
  later showed the handover actually helped (fast ramp, no reopened
  questions).
- **Deal B — went badly or surprised him.** A handover CS bounced back, a
  risk that materialized post-handover, or a client reaction that didn't
  match what was written. Failure cases carry more decision-cue density
  than clean ones — this is the CDM literature's own finding, not a guess.

Have the actual transcripts/call recordings for both on hand if he wants to
point at a specific moment. Not required reading beforehand — a memory jog,
not a prep packet.

## Session structure (90 min planned, first item never gets cut if time runs short)

### 1. CDM walkthrough — Deal A, then Deal B (45-50 min, ~25 min each)

Two passes per deal, not one:

**Pass 1 — chronological retelling.** "Walk me through this deal from first
call to handover, in order." Don't interrupt. Note timestamps/turning points
as he talks — these become your probe targets in pass 2.

**Pass 2 — re-walk, probing at each turning point you noted.** For each one:
- "What did you notice right there that made you do X?"
- "What would a rep two years newer than you have missed at that moment?"
- "What almost went into the handover doc here, and what made you cut it?"
- "If that fact had been different, what would you have written instead?"

The third question is the highest-value one in the whole session — it
surfaces his *rejection* criteria, which the current corpus has zero of
(every ground-truth doc is an accepted final draft; none show what got cut
and why).

### 2. Question-bank capture (20-25 min)

"When your colleague dumps a transcript into Claude and asks you things —
what does he actually ask? Give me your own version: if I handed you a raw
transcript right now, what's the first question you'd ask about it?"

Push for specifics, not categories. Target 30-60 real questions, written in
his own words. Follow-ups: "what would you ask next, depending on the
answer?" — this captures the *iteration* his query-driven approach relies on,
which a single field-driven pass can't replicate.

Do not let this collapse into re-deriving the template's own field labels —
if an answer is just "I'd check the champion," push once more: "check for
what, specifically, that makes a champion count vs. not count?"

### 3. Negative examples (15 min)

"Show me a draft handover — yours or someone junior's — that you sent back.
What was wrong with it, in your words?" If none exist on file, do it live:
show him a real skill output (e.g. the Fyno one) and ask him to mark it up
the way he'd mark up a junior's draft. Capture the actual marks and his
stated reason for each, not a paraphrase.

### 4. Field triage (10 min, drop first if time is short)

Walk `handover-template.md`'s 10 sections with him, one line each: "Do you
read this section when CS hands you — sorry, when you receive a handover?
Do you act on it, or skip it?" Flag anything he skips consistently — that's
where generalization effort is wasted regardless of how well it's solved.

## After the session

1. Transcribe/paste the recording into
   `evals/elicitation/session-01-transcript.md` (gitignored — real deal
   names will surface).
2. Extract the question bank verbatim into
   `evals/elicitation/question-bank.md` — his words, not a paraphrase into
   template-field language. That paraphrase step happens later, in
   workstream C, and should be visible/reversible, not baked in at capture
   time.
3. Extract negative-example marks into
   `evals/elicitation/rejection-criteria.md` — one row per mark: what was
   there, what he said was wrong with it, what he'd have written instead.
4. Hand all three to whoever runs workstream C — that's where the question
   bank becomes an actual skill step, not before.

## What this session cannot do

One session with one expert is not a second sample size any more than a
third client's GT doc would be — it's a different *kind* of evidence
(procedural/tacit vs. document/declarative), and the two should be
triangulated against each other, not treated as interchangeable. If his
question bank and the existing field list mostly overlap, that's a genuine
finding (the template already covers his framework) — not a null result to
discard.

---
¹ Hoffman, Crandall & Shadbolt, "Use of the Critical Decision Method to
Elicit Expert Knowledge" (1998),
https://journals.sagepub.com/doi/10.1518/001872098779480442 — CDM's
retrospective-incident-probe structure is what sections 1-3 above follow.
