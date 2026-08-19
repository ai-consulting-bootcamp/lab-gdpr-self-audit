# Intellectus GDPR self-audit

**Project owner:** Paola Hintze  
**Assessment date:** 19 August 2026  
**Scope:** the evidenced public-data/demo MVP and the proposed production pilot are assessed separately. `TBD — legal review` is used where the project does not establish the facts needed for a reliable conclusion.

## Phase 1 — Personal data inventory

| Data category | Source | Purpose | Retention period | Crosses EU border? |
| --- | --- | --- | --- | --- |
| Consultant/client representative name, role or business contact data if entered | Direct intake/free text | Establish context and respond to the diagnostic request | Unknown; define case-based deletion | Unknown; deployment map missing |
| Free-text statements about identifiable people | Direct intake | Understand the stated organisational challenge | Unknown; define case-based deletion | Unknown |
| Public professional identity, role and affiliation | Organisation websites and bounded public search | Verify organisational context and evidence | Unknown; retain only cited evidence for an approved case period | Potentially; source and hosting locations vary |
| Public quotations, statements and contact details | Public websites/search results | Support or challenge diagnostic findings | Unknown; refresh or delete stale evidence | Potentially |
| URLs, provenance, retrieval dates and research snippets linked to people | Public web and workflow | Trace findings and enable human verification | Unknown; align with diagnostic retention | Unknown |
| Consultant user, run ID, timestamps and technical metadata | Web app/n8n | Security, troubleshooting and auditability | n8n configuration unknown; minimise and set a short schedule | Unknown |
| Uploaded file names/references | Consultant browser | Prospective document selection | Session-only in evidenced MVP; no server upload | No transmission evidenced; future state TBD |
| Employee/volunteer records and comments | Prospective client documents | Future organisational diagnosis | Not approved; schedule required before pilot | TBD — legal review |
| Donor/beneficiary information and case narratives | Prospective client documents | Future organisational diagnosis | Not approved; schedule required before pilot | TBD — legal review |
| Article 9 data or inferred sensitive attributes | Prospective documents or incidental public evidence | No approved purpose in current MVP | Exclude/delete unless specifically authorised | TBD — legal review |
| Diagnostic findings or hypotheses linked to a person | System inference, if future inputs permit it | No approved person-level decision purpose | Do not generate by default; retention TBD | TBD — legal review |

### Purpose-compatibility flags

- Public professional information was published for communication or transparency, not necessarily for AI-assisted organisational diagnosis. Reuse must remain bounded, expected, necessary and covered by the LIA; public availability does not remove GDPR protection.
- Internal HR, volunteer, donor or beneficiary data was collected for employment, programme delivery, safeguarding or fundraising. Reusing it for diagnosis, model improvement or cross-client benchmarking is not automatically compatible. The client must document the original purpose, notices, expectations and a lawful basis before any upload.
- No personal data may be used to train a model or improve the product under the diagnostic purpose without a separate assessment and transparent notice.

## Phase 2 — Role map

Roles depend on the operating stage. For the current demo, the project team determines the limited test/research purpose and acts as controller for any real public-source personal data it selects. In a client pilot, the client would normally determine why its internal data is analysed and act as controller; the Intellectus operator would normally be its processor. Final contracts and actual conduct must confirm this map.

| Entity | Role | Processing activity | DPA status |
| --- | --- | --- | --- |
| Social-impact client | Controller in production | Defines diagnostic purpose, data subjects, inputs and permitted outputs | N/A as controller; must execute processor DPA with Intellectus |
| Intellectus operator / Paola's delivery team | Controller for current self-directed demo; expected processor for client data | Intake, orchestration, research, report generation and consultant review | No production Article 28 DPA evidenced |
| Individual consultant | Authorised user under client/operator governance; separate role only if independently determining purposes | Submits intake and performs mandatory review | Access/confidentiality terms not evidenced |
| n8n hosting provider or self-hosted environment | Processor/subprocessor if it handles production personal data | Workflow execution, logs and payload handling | Hosting model and DPA unknown |
| Web hosting, storage and logging vendors | Processor/subprocessor | Serves app; future case-file and log storage | Vendors, regions and DPAs unknown |
| External AI/model provider | Prospective processor/subprocessor; not evidenced in current path | Future analysis of prompts/documents | Must remain disabled until vendor, DPA, settings and region are approved |
| Public website publishers/search service | Normally independent controllers, not Intellectus processors | Publish/index and return public-source material | DPA generally not the mechanism; terms and collection method require review |

### International transfers

The repository does not establish processing locations. Before production, create a data-flow and subprocessor register showing every region and remote-access location. Prefer EEA processing. For a transfer outside the EEA, record the applicable adequacy decision or execute the appropriate Standard Contractual Clauses and a transfer impact assessment; add supplementary technical measures where necessary. A vendor's general privacy policy is not a transfer mechanism.

## Phase 3 — Lawful basis assessment

| Purpose | Proposed lawful basis | One-line justification | Legal review? |
| --- | --- | --- | --- |
| Receive limited business intake and provide a requested diagnostic | Legitimate interests, Article 6(1)(f); contract only if necessary for a contract with the individual | A corporate client request creates a legitimate service interest, provided personal detail is incidental and minimised | Yes: confirm client type and notices |
| Bounded research on public professional information | Legitimate interests, Article 6(1)(f) | Relevant public professional evidence may support an organisation-level diagnostic when collection is necessary, expected and balanced | LIA required; completed below as first pass |
| Generate organisation-level findings and a consultant-reviewed draft | Client determines basis; Intellectus acts on documented processor instructions | A processor does not select a blanket basis for the client's employee, volunteer, donor or beneficiary data | `TBD — legal review` before private data |
| Keep minimal security and audit logs | Legitimate interests, Article 6(1)(f), or legal obligation where specifically applicable | Limited logs can protect the service and demonstrate authorised processing | Yes: define fields and retention |
| Process Article 9 data | No approved basis | Article 6 alone is insufficient; a specific Article 9(2) condition and necessity evidence are required | `TBD — legal review`; exclude by default |
| Train models, improve the product or benchmark clients with case data | No approved basis or purpose | This is distinct from delivering a diagnostic and is not necessary for the requested service | Prohibited until separately assessed |

### LIA A — bounded public professional research

1. **Purpose test — legitimate interest.** The concrete interest is to give a consultant a traceable, current evidence base for an organisation-level conversation and reduce unsupported assumptions. The interest is lawful and sufficiently specific; it does not include compiling person-level profiles.
2. **Necessity test.** Search must be limited to named organisations, a short research window and pre-defined diagnostic questions. Prefer organisational facts and aggregated data; retain a person's name or quotation only when the evidence cannot be understood without it. Less intrusive alternatives include client-supplied non-personal evidence, aggregate reporting and manual verification. If those alternatives meet the need, personal data must not be collected.
3. **Balancing test.** Professionals may reasonably expect their public role and official statements to be read, but not unlimited aggregation, sensitive inference or consequential scoring. Risks include loss of context, stale information and unexpected recombination. Controls are source citation, data minimisation, no sensitive/person-level inference, short retention, objection handling, consultant review and no automated individual decision. With these limits, the organisation-level use may proceed; scraping private/social profiles or expanding to vulnerable beneficiaries fails this LIA and requires new legal review.

### LIA B — intake and minimal operational logs

1. **Purpose test.** The interests are responding to a requested business diagnostic, securing the service and diagnosing failures.
2. **Necessity test.** Intake needs organisation-level context, not employee or beneficiary details. Logs need event, run and security metadata, not full request bodies. Optional fields and metadata-only logging provide less intrusive means.
3. **Balancing test.** A consultant expects submitted business information to be processed for the request, but named third parties do not. Free-text warnings, field limits, role-based access, metadata-only logs, a short deletion schedule and privacy information reduce the impact. The basis is defensible only after these controls and a documented right-to-object route are in place.

## Phase 4 — Risk and rights analysis

### Special-category data — Article 9

The demonstrated public-data MVP does not intentionally request Article 9 data, but free text or public evidence could reveal it. Future employee, volunteer, donor or beneficiary documents could contain health, disability, ethnicity, beliefs, political opinions or trade-union data and could also lead to sensitive inferences. There is no approved Article 9 condition; input validation should warn and block such data, and any production exception requires a specific Article 6 basis plus Article 9(2) condition and documented necessity.

### Automated decision-making — Article 22

The current system drafts organisation-level research findings and does not make legal or similarly significant decisions about people. A consultant must meaningfully review sources, unknowns, hypotheses and recommendations before client use, so Article 22 is not currently triggered. This conclusion must be revisited if Intellectus is used to rank staff, select beneficiaries, determine access to services or otherwise make consequential person-level recommendations; a nominal click-through would not count as meaningful review.

### DPIA trigger

Applied to the nine EDPB criteria: innovative technology applies to the MVP. Evaluation/scoring of people, solely automated significant decisions, systematic monitoring, large-scale processing and sensitive data at scale are not evidenced in the current demo; international-transfer obstruction is unknown. The intended private-document pilot would add matching/combining client and public datasets, data concerning potentially vulnerable beneficiaries, and possible sensitive information. Therefore a documented DPIA screening is required now, and a **full DPIA must be completed before enabling the described private-document pilot**, because at least innovative technology, dataset combination and vulnerable-person data are reasonably anticipated. Any unmitigated high residual risk must be escalated as required before processing.

### Data-subject rights friction

- **Access:** data may be split across source snippets, intake, n8n executions, logs and outputs. The current design has no subject-to-run index, so a timely complete search is not demonstrated. Add case IDs, source lineage and an owner for one-month responses.
- **Rectification:** a source may be wrong or a generated inference may misstate it. Preserve source/provenance, label facts versus hypotheses, permit correction and propagate changes to derivative outputs.
- **Erasure:** deletion must cover intake, execution payloads, logs, stored reports and caches without deleting another client's record. Current automated cascade deletion is not evidenced; configure retention and test case-level erasure.
- **Objection/restriction:** legitimate-interests processing requires an intake channel and the ability to pause public-source use while the objection is assessed. No operational workflow is evidenced.
- **Transparency:** people found through public research may not have interacted with Intellectus. Draft an Article 14 approach, including any carefully justified exception and public notice; do not assume public availability removes the duty.

## Phase 5 — Law stacking check

- **EU AI Act:** the present organisation-level decision-support use is not evidenced as an Annex III high-risk use. It should be treated as a minimal/limited-risk hypothesis, with AI literacy, clear disclosure of AI assistance, meaningful human review and traceable outputs; reassess immediately if person-level employment, eligibility or essential-service decisions are introduced.
- **ePrivacy:** the evidenced core does not require non-essential cookies, tracking pixels or electronic-communications content. If analytics, advertising cookies or similar device access is added, obtain valid prior consent where required and provide controls before activation.
- **Data Act:** N/A to the current system because it does not use connected-product/IoT data or provide a cloud-switching service. Reassess if the product scope changes.

## Accountability test

Could the project demonstrate compliance using its pre-audit documentation alone? **No.** The technical repository proves a bounded workflow, public evidence boundary, human-review requirement and absence of committed credentials/private client data, but it does not prove production GDPR governance.

| Accountability artefact | Status after this lab | Gap / next evidence |
| --- | --- | --- |
| Data-flow and processing brief | Draft exists in this submission | Validate against actual hosting and configurations |
| Personal-data inventory / draft ROPA input | Draft exists in this submission | Convert to an Article 30 record with owners, volumes and systems |
| LIA | First-pass LIA in this audit | Legal/DPO approval and periodic review missing |
| Controller-processor DPA and instructions | Missing | Execute before client personal data flows |
| Subprocessor and international-transfer register | Missing | Record vendors, countries, SCCs/adequacy and TIAs |
| DPIA | Missing | Complete before private-document pilot |
| Privacy notice / Article 14 approach | Missing | Publish before real personal-data research at scale |
| Retention and deletion schedule | Missing | Define per system and test deletion |
| Data-subject rights procedure | Missing | Assign owner, identity checks, search/export/deletion workflow |
| Access-control and review records | Partial technical boundary only | Implement roles, authentication and auditable approval |
| Incident-response and 72-hour escalation procedure | Missing | Document, assign and test |
| AI system/use-case register and human-review SOP | Partial project documentation | Add accountable reviewer, decision rules and review log |

### Legal-review preparation for private client documents

Counsel will need: each data-subject group; sample document types with personal data redacted; original collection purposes and privacy notices; exact diagnostic purposes; expected scale and frequency; special-category and vulnerable-person involvement; controller instructions; hosting/subprocessor countries; retention; model-training settings; access roles; intended outputs; and whether outputs can affect individuals. Preparing this evidence prevents the legal review from relying on an abstract architecture.

## Data protection by design checklist — private-document pilot

| Design principle | Current state | Result | Required change |
| --- | --- | --- | --- |
| Data minimisation | No production upload; no approved field/document allowlist | Unknown | Permit only approved formats/fields; redact identifiers and Article 9 data by default |
| Purpose binding | Diagnostic purpose is stated, but not technically enforced for private data | Fail | Encode purpose, client/case isolation and prohibition on training/reuse |
| Access controls | Public repo proves no credentials, not production identity or roles | Fail | Authenticated gateway, least-privilege roles, MFA where appropriate and review logs |
| Retention enforcement | No automated deletion/anonymisation evidenced | Fail | Set per-layer TTLs and test cascade deletion for intake, n8n, logs, files and outputs |
| Subject-rights workflow | No subject-to-source/run/output lineage or tested request process | Fail | Add searchable lineage, export/correction/deletion controls and one-month SLA ownership |
| Incident response | No breach workflow or 72-hour escalation evidence | Fail | Create detection, containment, processor notification and controller escalation playbook |

**Pilot gate:** do not enable private documents until every Failed/Unknown control has an approved owner, implementation evidence and acceptance test.

## Reference framework

- [GDPR — Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)
- [EDPB SME guide: DPIA criteria and compliance](https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en)
- [European Commission: GDPR application for organisations](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/application-gdpr_en)
- [European Commission: Standard Contractual Clauses](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en)
- [EU AI Act — Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
