# Gold label: new-business-registration-demo.csv, audited against `new-business-registration`

Computed by hand from `references/rubric.md`'s six dimensions and
`evals/illustrative/BRIEF-new-business-registration.md`'s construction,
against today = 2026-08-17. This rubric is deterministic — every finding
below is a fact, not a judgment call.

## Expected findings table (registrations sorted by completeness, cleanest first)

| Company | Submitted By | Missing Dimensions | Count Missing |
|---|---|---|---|
| Acme Logistics | Alex | None | 0 |
| TechFlow Systems | Jordan | None | 0 |
| Valley Logistics | Riley | None | 0 |
| Legacy Systems | Morgan | None (expiry is set even though past) | 0 |
| Coastal Industries | Maya | Legal entity + domain identified (has domain, missing entity) | 1 |
| Metropolitan Finance | Casey | Legal entity + domain identified (has domain, missing entity) | 1 |
| Frontier Retail | Taylor | Duplicate/conflict check run (empty cell = no evidence) | 1 |
| Rapid Fulfillment | Sam | All six dimensions | 6 |

## Per-row detail (six dimensions checked per row)

### Acme Logistics (submitted by Alex)
- 1. Legal entity + domain identified: **Present** (legal_entity="Acme Logistics Inc", domain="acme-logistics.com")
- 2. Duplicate/conflict check run: **Present** (duplicate_check_run="Yes")
- 3. Source attribution recorded: **Present** (source="Outbound prospecting")
- 4. ICP fit stated: **Present** (icp_fit_notes="Mid-market logistics/supply chain fits target")
- 5. Requested support/resources specified: **Present** (requested_support="Deal registration protection")
- 6. Registration expiry / validity window set: **Present** (expiry_date="2026-11-01")

**Missing: None (all 6 present)**

### TechFlow Systems (submitted by Jordan)
- 1. Legal entity + domain identified: **Present** (legal_entity="TechFlow Systems LLC", domain="techflow.io")
- 2. Duplicate/conflict check run: **Present** (duplicate_check_run="Yes")
- 3. Source attribution recorded: **Present** (source="Referral from existing customer")
- 4. ICP fit stated: **Present** (icp_fit_notes="Enterprise SaaS segment aligns with ICP")
- 5. Requested support/resources specified: **Present** (requested_support="Technical resources for integration")
- 6. Registration expiry / validity window set: **Present** (expiry_date="2026-10-15")

**Missing: None (all 6 present)**

### Rapid Fulfillment (submitted by Sam)
- 1. Legal entity + domain identified: **Missing** (legal_entity empty, domain empty)
- 2. Duplicate/conflict check run: **Missing** (duplicate_check_run empty)
- 3. Source attribution recorded: **Missing** (source empty)
- 4. ICP fit stated: **Missing** (icp_fit_notes empty)
- 5. Requested support/resources specified: **Missing** (requested_support empty)
- 6. Registration expiry / validity window set: **Missing** (expiry_date empty)

**Missing: All 6 dimensions**

### Coastal Industries (submitted by Maya)
- 1. Legal entity + domain identified: **Missing** (legal_entity="Coastal Industries Corp" present, but domain empty — rubric requires both entity AND domain)
- 2. Duplicate/conflict check run: **Present** (duplicate_check_run="Yes")
- 3. Source attribution recorded: **Present** (source="Event lead - Logistics Summit 2026")
- 4. ICP fit stated: **Present** (icp_fit_notes="Mid-market distribution fits target segment")
- 5. Requested support/resources specified: **Present** (requested_support="Marketing support for launch")
- 6. Registration expiry / validity window set: **Present** (expiry_date="2026-12-01")

**Missing: Legal entity + domain identified (1 of 6)**

### Metropolitan Finance (submitted by Casey)
- 1. Legal entity + domain identified: **Missing** (domain="metropolitan-finance.com" present, but legal_entity empty — rubric requires both entity AND domain)
- 2. Duplicate/conflict check run: **Present** (duplicate_check_run="Yes")
- 3. Source attribution recorded: **Present** (source="Inbound web form")
- 4. ICP fit stated: **Present** (icp_fit_notes="Financial services sector matches ICP")
- 5. Requested support/resources specified: **Present** (requested_support="Deal registration protection")
- 6. Registration expiry / validity window set: **Present** (expiry_date="2026-09-30")

**Missing: Legal entity + domain identified (1 of 6)**

### Frontier Retail (submitted by Taylor)
- 1. Legal entity + domain identified: **Present** (legal_entity="Frontier Retail Group", domain="frontier-retail.com")
- 2. Duplicate/conflict check run: **Missing** (duplicate_check_run empty — no "Yes", no "No", no evidence a check happened)
- 3. Source attribution recorded: **Present** (source="Outbound prospecting")
- 4. ICP fit stated: **Present** (icp_fit_notes="Retail SMB segment fits profile")
- 5. Requested support/resources specified: **Present** (requested_support="Co-sell support from SE team")
- 6. Registration expiry / validity window set: **Present** (expiry_date="2026-11-30")

**Missing: Duplicate/conflict check run (1 of 6)**

### Valley Logistics (submitted by Riley)
- 1. Legal entity + domain identified: **Present** (legal_entity="Valley Logistics Partners", domain="valleylogistics.com")
- 2. Duplicate/conflict check run: **Present** (duplicate_check_run="Yes")
- 3. Source attribution recorded: **Present** (source="Partnership channel")
- 4. ICP fit stated: **Present** (icp_fit_notes="Logistics vertical - enterprise segment")
- 5. Requested support/resources specified: **Present** (requested_support="Technical resources and deal support")
- 6. Registration expiry / validity window set: **Present** (expiry_date="2026-10-01")

**Missing: None (all 6 present)**

### Legacy Systems (submitted by Morgan)
- 1. Legal entity + domain identified: **Present** (legal_entity="Legacy Systems Solutions Inc", domain="legacy-systems.io")
- 2. Duplicate/conflict check run: **Present** (duplicate_check_run="Yes")
- 3. Source attribution recorded: **Present** (source="Outbound prospecting")
- 4. ICP fit stated: **Present** (icp_fit_notes="Legacy software modernization vertical")
- 5. Requested support/resources specified: **Present** (requested_support="Deal registration protection")
- 6. Registration expiry / validity window set: **Present** (expiry_date="2026-07-01" — past date, but still "set"/"defined" per rubric)

**Missing: None (all 6 present)**

## The traps (findings a correct run must get right)

1. **Coastal Industries domain missing — must flag as incomplete on dimension 1.** The rubric says "legal entity + domain identified" (the + implies both are required). Having one but not the other fails the dimension. Domain is present but entity is missing in Met Finance — symmetric trap.

2. **Metropolitan Finance entity missing — must flag as incomplete on dimension 1.** Mirror of trap 1. A complete legal entity + domain check requires both to be present.

3. **Frontier Retail duplicate_check_run is empty (not "No", blank cell) — must flag as "no evidence a check happened".** An empty cell and an explicit "No" both indicate absence of a duplicate check. No distinction.

4. **Legacy Systems expiry_date = 2026-07-01 (past relative to today 2026-08-17) — must NOT flag dimension 6 as missing.** The rubric says "defined validity window or expiry date" — past dates are still defined/set. This row should show all 6 dimensions present, not flag expiry as missing just because it's expired.

5. **Rapid Fulfillment must show all 6 dimensions missing.** The row is a stress test: empty on all seven required columns (legal_entity, domain, duplicate_check_run, source, icp_fit_notes, requested_support, expiry_date). Should flag all 6 rubric dimensions as missing.

## Not present: reporting any of these is a hallucination

- A seventh dimension beyond the six listed (the rubric lists exactly six).
- Any row marked as "complete" or "approved" or "ready to proceed" — the skill audits completeness only, never approves.
- Any claim that a field "is visible but unclear" or "needs clarification" — the rubric checks presence/absence, not content quality or tone. Filled ≠ clear.
- Any invented company name, domain, entity, or value not present in the CSV.
- A claim that any column is missing from the export — all ten columns (company, legal_entity, domain, submitted_by, submitted_date, duplicate_check_run, source, icp_fit_notes, requested_support, expiry_date) are present in this sheet.
