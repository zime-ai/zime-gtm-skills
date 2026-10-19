# CRM field map

This map comes from vendor documentation. It is not tested against a live account. Field names can differ in your org, so read the schema first and trust it over this table.

The CSV columns are the names the pipeline skills detect. Day columns are computed from dates, against today or against the payload's `as_of` date.

## Columns

| CSV column | Meaning |
|---|---|
| `deal_name` | Name of the deal |
| `owner` | Name of the deal owner |
| `stage` | Stage label, not an internal ID |
| `amount` | Deal amount in the deal currency |
| `close_date` | Expected close date, `YYYY-MM-DD` |
| `probability` | Whole number from 0 to 100 |
| `forecast_category` | Commit, Best case, Pipeline, or the CRM's own labels |
| `next_step` | Next step text, copied as it is |
| `contacts` | Count of associated contacts |
| `days_in_stage` | Days since the deal entered its current stage |
| `days_since_last_activity` | Days since the last logged activity. Blank when none |
| `days_to_close` | Days from the as-of date to the close date. Negative when past |
| `created_days_ago` | Days since the deal was created |

A column the CRM cannot give is left out and named in the report. `next_step_days_overdue` needs a dated next step, which most CRMs do not hold, so it is usually left out.

## HubSpot (deals)

Route: the remote HubSpot MCP server, with a connector that has read scopes. Run the user-details tool first to see which objects the account allows. If the account has Sensitive Data turned on, activity records (calls, emails, meetings, notes, tasks) are blocked. The deal properties below are not.

| CSV column | HubSpot property | Note |
|---|---|---|
| `deal_name` | `dealname` | |
| `owner` | `hubspot_owner_id` | An ID. Look up the owner name with the owner tool |
| `stage` | `dealstage` | An internal ID. Look up the label in the deal pipeline |
| `amount` | `amount` | |
| `close_date` | `closedate` | |
| `probability` | `hs_deal_stage_probability` | A fraction from 0 to 1. Multiply by 100 |
| `forecast_category` | `hs_manual_forecast_category` | Blank when the team does not forecast by category |
| `next_step` | `hs_next_step` | |
| `contacts` | `num_associated_contacts` | |
| `days_in_stage` | `hs_date_entered_<stage id>` | Use the property for the current stage ID |
| `days_since_last_activity` | `notes_last_contacted` | Last logged call, email, or meeting. `notes_last_updated` also counts notes and tasks |
| `created_days_ago` | `createdate` | |

Limits: the search tool returns up to 200 records a page and allows 5 filter groups. Stage entry dates exist only for stages the deal has entered.

## Salesforce (Opportunity)

Route: the hosted `sobject-reads` server (read-only). An admin must enable it. It needs Enterprise edition or above and an app for OAuth with PKCE. Read the object schema with the schema tool first. Then use the query tool. A query needs a WHERE and a LIMIT, and one transaction returns at most 50,000 records.

| CSV column | Salesforce field | Note |
|---|---|---|
| `deal_name` | `Name` | |
| `owner` | `Owner.Name` | A relationship field in the same query |
| `stage` | `StageName` | |
| `amount` | `Amount` | |
| `close_date` | `CloseDate` | |
| `probability` | `Probability` | Already 0 to 100 |
| `forecast_category` | `ForecastCategoryName` | |
| `next_step` | `NextStep` | 255 characters at most |
| `contacts` | `OpportunityContactRole` | One count query, grouped by `OpportunityId` |
| `days_in_stage` | `LastStageChangeDate` | `LastStageChangeInDays` exists only with Pipeline Inspection |
| `days_since_last_activity` | `LastActivityDate` | Last completed task or event |
| `created_days_ago` | `CreatedDate` | |

Stage history is in `OpportunityHistory`. Buyer roles are in `OpportunityContactRole`. Facts such as an economic buyer or a MEDDICC score are custom fields that end in `__c`, so the user must name them.

## Other CRMs

Each has an official server. Use a read-only route and map fields from its schema tool.

| CRM | Read-only route | Note |
|---|---|---|
| Pipedrive | Native server, signed in with OAuth | Use is metered by a token allowance per plan |
| Attio | Hosted server | Reads need no confirmation, and writes ask the user |
| Close | Hosted server with the `mcp.read` scope | Pick the read scope when you connect |
| Zoho CRM | The Data Insights server | The other Zoho servers can change records |
| Dynamics 365 | Sales server plus Dataverse | Needs a supported client. Claude Desktop is not supported |

## Reading a stage

Match the stage label to the rubric of the skill you feed. A CRM often names stages differently from the skill (for example Qualified To Buy or Needs Analysis). If a label does not clearly match, keep the CRM's label and say so. Never rename a stage to fit.
