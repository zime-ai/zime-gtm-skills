---
name: adoption-leaderboard
description: Scores a rep's or a team's recent sales calls against a fixed set of five winning-behavior checklists (rapport, upsell signals, renewal risk, customer experience, value realization), then ranks reps lowest-adoption-first so the highest-leverage coaching targets lead. Use when running a team calibration, prepping 1:1 coaching from real call evidence instead of impressions, or checking whether a specific behavior is actually landing across a book of calls.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Behavior adoption
  zime:input-modes: transcript,connector
---

# Behavior Adoption Leaderboard

Scores a set of recent sales calls against five fixed behavior checklists
(`references/behavior-checklists.md`) and ranks reps by adoption, lowest
first — the reps most in need of coaching lead the report, not trail it.

Run this end to end in one pass. Don't stop to ask which calls to include,
who's internal, or how to interpret an ambiguous call — apply the default
rule in the relevant step below, decide it yourself, and note the assumption
once. The user can correct any assumption after seeing the leaderboard;
that's a quick re-run, not a precondition for the first one.

## When to use this

- Prepping a 1:1 or team coaching session from call evidence instead of
  manager impression.
- Running a team calibration: which behaviors is the team actually landing,
  and which reps most need attention.
- Checking whether a specific behavior (e.g. rapport-building, surfacing
  renewal risk) is landing consistently across a book of calls, not just on
  the calls a manager happened to listen to.

## Step 1: Choose an input source

Two modes. Neither is the "real" one — use whichever the user has.

**Connector mode** — if this conversation has tools that can (a) list or
search meetings/calls and (b) return call transcripts, use them. Match by
capability, not by brand or vendor: any pair of list-calls + get-transcript
tools works, whatever the source is called. If several are connected, prefer
the one with organization-wide coverage and speaker emails on calls; say
which one you picked and why. Verify the choice with one cheap call: list a
single recent meeting before proceeding.

**Local mode** — if no such tools are present, or the user points at a
directory instead, read transcript files directly:
`.txt`/`.vtt`/`.json`/`.md`, same formats every other skill in this repo
accepts. Speaker labels carry attribution when the source provides them;
where they don't (generic "Speaker 1" labels), infer rep vs. external
participant from context and state the inference once — see Step 3's edge
handling.

If both a connector and local files are available, ask the user which to
use; otherwise proceed on whichever exists without asking.

## Step 2: The behaviors being scored

Five fixed checklists, defined in full in
`references/behavior-checklists.md`: **Rapport**, **Upsell opportunities**,
**Renewal challenges**, **Customer experience**, **Value realization**. Each
carries one or more numbered checklist items (`CH1.1`, `CH2.1`, etc.) that
get scored per call in Step 4. This skill scores against this fixed set —
it doesn't take a custom behavior list.

## Step 3: Gather calls

1. **Connector mode**: query workspace-wide, not just the calling user's own
   calls — a personal/service-account scope often returns almost nothing.
   Pull newest first, using the tool's date range and pagination options.
   **Local mode**: read every transcript file in the directory the user
   pointed at.
2. Keep only external sales calls: at least one participant outside the
   selling org. Ask the user for the org's own email domain if it isn't
   obvious from the data; if genuinely unavailable, infer internal vs.
   external from the majority participant domain across the files and state
   that inference once. Skip internal-only meetings, all-hands, recruiting
   interviews, and calls where the org is clearly the *buyer* being pitched
   by an outside vendor (see Step 4 for how to tell from the transcript).
3. Target coverage before settling: at least 10 qualifying external calls
   and at least 5 distinct reps, where that many exist. If the first pull is
   thin, widen the window (connector mode: further back in history; local
   mode: check for more files) before settling for less. Never ask
   permission to widen — just widen.
4. Cap scoring at the 10 most recent qualifying calls. Label them C1
   (newest) to C10. Label distinct reps S1, S2, … and keep a legend (name to
   label) for your own bookkeeping — the legend and the raw per-call grid
   are internal working state, never shown in the final output.
5. Fetch and score calls one at a time (Step 4) rather than accumulating raw
   transcripts — keep only the scores, the legend, and one short evidence
   quote per satisfied item.

## Step 4: Score each call

Full discipline in `references/scoring.md` — read it before scoring the
first call. In short: every checklist item gets exactly 1 (transcript shows
a rep doing it, with a quote as evidence) or 0 (absence is the evidence), no
partial credit, no hedging language on an individual mark. Decide
selling-vs-buying and internal-vs-external from transcript evidence, never
by asking.

## Step 5: Build the leaderboard

Roll per-item scores up to adoption percentages per `references/scoring.md`,
then:

1. **Table** — rows are reps ordered by overall adoption, lowest first;
   columns are Rep, Adoption (overall), then one column per behavior using
   its title (never `BH1`/`BH2` codes). Every cell a whole number with a `%`
   sign, e.g. `43%`. No calls column, no internal grid.

   ```
   | Rep | Adoption | Rapport | Upsell opportunities | Renewal challenges | Customer experience | Value realization |
   |---|---|---|---|---|---|---|
   | S1 | 24% | 0% | 20% | 0% | 40% | 20% |
   | S2 | 46% | 40% | 33% | 60% | 40% | 60% |
   ```

2. **Leaderboard narrative** — lead with the team pattern: name the two or
   three behaviors with the lowest adoption across the whole team, since
   those are the biggest, most actionable gaps. Then, lowest-adoption rep
   first, always show at least the bottom 5 reps (all of them if 5 or
   fewer): their current adoption, the behaviors dragging it down, and for
   each the one or two checklist items they miss most, with what to coach.
3. Summary line, filled from the actual data: "X of Y reps consistently run
   these behaviors today (adoption 50% or higher); the rest do not."

Stop there. No projection table, no outreach step — the leaderboard and the
coaching notes are the deliverable.

## Sample data

`assets/` ships 6 short synthetic transcripts across 4 reps (`S1`–`S4`), a
deliberately mixed spread — some reps land most behaviors, some land almost
none. Run local mode against `skills/adoption-leaderboard/assets/` first:

```bash
claude "run adoption-leaderboard on skills/adoption-leaderboard/assets/"
```

## What this does not do

No API calls beyond whatever connector the user already has open, no
telemetry, no data retention beyond the current session, no outreach or
email step. It reads what you point it at (or what a connector already
present in the conversation returns) and nothing else.
