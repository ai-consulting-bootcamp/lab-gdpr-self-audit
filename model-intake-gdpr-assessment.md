# Model Intake Brief: GDPR self-assessment

**Date:** 17 November 2026. **Recommendation:** proceed with conditions for the local educational prototype. Continue with offline fixtures and screened non-personal documents; hold unreviewed personal-data flows and external/client deployment until the gates below are met. This is a first-pass assessment, not a finding that a breach occurred.

Read [the processing brief](model-intake-data-processing-brief.md) first. Source and legal references are in [the evidence register](model-intake-evidence-and-sources.md). “Observed” means source inspection or recorded local execution; “confirmed” means the owner's statement; “potential” means a supported risk, not an assertion that real data was processed. Proposed safeguards and retention periods below are **not implemented**.

## Scope and GDPR applicability

The owner confirms local educational use of public model documents and no real client data. The inspected code can nevertheless collect and forward incidental personal data, and services receive operator metadata. GDPR territorial scope must be determined under Article 3 using the operator's establishment and actual activities; being public, educational or locally executed is not by itself an exemption. This assessment conservatively plans for an EEA professional context, without assuming the owner's location or applying the personal/household exemption to a future service. [E1–E9; L1]

## Phase 1: personal data inventory

Purposes: **P1** source discovery/provenance; **P2** evidence assessment; **P3** report review/retention/sharing; **P4** operation/troubleshooting. Multiple purposes have separate rows. “Unknown/potential” in the border column means the route is external but its geography is unverified; crossing an EU border within the EEA is distinct from a Chapter V transfer outside the EEA.

| Data category | Source | Purpose(s) | Retention period (known/estimated) | Crosses EU border? |
|---|---|---|---|---|
| Identifiable model-owner handle or personal provider name (possible; ordinary organisation IDs are non-personal) | Operator's model/provider fields and Hub response | P1: find the exact model and establish provenance | Current: transient run/session; API retention unknown. Proposed: discard raw content after the run | Unknown/potential: Tavily, HF and Jina routes |
| Same identifiable handle/name | Normalised target in assessment prompt | P2: bind findings to the model | Current: local run plus vendor handling, no verified account schedule. Proposed: retain organisation/model reference only where possible | Unknown/potential: OpenAI route |
| Same identifiable handle/name | Report header, metadata and local recent-model list | P3: retain review context | Current: no export expiry; session duration unverified. Proposed: 30-day review then delete/minimise exports | Local storage alone: no proven crossing; sharing/backup unknown |
| Named authors, named contact emails, personal references in page text (possible) | Public model cards/provider documents via Tavily/Jina; Hub `author` metadata | P1: retrieve source material | Current: in-memory source text and vendor handling; no fixed limit. Proposed: extract relevant sections and remove unnecessary identifiers immediately | Unknown/potential: external collection services |
| Same incidental names/emails/references | Snippets and extracted text in assessment prompt | P2: evaluate documentation | Current: up to 3,500 characters per source plus snippets; `store: false`; vendor retention not independently verified. Proposed: exclude identifiers before dispatch | Unknown/potential: OpenAI route |
| Same incidental names/emails/references in quotations | Generated findings, source metadata, exports | P3: human review and educational sharing | Current: manual deletion only for files; no schedule. Proposed: review at 30 days, retain only necessary redacted evidence | Unknown if published/shared; local-only copy does not establish a transfer |
| Identifying URL paths or query parameters (possible) | Search results and citations | P1: retrieve and check links | Current: run state and service logs unknown. Proposed: reject unnecessary identifying parameters before any request | Unknown/potential: Jina and source-site requests |
| Same identifying URLs | Report citations | P3: trace findings | Current: no expiry for exports. Proposed: stable non-identifying citations and 30-day review | Depends on report distribution and backup |
| Operator IP, request time, user agent, account-linked request/usage metadata | HTTP connection and API authentication; transient events/token usage | P4: deliver, secure and diagnose API service | Current: provider policies/settings unknown; local trace kept in session. Proposed: minimal local diagnostics, seven-day expiry if persisted | Unknown/potential: every external endpoint |
| Local run history and chosen models, if linked to an identifiable operator | Streamlit recent models, last trace/analysis; browser session persistence | P4: resume/replay the local workflow | Current: recent list capped at five entries, but count is not a time limit. Proposed: clear session after work and verify browser/server storage | Local by intended use; telemetry/backup route unverified |
| Special-category information or inferences about a person (contingent, not evidenced) | Unexpected source text or generated quote/inference | P2: unintended incidental processing; no authorised purpose | No approved retention or Article 9 condition. Proposed: reject before dispatch; restrict and delete accidental copies subject to documented incident handling | Potential if included in source/prompt |

**Non-personal boundary:** fixed regulatory passages, generic checklist queries and their vectors do not describe individuals in the inspected implementation. Pinecone stores that regulatory corpus; no evidence shows that source pages, user histories or reports are upserted there. Corporate names, download/like totals and model performance facts are not automatically personal data. API keys are secrets and account-linking credentials, so the audit neither reads nor publishes their values. [E2–E7]

**Purpose-change flags:** publication for attribution or contact does not automatically authorise sending a person's details to an LLM for model-documentation assessment (P1→P2), or republishing them in a downloadable/public demonstration (P2→P3). Those are potential secondary uses requiring necessity, expectations, transparency and compatibility analysis; the audit does not declare every public-source reuse incompatible. Personal contact information is usually unnecessary for the checklist and should be removed. No training/fine-tuning reuse is implemented; adding it would require a fresh purpose/basis assessment, not an assumption that existing access authorises it. [E3, E9; L1, L3]

## Phase 2: role map and transfers

Roles are activity-specific. A locally installed library is not itself a third-party processor. Vendor labels below are provisional until the service contract and its distinct account/security purposes are checked.

| Entity | Role (controller / processor / joint controller) | Processing activity | DPA in place? |
|---|---|---|---|
| Project owner, Sergii Rostovskyi | Controller for prototype purposes if GDPR applies | Chooses sources, APIs, report purposes and retention | No self-DPA needed; owner confirms no DPA documentation arranged |
| Client | No current client; future client normally controller | Defines business purpose and authorised use | N/A now; establish client–consultant DPA if consultant processes for it |
| Consultant/team | Same person as owner now, not a separate processor; future role conditional | Builds/operates service or accesses client data on instructions | N/A internally; future processor obligations require agreement |
| OpenAI API contracting entity | Expected processor for customer content; assess separate controller purposes under terms | LLM assessment; regulatory embeddings; service metadata | Applicability/acceptance not verified; obtain applicable DPA and subprocessor terms |
| Tavily contracting entity | Processor candidate for query service; separate controller purposes possible | Model queries, returned snippets, request metadata | Not documented; verify role and binding terms |
| Jina Reader contracting entity | Processor candidate for requested extraction; separate service purposes possible | URL fetch/extraction and service metadata | Not documented; public keyless access does not establish suitable processor terms |
| Hugging Face / source-site operators | Generally independent controllers for their own public publication/access logs; service-specific review needed | Public model metadata and HTTP access | An Article 28 DPA is not automatically required for independent-controller access; confirm actual service role |
| Pinecone contracting entity | Processor candidate where personal data is processed; corpus content currently non-personal | Regulatory vector storage/query; account/service metadata | No documented DPA; establish scope, terms and region before personal data is introduced |
| Streamlit and LangGraph software | No separate controller/processor merely through local library execution | Local UI and orchestration | N/A for local code; assess any actual telemetry recipient separately |
| Telemetry, OS backup/sync or future hosting vendor | Unknown; no hosted deployment confirmed | Conditional diagnostics, replication or hosting | Not evidenced; identify recipients before asserting coverage |
| GitHub | Ancillary repository service, outside the live inference path; terms determine roles | Code, Git identity and any deliberately published example reports | No lab-specific agreement evidenced; avoid personal data in submitted report examples |

No evidence establishes joint determination with a vendor, so no joint-controller relationship is asserted. If a future consultant contracts with vendors on a client's behalf, map the subprocessor chain and authorisation, rather than simply copying today's owner–vendor map. [E1–E8; L1]

| Route | Location/transfer finding | Mechanism and required evidence |
|---|---|---|
| Local application → OpenAI assessment/embeddings | Global endpoint in code; no account region evidence; personal source text possible in assessment | **TBD — legal review:** identify exporter/importer and locations; applicable adequacy (including verified entity/certification/scope if using EU–US DPF) or SCCs with transfer assessment and needed safeguards |
| Local application → Tavily / Jina | Queries, URLs, operator metadata; Jina also handles fetched content; geography unknown | **TBD — legal review** for each vendor; DPA alone does not prove a valid Chapter V route |
| Local application → HF / source sites | Direct model lookup or link check exposes IP/request metadata; geography unknown | Assess actual recipient role and whether the operation is a Chapter V transfer; document mechanism where required, rather than assuming every public HTTP request has the same role structure |
| Local application → Pinecone | Regulatory vectors non-personal; account/service data may be personal; selected cloud/region unverified | Verify index region, account terms, support/subprocessor access; apply transfer rules to any personal-data flow |
| Local export → backup, collaborator or GitHub | No automatic publication demonstrated; later distribution can create a separate disclosure | Keep personal data out of lab evidence; document recipient, jurisdiction, purpose and mechanism before any real-data sharing |

The required mechanism is **unverified**, not “SCCs in place.” EEA hosting would not alone resolve non-EEA support or subprocessor access. No cloud-console inspection, signed agreement review or production network capture was performed.

## Phase 3: lawful basis by purpose

These are candidate bases, not retrospective legal approval. The six Article 6 choices are consent, contract, legal obligation, vital interests, public task and legitimate interests. Public availability is not a seventh basis; the AI Act checklist is not itself a legal obligation to process authors' personal details. [L1, L3]

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| P1: collect public source provenance | Art. 6(1)(f), candidate only: **TBD — legal review** | Reliable model research can be legitimate, but only necessary public attribution may be defensible | Yes: LIA-1, indirect notice and source expectations |
| P2: assess evidence using LLM | Art. 6(1)(f), candidate only: **TBD — legal review** | Assessment has a concrete purpose, but sending incidental contacts is usually unnecessary when redaction is possible | Yes: LIA-2; hold identifiable payloads pending decision |
| P3: retain/share evidence reports | Art. 6(1)(f), candidate only for restricted evidence: **TBD — legal review** | Traceable review may justify limited attribution, not unrestricted public replication of contact data | Yes: LIA-3; remove unnecessary identifiers from demonstrations |
| P4: operation and minimal diagnostics | Art. 6(1)(f), candidate for controller's diagnostics: **TBD — legal review** | Minimal metadata may be needed to detect failures and protect service access | Yes: LIA-4, actual fields/recipients/retention must be established |
| Regulatory corpus indexing and generic retrieval | N/A for non-personal content; P4 covers personal service metadata | The inspected corpus and fixed queries do not relate to identifiable persons | Reassess if corpus/query contents change |
| Any future training, person scoring, marketing or sensitive-data analysis | No approved purpose or basis | No such workflow is established by the current implementation | Yes, before introducing it; Art. 9/10 conditions where relevant |

The owner being an API customer does not make Article 6(1)(b) a basis for processing unrelated authors' data. Vendor independent-controller activities require the vendor's own basis, while a processor acts within the controller's documented instructions. Consent, public task, vital interests and legal obligation are not evidenced for P1–P4.

### Three-part legitimate interests assessments

| LIA | 1. Legitimate interest | 2. Necessity and less intrusive alternative | 3. Balancing against the individual | Outcome |
|---|---|---|---|---|
| LIA-1 / P1 | Identify reliable documentation for an exact model and avoid misattribution | Model ID and corporate source URL are usually sufficient; remove named contacts and retain personal attribution only when essential | Professional publication may support limited research expectations; it does not eliminate privacy or notice duties. Identifiable sole developers and sensitive context need separate consideration | **TBD — legal review:** specific source necessity and reasonable expectations not established |
| LIA-2 / P2 | Reduce manual effort in comparing model documentation with a fixed checklist | Compare local/manual review and redacted excerpts. Synthetic probe shows the current payload keeps an unnecessary contact, so this example fails necessity | Additional vendor disclosure and retention can exceed expectations for a public contact; redaction and rights handling are not implemented | **TBD — legal review:** do not rely on LI for the unredacted probe-equivalent flow |
| LIA-3 / P3 | Preserve enough evidence for a human to verify findings | Retain model facts and stable citations; remove personal quotes/contacts; limit audience and lifetime instead of publishing full copies | Public duplication may amplify unwanted exposure and make deletion difficult; restricted, short-lived evidence is less intrusive | **TBD — legal review:** retention and distribution safeguards not established |
| LIA-4 / P4 | Keep API access reliable and diagnose failures or misuse | Prefer error category, time and minimal usage counts; avoid prompt bodies, persistent IP logs and identifiers unless necessary | Brief, access-limited diagnostics may be expected; undisclosed telemetry or indefinite linkage changes the balance | **TBD — legal review:** vendor settings, local retention and telemetry remain unverified |

## Phase 4: risk and rights analysis

### Special-category data (Article 9)

No real special-category data was established in this audit, and the tool is not intended to infer health, politics, religion, ethnicity, union membership, genetics, biometric identity or sexual life/orientation. Public source text or outputs could nevertheless contain such information about a person; a discussion of model bias or medical use alone is not a person's health record. No Article 9 condition is established, and public availability alone does not establish that the person manifestly made the relevant data public. Exclude it from the permitted workflow and record **TBD — legal review** before any intentional processing, with an Article 6 basis and separate Article 9 condition. [E1–E3; L1]

### Automated decision-making (Article 22)

The system assigns evidence statuses to model documentation, not scores to natural persons, and no legal or similarly significant personal decision is shown. It can inform model procurement, but the inspected workflow has no automatic approval/rejection action or client deployment. The user guide asks for human review; this is an intended safeguard, not an enforced decision record. If future use determines opportunities for identifiable developers or other people, reassess significance and meaningful human control, including intervention and contest routes where Article 22 applies. [E1, E6; L1]

### DPIA trigger

The screen below identifies one precautionary criterion, innovative technology, with sensitive content contingent rather than established. A mandatory DPIA is not demonstrated for the confirmed local public-document use, but a documented screening decision and applicable national mandatory-list check remain necessary before expansion. Two criteria generally indicate the need for a DPIA, while one can be enough where the processing is likely to create high risk; this is not a mechanical exemption. Reassess before adding sensitive content, person evaluation, vulnerable subjects, scale or systematic monitoring, and consult the supervisory authority if a completed DPIA leaves unmitigated high risk. [L1, L2]

| WP29/EDPB criterion | Applies now? | Project-specific reasoning |
|---|---|---|
| Evaluation or scoring of people | No evidence | Documentation status is about models; no personal profile/evaluation is implemented |
| Automated decisions with legal/similarly significant effect | No evidence | No decision execution about people |
| Systematic monitoring | No evidence | On-demand documentation lookup, not tracking individuals; repeated lookup alone is not necessarily personal monitoring |
| Sensitive data or data of a highly personal nature | Contingent/unknown | Not found in demonstrated input; uncontrolled source text can introduce it |
| Large-scale processing | No evidence | One local learner and a few source pages per run; lifetime usage volume unverified |
| Matching or combining datasets about people | No evidence | Combining regulatory text with model documentation does not establish person-level matching |
| Vulnerable data subjects | No evidence | No employee, child, patient or dependent-person workflow |
| Innovative use of technology | Yes, precautionary | LLM assessment with retrieval merits screening when personal text enters |
| Preventing exercise of a right or use of a service/contract | No evidence | Output does not gate a person's access or rights |

**Correction to the worksheet's shorthand:** its final item says “cross-border transfer preventing rights exercise”; the endorsed ninth criterion concerns prevention of rights or access to a service/contract, not international transfer by itself. Sensitive/highly personal data and scale are separate criteria. Cross-border risks are still assessed in Phase 2. [L2]

### Data subject rights friction

Access, correction and erasure are difficult because the implementation has no subject index, recipient ledger or coordinated deletion workflow across local downloads and API providers. Objection/restriction requests would require manual source suppression and pausing affected runs; simply regenerating a report could reintroduce the same information. A sole operator could manually handle a small case, but timely completion is not demonstrated, and no training-related unlearning capability should be claimed or required of a workflow that does not train models. The default response period is one calendar month, subject to lawful extensions and notice, rather than a universal 30-day deadline. [E3, E6–E8; L1, L5]

| Right | Current support / friction | Required operational response |
|---|---|---|
| Information, Arts. 13/14 | No privacy notice arranged; public-source data is indirect collection | Explain sources, purposes, recipients and rights; document any applicable Art. 14 exception rather than assuming one |
| Access, Art. 15 | Manual search of exports possible; no complete recipient/prompt ledger | Verify identity proportionately, locate copies and obtain processor assistance |
| Rectification, Art. 16 | Editable Markdown, but copies and future re-scraping remain | Correct/suppress affected personal text and notify relevant recipients as required |
| Erasure, Art. 17 | Manual file deletion only; vendor/backups unverified | Decide applicable grounds/exceptions, remove controlled copies, coordinate vendors and record limits |
| Restriction, Art. 18 | No flag or quarantine feature | Pause use and isolate affected material pending resolution |
| Portability, Art. 20 | Markdown export exists but is not a complete rights workflow | Applies only under the relevant consent/contract and automated-processing conditions; not automatically to these proposed LI activities |
| Objection, Art. 21 | No suppression list; no marketing workflow | Assess objections to LI and stop unless lawful overriding grounds apply; marketing objection is absolute if marketing is later added |
| Automated-decision protections, Art. 22 | Not triggered on established facts | Reassess if decisions about people are introduced; do not equate a disclaimer with meaningful human review |

## Phase 5: law stacking check

- **AI Act:** Hypothesis: not high-risk under the demonstrated documentation-research purpose; distinguish the wrapper from models it assesses, and review applicable AI interaction/output transparency and organisational literacy duties when deployed beyond personal learning. [L6]
- **ePrivacy:** No deliberate advertising pixels, private-message ingestion or marketing flow was found, but session persistence and unverified framework telemetry require browser/network inspection; necessary storage may be exempt, while non-essential device access needs prior consent under applicable national rules, whose satisfaction is unverified. [E6, E7; L7]
- **Data Act:** Connected-product/IoT data is N/A; cloud-switching terms may matter for Pinecone/API service procurement, without making the local prototype an IoT data holder or automatically imposing cloud-provider duties on its owner. [L8]

AI and GDPR compliance remain separate assessments. Do not rely on proposed Data Omnibus relaxations; the course sources have different update dates, addressed in [the evidence register](model-intake-evidence-and-sources.md#course-material-reconciliation).

## Findings and release gates

| ID | Gap / evidence | Priority and owner | Closure evidence |
|---|---|---|---|
| G1 | Unnecessary contact text reaches the assessment payload; synthetic proof [E9] | First: owner/developer; before further unreviewed live input | Pre-dispatch minimisation, approved input boundary and tests showing contacts excluded; reject sensitive/private content |
| G2 | DPA applicability, roles, actual regions and transfer routes unverified [E8] | Second: owner with counsel/vendor contacts; before personal-data transfer | Applicable accepted agreements, subprocessor list, routing/retention settings and justified transfer mechanism |
| G3 | No approved purpose-specific LIA or indirect-data notice [E8] | Second: owner/counsel; before reliance on LI | Completed necessity/balancing analysis, lawful-basis decision and notice/exception record |
| G4 | No export expiry or complete rights/incident process [E6–E8] | Third: owner; before external/client use | Approved retention schedule, deletion/access exercise, recipient register and incident playbook |
| G5 | DPIA decision, telemetry and browser persistence not fully verified | Third: owner; before external/client use | Signed screening and national-list review; actual storage/network inspection; expanded DPIA if required |
| G6 | Source collection is broader than privacy controls imply | First: developer; before unreviewed live input | HF page reads use explicit allowed domains; check redirect destination before sending requests; verify against controlled fixtures |

G6 follows code: the HF route calls `_read_pages` without `allowed_domains`, and direct link checking follows redirects before evaluating the destination. These are control gaps, not evidence of actual hostile redirection or disclosure. The supplied domain search filters and quote checks are useful but do not perform personal-data minimisation. [E2, E3]

## Accountability test

**Could the current project demonstrate compliance using only its existing documentation? No.** Architecture, usage limits and sample reports exist, but contracts, approved LIA, notice, retention/rights operations and transfer evidence are missing or unverified. This lab adds a brief, inventory, provisional role/basis analysis and action plan; it does not convert those drafts into accepted DPAs, approved legal decisions or implemented controls. See [the accountability and design checklist](model-intake-accountability-and-design.md).
