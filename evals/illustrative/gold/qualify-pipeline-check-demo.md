# Gold label: qualify-pipeline-check-demo.csv

Computed by hand from `references/rubric.md`'s exact six-flag system against
2026-08-17. This rubric is deterministic — every cell below is a fact, not a
judgment call, unlike the transcript-audit gold files.

## Expected output table (flagged deals first, ordered by flag count descending)

All flagged deals listed with their flags and evidence. Clean deals are rows
that must appear in the output but with zero flags.

| Deal | Flags | Flag numbers | Evidence |
|---|---|---|---|
| Phantom Startup | 6 | 1,2,3,4,5,6 | buyer_role=(empty); pain=(empty); budget=(empty), amount=(empty); close_date=2026-08-20 < procurement_timeline=2026-09-15; next_step=(empty); meddicc_score=(empty) |
| Future Forward Consulting | 1 | 4 | close_date=2026-09-15 < procurement_timeline=2026-10-01 |
| Horizon Development Corp | 1 | 1 | buyer_role=(empty) |
| Nexus Technologies | 1 | 2 | pain=(empty) |
| Rapid Deployment Systems | 1 | 4 | close_date=2026-08-25 < procurement_timeline=2026-09-15 |
| Velocity Analytics Group | 1 | 5 | next_step=(empty) while status=Active |
| Enterprise Solutions Partners | 1 | 6 | meddicc_score=(empty) |
| Tech Innovations Inc | 0 | none | clean |
| Global Logistics Solutions | 0 | none | clean |
| Strategic Partners Ltd | 0 | none | clean |

Closing lines expected:
1. **"7 of 10 deals in Qualify pipeline flagged"**
2. **"Most common flag: close date sooner than procurement timeline (3 deals)"** — appearing on Phantom Startup, Future Forward Consulting, and Rapid Deployment Systems.

## The traps (findings a correct run must get right)

1. **Phantom Startup must flag all 6 checks**: empty on buyer, pain, budget,
   amount, close_date, next_step (while actively worked), and meddicc_score.
   Every cell that a check reads is empty, triggering every flag.

2. **Strategic Partners Ltd must NOT flag on budget (flag #3)**: even though
   the explicit `budget` field is empty, the `amount` field is 55000. The
   rubric says "Flagged only if **both** the budget field and the deal value
   field are empty" — a deal with a value number standing in satisfies the
   budget-signal check. Flagging this deal on budget is the critical trap.

3. **Future Forward Consulting and Rapid Deployment Systems must be the only
   flag #4 instances**: both have close dates sooner than their stated
   procurement timelines. No other deal has this condition.

4. **Rows 1, 2, and Strategic Partners Ltd (Row 4) must all be Clean (0
   flags)**: tests the reads-well-too requirement — the sample must include
   at least two genuinely healthy deals, and here we have three. If the skill
   flags any of these on any check, it has misunderstood the rubric.

5. **The six flagged deals must sort correctly**: flagged deals ordered by
   flag count descending (Phantom Startup at 6 flags first, then six 1-flag
   deals). Within ties, order doesn't matter per the skill spec, but all
   flagged deals must come before clean deals.

## Not present: reporting any of these is a hallucination

- Any flag on Tech Innovations Inc, Global Logistics Solutions, or Strategic
  Partners Ltd (all are clean).
- A seventh flag type or a different count than 1-6 for any flag.
- An inferred buyer name, pain statement, or next step not present in the
  CSV cell.
- A claim that any of the six flagged deals is not in scope (all ten rows are
  in the Qualify stage, all are in scope).
- A closing line that does not match the format specified in SKILL.md ("N of
  M deals in Qualify pipeline flagged" and "The single most common flag is
  [flag name]").
