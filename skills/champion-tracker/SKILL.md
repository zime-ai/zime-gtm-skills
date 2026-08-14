---
name: champion-tracker
description: Tracks champion strength across a deal's call(s) — builds an action ledger, one row per named contact per cited quote, tagging each as either an act of internal selling (looping in a stakeholder, pushing back for the rep in a room the rep wasn't in) or mere positive sentiment (encouraging words, no action), then reads the trend across calls. Use when a rep or manager wants to know if a deal actually has a champion or just an enthusiastic contact, especially before a forecast call or a stalled deal review.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript
---

# Champion Tracker

Tracks champion strength across a deal's call history. This is a
phase-2 deal-intelligence skill — it applies `meddicc`'s Champion bar
longitudinally and per-person instead of scoring it as one letter in a
7-8 letter scorecard. Where `meddicc` asks "is there a champion, this
call?", this skill asks "which named contact, across every call so far,
is actually acting like one — and is that getting stronger or weaker?"

## When to use this

- A rep wants to know whether a contact who sounds enthusiastic is
  actually doing anything for the deal, before calling them a champion in
  a forecast update.
- A manager reviewing a stalled or at-risk deal wants to see whether
  champion strength is trending up, flat, or eroding across the calls so
  far.
- Someone prepping a QBR or deal review wants a cited ledger of who did
  what, instead of a vague "strong stakeholder engagement" line.

## Inputs

One or more call transcripts from the same deal. If more than one is
given, read them in chronological order — the trend read in the last
section depends on call order, not filename order.

## Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run champion-tracker on ./calls/call1.txt ./calls/call2.txt"
```

Read every transcript given, in order. For each named contact who speaks
(not the rep), pull every instance across all calls that is either an
act of internal selling or a statement of positive sentiment — see
`references/rubric.md` for the exact test and worked examples. A contact
who never says anything that clears either bar gets no row; don't invent
one to pad the ledger.

## Champion definition

Reused verbatim from `meddicc`'s Champion letter (see
`skills/meddicc/references/rubric.md`): someone inside the account who
will sell on the rep's behalf when the rep isn't in the room — actively,
not just someone who likes the product. Evidence of the champion *doing*
something (looping in a stakeholder, pushing internally), not just saying
positive things to the rep. This skill applies that exact bar to every
named contact, across every call, instead of scoring it as one line in a
bigger rubric.

## Action ledger

One markdown table, one row per cited instance, in call order:

| Contact | Call | Quote | Tag | Why |

- **Tag** is `Action` or `Sentiment` — see `references/rubric.md` for the
  test. Never a third value, never "leaning champion" — a row is one or
  the other.
- **Why** is one short phrase naming what the action was (e.g. "looped in
  procurement") or what the sentiment was (e.g. "praised the demo").
- No row ships without its quote. A contact with no cited row doesn't
  appear in the ledger.

## Champion read

After the ledger, name the strongest champion candidate (the contact
with the most/strongest Action rows), or state there is no champion
candidate if every contact's every row is Sentiment — see "no champion,
only a friend" below. Don't call someone a champion on sentiment alone,
no matter how enthusiastic the language.

## Trend

If 2 or more calls were given: one line — **strengthening**, **flat**, or
**weakening** — comparing the champion candidate's Action rows across
calls (more/stronger actions later = strengthening, same = flat,
fewer/absent after being present = weakening). Cite the specific rows the
call is based on.

If only one call was given: **"insufficient history"** — don't guess a
trend from a single data point.

## The "no champion, only a friend" finding

If every named contact's every row across every call is Sentiment, say so
explicitly as the headline finding — "no champion, only a friend" — not
softened into "strong stakeholder engagement" or similar. An account full
of people who like the product but never act for it is a real risk
signal, not a strength to report.

## Sample data

`assets/sample-call-1.txt` and `assets/sample-call-2.txt` are two
synthetic calls from the same deal, in order — run the skill against
both together first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
