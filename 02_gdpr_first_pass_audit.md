# GDPR first-pass audit — Mobile Game Competitor Snapshot Agent

Legal references: [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/), [EDPB DPIA guidance](https://www.edpb.europa.eu/topics/accountability-and-compliance-tools/data-protection-impact-assessment_en), [AI Act FAQ](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act), and [ePrivacy Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0058).

## Brief check

The system **does process personal data**: a requester’s email; names and job titles in public news/search results; and any personal data in an uploaded strategy/KPI PDF. Company/game metrics are generally non-personal, but a studio name can identify an individual. Sensitive data may arrive incidentally; no filtering is documented.

**Flow:** web form → n8n; optional PDF → PDF loader/chunker → OpenAI embeddings → Pinecone `custom-strategy` namespace; competitor name → Tavily, GNews and Apple; merged results plus Pinecone retrieval → OpenAI `gpt-4o-mini` → HTML → Gmail to the submitted address. The workflow is hosted and used for client studios, but regions, retention, access controls, DPAs and transfer safeguards are not documented.

**Purposes:** (1) receive and email the requested report; (2) ingest the strategy/KPI playbook for retrieval; (3) conduct competitive research and generate recommendations. It assists product/marketing prioritisation, not decisions about a natural person. Human review is after delivery, not before it.

## Phase 1 — Personal-data inventory

| Data category | Source / purpose | Retention | EU border? | Purpose issue |
|---|---|---|---|---|
| Requester email | Form; deliver the requested report | Unknown (n8n/Gmail/vendor logs) | Possible; region not documented | Contract basis is plausible, but controller and service terms are unconfirmed |
| Uploaded PDF contents and embeddings | Requester; customise report/RAG | Unknown; stored in execution/Pinecone paths; `clearNamespace` is not a rights workflow | Possible via OpenAI/Pinecone | If it contains employee/third-party data, vendor disclosure may exceed its original internal purpose |
| Names, titles and article text | Tavily/GNews public sources; competitor report | Unknown across API, model and Gmail paths | Possible | Public availability does not remove notice, accuracy, minimisation or objection duties; compatibility is undocumented |
| Derived summaries/recommendations | OpenAI from the above; report and email | Unknown | Possible | Inferences must not be presented as verified facts; no individual profiling is intended |

## Phase 2 — Role and transfer map

| Entity | Provisional role | Activity | DPA / transfer evidence |
|---|---|---|---|
| Client studio | Controller | Determines report purpose, audience and strategy data | Not evidenced |
| Jędrzej/team and hosted n8n | Processor for client; possibly separate controller for own service | Operates workflow and sends reports | DPA and role boundary unknown; required |
| n8n host | Processor/subprocessor | Form, execution and binary handling | DPA, region and retention unknown |
| OpenAI | Processor/subprocessor, subject to contract | Embeddings, chat generation and prompts | DPA, model retention, region and SCC/adequacy basis unknown |
| Pinecone | Processor/subprocessor | Stores/retrieves strategy vectors and chunks | DPA, tenant isolation, region and deletion evidence unknown |
| Gmail/Google | Service provider/processor for delivery | Stores and transmits report email | DPA, region and retention unknown |
| Tavily, GNews and Apple | API vendors; role depends on terms/query data | Public research and storefront lookup | Terms, role and transfer mechanisms unknown |

Data may leave the EEA because the workflow calls multiple external services, but the repository proves neither location nor mechanism. Before production, document each destination, adequacy decision or SCCs, any transfer-impact assessment, onward transfers and deletion commitments.

## Phase 3 — Lawful basis

| Purpose | Proposed basis | Justification / status |
|---|---|---|
| Process requester email and deliver report | Contract (Art. 6(1)(b)) | Necessary to fulfil the request; verify the contracting controller. **TBD — legal review.** |
| Process optional strategy PDF for customisation | Contract (Art. 6(1)(b)) | Necessary only when selected; minimise it and require a basis for third-party data. **TBD — legal review.** |
| Public-source research and report generation | Legitimate interests (Art. 6(1)(f)) | Business intelligence is concrete; the LIA needs volume, notice and vendor facts. **TBD — legal review.** |
| Vendor/execution retention and logging | Not documented | Purpose, retention and controller are absent. **TBD — legal review.** |

**LIA for research:** (1) **Legitimate interest:** improve product and marketing decisions through market intelligence. (2) **Necessity:** on-demand public searches are less intrusive than user-level collection, but must exclude person-level enrichment and unnecessary article text. (3) **Balancing:** public availability lowers expectations; aggregation, AI transformation, distribution and inaccuracies increase impact. Sign-off requires documented notice/objection, minimisation, retention, vendor terms and safeguards.

## Phase 4 — Risk and rights

**Special category data (Art. 9):** None is intentionally requested and no Article 9 condition is identified. It could arrive in the PDF/public text or be inferred; block or redact it, or obtain a documented condition and legal review before processing.

**Automated decision-making (Art. 22):** It recommends product tests and prioritisation, not legal or similarly significant decisions about individuals; Article 22 is not triggered on the documented use. If repurposed for employment or individual profiling, stop deployment until human intervention, contest and explanation safeguards exist.

**DPIA trigger:** Likely **yes**. **Matching/combining datasets** (PDF + APIs + vector retrieval) and **innovative technology** (LLM/RAG) apply; sensitive/highly personal data and large-scale processing are Unknown. Individual scoring, significant automated decisions, systematic monitoring, vulnerable subjects and preventing rights exercise are not evidenced. Two likely criteria justify a DPIA before deployment.

**Rights friction:** Access and erasure cannot be answered reliably: there is no subject identifier, copy inventory, retention schedule, per-user Pinecone deletion or vendor-request process. `clearNamespace: true` is not selective erasure and risks other tenants; add a request route, source traceability and a 30-day process for access, erasure, objection and rectification.

## Phase 5 — Law stacking

- **AI Act:** Likely minimal/no-risk rather than an Annex III high-risk use because it is competitive intelligence, not a sensitive-domain decision system. Reassess if used to decide about workers or other individuals; document AI-generated output and human oversight, and confirm any applicable transparency duty under current AI Act rules.
- **ePrivacy:** No cookies, tracking pixels, device telemetry or email tracking are documented; no separate ePrivacy consent trigger is evidenced. Recheck the form and email configuration before launch, especially if non-essential tracking or communication-content analytics are added.
- **Data Act:** **N/A** on current evidence: no connected product/IoT data or cloud-switching use is described.

## Verify — accountability test

The current project documents cannot demonstrate compliance to a regulator. Present: system description, workflow export and a screenshot. Missing or entirely unverified: RoPA/data-flow register, privacy notice, controller/processor allocation, DPAs, subprocessor list, transfer map and SCC/adequacy assessment, LIA, DPIA, retention/deletion schedule, access controls, rights workflow, security/breach procedure, and evidence that the PDF namespace is tenant-isolated.

## Phase 6 — Client memo

**To:** Client Data Protection Officer / legal counsel  
**Subject:** Mobile Game Competitor Snapshot Agent — first-pass GDPR advice

**Bottom line: proceed with conditions.** The use case is commercially low-impact as designed, but personal data is sent through an undocumented multi-vendor chain and the project has no evidence of lawful-basis, transfer, retention or rights controls.

**Three sequenced actions:** (1) **Before another client run,** confirm the controller/processor model and execute DPAs with the operator, n8n host, OpenAI, Pinecone and Gmail; document API-vendor roles, locations, SCCs or adequacy decisions, onward transfers and model-retention settings. (2) **Before deployment,** complete a DPIA and the research LIA; publish a concise privacy notice; restrict the PDF to necessary business content; block/redact special-category and unnecessary employee data; and add a human review and rights-request route. (3) **Before scaling,** implement per-client namespaces and selective deletion, a written retention schedule covering n8n, Pinecone, Gmail and vendor logs, least-privilege access, audit logging, incident response and a test that access/erasure requests can be fulfilled within one month.

**Residual risks:** Public articles may be inaccurate or unexpected for named individuals; LLM summaries may create misleading inferences and invite over-reliance even when source data is public; and international vendor access or onward transfers may remain outside the client’s control.

Do not treat the workflow’s post-delivery human reading as a substitute for governance: it does not correct inaccurate source data, answer rights requests, or establish a transfer mechanism. The client should designate a controller owner and a processor contact, maintain a current vendor register, and test deletion with a synthetic PDF before allowing real personal data. Release should be gated on signed records, not only a successful workflow run.

This memo is not a legal opinion, DPIA or certification. The client should obtain legal counsel’s sign-off before relying on it for compliance or production decisions.
