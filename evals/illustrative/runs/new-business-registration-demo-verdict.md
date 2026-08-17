## Row-by-row accuracy (OUTPUT vs GOLD)

| Company | Gold | Output | Verdict |
|---|---|---|---|
| Acme Logistics | None missing | None missing | ✅ correct |
| TechFlow Systems | None missing | None missing | ✅ correct |
| Rapid Fulfillment | All 6 missing | Lists 7 items ("Legal entity, domain, dedup check, source, ICP fit, requested support, expiry") but labels "all 6" | ⚠️ right conclusion, wrong mechanics — splits dimension 1 into two separate items, math don't add up (7 items, "6" label) |
| Coastal Industries | Dim 1 missing (domain absent) | "Domain missing" | ✅ correct |
| Metropolitan Finance | Dim 1 missing (entity absent) | "Legal entity missing" | ✅ correct |
| Frontier Retail | Dim 2 missing (dedup blank) | "Dedup check not run" | ✅ correct |
| Valley Logistics | None missing | None missing | ✅ correct |
| Legacy Systems | None missing (expiry past but still set) | "Expiry already passed... stale/invalid registration" | ❌ wrong — flags dim 6 missing/invalid when rubric say past date still counts as set |

**Score: 6/8 rows fully correct, 1/8 sloppy-but-right (Rapid), 1/8 wrong (Legacy).**

## Five traps

1. Coastal domain trap — **PASS**
2. Metropolitan entity trap — **PASS**
3. Frontier blank-dedup trap — **PASS**
4. Legacy past-expiry trap — **FAIL**. Gold explicit: past expiry still "defined," must show 0 missing. OUTPUT calls it "stale/invalid," recommends "re-registration with fresh expiry window" — treats date validity as a completeness defect, which rubric forbids.
5. Rapid all-6-missing trap — **PASS on substance, flawed on execution**. Conclusion (everything missing) right, but output enumerates 7 items while claiming "6," effectively inventing a 7th dimension by splitting "legal entity + domain" into two separate line items.

**3.5/5 traps clean.**

## Hallucinations / scope violations

1. **7th dimension leak (Rapid row)** — rubric has exactly 6 dimensions ("legal entity + domain" is ONE). Output enumerates entity and domain separately, contradicting its own "6-dimension rubric" framing stated in line 1. Gold explicitly flags a 7th dimension as hallucination.
2. **"Clean, approve" language** — summary recommends approval for Acme/TechFlow/Valley. Gold explicitly: audit checks completeness only, never approves. This is out-of-scope judgment injected into an audit report.
3. **Legacy Systems verdict overreaches** — calling it "stale/invalid" and prescribing "re-registration with fresh expiry window, not a rubber-stamp renewal" is a content-quality/temporal judgment the rubric doesn't ask for (rubric = presence/absence only). Directly contradicts trap 4.
4. **Action recommendations beyond audit scope** — "Send back entire" (Rapid), "run dedup check before approving" (Frontier) etc. Rubric is a completeness audit; prescribing remediation actions isn't itself wrong content-wise but strays past what gold's rubric defines as in-scope output.

No invented companies/domains/values found. No missing-column claims. No "unclear/needs clarification" language.

## Bottom line

OUTPUT gets the easy rows right and nails 3 of 5 traps (Coastal, Metropolitan, Frontier). It fails the Legacy Systems trap outright (core rubric violation: judging expiry validity instead of presence) and muddies the Rapid Fulfillment row by silently splitting one dimension into two. Add the unauthorized "approve" framing and it's a mediocre, not clean, pass.
