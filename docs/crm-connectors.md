# Connect your CRM (optional)

No skill needs a CRM. Every pipeline skill reads a CSV export. Your CRM can already have an AI connector. If it does, the `crm-export` skill can read open deals through it. It then writes a small local CSV for the other skills.

The field maps below come from vendor documentation. They are not tested against a live account. Read your CRM's schema first and trust it over this page. Checked on 2026-10-19.

## Before you connect

1. Review the connector with your own security team. These skills add no connector. They use one that you set up.
2. Use a read-only route. The skills only read. A read-only route means a prompt cannot make the agent change a record.
3. Connect as a user with the narrowest access that covers the deals you want to review. The connector acts with that user's permissions.
4. Try it in a sandbox first.
5. Never paste a password, token, or key into the chat. The connector holds the credentials.
6. Know what leaves your machine. The rows the agent reads go to your model provider, as any file does. `crm-export` asks for the columns a skill needs and leaves out contact details and free-text notes.

CRM text fields are written by other people, including customers. Every skill here treats that text as data to score, never as an instruction. A skill that finds an instruction in a record reports it.

## HubSpot

- Server: the remote HubSpot MCP server at `https://mcp.hubspot.com`.
- Setup: create an MCP connector in your HubSpot account under Development, then MCP Connectors. The client must support OAuth 2.1 with PKCE. When you install, grant read access only. HubSpot sets the scopes from the tools and from what you grant.
- Check: run the user-details tool first. It shows which objects and tools your account allows.
- Gotcha: if the account has Sensitive Data turned on, activity records (calls, emails, meetings, notes, tasks) are blocked through the connector. Deal properties still work.
- Gotcha: a deal stage is an internal ID. The skill looks up the pipeline to get the label.
- Limits: the search tool returns up to 200 records a page.

## Salesforce

- Server: the hosted `sobject-reads` MCP server. It is read-only. Production URL: `https://api.salesforce.com/platform/mcp/v1/platform/sobject-reads`. A sandbox has its own URL in the Salesforce docs.
- Setup: an admin turns the server on, because servers are off by default. It needs Enterprise edition or above. You connect with OAuth 2.0 and PKCE through an app that your admin creates.
- Permissions: every call runs as the signed-in user, with that user's object access, field-level security, and sharing rules.
- Tools: a schema tool, a query tool (SOQL), and a search tool. A query needs a WHERE and a LIMIT. One transaction returns at most 50,000 records.
- Gotcha: `LastStageChangeInDays` needs Pipeline Inspection. `crm-export` computes days from `LastStageChangeDate` instead.
- Gotcha: MEDDICC and similar facts are custom fields that end in `__c`. You name them once.
- Salesforce advises the hosted server over a custom proxy.

## Other CRMs

Each has an official server. Pick the read-only route.

- Pipedrive: native server with OAuth. Use is counted against a token allowance for your plan.
- Attio: hosted server at `https://mcp.attio.com/mcp` with OAuth. Reads run at once and writes ask you first.
- Close: hosted server at `https://mcp.close.com/mcp`. Send the `mcp.read` scope for read-only.
- Zoho CRM: use the Data Insights server, which is read-only. The other Zoho servers can change records and settings.
- Dynamics 365: the Sales server plus Dataverse. It needs a supported client. Claude Desktop is not supported.

## Run it

```
claude "run crm-export for forecast-review"
```

`crm-export` reads the schema, maps the fields (`skills/crm-export/references/crm-mapping.md`), writes `.agents/crm-export-<date>.csv`, and gives you the next command. When you are done, delete the file. The `.agents/` folder is gitignored.
