No column missing — all synonyms matched (stage, deal_name, owner, created_date, last_activity_date, close_date, deal_value, contacts, meetings_held, meeting_outcome, prospect_replied all present). Scope: 8/8 rows Prospect stage.

| Deal | Flags | Evidence | Suggested action |
|---|---|---|---|
| StaleVenture Corp | 5 — No two-way engagement, No meeting held, Single-threaded unresponsive, Aged no activity, Close date past | `prospect_replied = No`, `meetings_held = 0`, `contacts = David Foster` (1, unresponsive), `created_date = 2026-05-15` / `last_activity_date = 2026-05-16` (sat 94 days, no activity since), `close_date = 2026-08-10` (past today 2026-08-17) | Dead deal — pull from pipeline or force real re-engagement now |
| NoEngagementVenture | 3 — No two-way engagement, No meeting held, Aged no activity | `prospect_replied = No`, `meetings_held = 0`, `created_date = 2026-07-05` / `last_activity_date = 2026-07-06` (sat 43 days, no activity since) | No prospect signal ever — verify still live before next review |
| AgedOnceActive | 1 — Aged no activity | `created_date = 2026-06-19` / `last_activity_date = 2026-06-20` (sat 59 days since, nothing after one early meeting) | Went quiet after early meeting — check if it stalled |
| CrossStateServices | 1 — Close date past | `close_date = 2026-08-10` (past today 2026-08-17), still `stage = Prospect` | Update close date or advance stage — engagement itself looks fine |
| PlaceholderDeal LLC | 1 — Placeholder deal | `deal_value = (empty)` | Get rep to enter real deal value |
| TechStartup Inc | Clean | — | — |
| RetailBrand Ltd | Clean | — | — |
| SingleReply Inc | Clean | — | — |

5 of 8 deals in Prospect pipeline flagged
Most common flag: Aged with no activity
