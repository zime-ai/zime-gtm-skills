# Token reference

Run `python3 scripts/tokens.py` for the live, authoritative list grouped by
slide — this file is the *source* for each token, not the schema (the schema
is discovered from the template, never hand-maintained twice).

| Token | Source | Citation requirement |
|---|---|---|
| `CLIENT`, `CLIENT_SHORT`, `CLIENT_SHORT_UPPER`, `CLIENT_UPPER` | given (client's name) | — |
| `CHAMPION_FIRST`, `CHAMPION_TITLE` | given / CRM contact record | — |
| `CHAMPION_GOAL` | a transcript | quote verbatim, cite the call |
| `CHAMPION_QUOTE` | a transcript | quote verbatim, cite the call |
| `INITIATIVE_NAME`, `RUBRIC_NAME` | chosen from the initiative catalogue (slide 12) | — |
| `BLOCKER_1..3_{TITLE,DESC}` | transcripts | each traceable to a specific call moment |
| `ROOT_CAUSE_1..2` | a transcript | where their best practices actually live today (a person, a recorder tool) |
| `RISK_1..4_{LABEL,STAT,DESC}` | CRM math (show the arithmetic) or a figure the client stated on a call | never invented — `[[TBD: ...]]` if neither source has it |
| `NEED_1..5_{TITLE,DESC}` | derived from the champion's goal + chosen initiative | — |
| `STEP1_SUBTITLE`, `STEP2_TITLE` | derived from the chosen initiative (verb differs: "apply to every deal" for a sales motion vs. "expand every account" for a CS motion) | — |
| `METRIC_PRODUCTIVITY`, `METRIC_TIME_SAVED`, `METRIC_HEADCOUNT_SAVED`, `METRIC_WIN_RATE` | benchmark from a comparable past deal, or `[[TBD]]` | never invented |
| `ROI_HEADLINE_STAT`, `ROI_HEADLINE_DESC` | CRM math, arithmetic shown | never invented |
| `ACV_TOTAL`, `ACV_TOTAL_LINE`, `LINE_1..2_{LABEL,PRICE,DESC}` | the user's prompt (commercials aren't in any transcript/playbook/CRM) | `[[TBD: commercials not yet agreed]]` if not given |
| `STEP_1..4_TASK`, `STEP_3_LINK`, `STEP_4_LINK`, `STEP_ETA_TBC` | the call's agreed next steps | each an actual agreed action, not a template guess |
| `STACK_TOOL_1`, `STACK_TOOL_2` | their actual recorder + CRM tool names, from a transcript or CRM | — |
| `CLIENT_TOOLS` (slide 9, pre-POC only) | their actual tool names | — |
| `KPI_*_LINE` (slide 9, pre-POC only) | derived from initiative + goal | — |
| `POV_W1..3_TASK1..2_{TITLE,DESC}`, `POV_OUTCOME_1..2` (slide 20, pre-POC only) | the agreed POV plan | — |

## `remove_slots` — optional slots

Some slots are optional in the source decks (e.g. Astra used all 5 `NEED_*`
slots and all 4 `STEP_*` next-steps rows, but a thinner deck might not need
all of them). To drop one, add it to `remove_slots` in the spec by its slot
prefix (the token minus its `_TITLE`/`_DESC`/`_TASK` suffix):

```json
"remove_slots": { "6": ["NEED_5"] }
```

The slide-number key is organizational only — slot names are unique across
the whole template, so `fill.py` matches by slot name regardless of which
slide key it's filed under.
