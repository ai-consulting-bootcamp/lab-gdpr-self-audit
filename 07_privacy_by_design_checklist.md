# Stretch: Data Protection by Design Checklist

**System:** Fix My Process (Ironhack Project 3) · **Input:** [00_data_processing_brief.md](00_data_processing_brief.md) · **Lens:** GDPR only · **Date:** 17 Nov 2026

**Highest-risk processing activity** (repurposing flag 1 in [Phase 1](01_data_inventory.md)): the free-text problem description, which can carry colleague and customer data and goes to OpenAI and then into Airtable, Notion and Slack (purposes 1 to 4).

| Design principle | Current state of your system | Pass / Fail / Unknown |
|---|---|---|
| Data minimisation | No name or login is collected, but the free text is not filtered; only an on-screen warning. Red cases send the full text to Slack | Fail |
| Purpose binding | Nothing technical restricts the data to purposes 1 to 4; the same records could feed department summaries | Fail |
| Access controls | Who can open the Airtable base, Notion pages, Slack channels and the Ironhack n8n instance is not documented | Unknown |
| Retention enforcement | No retention period; records stay until someone deletes them | Fail |
| Subject rights workflow | Only manual search and deletion across five stores, linked by reference code | Fail |
| Incident response | The error handler alerts on workflow failures, not on breaches; no 72-hour notification process | Fail |

**What needs to change**

- **Minimisation:** add a redaction step before the first LLM call that removes names, emails, phone numbers and customer IDs; send the Board the summary, not the full text.
- **Purpose binding:** keep reports and Board data in separate tables or views, and record in the DPIA that case data cannot be reused for evaluating teams without a new assessment.
- **Access controls:** move to company-owned workspaces, limit the Airtable base and Notion pages to the enablement team and Board, and document who has access.
- **Retention:** a scheduled n8n job that deletes or anonymises cases after 90 days and error records after 30, and shorter n8n execution history.
- **Subject rights:** one lookup by reference code that lists and deletes the record in Airtable, Notion and Slack, with a log of each request.
- **Incident response:** add Fix My Process to Kleinanzeigen's breach procedure, name an owner, and get breach notice terms into each vendor DPA so the 72-hour clock (Art. 33) can be met.
