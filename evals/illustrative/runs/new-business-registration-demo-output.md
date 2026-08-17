Ran structural sweep on 8 registrations against 6-dimension rubric (entity/domain, dedup check, source, ICP fit, requested support, expiry).

| Company | Submitted by | Dimensions missing |
|---|---|---|
| Acme Logistics | Alex | none — clean |
| TechFlow Systems | Jordan | none — clean |
| Rapid Fulfillment | Sam | Legal entity, domain, dedup check, source, ICP fit, requested support, expiry — **all 6 missing** |
| Coastal Industries | Maya | Domain missing (entity name present, no domain to disambiguate) |
| Metropolitan Finance | Casey | Legal entity missing (domain present) |
| Frontier Retail | Taylor | Dedup check not run |
| Valley Logistics | Riley | none — clean |
| Legacy Systems | Morgan | Expiry already passed (2026-07-01, today 2026-08-17) — stale/invalid registration |

Summary:

**Clean, approve:** Acme Logistics, TechFlow Systems, Valley Logistics.

**Need fix before approval:**
- Rapid Fulfillment — bare shell record, basically just a name. Send back entire.
- Coastal Industries — add domain (entity name alone risks parent/subsidiary confusion).
- Metropolitan Finance — add legal entity name.
- Frontier Retail — run dedup/conflict check before approving.
- Legacy Systems — expired, needs re-registration with fresh expiry window, not a rubber-stamp renewal.
