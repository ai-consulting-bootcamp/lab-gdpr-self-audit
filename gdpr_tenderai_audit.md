# TenderAI Assistant — GDPR Audit

**Project:** TenderAI — Enterprise RAG AI Assistant
**Audit:** GDPR Lens
**Client:** [Client Name / TBD]
**Auditors:** [Your Name / Team]
**Date:** 19 August 2026

---

# Data Processing Brief

## TenderAI Assistant — GDPR Data Processing Brief

TenderAI is an enterprise Retrieval-Augmented Generation (RAG) AI assistant designed to help organisations analyse tender requirements, retrieve relevant company knowledge, assess compliance, and generate evidence-based tender/proposal responses. The current MVP uses synthetic enterprise documents for testing. These include company profile, certification, renewable-energy project-reference, technical-capability and tender-response-guideline documents.

The production system is intended to allow a client organisation to upload enterprise documents and submit tender requirements or questions. Those documents may contain personal data even though processing personal data is not the primary purpose of TenderAI. Examples include names, professional contact details, job titles, employment history, qualifications, biographies, project personnel information and free-text references to identifiable individuals.

The data may originate directly from client employees or users uploading documents, from existing company records, from project references and from other business documents supplied by the client. TenderAI processes the uploaded material through document extraction, chunking, embedding, vector storage and retrieval. Relevant retrieved content can then be supplied to an LLM to generate tender assessments, evidence summaries and draft responses.

The current architecture uses external AI services for embeddings and LLM processing and Pinecone as the vector database/retrieval layer. A final production hosting configuration and the precise processing locations of all providers have not yet been established in the project documentation.

The client organisation would provisionally determine the purposes and means of the processing and would therefore be treated as the controller. TenderAI would provisionally act as a processor where it processes client information only on the client's documented instructions. The contractual GDPR roles of external providers must be confirmed from the final production contracts and service configuration.

TenderAI does not currently make decisions about individuals such as employment, credit, insurance or access to public services. Its principal function is to assist organisations with tender/proposal work. It can, however, generate assessments and recommendations concerning documents or tender requirements. A human user reviews the retrieved evidence and generated outputs before they are used in a tender or proposal.

Because the production system may process personal data contained within enterprise documents, GDPR applies to that processing unless the relevant data has been effectively anonymised or is otherwise outside the scope of personal data.

**Initial conclusion:** The current synthetic MVP does not intentionally process real personal data, but the intended production architecture is capable of processing personal data throughout the RAG pipeline. The production deployment therefore requires a GDPR assessment before real client data is introduced.

---

# Phase 1 — Personal Data Inventory

## 1. Inventory of Personal Data

| Data category                                                                       | Source                                                                                                 | Purpose(s)                                                                                      | Retention period (known / estimated)                                                                | Crosses EU border?                                                                       |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Names and professional identifiers                                                  | Client-uploaded enterprise documents, such as company profiles, project references, CVs or biographies | Document ingestion, knowledge-base creation, retrieval, tender analysis and response generation | **TBD — legal review.** No production personal-data retention schedule is currently defined.        | **TBD — legal review.** Depends on the final processing locations of external providers. |
| Professional contact information                                                    | Client-uploaded documents                                                                              | Document ingestion, retrieval and AI-assisted analysis where contained in relevant documents    | **TBD — legal review.**                                                                             | **TBD — legal review.** Provider processing locations must be verified.                  |
| Professional information such as job title, employer, qualifications and experience | Client-uploaded enterprise documents                                                                   | Knowledge-base creation, evidence retrieval, tender analysis and response generation            | **TBD — legal review.**                                                                             | **TBD — legal review.**                                                                  |
| Employment/project information concerning identifiable individuals                  | Project references, CVs, company documents and other enterprise material                               | Retrieval and use as supporting evidence for tender/proposal preparation                        | **TBD — legal review.**                                                                             | **TBD — legal review.**                                                                  |
| Free-text content relating to identifiable individuals                              | Client-uploaded PDFs and other enterprise documents                                                    | Text extraction, chunking, semantic retrieval, tender analysis and LLM response generation      | **TBD — legal review.** Source documents, chunks and outputs require separate retention assessment. | **TBD — legal review.**                                                                  |
| Extracted document text containing personal data                                    | Client-uploaded documents processed by TenderAI                                                        | Text processing, chunking, embedding, retrieval and AI-assisted analysis                        | **TBD — legal review.**                                                                             | **TBD — legal review.**                                                                  |
| Document chunks potentially containing personal data                                | Extracted text generated by the ingestion pipeline                                                     | Retrieval and evidence grounding for tender assessments and draft responses                     | **TBD — legal review.**                                                                             | **TBD — legal review.**                                                                  |
| Vector embeddings potentially linked to personal data                               | Generated from document chunks using the embedding service                                             | Semantic search and retrieval from the TenderAI knowledge base                                  | **TBD — legal review.** Embedding deletion/retention rules are not currently documented.            | **TBD — legal review.** Depends on embedding and vector-database locations.              |
| Document metadata potentially containing personal data                              | Client documents and application-generated metadata                                                    | Document identification, retrieval, source citation and evidence traceability                   | **TBD — legal review.**                                                                             | **TBD — legal review.**                                                                  |
| Retrieved passages potentially containing personal data                             | TenderAI knowledge base / Pinecone retrieval                                                           | Provide relevant evidence to the LLM and support grounded analysis                              | **TBD — legal review.**                                                                             | **TBD — legal review.**                                                                  |
| LLM inputs containing personal data                                                 | Retrieved document content and user prompts                                                            | Generate tender assessments, evidence summaries and draft responses                             | **TBD — legal review.** Provider retention and logging settings must be verified.                   | **TBD — legal review.**                                                                  |
| AI-generated outputs potentially containing personal data                           | TenderAI LLM responses and generated reports                                                           | Support client tender/proposal work and provide evidence-based outputs                          | **TBD — legal review.**                                                                             | **TBD — legal review.**                                                                  |

## 2. Current MVP vs Production Processing

### Current MVP

The current MVP was tested using synthetic enterprise documents created for the project.

Examples include:

* Company Profile
* ISO Compliance and Certifications
* Renewable Energy Project References
* Technical Capabilities
* Tender Response Guidelines

These documents were created for testing and are not intended to represent real individuals.

**Current assessment:**

> No intentional processing of real-world personal data has been identified in the current synthetic test dataset.

### Intended Production Deployment

The intended production deployment may process client enterprise documents containing information about identifiable individuals.

GDPR therefore becomes relevant if such documents are uploaded into the production TenderAI system.

## 3. Purpose Limitation Flag

A significant purpose-limitation question arises where personal information was originally collected for one business purpose and is subsequently processed through TenderAI for another purpose.

For example, an employee biography, project reference or CV may originally have been collected for employment, project-management or corporate-record purposes and later uploaded to TenderAI for AI-assisted tender preparation.

The client must establish:

1. Why the personal data was originally collected.
2. Whether TenderAI processing is compatible with that original purpose.
3. Whether the new processing is necessary.
4. Whether individuals were appropriately informed.
5. Which Article 6 lawful basis applies.
6. Whether unnecessary personal data can be removed before ingestion.

**Assessment: TBD — legal review.**

## 4. Phase 1 Findings

### Finding 1 — Personal data may enter the RAG pipeline

The current MVP uses synthetic data, but production users may upload documents containing personal data.

**Risk status: Gap requiring production controls.**

### Finding 2 — Retention is not yet defined

The project does not currently document GDPR-specific retention periods for source documents, extracted text, chunks, embeddings, metadata, retrieved passages or generated outputs.

**Risk status: Gap identified.**

### Finding 3 — International transfer status is not established

The project uses external AI and vector-database services, but production processing locations and transfer mechanisms have not been fully documented.

**Risk status: Gap identified — TBD — legal review.**

### Finding 4 — Purpose limitation requires client-level assessment

Whether personal data contained in client documents can lawfully be reused through TenderAI depends on the original collection purpose, compatibility, necessity, transparency and lawful basis.

**Risk status: TBD — legal review.**

## Phase 1 Conclusion

TenderAI's current synthetic MVP does not intentionally process real personal data.

However, the production architecture is capable of processing personal data throughout the RAG pipeline, from document ingestion through extraction, chunking, embeddings, retrieval, LLM processing and generated outputs.

The principal unresolved Phase 1 issues are:

* retention periods;
* international transfer locations and mechanisms;
* purpose compatibility;
* data minimisation;
* treatment of personal data contained in embeddings and outputs.

**Phase 1 status: Complete.**

---

# Phase 2 — Role Map

## 1. Controller / Processor Analysis

The GDPR role allocation must be based on who determines the purposes and essential means of processing.

| Entity                                | Role                                          | Processing activity                                                                                                                            | DPA in place?                                                                            |
| ------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Client organisation**               | **Controller — provisional**                  | Determines why documents are processed, what tender/proposal purposes apply, who can access information and applicable retention requirements. | **TBD — legal review.**                                                                  |
| **TenderAI / development team**       | **Processor — provisional**                   | Operates the TenderAI application and processes client information according to documented instructions.                                       | **TBD — legal review.**                                                                  |
| **OpenAI**                            | **Role TBD — legal review**                   | Provides embedding and LLM services used by the application.                                                                                   | **TBD — legal review.**                                                                  |
| **Pinecone**                          | **Role TBD — legal review**                   | Provides vector storage and retrieval services for embeddings and associated metadata.                                                         | **TBD — legal review.**                                                                  |
| **Hosting / infrastructure provider** | **TBD — legal review**                        | May host application components, databases or files depending on the final production architecture.                                            | **TBD — legal review.**                                                                  |
| **Client authorised users**           | Users acting under the controller's authority | Upload documents, submit requirements, review evidence and use generated outputs.                                                              | N/A — they are not automatically separate processors merely because they use the system. |

## 2. Client Organisation

The client organisation is provisionally considered the **controller** because it determines the business purposes for which its enterprise information is processed.

The client determines:

* Which documents may be uploaded.
* Which processing purposes apply.
* Which categories of information are necessary.
* Which users may access the system.
* How long information should be retained.
* Whether information may be reused.
* Which external services may process the information.

**Assessment: Controller — provisional.**

## 3. TenderAI / Development Team

If TenderAI operates as a service on behalf of the client and processes client information only according to documented client instructions, TenderAI would provisionally act as a **processor**.

Processing activities include:

* receiving documents;
* extracting text;
* creating chunks;
* generating embeddings;
* storing/retrieving information;
* sending relevant content to configured AI services;
* generating AI-assisted outputs.

TenderAI should not independently determine new purposes for the client's personal data if acting as a processor.

**Assessment: Processor — provisional.**

**DPA:** TBD — legal review.

An Article 28 DPA would generally be required before production processing where TenderAI acts as a processor.

## 4. OpenAI

The current architecture uses OpenAI services for embedding generation and LLM processing.

The precise GDPR role and contractual arrangement must be confirmed from the production configuration and applicable provider terms.

The audit must verify:

* contractual role;
* applicable data-processing terms;
* processing locations;
* retention settings;
* subprocessors;
* provider-controlled processing purposes;
* applicable international-transfer mechanism.

**Assessment: TBD — legal review.**

## 5. Pinecone

Pinecone is used as the vector database and retrieval layer.

Embeddings and associated metadata may remain linked to source documents and therefore should not automatically be treated as outside GDPR.

The production assessment must verify:

* contractual role;
* DPA;
* processing/storage region;
* subprocessors;
* deletion controls;
* security measures;
* international-transfer mechanism.

**Assessment: TBD — legal review.**

## 6. International Transfers

The project documentation does not currently establish that all processing remains inside the EEA.

Potential transfers could occur through:

* OpenAI;
* Pinecone;
* hosting infrastructure;
* relevant subprocessors.

The production architecture must identify the location of each relevant processing activity.

Where personal data leaves the EEA, the applicable GDPR Chapter V mechanism must be documented, such as:

* an adequacy decision;
* Standard Contractual Clauses;
* another applicable transfer mechanism.

**Current status: TBD — legal review.**

## 7. Phase 2 Findings

### Finding 1 — Controller/processor roles require confirmation

The client is provisionally the controller and TenderAI is provisionally the processor, subject to the final operating and contractual model.

### Finding 2 — Production DPAs are not documented

The current MVP project does not contain production DPAs covering the relevant controller/processor relationships.

**Status: Gap identified.**

### Finding 3 — Subprocessor inventory is incomplete

A complete production subprocessor register has not yet been established.

**Status: Gap identified.**

### Finding 4 — International transfer mechanism is unresolved

The locations of all relevant external processing and applicable Chapter V mechanisms have not yet been documented.

**Status: Gap identified — TBD — legal review.**

## Phase 2 Conclusion

The provisional role allocation is:

**Client = Controller → TenderAI = Processor → relevant external providers = roles to be confirmed.**

Production processing should not begin until the contractual roles, DPAs, subprocessor chain and international-transfer arrangements have been documented.

**Phase 2 status: Complete.**

---

# Phase 3 — Lawful Basis Assessment

## 1. Processing Purposes

The following purposes have been identified:

1. Client document ingestion and knowledge-base creation.
2. Semantic retrieval of relevant enterprise information.
3. AI-assisted tender requirement analysis.
4. Generation of tender/proposal responses and reports.
5. Storage of source documents, chunks, embeddings and metadata.
6. Administration, security and troubleshooting of the service.
7. Potential future reuse of information for other client purposes.

## 2. Lawful Basis Table

| Purpose                                                            | Proposed lawful basis  | One-line justification                                                                                                                                                     | Flag for legal review? |
| ------------------------------------------------------------------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Client document ingestion and processing for tender/proposal work  | **TBD — legal review** | The client must determine the appropriate Article 6 basis based on the original collection context, relationship with individuals, necessity and applicable law.           | **Yes**                |
| Retrieval and analysis of client information for a specific tender | **TBD — legal review** | The processing is directly connected to the client's tender/proposal activity, but the lawful basis depends on the underlying personal-data context.                       | **Yes**                |
| Generation of AI-assisted tender responses and reports             | **TBD — legal review** | AI generation is a means of carrying out the client's stated tender/proposal purpose and does not itself establish a separate Article 6 basis.                             | **Yes**                |
| Storage of documents, chunks and embeddings                        | **TBD — legal review** | Storage is necessary only to the extent required for the identified processing purpose and must be covered by the applicable basis and retention policy.                   | **Yes**                |
| Security, access control and service administration                | **TBD — legal review** | Security and operational processing may potentially rely on legitimate interests where the three-part LIA is satisfied, but this must be assessed in the client's context. | **Yes**                |
| Future reuse of personal data for a different purpose              | **TBD — legal review** | A new purpose cannot automatically rely on the original processing basis; compatibility, transparency and a lawful basis must be assessed separately.                      | **Yes**                |

## 3. Legitimate Interests Assessment

Legitimate interests should **not** be assumed merely because TenderAI provides a business benefit.

If legitimate interests is considered, the client must document all three elements.

### Test 1 — Is the interest legitimate?

Potential interest:

> Efficient and accurate preparation of tenders and proposals using the client's existing business information.

This is potentially a legitimate business interest, but the precise interest must be documented by the client.

**Assessment: TBD — legal review.**

### Test 2 — Is the processing necessary?

The client must establish whether processing personal data through TenderAI is genuinely necessary for the stated tender/proposal purpose and whether the same objective could reasonably be achieved using less personal information.

Possible safeguards include:

* removing unnecessary names/contact details;
* redacting personal information before ingestion;
* restricting uploads to relevant documents;
* preventing unnecessary personal information from entering prompts.

**Assessment: TBD — legal review.**

### Test 3 — Does the individual's interest override?

The client must balance the expected business benefit against the privacy impact on individuals whose data appears in uploaded documents.

Relevant factors include:

* reasonable expectations;
* sensitivity of the information;
* volume of personal data;
* whether special-category information is present;
* whether data is transferred to external providers;
* whether effective safeguards are implemented.

**Assessment: TBD — legal review.**

### Lawful Basis Conclusion

No Article 6 lawful basis should be treated as conclusively established from the current MVP documentation.

**Overall assessment: TBD — legal review.**

---

# Phase 4 — Risk and Rights Analysis

## 1. Special-Category Data — Article 9

The current synthetic MVP does not intentionally contain Article 9 personal data.

However, production client documents could contain or reveal information concerning health, disability, racial or ethnic origin, religious beliefs, trade-union membership or other Article 9 categories.

TenderAI could also expose such information through retrieved passages or generated outputs if it is present in source documents.

**Assessment: TBD — legal review.** The client should establish whether Article 9 data enters the system and, if so, identify an applicable Article 9(2) condition and appropriate safeguards before processing.

## 2. Automated Decision-Making — Article 22

TenderAI does not currently make decisions about individuals with legal or similarly significant effects.

Its primary function is to assist users with tender analysis and proposal preparation. The system generates retrieval results, compliance assessments and draft responses, but a human user reviews and decides how those outputs will be used.

**Assessment: Article 22 is not currently identified as a primary risk based on the intended TenderAI use case.**

However, this conclusion must be revisited if the system is later used to score, rank, approve or reject individuals.

## 3. DPIA Trigger

The EDPB criteria were assessed as follows:

| EDPB criterion                                     | Applies?                                          | Reason                                                                                                                                             |
| -------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluation or scoring of people                    | **No / currently not identified**                 | TenderAI evaluates tender requirements and documents rather than individuals.                                                                      |
| Automated decision-making with significant effects | **No**                                            | The system does not currently make decisions about individuals.                                                                                    |
| Systematic monitoring                              | **No**                                            | The current use case does not involve systematic monitoring of individuals.                                                                        |
| Special-category data at scale                     | **Unknown**                                       | Production documents could contain Article 9 data, but this is not established in the current MVP.                                                 |
| Large-scale processing                             | **Unknown / likely not established at MVP stage** | The current project does not establish production volume or scale.                                                                                 |
| Matching or combining datasets                     | **Yes / potentially**                             | RAG combines uploaded documents, extracted content, metadata and retrieval results to produce outputs. This criterion must be assessed in context. |
| Vulnerable data subjects                           | **No / currently not identified**                 | The intended users are enterprise organisations and the system is not specifically directed at vulnerable individuals.                             |
| Innovative technology                              | **Yes**                                           | The system uses RAG, embeddings and generative AI technology to process enterprise information.                                                    |
| Cross-border processing                            | **Potentially**                                   | External AI/vector services may process data outside the EEA depending on production configuration.                                                |

### DPIA Assessment

At least the **innovative-technology** criterion applies, with potential application of **data matching/combining** and **cross-border processing** depending on the final architecture.

However, the lab's simplified two-criteria rule should not be treated as a legal test by itself. The actual DPIA requirement depends on whether processing is likely to result in a high risk to individuals' rights and freedoms.

**Assessment: DPIA — TBD / legal review required before production processing.**

Given the use of generative AI, external processors, potential personal data in enterprise documents and unresolved international transfers, conducting a DPIA before production deployment is the prudent recommendation.

## 4. Data Subject Rights Friction

### Right of Access

A client may need to identify what personal data concerning an individual exists across:

* source documents;
* extracted text;
* chunks;
* metadata;
* embeddings;
* retrieval records;
* generated outputs.

**Current capability: Partial / Unknown.**

The MVP does not yet provide a dedicated data-subject access workflow.

### Right to Erasure

Deletion can be operationally difficult because personal information may exist across source files, extracted content, chunks, vector records and generated reports.

**Current capability: Gap identified.**

A production architecture should support traceable deletion from all relevant storage layers.

### Right to Object

Where processing relies on legitimate interests, an individual may have a right to object in applicable circumstances.

**Current capability: TBD — legal review.**

The client needs an operational process for receiving, assessing and responding to objections.

### Right to Rectification

If inaccurate personal information is contained in source documents or subsequently appears in generated outputs, the client needs a process to correct the underlying data and prevent outdated information from continuing to be retrieved.

**Current capability: Gap / workflow not documented.**

---

# Phase 5 — Law Stacking Check

## AI Act Cross-Check

TenderAI is primarily an enterprise RAG assistant for tender/proposal work and, based on the current use case, is **not identified as a high-risk AI system merely because it uses generative AI**. The AI Act may impose transparency, GPAI or other obligations depending on the final deployment model and whether TenderAI is placed on the market as an AI system or integrates GPAI components, while GDPR separately governs personal-data processing.

## ePrivacy Check

**N/A based on the current architecture and documented use case.** TenderAI does not currently use cookies, tracking pixels, device-level tracking or electronic-communications metadata as part of its core RAG workflow. If the future client-facing application introduces tracking technologies, ePrivacy requirements must be assessed separately.

## Data Act Check

**N/A based on the current use case.** TenderAI does not currently process connected-product or IoT-generated data and does not involve cloud switching as a core function.

---

# Phase 6 — Compliance Memo

## Recommendation: Proceed with Conditions

**To:** Client Data Protection Officer / Legal Counsel
**Subject:** GDPR readiness assessment — TenderAI Enterprise RAG AI Assistant

### Bottom Line

**Proceed with conditions.** TenderAI can support the client's tender and proposal workflow, but production processing of documents containing personal data should not begin until the lawful basis, processor contracts, retention controls, international transfers and data-subject rights workflow are documented.

### Key Findings

The current TenderAI MVP was tested with synthetic enterprise documents and therefore does not intentionally process real-world personal data. The intended production architecture is different: client documents may contain names, professional contact information, employment/project information and other personal data, which can flow through document extraction, chunking, embeddings, Pinecone retrieval, LLM processing and generated outputs.

The main GDPR risk is therefore not the current synthetic MVP itself, but the transition from a controlled test environment to production client data.

### Top Three Actions

**1. Establish the production data-governance and contractual framework before processing personal data.** Confirm the controller/processor allocation, execute the required Article 28 DPA with applicable processors, document subprocessors, and verify the contractual and technical arrangements for OpenAI, Pinecone and hosting providers.

**2. Complete the lawful-basis, transfer and DPIA assessment.** For each processing purpose, document the applicable Article 6 basis. Where legitimate interests is considered, complete the three-part LIA. Confirm all processing locations and Chapter V transfer mechanisms, and complete a DPIA if the final processing is likely to result in high risk.

**3. Implement privacy-by-design controls before production.** Introduce document-level data minimisation/redaction, defined retention periods, deletion capability across source documents and vector records, access controls, and a documented workflow for access, erasure, rectification and objection requests.

### Residual Risks

Even after these actions, residual risks will remain. Personal information may be unintentionally included in uploaded documents, including potentially sensitive or special-category information. Generated AI outputs may reproduce inaccurate or unnecessary personal information despite source controls. Finally, reliance on external AI and infrastructure providers creates ongoing vendor, subprocessor, transfer and model/service-change risks that require continuing governance rather than a one-time compliance check.

### Accountability Position

This assessment is not a legal opinion, DPIA or certification. The client should be able to demonstrate its GDPR compliance through documented records including the DPA, lawful-basis analysis/LIA, DPIA where required, privacy notice, retention schedule, records of processing activities, subprocessor register, transfer assessment and data-subject rights procedures.

**Final recommendation: PROCEED WITH CONDITIONS.**

---

# Phase 7 — Accountability Verification

## Regulator Accountability Test

The question is:

> Could the organisation demonstrate GDPR compliance to a regulator using only the documentation currently contained in the TenderAI project?

**Answer: No — not yet.**

The project demonstrates the technical RAG architecture, but several GDPR accountability documents are not currently present.

| Documentation                                | Current status                 | Required action                                                                |
| -------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------ |
| Data Processing Brief                        | **Present**                    | Maintain and update for production architecture                                |
| Personal Data Inventory                      | **Present in audit**           | Validate with client                                                           |
| Controller/Processor Role Map                | **Present in audit**           | Confirm contractually                                                          |
| Article 28 DPA with TenderAI/client          | **Missing / TBD**              | Establish before applicable production processing                              |
| DPA / provider terms for external processors | **TBD**                        | Verify for each applicable provider                                            |
| Subprocessor register                        | **Missing**                    | Create and maintain                                                            |
| Lawful-basis assessment                      | **TBD**                        | Complete with client/legal counsel                                             |
| Legitimate Interests Assessment              | **Missing**                    | Complete if legitimate interests is selected                                   |
| DPIA                                         | **Missing**                    | Complete if final assessment confirms high risk; recommended before production |
| Privacy notice                               | **Missing from project**       | Update to cover relevant AI/RAG processing                                     |
| Retention schedule                           | **Missing**                    | Define retention and deletion rules                                            |
| Records of Processing Activities (ROPA)      | **Missing**                    | Client to establish/update                                                     |
| International-transfer assessment            | **Missing**                    | Identify locations and applicable Chapter V mechanisms                         |
| Data-subject rights workflow                 | **Missing**                    | Establish access, erasure, rectification and objection procedures              |
| Security controls/documentation              | **Partially documented / TBD** | Formalise production controls                                                  |
| Incident/breach response process             | **Missing from project**       | Establish documented process                                                   |
| AI vendor change/model-change governance     | **Missing**                    | Add contractual and operational controls                                       |

## Accountability Conclusion

The current project cannot yet demonstrate full GDPR accountability using the project documentation alone.

The main missing evidence concerns:

* lawful basis;
* DPAs;
* DPIA;
* retention;
* international transfers;
* subprocessors;
* privacy notice;
* ROPA;
* data-subject rights;
* incident response.

**Status: Gap identified — production governance required.**

---

# Phase 8 — Data Protection by Design Checklist

## Highest-Risk Activity

The highest-risk activity is the processing of client enterprise documents containing potentially identifiable personal information through the RAG pipeline and external AI/vector services.

| Design principle                                                                            | Current state of TenderAI                                                                                                                     | Pass / Fail / Unknown |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **Data minimisation: only the minimum necessary data is collected**                         | Users can upload enterprise documents, but the MVP does not technically enforce removal of unnecessary personal information before ingestion. | **Fail / Unknown**    |
| **Purpose binding: data is technically restricted to the stated purpose**                   | The architecture supports tender/proposal retrieval, but formal technical purpose restrictions and client-level policies are not implemented. | **Fail / Unknown**    |
| **Access controls: access is limited to those who need it**                                 | Application access exists, but a complete production GDPR access-control model and evidence are not documented in the MVP.                    | **Unknown**           |
| **Retention enforcement: automated deletion or anonymisation is in place**                  | No documented automated GDPR retention/deletion workflow currently exists across source files, chunks, embeddings and outputs.                | **Fail**              |
| **Subject rights workflow: system can support an access or erasure request within 30 days** | No dedicated end-to-end data-subject rights workflow exists in the MVP.                                                                       | **Fail**              |
| **Incident response: breach detection and 72-hour notification process is documented**      | No complete GDPR incident-response and notification workflow is documented in the project.                                                    | **Fail / Unknown**    |

## Required Changes

### Data Minimisation

Introduce upload guidance and technical controls to minimise personal data before ingestion.

Potential controls include:

* document classification;
* PII detection;
* redaction;
* exclusion rules;
* restricted document types;
* warnings before ingestion.

### Purpose Binding

Define the permitted purposes for each client knowledge base and prevent unrelated reuse.

The system should distinguish between:

* source-document purpose;
* tender/proposal purpose;
* generated-output purpose;
* any future secondary purpose.

### Access Controls

Implement role-based access control so users can access only the client knowledge bases and documents required for their role.

### Retention Enforcement

Define retention periods for:

* uploaded files;
* extracted text;
* chunks;
* embeddings;
* metadata;
* logs;
* generated reports.

Implement deletion procedures that cover the complete data lifecycle.

### Data Subject Rights

Create a traceability mechanism linking stored chunks/embeddings to source documents so that deletion or rectification requests can be acted upon.

### Incident Response

Document:

* breach detection;
* internal escalation;
* processor notification;
* investigation;
* controller notification;
* regulator notification where legally required;
* data-subject notification where required.

---

# Final Audit Summary

## Overall GDPR Status

**PROCEED WITH CONDITIONS**

The TenderAI MVP itself was developed and tested using synthetic enterprise documents and therefore does not intentionally process real personal data in the current test environment.

However, the intended production system is capable of processing personal data contained in client documents throughout the RAG pipeline.

The main GDPR gaps are governance and production controls rather than the core RAG functionality.

### Critical Pre-Production Actions

1. **Confirm the controller/processor structure and establish the required DPAs.**
2. **Determine lawful bases, international transfers and DPIA requirements.**
3. **Implement retention, deletion, minimisation and data-subject rights controls.**

### Principal Residual Risks

1. **Unintentional processing of personal or special-category information contained in uploaded documents.**
2. **AI-generated outputs reproducing inaccurate, excessive or unnecessary personal information.**
3. **Ongoing dependency on external AI/vector/infrastructure providers and their subprocessors, processing locations and service changes.**

### Final Position

> **TenderAI should proceed to production only with the GDPR conditions identified in this audit completed and documented. The synthetic MVP can continue to be developed and tested, but real client documents containing personal data should not be introduced into production until the outstanding GDPR governance and technical controls have been addressed.**

# Phase 3 — Lawful Basis Assessment

## 1. Purpose-by-Purpose Assessment

The lawful basis must be assessed separately for each processing purpose. The current TenderAI MVP uses synthetic enterprise documents, so no lawful basis has been established for processing real client personal data in the development environment. The following assessment applies to the intended production deployment.

| Purpose                                                          | Proposed lawful basis               | One-line justification                                                                                                                                                                                             | Flag for legal review?       |
| ---------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **1. Document ingestion and processing**                         | **Legitimate interests — proposed** | The client has a legitimate business interest in processing necessary enterprise information to prepare tenders and proposals; necessity and balancing must be demonstrated through an LIA.                        | **Yes — TBD — legal review** |
| **2. Text extraction, chunking and indexing**                    | **Legitimate interests — proposed** | Processing document content into searchable representations is necessary to operate the client's authorised TenderAI knowledge base for the stated tender/proposal purpose, subject to minimisation and balancing. | **Yes — TBD — legal review** |
| **3. Semantic retrieval and evidence grounding**                 | **Legitimate interests — proposed** | Retrieving relevant information from the client's knowledge base is necessary to provide evidence-grounded tender analysis and reduce unsupported AI-generated content.                                            | **Yes — TBD — legal review** |
| **4. Tender requirement analysis and compliance assessment**     | **Legitimate interests — proposed** | The client has a business interest in analysing tender requirements and identifying supporting or insufficient evidence, provided personal data is relevant and necessary to that purpose.                         | **Yes — TBD — legal review** |
| **5. LLM processing and generation of AI-assisted responses**    | **Legitimate interests — proposed** | Sending the minimum necessary retrieved content to the configured LLM service supports the client's tender-response purpose, subject to vendor safeguards, minimisation and transfer assessment.                   | **Yes — TBD — legal review** |
| **6. Generation of reports and proposal outputs**                | **Legitimate interests — proposed** | Generating evidence-based reports and draft tender responses supports the client's stated business purpose and should use only information necessary for that purpose.                                             | **Yes — TBD — legal review** |
| **7. Retention of documents, embeddings, metadata and outputs**  | **TBD — legal review**              | Retention depends on the client's documented purpose, retention schedule and whether continued storage is necessary; indefinite retention cannot be assumed to be justified.                                       | **Yes — TBD — legal review** |
| **8. Reuse of personal data for a materially different purpose** | **TBD — legal review**              | A new purpose may not be compatible with the original collection purpose and requires a separate purpose-compatibility and lawful-basis assessment before reuse.                                                   | **Yes — TBD — legal review** |

---

## 2. Legitimate Interests Assessment — LIA

Legitimate interests is proposed as the preliminary Article 6 basis for several operational TenderAI purposes because the scenario concerns a business client using its own enterprise information to support legitimate tender and proposal activities.

This is **not a final legal conclusion**. The client must complete and document an LIA before production processing where legitimate interests is relied upon.

### 2.1 Is the interest legitimate?

**Assessment: Potentially yes — subject to confirmation.**

The concrete business interest is to allow the client to efficiently search, analyse and reuse relevant enterprise information when preparing tenders and proposals.

TenderAI is intended to:

* retrieve relevant company evidence;
* assess tender requirements;
* identify supporting or insufficient evidence;
* reduce manual document-search effort;
* produce evidence-grounded draft responses and reports.

These are identifiable business purposes rather than an abstract interest in using AI.

**Status: TBD — legal review.**

---

### 2.2 Is the processing necessary?

**Assessment: Potentially yes — but data minimisation must be demonstrated.**

TenderAI's RAG architecture requires access to relevant document content in order to retrieve evidence and generate grounded outputs.

However, necessity does not automatically justify processing every piece of personal data contained in uploaded documents.

The client should therefore establish:

1. Which personal data is actually necessary for tender preparation.
2. Whether unnecessary personal data can be removed before ingestion.
3. Whether access can be restricted to relevant documents or document sections.
4. Whether anonymisation or pseudonymisation is possible.
5. Whether the same business objective can reasonably be achieved using less personal data.

For example, a tender response may require evidence of a project's technical experience but not the personal telephone number or private contact details of an employee mentioned in the source document.

**Status: TBD — legal review.**

---

### 2.3 Does the individual's interest override?

**Assessment: TBD — balancing test required.**

The client must balance the business benefit of AI-assisted tender preparation against the privacy impact on individuals whose personal data appears in enterprise documents.

Relevant factors include:

* reasonable expectations of the individuals;
* sensitivity of the information;
* whether special-category data is present;
* whether the information is publicly available or internally held;
* whether individuals were informed about the processing;
* the scale of processing;
* whether personal data is sent to external AI providers;
* whether safeguards such as access controls, minimisation, retention limits and deletion procedures are implemented.

The balance may be more favourable where only necessary professional information is processed, access is restricted, and personal information is minimised before transmission to external providers.

It may be less favourable where sensitive information is unnecessarily ingested, retained indefinitely, or transmitted to providers without adequate safeguards.

**Status: TBD — legal review.**

---

## 3. Purpose Limitation and Secondary Use

The client must distinguish between processing necessary for the stated TenderAI purpose and later reuse of the same personal data for unrelated purposes.

For example, personal data contained in an employee CV or project biography may originally have been collected for employment, project-management or corporate-record purposes. Uploading that information into TenderAI for tender preparation represents an additional processing activity.

Before such information is processed, the client should assess:

* the original collection purpose;
* the proposed TenderAI purpose;
* compatibility between the purposes;
* the individual's reasonable expectations;
* the nature of the personal data;
* the safeguards applied;
* whether another lawful basis is required;
* whether unnecessary personal data can be excluded.

**Finding: Purpose compatibility is not currently documented in the TenderAI MVP.**

**Risk level: Medium/High — depending on the categories and volume of personal data introduced into production.**

---

## 4. Current Development Environment vs Production

### Current MVP

The TenderAI MVP was developed and tested using synthetic enterprise documents.

Therefore:

> No real-world personal-data lawful basis is currently being relied upon for the synthetic test dataset.

### Production

Before real client documents containing personal data are uploaded, the client must establish the applicable lawful basis for each processing purpose and document the relevant safeguards.

The TenderAI implementation should not assume that because a document is supplied by an authorised client user, every category of personal data inside that document can automatically be processed for every TenderAI purpose.

---

## 5. Phase 3 Findings

### Finding 1 — Lawful bases are not currently documented

The MVP does not contain a production GDPR lawful-basis register linking each personal-data processing purpose to an Article 6 basis.

**Status: Gap identified.**

### Finding 2 — Legitimate interests may be appropriate but requires an LIA

Legitimate interests is a plausible preliminary basis for several client-controlled tender activities, but the three-part LIA must be completed by the controller before relying on it.

**Status: TBD — legal review.**

### Finding 3 — Necessity and data minimisation require further work

The system currently allows enterprise documents to enter the RAG pipeline without a documented mechanism that distinguishes necessary personal data from unnecessary personal information contained in those documents.

**Status: Gap identified.**

### Finding 4 — Secondary use requires purpose-compatibility analysis

The current project does not technically or contractually establish whether personal data originally collected for another purpose may be reused through TenderAI.

**Status: Gap identified — TBD — legal review.**

### Finding 5 — Retention requires a separate lawful-basis and purpose assessment

The current MVP does not define how long source documents, chunks, embeddings, metadata or generated outputs containing personal data should remain available.

**Status: Gap identified.**

---

## Phase 3 Conclusion

The current TenderAI MVP has not established a final lawful basis for production processing of personal data because it was developed using synthetic documents.

For production, **legitimate interests is a potential Article 6 basis for several tender-related processing activities**, but it cannot be treated as automatically valid. The client must complete the three-part LIA, demonstrate necessity and balancing, define retention periods, implement data minimisation, and assess whether any secondary use is compatible with the original collection purpose.

**Phase 3 status: Complete — proceed to Phase 4.**
# Phase 4 — Risk and Rights Analysis

## 1. Special-Category Data — Article 9

The current TenderAI MVP uses synthetic enterprise documents and has not intentionally processed real special-category personal data. However, production client documents could contain or reveal information concerning health, disability, racial or ethnic origin, religious beliefs, trade-union membership, political opinions, or other Article 9 categories, particularly where free-text CVs, employee biographies or project documents are uploaded.

TenderAI could also indirectly expose sensitive information through retrieved passages or generated outputs. The current system does not implement a dedicated Article 9 detection or filtering mechanism.

If special-category data is processed, the client must identify an applicable Article 9(2) condition and implement appropriate safeguards before processing. **Status: TBD — legal review.**

---

## 2. Automated Decision-Making — Article 22

TenderAI is primarily a decision-support and document-analysis system rather than a system that makes decisions about individuals. It analyses tender requirements, retrieves supporting evidence and generates assessments or draft responses for human users.

The current architecture does **not** automatically make employment, credit, insurance, eligibility or other decisions producing legal or similarly significant effects on individuals.

Human users review and control the final tender assessment and generated proposal content before it is used externally.

**Assessment: Article 22 is not currently triggered by the intended TenderAI use case, based on the available facts.**

However, this conclusion depends on the system remaining a business/tender-assistance tool. If a future deployment introduces automated scoring, ranking or recommendations about identifiable individuals that materially affect them, Article 22 must be reassessed.

**Status: No current Article 22 trigger identified — reassess if system scope changes.**

---

## 3. DPIA Trigger — EDPB Nine Criteria

The EDPB's criteria are used to determine whether processing is likely to result in a high risk to individuals.

| EDPB criterion                                            | Applies?                | TenderAI assessment                                                                                                                                                                                                             |
| --------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Evaluation or scoring**                              | **Potentially**         | The current system assesses tender requirements and evidence, but does not score or evaluate individuals. If future versions evaluate identifiable people, this criterion would become more relevant.                           |
| **2. Automated decision-making with significant effects** | **No — current design** | TenderAI does not make decisions producing legal or similarly significant effects on individuals. Human users review and control outputs.                                                                                       |
| **3. Systematic monitoring**                              | **No — current design** | TenderAI is not designed to systematically monitor individuals or their behaviour.                                                                                                                                              |
| **4. Sensitive data or data of highly personal nature**   | **Potentially**         | Client documents may contain special-category or highly personal information even though the current synthetic dataset does not.                                                                                                |
| **5. Large-scale processing**                             | **TBD**                 | The intended deployment could involve large volumes of enterprise documents, but the project does not yet define the number of data subjects, volume, geographic scope or duration of processing.                               |
| **6. Matching or combining datasets**                     | **Potentially**         | TenderAI combines uploaded documents, extracted text, chunks, embeddings, metadata, retrieval results and user prompts within the RAG pipeline. This is primarily document-level combination rather than profiling individuals. |
| **7. Vulnerable data subjects**                           | **Potentially**         | Employees or other individuals whose information appears in client documents may have limited control over how their professional information is reused in an enterprise AI system.                                             |
| **8. Innovative technology**                              | **Yes**                 | TenderAI uses generative AI, embeddings, vector search and RAG technology to process and retrieve enterprise information.                                                                                                       |
| **9. Cross-border processing / transfer**                 | **Potentially**         | External AI, vector-database and infrastructure providers may process information outside the EEA. Locations and transfer mechanisms are not yet fully established.                                                             |

### DPIA Assessment

At least **two EDPB criteria can potentially apply** to the intended production architecture, particularly **innovative technology** and **potential sensitive/highly personal data**, with additional criteria potentially applying depending on scale, data categories and international processing.

The current project therefore treats a **DPIA as likely required before production processing of real client personal data**, subject to confirmation by the controller and legal/DPO review.

The DPIA should specifically assess:

* personal data entering the RAG pipeline;
* potential special-category data;
* data minimisation;
* purpose compatibility;
* external AI processing;
* international transfers;
* access controls;
* retention and deletion;
* generated outputs;
* security risks;
* data-subject rights;
* potential model or retrieval errors;
* risks arising from incorrect or inappropriate information being surfaced to users.

**Status: DPIA likely required — legal/DPO confirmation recommended before production.**

---

## 4. Data Subject Rights Friction

### Right of Access — Article 15

A candidate or employee whose personal data appears in a client document may request access to their personal data.

TenderAI currently does not provide a dedicated GDPR rights-management interface capable of automatically identifying all instances of an individual's data across:

* source documents;
* extracted text;
* document chunks;
* metadata;
* embeddings;
* retrieval results;
* generated outputs.

A manual process would therefore currently be required.

**Current capability: Partial / operationally difficult.**

---

### Right to Erasure — Article 17

The current MVP does not implement a complete automated deletion workflow covering all representations of personal data.

Deleting the original PDF may not automatically remove:

* extracted text;
* chunks;
* embeddings;
* metadata;
* cached information;
* generated reports containing the information.

The production architecture therefore needs a deletion process that identifies and removes relevant derived representations where legally required.

**Current capability: Not demonstrated — gap identified.**

---

### Right to Object — Article 21

Where processing relies on legitimate interests, individuals may have a right to object in applicable circumstances, including to certain forms of profiling.

The current TenderAI MVP has no dedicated workflow for recording, evaluating and implementing objections relating to personal data contained within client documents.

The client therefore needs a documented process for receiving objections and determining whether processing must stop or whether another lawful basis or legal exception applies.

**Current capability: Not demonstrated — gap identified.**

---

### Other Relevant Rights

The production design should also consider:

* **Article 13/14:** transparency and information provided to individuals;
* **Article 16:** rectification of inaccurate personal data;
* **Article 18:** restriction of processing;
* **Article 20:** data portability where applicable;
* **Article 22:** automated decision-making rights if the system's scope changes.

The current MVP does not contain a dedicated rights-management workflow for these requests.

---

## 5. Phase 4 Findings

### Finding 1 — Special-category data controls are not implemented

The production architecture may receive documents containing Article 9 data, but the MVP does not contain dedicated detection, filtering or governance controls for such information.

**Status: Gap identified — TBD — legal review.**

### Finding 2 — Article 22 is not currently triggered

TenderAI is designed as a human-reviewed tender/proposal assistant and does not currently make decisions producing legal or similarly significant effects on individuals.

**Status: Pass for current scope — monitor scope changes.**

### Finding 3 — DPIA is likely required

The system uses innovative AI/RAG technology and may process highly personal or special-category information at potentially significant scale. Additional criteria may apply depending on production deployment.

**Status: Gap identified — DPIA required/confirmation recommended before production.**

### Finding 4 — Access requests are not operationalised

The current architecture does not provide a dedicated mechanism to locate all personal-data representations across the RAG pipeline.

**Status: Gap identified.**

### Finding 5 — Erasure is not fully implemented

The MVP does not demonstrate complete deletion of source data and derived representations such as chunks, embeddings and metadata.

**Status: Gap identified — high priority.**

### Finding 6 — Objection workflow is not implemented

The current system has no dedicated workflow for receiving and processing Article 21 objections relating to personal data used through TenderAI.

**Status: Gap identified.**

---

## Phase 4 Conclusion

TenderAI's principal GDPR risks are not currently associated with automated decisions about individuals. Instead, the major risks arise from **personal data entering the RAG pipeline, potential special-category information, insufficient retention/deletion controls, unresolved international processing, and the absence of mature data-subject-rights workflows**.

The current synthetic MVP reduces immediate privacy exposure during development, but it does not by itself demonstrate production GDPR compliance.

Before real client personal data is processed, the architecture should implement appropriate minimisation, retention, deletion, access-control and rights-management mechanisms and the client should complete the required DPIA and legal assessments.

**Phase 4 status: Complete — proceed to Phase 5.**
# Phase 5 — Law Stacking Check

## AI Act Cross-Check

**Risk tier: likely not high-risk under Annex III based on the current TenderAI use case.** TenderAI is an enterprise RAG assistant for tender analysis, evidence retrieval and proposal drafting rather than a system performing recruitment, credit assessment, biometric identification or another Annex III high-risk use case; however, the AI Act may still impose obligations depending on the final deployment and model-provider role, including transparency, AI literacy, documentation and GPAI-related obligations where applicable.

## ePrivacy Check

**N/A based on the current TenderAI architecture.** The current system does not use cookies, tracking pixels, device-level tracking or electronic communications content for its intended tender-analysis workflow; if a future web deployment introduces tracking technologies or processes electronic communications, ePrivacy requirements must be assessed separately.

## Data Act Check

**N/A based on the current TenderAI architecture.** TenderAI does not currently process data generated by connected products or IoT devices and does not involve a cloud-switching use case; the Data Act should be reassessed if the architecture later incorporates connected-product or IoT data.

---

## Phase 5 Conclusion

The GDPR remains the primary data-protection framework for TenderAI because the main compliance questions concern personal data processed through the RAG pipeline.

The AI Act provides an additional layer of AI-specific governance and should be assessed alongside GDPR rather than treated as a substitute for it. ePrivacy and the Data Act are not currently primary requirements based on the documented TenderAI scope.

**Phase 5 status: Complete — proceed to Phase 6.**
# Phase 6 — Compliance Memo

## GDPR Readiness — TenderAI Enterprise RAG AI Assistant

**To:** Client Data Protection Officer / Legal Counsel
**From:** TenderAI Project Team
**Date:** 19 August 2026
**Subject:** GDPR readiness assessment — TenderAI Enterprise RAG AI Assistant

### Bottom Line

**Proceed with conditions.** The TenderAI MVP can continue development and testing because the current environment uses synthetic enterprise documents, but production deployment with real client personal data should not begin until the key GDPR governance, contractual, transfer, retention and data-subject-rights controls are established.

### Top Three Actions

**1. Establish the production data-governance and contractual framework before processing real client data.**
Confirm the controller/processor allocation, execute the required Article 28 DPA where TenderAI acts as processor, document all subprocessors, and verify the contractual roles and data-processing arrangements of OpenAI, Pinecone and the final hosting provider. At the same time, identify every processing location and document the appropriate GDPR Chapter V transfer mechanism where personal data leaves the EEA.

**2. Complete a DPIA and formalise purpose, minimisation and retention controls before production deployment.**
The client should complete a DPIA addressing the use of innovative RAG/generative-AI technology, potential sensitive information, scale, international processing, access controls and data-subject risks. The client should also define which personal data may enter TenderAI, prohibit unnecessary sensitive information where possible, establish purpose-specific retention periods, and ensure that deletion covers source documents and relevant derived data such as chunks, metadata and embeddings.

**3. Implement a data-subject-rights and human-governance workflow.**
TenderAI currently does not provide a complete mechanism for locating, correcting, restricting or deleting an individual's information across the RAG pipeline. Before production, the client and TenderAI team should define procedures for access, erasure, rectification and objection requests, including ownership, response timelines and technical deletion procedures. Human review of AI-generated tender outputs should also remain mandatory before external use.

### Residual Risks

Even after these actions, three material risks will remain. First, sensitive or inaccurate personal information may enter uploaded documents and be reproduced in retrieved passages or generated outputs despite minimisation controls. Second, third-party model and infrastructure providers create continuing dependency on their security, processing locations and service changes. Third, complete deletion and rights management across source documents, embeddings and generated outputs may remain technically complex and require ongoing testing.

### What This Memo Is Not

This memo is a **first-pass compliance assessment**, not a legal opinion, DPIA, certification or guarantee of GDPR compliance. The client should engage its DPO and/or qualified legal counsel before relying on this assessment for production compliance decisions.

# Phase 7 — Accountability and Verification

## Accountability Test

The accountability principle requires the organisation to be able to demonstrate compliance rather than simply state that compliance measures exist.

The test applied here is:

> **Could TenderAI demonstrate GDPR compliance to a regulator using only the documentation currently available in the project repository?**

**Answer: No — not yet.**

The current project provides substantial technical evidence about the TenderAI architecture and RAG workflow, but it does not yet contain the full set of governance and legal documentation required to demonstrate production GDPR compliance.

---

## 1. Compliance Documentation Inventory

| Documentation                                               | Current status        | Assessment                                                                                                                                    |
| ----------------------------------------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data Processing Brief**                                   | **Exists**            | Documents the categories, sources, purposes, processing locations and potential data flows identified during this audit.                      |
| **GDPR Audit**                                              | **Exists**            | This document provides the first-pass GDPR assessment and identifies current compliance gaps.                                                 |
| **Data Processing Agreement (DPA)**                         | **Missing**           | No production Article 28 DPA with the client is currently included in the project.                                                            |
| **OpenAI processing agreement / contractual documentation** | **Missing / TBD**     | Provider terms, role, processing configuration and applicable contractual safeguards must be verified for the production deployment.          |
| **Pinecone DPA / contractual documentation**                | **Missing / TBD**     | Provider role, region, subprocessors and applicable contractual safeguards must be verified.                                                  |
| **Hosting-provider DPA**                                    | **Missing / TBD**     | Final production hosting provider has not yet been established in the project documentation.                                                  |
| **Legitimate Interests Assessment (LIA)**                   | **Missing**           | No formal LIA currently exists for any processing purpose relying on legitimate interests.                                                    |
| **Data Protection Impact Assessment (DPIA)**                | **Missing**           | The audit identifies a likely DPIA requirement, but a completed DPIA is not currently included.                                               |
| **Privacy Notice**                                          | **Missing**           | No production privacy notice explaining the TenderAI processing has been included in the project.                                             |
| **Retention Schedule**                                      | **Missing**           | Retention periods for documents, chunks, embeddings, metadata and outputs are not currently defined.                                          |
| **Records of Processing Activities (RoPA)**                 | **Missing**           | No formal Article 30 record covering the TenderAI processing activities is currently included.                                                |
| **Subprocessor Register**                                   | **Partial / Missing** | OpenAI and Pinecone have been identified, but the complete production subprocessor chain has not been documented.                             |
| **International Transfer Assessment**                       | **Missing**           | Processing locations and applicable Chapter V transfer mechanisms have not yet been fully established.                                        |
| **Data Subject Rights Procedure**                           | **Missing**           | No operational workflow currently exists for access, erasure, rectification, restriction or objection requests.                               |
| **Deletion / Erasure Procedure**                            | **Missing**           | The MVP does not demonstrate complete deletion across source files, chunks, metadata and embeddings.                                          |
| **Security / Technical Measures Documentation**             | **Partial**           | The project contains technical architecture and implementation information, but a formal GDPR security-measures document is not yet included. |
| **Incident Response / Breach Procedure**                    | **Missing**           | No documented production breach-response and notification procedure is currently included.                                                    |
| **AI Act documentation**                                    | **Partial**           | The project has previously been assessed through an AI Act lens, but production compliance documentation would still need to be maintained.   |

---

## 2. What a Regulator Could Currently Verify

A regulator could currently verify that:

* TenderAI is an enterprise RAG assistant designed for tender and proposal support.
* The MVP has been tested using synthetic enterprise documents.
* The technical architecture includes document ingestion, extraction, chunking, embeddings, vector retrieval and LLM processing.
* Personal data could enter the production RAG pipeline through client-uploaded documents.
* Potential external processing by OpenAI and Pinecone has been identified.
* The project has identified important GDPR risks involving retention, international transfers, purpose limitation, special-category data and data-subject rights.
* The project has considered GDPR alongside the AI Act, ePrivacy and Data Act.

However, a regulator could **not yet verify** from the repository that the production system has:

* a valid DPA framework;
* a completed DPIA;
* documented lawful-basis assessments;
* a defined retention schedule;
* a complete RoPA;
* a complete subprocessor register;
* validated international-transfer mechanisms;
* operational data-subject-rights procedures;
* tested deletion across the RAG pipeline;
* a documented incident-response process.

---

## 3. Highest-Priority Missing Evidence

The following documents should be created before production processing of real personal data:

### Priority 1 — DPIA

A formal DPIA should document the processing, necessity and proportionality assessment, risks to individuals and mitigation measures.

### Priority 2 — DPA and Processor Documentation

The client/TenderAI relationship and all relevant processor/subprocessor relationships should be documented through appropriate contractual arrangements.

### Priority 3 — Retention and Deletion Schedule

The organisation should define how long each representation of personal data is retained and implement deletion across:

**Source document → extracted text → chunks → metadata → embeddings → generated outputs.**

### Priority 4 — International Transfer Assessment

Every external processing location should be identified and the applicable Chapter V transfer mechanism documented.

### Priority 5 — Data Subject Rights Procedure

The production system should support a documented workflow for identifying and responding to requests for access, rectification, erasure, restriction and objection.

---

## 4. TBD — Legal Review: Information a Lawyer Would Need

The following information should be prepared before seeking legal advice:

1. **Exact client entity and jurisdictions** — who is the controller and where are the relevant data subjects located?
2. **Final production architecture** — where are the application, documents, vector database and generated reports hosted?
3. **Provider contracts** — what contractual terms and DPAs apply to OpenAI, Pinecone and hosting providers?
4. **Processing locations** — where does each provider store and process client data?
5. **Data categories** — exactly what personal and special-category data can enter the system?
6. **Volume and scale** — approximately how many documents and data subjects will be processed?
7. **Retention requirements** — how long does the client need each category of information?
8. **Purpose compatibility** — why was the information originally collected and why is it now being used by TenderAI?
9. **User access model** — which employees or contractors can upload and retrieve information?
10. **Deletion architecture** — how can a specific individual's information be located and deleted from every relevant representation?

Providing this information will allow counsel or the DPO to make a much more precise assessment instead of relying on assumptions.

---

## 5. Final Verification Finding

**Overall accountability status: PARTIAL — NOT PRODUCTION READY.**

TenderAI has sufficient technical documentation to explain the architecture and perform a first-pass GDPR assessment, but it does not yet have sufficient governance evidence to demonstrate full accountability for production processing of personal data.

The most important gap is therefore not that TenderAI is inherently incompatible with GDPR. The principal issue is that the project currently lacks the **documentary and operational controls required to prove compliance**.

The recommended path is to keep the MVP development and synthetic-data testing active while completing the missing governance documentation and technical controls before processing real client personal data.

### Final Audit Position

**PROCEED WITH CONDITIONS.**

The conditions are:

1. Complete the DPIA and lawful-basis assessments.
2. Establish DPAs and verify all processor/subprocessor arrangements.
3. Define retention and implement end-to-end deletion.
4. Complete the international-transfer assessment.
5. Implement data-subject-rights procedures.
6. Document security and incident-response measures.

**Phase 7 status: Complete — accountability test performed.**
# Phase 8 — Stretch: Data Protection by Design Checklist

The highest-risk processing activity in TenderAI is the ingestion and AI processing of client enterprise documents that may contain personal data. The following checklist assesses the current MVP against GDPR data-protection-by-design principles.

| Design principle                                                                            | Current state of TenderAI                                                                                                                                                                                                                                                                                 | Pass / Fail / Unknown |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **Data minimisation: only the minimum necessary data is collected**                         | The MVP accepts enterprise PDFs and processes their content without a production mechanism that automatically identifies and removes unnecessary personal data before ingestion. A production upload policy should restrict documents to those necessary for the stated tender/proposal purpose.          | **FAIL**              |
| **Purpose binding: data is technically restricted to the stated purpose**                   | The current architecture is designed for tender analysis, retrieval and proposal generation, but there is no documented technical control preventing uploaded information from being reused for another purpose. Purpose restrictions should be enforced through access, workflow and retention controls. | **FAIL**              |
| **Access controls: access is limited to those who need it**                                 | The MVP supports authorised users but the project does not yet document a production-grade role-based access-control model, tenant isolation policy or detailed audit logging for access to personal data.                                                                                                | **UNKNOWN**           |
| **Retention enforcement: automated deletion or anonymisation is in place**                  | No GDPR-specific automated deletion mechanism is currently implemented for source documents, extracted text, chunks, embeddings, metadata or generated reports. Retention periods must first be defined with the client and then technically enforced.                                                    | **FAIL**              |
| **Subject rights workflow: system can support an access or erasure request within 30 days** | The current MVP does not provide a dedicated workflow to identify, retrieve, export or delete all personal data associated with an individual across source documents, chunks, metadata, embeddings and generated outputs. A rights-management workflow is therefore required for production.             | **FAIL**              |
| **Incident response: breach detection and 72-hour notification process is documented**      | The MVP does not currently contain a documented GDPR incident-response procedure covering detection, investigation, escalation, controller notification and the GDPR 72-hour supervisory-authority notification requirement where applicable.                                                             | **FAIL**              |

## Required Changes for Fail / Unknown Findings

### 1. Data Minimisation

Before production deployment, establish an upload policy defining which documents and personal-data fields are necessary for TenderAI's tender-processing purpose. Where practical, unnecessary personal data should be removed or redacted before ingestion.

### 2. Purpose Binding

Document the permitted purposes for each category of client data and ensure that the application, user permissions and retention policies prevent unauthorised secondary use. Future use of historical information should require a separate legal and purpose-compatibility assessment.

### 3. Access Controls

Implement production-grade authentication and role-based access controls. Access should be restricted according to the user's role and client/tenant, with appropriate logging of document access and administrative activity.

### 4. Retention and Deletion

Define retention periods for:

* Original uploaded documents.
* Extracted text.
* Document chunks.
* Embeddings.
* Metadata.
* Retrieved passages where stored.
* AI-generated outputs and reports.

Deletion should propagate through the relevant storage and retrieval layers rather than deleting only the original PDF.

### 5. Data Subject Rights

Design a process that allows the controller to locate and manage personal data across the RAG pipeline. The production architecture should support appropriate access, correction, erasure and objection requests within the applicable GDPR deadlines.

Particular attention is required for embeddings because deleting the original source document alone may not remove all representations of the underlying personal data.

### 6. Incident Response

Create a documented security and privacy incident procedure covering detection, containment, investigation, controller notification, processor escalation and regulatory notification where required. The procedure should support the controller's assessment of whether a personal-data breach must be notified to the supervisory authority within 72 hours.

## Phase 8 Conclusion

The current TenderAI MVP demonstrates the core RAG functionality but is **not yet production-ready from a GDPR data-protection-by-design perspective**.

The most important engineering gaps are:

1. **No enforced data-minimisation mechanism.**
2. **No production retention/deletion workflow.**
3. **No dedicated data-subject-rights workflow.**
4. **Production access-control and tenant-isolation requirements are not yet documented.**
5. **No documented GDPR incident-response process.**

These controls should be addressed before real client personal data is introduced into the production TenderAI environment.

**Phase 8 status: Complete — GDPR design gaps identified and remediation requirements documented.**
