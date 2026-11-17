# CompanyScope — data processing brief

**To** Data Protection Officer / legal counsel of a prospective German law firm or in-house legal team\
**From** Sean Langsdorf · Ironhack AI Consulting & Integration · 17 November 2026

**System actually reviewed.** CompanyScope is the Project 3 company-research MVP, not the earlier INCEPT legal-intake prototype. This brief is based on CompanyScope's public repository at commit `542665b0a4c6c5c18a8ac59896b87d5bd0eb39f6`, including its 34-node n8n workflow export. The project documents a local demo, not an operating client service. The prospective firm's role and controls are an assessment of deployment, not claims about an existing customer.

**What enters the system and why.** A researcher enters a German company name and optional register identifier through a signed-in n8n form, a token-authenticated webhook or the manual demo path. Most incorporated-company attributes are not personal data by themselves. The workflow nevertheless processes personal data when a company name identifies a person, a registered address is also a home, or a public excerpt identifies a director, employee, spokesperson or another person. Excerpts can carry names, roles, contact details and allegations or descriptions about individuals. Researchers' activity and time stamps may also be personal data when linked to an account. The current workflow does not intentionally seek health, political or other sensitive attributes and is not designed to ingest email, client files or attachments. Its text fields and public sources do not guarantee those data stay out.

| Stage and separate purpose | Data movement |
| --- | --- |
| Identify the exact legal entity | Local n8n normalizes the input and sends the entered company name to OpenRegister search. It matches internally using name or register ID and sends the selected provider company ID for details. Ambiguity stops the research before further enrichment. |
| Find public leads about that company | n8n constructs a Tavily query from company name, register court, address and purpose text. It requests up to eight results and selects up to five company-relevant excerpts. Relevance checks do not redact personal data. |
| Produce a briefing for a human researcher | Local RAG selects up to three methodology cards, not customer records. OpenAI's Responses API receives registry evidence and accepted web excerpts, including their URLs, plus the cards. The workflow requests structured synthesis with `store:false` and checks the output and source IDs. |
| Deliver the report and support technical operations | The workflow saves accepted Markdown on the n8n host and returns HTML to the form or richer JSON to the webhook/manual path. The CLI can save an additional Markdown copy and metadata sidecar. The export keeps full success and error execution data. |

**Where and for how long.** The documented form is local, but the operator's physical hosting region, backup locations and n8n pruning settings were not verified. The export writes to `/tmp/companyscope-reports`, which is not proof of scheduled deletion. The CLI separately writes under `projects/ironhack_project3/reports/`. Vendor account terms, processing regions, onward access and effective retention remain unverified. An API endpoint or EEA-looking domain does not establish an EEA-only data flow.

**Effect on people.** CompanyScope returns a company briefing and suggested follow-up questions. It does not score people, determine eligibility, reject counterparties or take action on a report. A qualified user is expected to verify facts and context before relying on it, but there is no documented sign-off gate. A wrong or stale attribution can still harm a person named in a report or influence a business decision.

[Source repository at audited commit](https://github.com/sean173-lang/CompanyScope/tree/542665b0a4c6c5c18a8ac59896b87d5bd0eb39f6) · [Replayed data-flow evidence](companyscope-data-flow-run.json)
