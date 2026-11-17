# Phase 6: Compliance Memo

**System:** Fix My Process (Ironhack Project 3) · **Input:** [00_data_processing_brief.md](00_data_processing_brief.md) · **Lens:** GDPR only · **Date:** 17 Nov 2026

**To:** Data Protection Officer, Kleinanzeigen
**From:** Ayhan Demir
**Re:** GDPR review of Fix My Process

**Bottom line: proceed with conditions.** The system can run a pilot under legitimate interests, but no real employee data should enter it until processor contracts, transfer safeguards and input controls are in place.

Fix My Process asks for no names, yet the free-text description will often contain colleagues, customers and the employee's own views. That text reaches up to eleven services, at least eight with US infrastructure, all on free plans with no DPAs, no EU regions and no retention period. Employees get no privacy notice. Outputs concern processes rather than people, so Article 22 is not triggered today.

**Top three actions**

1. **Contracts and transfers before any real data flows.** Sign DPAs with every processor (OpenAI, Cohere, Pinecone, Tavily, Airtable, Notion, Slack, Render and the n8n host), confirm DPF certification or SCCs for each US transfer, and use EU regions where offered. Replace GNews and the Ironhack n8n instance if their location and terms cannot be documented.
2. **DPIA before the pilot.** The system meets at least two EDPB criteria (employees as vulnerable data subjects, innovative technology). Include the LIA, a retention schedule (I propose 90 days for cases, 30 for error records) and an Article 13 privacy notice.
3. **Minimise at input and lock the purpose.** Filter names and customer details before the LLM call, send only summaries to Slack and Notion, and state that case data will not be used to evaluate teams or individuals. Department summaries need their own assessment before they are built.

**Residual risks**

- Filters will miss some personal and special-category data in free text.
- US transfers rest on the Data Privacy Framework, upheld by the General Court but now under appeal at the CJEU; a ruling against it would force SCCs or EU-only vendors.
- Department-level records make team comparison easy, whatever the policy says.

**What this memo is not.** It is not a legal opinion, a DPIA or a certification. It is a first consultant review based on the data processing brief. Please engage legal counsel, and involve the works council for employee data, before relying on it for compliance decisions.
