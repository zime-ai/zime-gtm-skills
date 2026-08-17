Ran 10 registrations against `references/rubric.md`, no canonical framework, checks built from general partner-program practice.

| Registration | Flags | Evidence | Suggested action |
|---|---|---|---|
| REG-103 | End-client not distinct from partner; conflict/permission unverifiable as result | `end_client_name = Northlake Partners` (identical to `partner_name = Northlake Partners`) | Reject/return — confirm actual end-client entity, re-submit before conflict/permission checks mean anything |
| REG-107 | Conflict check not run; commercial terms not recorded | `conflict_check_done = (empty)`; `margin_tier = (empty)` | Hold — require conflict check result and margin/discount tier before accept |
| REG-104 | Conflict check found a real conflict, not cleared | `conflict_check_done = Yes - existing direct AE has an active opportunity with Echo Inc` | Do not register — route to house pipeline owner, resolve conflict before any registration |
| REG-102 | Partner identity ambiguous — no named contact | `partner_contact = (empty)` | Return to partner — get named contact before accept |
| REG-105 | End-client permission not confirmed | `permission_confirmed = No response yet - contact not confirmed` | Hold — do not let partner engage contact until confirmed |
| REG-108 | No expiry/protection window set | `expiry_date = (empty)` | Return — require expiry date, open-ended registration has no forcing function |
| REG-109 | Expiry window essentially already elapsed | `expiry_date = 2026-08-18` (today 2026-08-17, 1 day left) | Flag for renewal decision now, not after lapse |

Clean, no flags: REG-100, REG-101, REG-106.

7 of 10 registrations flagged
Most common flag: missing required field (contact / conflict check / commercial terms / expiry) — 4 of 7 flagged rows
