# GDPR Audit — Project 3: AI Interview Preparation Agent

**Lab:** Audit your own project — GDPR lens  
**System:** AI Interview Preparation Agent (Project 3)  
**Assessment type:** First-pass audit based on the reported workflow; implementation and vendor settings still require verification.  
**Decision:** **Proceed with conditions; do not use real applicants' CVs until safeguards are verified.**

> **Scope note:** This lab audits the **actual Project 3 agent**, not the fictional TalentBridge CV-screening case used in the previous partner lab. Statements marked **TBD — verify** are not claims that a control exists. No workflow execution, vendor agreement, or storage location has been independently inspected for this document.

## Kick-off — Data processing brief

The Project 3 AI Interview Preparation Agent accepts a user's **CV upload** and a **job description** through an n8n form. **User-reported safeguard:** before proceeding with the CV check, the workflow requests the user's consent/permission to analyse the CV. The exact consent text, whether refusal stops processing, and whether a timestamped record is kept have not been independently verified. It uses AI to produce personalised interview-preparation material, including suggested STAR-style responses. The reported workflow includes **n8n**, an **OpenAI GPT-4o-mini** model, **Pinecone** for retrieval-augmented generation (RAG), **Tavily** and **NewsAPI** for external research, and **Notion** for delivery/storage of generated reports. Exact node settings and routing must be verified against the actual workflow export.

The CV may contain a person's name, contact details, education, work history, employers, dates, skills and achievements. It might also contain a photo or voluntarily disclosed sensitive details (for example, disability or health information). The job description may contain employer and recruiter information. The agent may derive or generate assessments about the user's experience and interview suitability; generated STAR examples may include inaccurate or invented achievements unless checked.

**Sources:** direct CV and job-description submissions; public web/news sources retrieved for interview context; AI-generated draft answers. **Purposes:** (1) intake and parsing, (2) job-specific retrieval and contextual research, (3) generation of interview guidance, (4) delivery and temporary storage of the report, and (5) troubleshooting/security logging where enabled. There is **no confirmed purpose** of training or improving a vendor's models with submitted CVs; vendor terms and settings must be checked.

**Recipients:** the workflow operator and service providers listed above, but **which provider receives which raw or transformed fields is TBD — verify**. **Storage/processing locations:** not established; n8n deployment region, Pinecone region, OpenAI API processing arrangements, Notion workspace location, and other vendor access need verification. **Decisions:** the system recommends interview answers and preparation strategies; it is **not reported to select or reject job applicants**. The user decides whether to use the output. There is personal-data processing because an identifiable person's CV is submitted, even if the generated advice is only for personal use.

**Consent-control distinction:** A pre-check permission prompt is a positive transparency and user-control measure, but it does not by itself establish valid GDPR consent. The proposed Article 6 basis for delivering the requested coaching remains conditional on the actual service relationship; if consent is chosen as the legal basis, the controller must demonstrate that it is freely given, specific, informed, unambiguous and withdrawable. Verify the prompt and whether any data is transmitted before the user agrees.

## CFU — Recognize

- **Personal data:** identifiers, contact details, employment/education histories, CV text, job-description contacts, inferred strengths/weaknesses, generated interview narratives, and potentially request metadata/logs.
- **Article 9:** sensitive information may be included incidentally in CVs; its presence, handling and exclusion rules are not confirmed.
- **International transfers:** possible through cloud vendors; actual transfer routes and safeguards are **TBD — verify**.

## Phase 1 — Personal data inventory

| Data category | Source | Purpose | Retention (known/estimated) | Crosses EEA border? |
|---|---|---|---|---|
| CV identity/contact details | User-uploaded CV | Identify and process the correct interview profile | **Unknown**; set a short, justified retention schedule | **Unknown**; inspect n8n, LLM and storage routes |
| CV employment, education and skills | User-uploaded CV | Match experience to job requirements and draft STAR examples | **Unknown** | **Unknown** |
| Incidental sensitive CV details / photo | User-uploaded CV | **Not needed** for ordinary interview coaching; should be excluded | **Unknown**; remove before sending to vendors | **Unknown** |
| Job description, possibly recruiter contact | User submission | Tailor questions and contextual advice | **Unknown** | **Unknown** |
| Embeddings / retrieved text | CV/job data and Pinecone RAG | Retrieve relevant context for generation | **Unknown**; verify index deletion | **Unknown**; Pinecone region TBD |
| Generated STAR answers and coaching report | LLM output | Provide interview-preparation advice | **Unknown**; verify Notion retention and sharing | **Unknown** |
| Execution logs / form metadata | n8n and APIs | Troubleshooting, access control and security | **Unknown** | **Unknown** |
| Public research results | Tavily / NewsAPI | Job/company interview context | **Unknown** | Check whether personal CV data is included in search queries |

**Purpose-change warning:** Reusing submitted CVs, embeddings or generated reports for model training, analytics, marketing or unrelated product development would be a separate purpose requiring fresh assessment. No such reuse is established by the known workflow.

## Phase 2 — Role map

| Entity | Provisional role | Processing activity | Article 28 DPA in place? |
|---|---|---|---|
| Project operator / deploying organisation | **Controller, provisionally** for a directly offered interview-coaching service; depends on real deployment | Defines why/how CVs are processed | **N/A** for controller's own processing |
| Project builder/team | Under controller's authority, or processor if delivering the service for a separate client — **TBD** | Configures and operates workflow | **TBD** if a separate processor relationship exists |
| n8n hosting provider (if cloud-hosted) | Processor, subject to actual terms | Form intake, workflow execution and logs | **TBD — verify** |
| OpenAI API provider | Provider role and contractual arrangements **TBD — verify** | Processes prompts and generates advice | **TBD — verify** |
| Pinecone | Processor role **TBD — verify** | Stores/queries vectors and metadata | **TBD — verify** |
| Notion | Processor role **TBD — verify** | Stores/delivers reports | **TBD — verify** |
| Tavily and NewsAPI | Roles **TBD**; depend on submitted queries and provider terms | Public research/search | **TBD**; minimise personal information in queries |

**Transfer check:** Document each provider's contracting entity, region, remote access, subprocessors and transfer mechanism. Depending on the actual arrangement, an adequacy decision (including a verified EU–US Data Privacy Framework certification where applicable), SCCs and any necessary transfer impact assessment may be relevant. **Do not assume US transfers or DPF coverage without evidence.**

## Phase 3 — Lawful basis assessment

| Processing purpose | Proposed Article 6 basis | One-line justification | Legal review? |
|---|---|---|---|
| Pre-check user permission for CV analysis | **User-reported workflow control; not itself a confirmed Article 6 lawful basis** | The agent asks permission before starting the CV check; verify wording, opt-out behaviour and evidence of choice | **Yes:** inspect n8n nodes and consent record |
| Receive CV/job description and generate requested coaching | **Art. 6(1)(b) — contract**, *if* the user is the service customer and processing is necessary to provide the requested service | CV analysis is central to the requested personalised coaching service | **Yes:** confirm controller, service terms and necessity; otherwise **TBD — legal review** |
| Save/share report in Notion | **Art. 6(1)(b) — contract**, only if storage/delivery is necessary for the service | Delivers the requested output; optional long-term storage requires separate justification | **Yes:** verify sharing and retention |
| Necessary security and troubleshooting logs | **Art. 6(1)(f) — legitimate interests**, provisionally | Security and fault diagnosis can serve a legitimate interest if logs are limited | **Yes:** complete LIA |
| Optional improvement/training using CVs or reports | **TBD — legal review; not authorised by the above purposes** | Model improvement is not automatically necessary for providing an individual coaching report | **Yes:** disable pending separate assessment |
| Processing any Article 9 special-category CV information | Article 6 basis **plus a separate Article 9 condition** required | Ordinary contract/legitimate interests alone do not authorise special-category processing | **Yes:** exclude/minimise; assess any unavoidable processing |

**Three-step LIA — limited security logs:**
1. **Purpose:** detect abuse, errors and unauthorised access to a CV-processing service.
2. **Necessity:** retain only minimal technical metadata, with redaction of CV content; verify whether less intrusive monitoring suffices.
3. **Balancing:** users expect their CVs to remain confidential; short retention, strict access and no reuse are needed. **Result: TBD — legal review** until the actual logging settings and safeguards are checked.

## Phase 4 — Risk and rights analysis

**Article 9 — sensitive data.** CVs may contain photographs or voluntary disclosures about health, disability, religion or other protected characteristics, but the actual test inputs are not verified. These fields are unnecessary for most interview coaching and should be removed or masked before AI processing; if special-category processing remains, identify a valid Article 9 exception as well as an Article 6 basis.

**Article 22 — automated decisions.** The reported agent drafts coaching advice rather than deciding employment outcomes, so Article 22 is **not expected to apply to the described use**. Verify that the workflow does not automatically rank, reject, or forward decisions about applicants; generated recommendations should be reviewed by the user and must not be presented as verified facts.

**DPIA trigger.** The EDPB criteria potentially engaged are **evaluation/scoring** (the agent assesses a CV), **innovative technology** (LLM/RAG), **matching datasets** (CV plus job information), and potentially **sensitive data** if CVs include it. Large-scale processing, systematic monitoring, vulnerable subjects and significant automated decisions are **not established**. A **DPIA screening is required as a prudent next step**; whether a formal DPIA is legally mandatory depends on the actual scale, design and high-risk assessment, not simply on counting hypothetical criteria.

**Rights friction.** **Access:** data may be distributed across n8n executions, prompts, Pinecone vectors and Notion pages; the operator needs a reliable export/search procedure. **Erasure:** deleting the Notion report alone may leave vectors, logs or vendor-held copies; document an end-to-end deletion workflow. **Objection:** if legitimate interests support any processing, provide a route to object and assess requests; no working response process has been demonstrated.

## Phase 5 — Law stacking

- **EU AI Act:** **Provisional minimal-risk/general-purpose coaching application**, not the Annex III employment-selection category on the stated facts; transparency and provider-related duties must be assessed for the actual deployment, including whether users interact directly with AI and whether AI-generated material needs identification.
- **ePrivacy:** No cookies or tracking pixels are established in the reported workflow; **check** the n8n form, analytics and any communication-content handling before marking ePrivacy not applicable.
- **EU Data Act:** No connected-product or IoT data identified; cloud-switching provisions may be relevant to vendor contracts, but not the core CV-coaching purpose.

## Phase 6 — Client recommendation memo (approx. 350 words)

**To:** Data Protection Officer / Legal Counsel, Project 3 Interview Coaching Service  
**Subject:** GDPR readiness review — AI Interview Preparation Agent

**Bottom line: PROCEED WITH CONDITIONS.** The agent has a legitimate coaching purpose, but real CVs should not be processed until data flows, vendor terms, retention and deletion controls have been verified.

The workflow takes a user's CV and job description and generates personalised interview guidance using an LLM and retrieval services. That is useful, but CVs contain identifiable employment histories and sometimes information that applicants never intended to share with multiple cloud providers. The most immediate risk is not an automatic hiring decision: it is losing control of where the information goes, how long copies remain, and whether the output invents achievements.

**1. Map and secure every vendor flow before using live data.** Export the actual n8n workflow and identify exactly what is sent to OpenAI, Pinecone, Tavily, NewsAPI and Notion. Confirm hosting regions, access permissions, subprocessors, vendor reuse settings and applicable Article 28 agreements. Where data is transferred outside the EEA, document a valid transfer mechanism. Do not send raw CV details to public-search services unless strictly necessary; use synthetic test CVs while these checks remain open.

**2. Establish lawful purposes and minimise CV content.** Confirm whether Article 6(1)(b) supports providing the coaching service to the user, and separately assess any security logging under Article 6(1)(f). Do not assume those bases cover vendor model training or other product improvement. Remove unnecessary photos, contact details and sensitive disclosures before prompting or embedding. Conduct a documented DPIA screening, followed by a full DPIA if the actual processing presents likely high risk.

**3. Build deletion, access and output-quality controls.** Set short, documented retention periods for uploaded files, execution logs, Pinecone records and Notion reports. Test that a user's access or erasure request can be handled across the full chain. Restrict Notion page sharing and make it clear that STAR examples are drafts requiring the user's factual review; never fabricate achievements as if verified.

**Residual risks:** Third-party services may still create transfer or security exposure; generated interview examples can contain inaccurate claims; and complete erasure may be difficult where backups and distributed logs persist.

This is a preliminary technical compliance assessment, **not** a legal opinion, completed DPIA or certification. Legal counsel should validate the proposed lawful bases and agreements before production use.

## Accountability test — evidence status

| Evidence a regulator may request | Current status |
|---|---|
| Actual workflow export and data-flow diagram | **Not provided for this review** |
| Records of processing activities / purposes | **Draft in this audit; formal record not verified** |
| Privacy notice for CV submissions | **Unknown** |
| Pre-CV-check permission prompt and evidence of user choice | **Reported by project owner; prompt, gate and logging not inspected** |
| Article 28 DPAs and subprocessor lists | **Unknown** |
| International transfer assessment and mechanisms | **Unknown** |
| LIA for security logs | **Draft test only; not completed** |
| DPIA screening / full DPIA decision | **Not evidenced** |
| Retention and deletion schedule | **Not evidenced** |
| Data subject request handling test | **Not evidenced** |
| Access controls and incident response procedures | **Not evidenced** |

**Accountability conclusion:** Based on currently available evidence, the project could **not yet demonstrate full GDPR compliance to a regulator**.

## Stretch — Data protection by design checklist

**Highest-risk activity:** transmitting and storing a user's CV and derived interview profile across the LLM, RAG and report-delivery stack.

| Design principle | Current state / necessary change | Pass / Fail / Unknown |
|---|---|---|
| Data minimisation | CV upload is known; stripping names, photos and sensitive fields is not evidenced. Add redaction before LLM/RAG calls. | **Unknown** |
| Purpose binding | No verified technical block on secondary model-training or unrelated reuse. Review vendor settings and contract restrictions. | **Unknown** |
| Access controls | n8n, Pinecone and Notion permission settings have not been inspected. Apply least privilege and restrict report sharing. | **Unknown** |
| Retention enforcement | No tested automatic deletion for executions, vectors or reports. Set and test deletion periods. | **Unknown** |
| Subject rights workflow | No end-to-end access/erasure test evidenced. Create an owner, lookup map and response procedure (generally one month under GDPR Article 12). | **Unknown** |
| Incident response | No verified breach runbook. Establish detection/escalation and assessment of supervisory notification within 72 hours **where required**. | **Unknown** |

## Submission evidence and limitations

- **Input (known):** a submitted CV and job description through an n8n form. **Do not publish a real person's CV or identifiable sample in GitHub.**
- **Expected processing:** retrieve relevant context, generate STAR-style interview guidance, and deliver a report to Notion.
- **Output (known at design level):** personalised interview-preparation report. **A recovered sample report has now been supplied:** [Siemens interview preparation report](sample_output_siemens_interview_report.md). The original execution log and inputs are still unavailable for independent verification.
- **Observed limitation from prior project review:** AI-generated STAR responses may invent or embellish metrics; outputs need user fact-checking. Third-party CV exposure and deletion remain unverified risks.
- **Evidence to attach before submission:** sanitised workflow JSON export, redacted sample form input, redacted execution screenshot/log, if available. A recovered sample report is linked above. Never include secrets, tokens, personal CVs or private Notion links.


### Recovered output evidence (added after audit draft)

The project owner supplied the text of a previously generated [Siemens interview preparation report](sample_output_siemens_interview_report.md), report identifier `RPT-20261112-3688`. It demonstrates the structure of the agent output, including CV-to-job matching, evidence gaps, interview questions and STAR examples. The underlying CV, job description and n8n execution trace were not supplied, so accuracy and run provenance remain unverified. In particular, the 22% and 15% achievements and named example employers must be checked against candidate-provided facts before use.
