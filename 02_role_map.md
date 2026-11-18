# Phase 2: Role Map

**System:** Fix My Process (Ironhack Project 3) · **Input:** [00_data_processing_brief.md](00_data_processing_brief.md) · **Lens:** GDPR only · **Date:** 17 Nov 2026

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| Kleinanzeigen (client) | Controller | Decides purposes (1) to (9); the Board and enablement team act inside it | n/a; must sign DPAs with all processors |
| Ayhan Demir (builder and operator) | Processor | Builds and runs the workflow for Kleinanzeigen | No: needed. Becomes a controller if he uses case data for his own purposes |
| Ironhack (n8n host) | Sub-processor | Runs every step, keeps execution history | No; location not documented |
| OpenAI | Processor | Research, reports, quality judge, embeddings | No |
| Cohere (Google Cloud as its sub-processor) | Processor | Reranking with the problem text as query | No |
| Pinecone | Processor | Document search, query embeddings | No |
| Tavily | Processor | Web search with an AI-written query | No |
| GNews | Unclear (likely independent controller of its search service) | News search, 2 to 4 word query | No; location not documented |
| OpenAlex | Independent controller of its public API | Keyword search | No; n/a if queries hold no personal data |
| Airtable | Processor | Case database, error records | No |
| Notion | Processor | Use-case pages | No |
| Slack | Processor | Board notices, red-case review, alerts | No |
| Render | Processor | Hosts the web page, request logs | No |

All services run on free or trial plans, which may not include a DPA or an EU data region. A pilot will likely need business plans.

**International transfers**

| Vendor | Destination | Transfer mechanism |
|---|---|---|
| OpenAI, Pinecone, Tavily, Airtable, Notion, Slack | US | EU-US Data Privacy Framework adequacy decision (2023/1795) if the vendor is certified (check dataprivacyframework.gov); otherwise SCCs (2021/914) plus a transfer impact assessment |
| Cohere | Canada (company), US (Google Cloud) | Canada adequacy decision for Cohere; the onward transfer to the US needs DPF or SCCs in Cohere's DPA |
| Render | EU (if Frankfurt) or US | Configure Frankfurt; US parent still needs DPF or SCCs |
| n8n (Ironhack), GNews | Not documented | Unknown: establish before use or replace |
| OpenAlex | US | Keep personal data out of queries, so no transfer of personal data |

## Sources

- Commission Implementing Decision (EU) 2023/1795 (EU-US Data Privacy Framework)
- DPF status: General Court dismissed Latombe's annulment action on 3 Sep 2025; appeal pending at the CJEU: https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law-blog/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework
- DPF participant list: https://www.dataprivacyframework.gov/list
