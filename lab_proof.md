# Phase 1: Personal data inventory

**Assessment date:** 18 November 2026  
**Scope:** Group A, procurement-report data, and Group B, author account/operator data, as distinguished in the data processing brief. “Possible” means the brief has not established that the item identifies a natural person. Current company records are synthetic; production data would need a fresh inventory.

| Data category | Source | Purpose(s) | Retention period (known/estimated) | Crosses EU border? |
|---|---|---|---|---|
| **Possible identifying details in web/news results** — names, descriptions, sole-trader details, or an identifying job title; names are not removed. | Articles and supplier web pages returned through Tavily/GDELT. | Use identifiable material, where present, as evidence for procurement-risk report claims; kept title/extract text is sent to the writing model. | Local run/report copies have no automatic expiry and remain until deleted; model-provider retention is not defined. | **Unknown.** Search/model vendor processing locations and subprocessors are not assessed; cannot rule out transfers outside the EU/EEA. |
| Same category: possible identifying details in web/news results | Kept search result and generated report. | Preserve quotes, links and dates in run records/reports so a reviewer can verify claims. | Local files have no automatic expiry; Notion/PDF copies may persist. Retention at those providers is not defined. | **Unknown.** Locations and transfers for local cloud sync, Notion and any report destination are not fully assessed. |
| **Public business email/phone details that could identify a natural person** — conditional; a generic company address/number alone may not identify a person. | Live web result; one historical result is in `runs/live-002.json`. | Historical capture in a run file. The brief cannot establish whether that text was also sent to OpenAI. Current code removes matching emails and some phone formats before the model prompt, run record and report; a national-format number may pass. | Historical run file remains until manually deleted. No automatic expiry. | **Unknown.** OneDrive cloud region and any applicable provider locations are not confirmed. |
| Same category: public business email/phone details | The historical live result copied into two regression-test files in the public GitHub repository. | Use as sample input to reproduce and test redaction behavior. | Replacement is planned, not done. Values remain in the repository and its history; GitHub retention/history details are not assessed. | **Unknown.** GitHub processing/location and any transfers are not confirmed. |
| **Sole-trader supplier identity or named supplier contact details** — possible, none confirmed in the current synthetic company data. | Supplier records or web search results. | If present in real data, calculate procurement exposure for that supplier. | Supabase retention is not defined; no automatic expiry is described. | **Unknown.** Supabase primary region is reported as `eu-central`; backups, support access and any other processing locations are unconfirmed. |
| Same category: sole-trader supplier identity or named contact | Supplier records or web search results. | If present in real data, provide supplier facts to the model and include relevant information in the report/recommendations. | Run files have no automatic expiry; reports may persist in Notion/PDF; provider retention is not defined. | **Unknown.** Model, Notion and other report-destination locations/transfers are not confirmed. |
| **Identifiable job-title or role information in policy passages** — possible in a small organization; no names were found in the reviewed policy files. | Internal policy documents (25 passages). | Retrieve relevant internal rules and use them to check/frame recommendations. | Passages remain in Supabase with no defined retention period; OpenAI retention for prompt/embedding calls is not defined. | **Unknown.** Supabase primary database region is `eu-central`; OpenAI processing and support locations have not been confirmed. |
| **Author's account identifiers/profile data** associated with OpenAI, Tavily, Supabase, Notion, n8n and Gmail accounts. API keys are credentials and should be secured; they are not automatically personal data by themselves. | Author's account registration and service use. | Authenticate and administer the services used to operate the prototype. | Provider account terms have not been reviewed. Local `.env` is excluded from publication; local retention/access controls need confirmation. | **Unknown.** Provider account locations and transfer terms have not been assessed. |
| **Email addresses** — the author's sender address and configured recipient address, which may identify a person. | Gmail account; recipient configured in n8n. | Address and deliver the report PDF and Notion link when the user clicks the email action. | No project deletion period is defined; copies may remain in n8n configuration/history and Gmail mailboxes under provider settings. | **Unknown.** Gmail and n8n processing/storage locations and subprocessors have not been confirmed. |
| **Personal data possibly embedded in operational logs/history** — not confirmed; usage logs are designed to contain only request number, model and token counts, but workflow history may retain payloads. | Local run/usage records, n8n execution history, Notion error table. | Monitor spending. | Local logs have no automatic deletion; n8n/Notion retention is not defined. | **Unknown.** Local `runs/` syncs through OneDrive (region unchecked); n8n/Notion locations and transfers are not assessed. |
| Same category: personal data possibly embedded in operational logs/history | Run traces and workflow execution records. | Troubleshoot errors and retain operational/test evidence. | No automatic deletion for local files; n8n history retention and access are not defined. | **Unknown.** OneDrive, n8n and Notion processing locations and transfers are not assessed. |

### Purpose-limitation flags

- **Public web/news details:** the original collection purpose and publisher's context are not established. Reusing identifiable names or contact details as evidence in an AI-assisted procurement report is a separate processing purpose to assess; public availability alone does not resolve compatibility or lawful basis.
- **Supplier records and policy passages:** current records are synthetic, so no real-person purpose change is confirmed. Before production, check whether identifiable supplier/contact details or role information collected for ordinary procurement or policy administration can also be used for AI-assisted analysis, prompt construction, report generation, testing and vendor processing.
- **Historical contact details:** the public business contact details were retained in a run file and copied into public test fixtures to support regression testing after being obtained from a live search. Confirm whether the relevant details identify a natural person; if they do, testing and public repository retention are additional purposes requiring assessment and remediation.

### Inventory limits and unresolved items

This inventory reflects the facts in the updated brief, not a verified audit of every vendor contract or production environment. The only confirmed infrastructure location is the Supabase primary database region (`eu-central`); **no cross-border transfer has been confirmed, but transfers outside the EU/EEA cannot be ruled out**. Confirm provider locations, subprocessors, backups, support access, retention periods and actual data in GitHub fixtures before completing the role map and lawful-basis assessment.

## Phase 2: Role map

**Scope:** The project has no real client or production users. The current prototype uses synthetic company records, but it has handled real public search results, and real contact details may remain in a historical run and public test fixtures. Roles below distinguish that current activity from the intended future bakery deployment. GDPR roles depend on who determines the purposes and essential means of each processing activity and on the actual contracts; this is a first-pass map.

| Entity | Role (controller / processor / joint controller) | Processing activity | DPA in place? |
|---|---|---|---|
| Bakery Foods Inc. (fictional intended client) | **No current role:** no real client or client personal data. In a future deployment, **likely controller** for procurement-related personal data because it would determine why the report is used and whose data is processed. | Would provide supplier/policy data and use the reports in procurement. | Not applicable to current prototype. For production, a controller–processor agreement with the developer is needed if the developer processes personal data on the bakery's documented instructions. No agreement is evidenced. |
| Author/developer | **Current: likely controller** for personal data in live search artifacts, tests and public repository if identifiable, because the author chose the test, storage and publication purposes. **Future: likely processor** when operating the integrated system solely on the bakery's instructions; may remain a separate controller for own account, security and independent development purposes. | Built/runs local app; handles search text and report data; keeps run files; created regression tests and published the repository; administers service accounts. | No client DPA applies to the current self-run prototype. A written Article 28 agreement with the bakery would be needed for processor activity before production; not in place/evidenced. |
| OpenAI — writing model/API | **Role TBD by contract and actual use.** Likely processor for personal data in prompts if it processes only on the controller's instructions; any own purposes would require separate role analysis. | Receives extracted report inputs, including search text after email/phone redaction; identifiable names may remain. | Data-processing terms/DPA status not established from the brief; verify the applicable account terms before personal data is sent. |
| OpenAI — embeddings API | **Role TBD by contract and actual use**, on the same controller/processor analysis. | Receives policy passages when loaded and fixed search phrases at run time; passages may contain identifiable role information. | Data-processing terms/DPA status not established; verify before personal data is sent. |
| Tavily | **Role for personal-data processing TBD.** Queries are built from product/market terms and contain no personal data by design; returned results may contain personal data. | Receives search words and returns title/extract/link/date results to the local app. | No DPA is evidenced. Confirm whether it receives or retains personal data and whether a processor relationship exists. |
| GDELT | **Role for personal-data processing TBD.** Queries are built from product/market terms and contain no personal data by design; returned results may contain personal data. | Receives search words and returns news results to the local app. | No DPA is evidenced. Confirm whether it receives or retains personal data and whether a processor relationship exists. |
| Supabase | **No personal data confirmed in current synthetic database.** In production, likely **processor** for any bakery personal data stored on the bakery's instructions. | Hosts the database; agent reads supplier, policy and other records. | No DPA is evidenced. Establish/verify Article 28 terms before production personal data is stored. |
| n8n / hosting operator (reported as Ironhack-hosted; legal entity and host not confirmed) | **Potential processor** for report content on behalf of the controller; role and subprocessor chain need confirmation. | Receives the finished report and PDF/link workflow payload; may retain execution history. | DPA, hosting contract and subprocessor terms are not established. Identify the contracting/hosting entities and confirm Article 28 terms before production. |
| Notion | **Potential processor** for report content on behalf of the controller; exact role depends on account terms and purposes. | Stores the completed/partial report automatically before review. Reports may contain identifiable people from web results. | DPA/terms not verified. Confirm the workspace plan, processing terms and subprocessors. |
| Gmail | **Role depends on account and purpose.** May process report delivery as a processor for the account holder and process account/service data for its own purposes; confirm terms. | Sends report PDF/Notion link on user click; processes sender and recipient addresses and message records. | DPA/terms not verified. Confirm account type and applicable data-processing terms. |
| Microsoft OneDrive | **Potential processor** for synced run/report files; confirm the account terms and any separate purposes. | The local `runs/` folder is in a OneDrive directory and syncs to cloud storage; it may include personal data. | DPA/terms and processing location not verified. |
| GitHub | **Role depends on the content and account terms.** The author is likely controller for deciding to publish test fixtures that contain identifiable contact details; GitHub's role for repository content must be confirmed from its terms. | Hosts the public repository and history, including two test files with real public business contact details that could identify a natural person. | DPA/terms and retention/history settings not reviewed. Remove or replace personal data and address repository history. |
| Service vendors as account providers (OpenAI, Tavily, Supabase, Notion, n8n, Gmail, Microsoft, GitHub) | Each may act as an **independent controller** for account, billing, security and service-use data, subject to its terms; this does not decide its role for report content. | Holds the author's sign-in/account identifiers and service metadata. | Controller-to-processor DPA is not the right default assumption for each provider's own account purposes; review each vendor's privacy terms and any separate processing agreement. |

### International transfers and transfer mechanisms

The brief does not establish that personal data has been transferred outside the EEA, but vendor and support locations are unknown, so no transfer mechanism can be confirmed. For any future or current transfer of personal data to a third country, identify the destination and recipient first; then document the applicable basis under GDPR Chapter V (for example, an applicable adequacy decision or Article 46 safeguards such as Standard Contractual Clauses) and any required transfer assessment. **No adequacy decision, SCCs, or other mechanism is evidenced in the project materials.** The Supabase `eu-central` primary database region alone does not establish the location of all processing, backups, support access or subprocessors.

### Role-map sources and caveat

- [GDPR, Regulation (EU) 2016/679 on EUR-Lex (Articles 4, 26, 28 and 44–46)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/)

This map does not establish legal roles from vendor names alone. Before production, verify actual contracts, instructions, vendor purposes, account plans, locations, subprocessors and transfers. Article 28 terms are required where a processor processes personal data on a controller's behalf; they are not a substitute for determining whether that relationship exists.

No joint-controller arrangement is apparent from the facts currently documented. If the author and bakery jointly determine the purposes and essential means of a processing activity, assess whether an Article 26 arrangement is required and document the allocation of responsibilities.

## Phase 3: Lawful basis assessment

**Assessment date:** 18 November 2026. The current project has no real client and uses synthetic company records. The entries below distinguish current, conditional processing of identifiable personal data from a possible production deployment. A “TBD” is intentional: the brief does not establish that the data identifies a person, that the relevant controller has selected a basis, or that the required assessment has been completed. Processors do not select a separate Article 6 basis for processing they carry out only on a controller's documented instructions; the controller must identify and document its basis.

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| Use identifiable details in public web/news results as source material for procurement-risk claims and AI-assisted report drafting (current test activity / future client use). | **TBD — legal review.** A controller may assess Article 6(1)(f) as a candidate only after the LIA below; public availability alone is not a lawful basis. | The business interest in substantiated procurement analysis may be legitimate, but necessity, reasonable expectations, source-purpose compatibility, transparency and impact on named individuals are unresolved. | **Yes.** Identify the controller, data subjects and publisher/source context; complete LIA and Article 6(4) compatibility assessment where this is further processing. |
| Retain identifiable quotes/source details in run records and reports so reviewers can verify claims. | **TBD — legal review.** No separate basis or retention need is documented. | Keeping evidence may support accuracy and accountability, but the project has no retention limit and may be able to retain a URL or redacted excerpt instead of identifiable details. | **Yes.** Determine necessity, minimize/redact, set a retention period, and confirm whether this is compatible with the original collection purpose. |
| Use sole-trader identity or contact details to calculate supplier exposure (conditional future processing; current supplier records are synthetic). | **TBD — legal review; candidate Article 6(1)(f) subject to LIA.** | Procurement continuity and supplier due diligence may be a legitimate business interest, but it is not yet shown that personal identifiers are necessary to calculate the exposure. | **Yes.** The bakery as controller must complete the supplier-data LIA and consider whether analysis can use an organization-level record or pseudonymous ID. |
| Send sole-trader details to the model and include them in a risk report/recommendations (conditional future processing). | **TBD — legal review; candidate Article 6(1)(f) subject to LIA and vendor/transfer review.** | The purpose may support procurement decisions, but including a person's details in an AI prompt/report could affect their business relationship; the actual impact, necessity, notice and vendor terms are unknown. | **Yes.** Confirm whether personal data is needed at all; if so, complete LIA, transparency and purpose-compatibility review before sending it to a model provider. |
| Use real public business contact details in regression tests and retain them in public GitHub fixtures/history, if they identify a natural person. | **TBD — legal review; no basis is evidenced.** | Reproducing the redaction bug can be achieved with synthetic placeholders, so continuing to publish real contact details is not shown to be necessary. | **Yes — remediate now.** Replace with synthetic values and remove the real values from repository history where feasible; confirm whether the contacts are personal data and document the incident/remediation assessment. |
| Use an identifiable job title/role in a policy passage to retrieve and apply an internal rule (conditional; no names found in reviewed policies). | **No Article 6 basis needed if the passage does not relate to an identifiable person. If it does: TBD — legal review.** | The system's purpose is to apply organizational policy, but a role should be generalized or removed if it identifies a person and is not necessary. | **Yes, if identifiable.** Verify small-company linkability and minimize before embedding or sending the passage to the model. |
| Process the author's account identifiers/profile data to provide and administer the author's service accounts. | **TBD — each service provider's own basis; outside the bakery's report-processing basis.** | The service provider determines its own purposes and terms for account administration; this project has not reviewed those notices or established each provider's basis. | **Yes.** Review the relevant account privacy notices/terms; do not treat this as the lawful basis for report content. |
| Use sender/recipient email addresses to send the report PDF and Notion link after the user clicks send (if an address identifies a person). | **TBD — legal review.** | The recipient, their relationship to the controller and whether delivery is necessary to a contract or supported by another basis are not defined. | **Yes.** Identify the controller, recipient and context; document the basis and provide any required privacy information before production. |
| Process personal data that may be embedded in logs/history to monitor spending. | **No basis required for the described usage log if it contains only non-personal request/model/token metadata. If personal data is present: TBD — legal review.** | The brief says usage logs contain no names by design, but workflow histories may retain report payloads; inspect actual fields and avoid logging report content for cost control. | **Yes, if any personal data is present.** Verify payloads and configure minimization/retention. |
| Retain personal data in logs/history to troubleshoot errors or preserve test evidence (if present). | **TBD — legal review; no separate basis established.** | Error investigation may be a legitimate operational need, but current data can be replaced with redacted/synthetic samples and no retention period is set. | **Yes.** Keep only necessary, redacted diagnostics for a defined period; establish a basis if identifiable data remains. |

### Legitimate Interests Assessment (LIA) — candidate only, not an approved basis

The following preliminary tests cover the candidate Article 6(1)(f) uses above. The conclusion for each remains **TBD — legal review**; the test does not itself establish a lawful basis or resolve purpose compatibility.

**LIA A — identifiable web/news details used in procurement-risk analysis**

1. **Legitimate interest?** Potentially, the controller has a concrete interest in assessing supply risks and supporting procurement decisions with verifiable sources. The controller and the precise interest must be identified.
2. **Necessary?** Not established. The same report may often use company-level facts, URLs, or redacted quotations without processing a person's name or contact details. Retain identifiable details only where the specific claim cannot reasonably be supported without them.
3. **Balancing?** Not established. A person may not expect an article or supplier-page reference to be reused in a commercial AI-assisted report; the report may affect reputation or a supplier relationship. Human review and source citations reduce some risks but do not settle the balance. Transparency, objection handling, safeguards and the source context need assessment.

**LIA B — sole-trader details used for procurement due diligence/reporting**

1. **Legitimate interest?** Potentially, the bakery may have a concrete interest in assessing supplier continuity, reliability and exposure.
2. **Necessary?** Not established. Test whether the procurement analysis can use a supplier ID or business-level attributes without sending a person's name/contact details to the AI model or including them in the report.
3. **Balancing?** Not established. The processing may affect an individual's business relationship, and data is sent to external services. The nature and sensitivity of the information, reasonable expectations, consequences, transparency, human review, vendor safeguards and rights must be assessed.

### Purpose compatibility reminder

For personal data collected for another purpose, document the original purpose and assess compatibility before reusing it for AI-assisted reporting, testing, public repository fixtures, or vendor processing. Article 6(4)'s compatibility factors are a separate question from selecting an Article 6(1) lawful basis; a candidate legitimate interest does not, by itself, resolve compatibility. The historical public contact details in tests should be replaced with synthetic values rather than retained while the basis is unresolved.

### Sources

- [GDPR, Regulation (EU) 2016/679 on EUR-Lex (Articles 5, 6 and 6(4))](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/)
- [EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f), final version](https://www.edpb.europa.eu/system/files/2024-10/edpb_guidelines_202401_legitimateinterest_en.pdf)

## Phase 4: Risk and rights analysis

### Special category data (Article 9)

The brief identifies no special-category data in the reviewed company or policy records, and the system is not designed to infer health, biometric, political, religious, ethnic-origin, trade-union, or sexual-orientation information about people. However, public web/news text is not fully screened for incidental sensitive information, and names are not removed. Before production, filter or exclude any such data; if processing is actually necessary, the controller must identify an applicable Article 9(2) condition as well as an Article 6 basis before processing.

### Automated decision-making (Article 22)

On the described design, Article 22 does **not appear to apply**: the system rates organizational procurement risks, takes no action automatically, and a human reads the report before deciding outside the system. Reassess if identifiable sole traders are evaluated or the bakery relies on the report to make a decision that legally or similarly significantly affects them; a nominal review that simply rubber-stamps the output may not be meaningful human involvement. If Article 22 applies, the controller must identify a permitted Article 22(2) exception and safeguards, including human intervention, the person's opportunity to express a view, and to contest the decision where Article 22(3) applies.

### DPIA trigger: EDPB nine-criteria screen

This is a preliminary screen of the possible production processing. The “two or more” rule is a screening heuristic: Article 35 requires a DPIA before processing where the nature, scope, context and purposes are likely to result in high risk; supervisory-authority lists and other facts also matter. The project should complete a documented DPIA screening before any real personal data is used in production.

| EDPB criterion | Applies? | Assessment based on the brief |
|---|---|---|
| 1. Evaluation or scoring | **No for people as currently designed; conditional** | The system scores/rates product and contract risks, not people. Reassess if supplier identity or risk scores become assessments of a sole trader's reliability or economic situation. |
| 2. Automated decision-making with legal or similarly significant effects | **No on current facts** | No decision or action is automated and the stated user reviews the report. Reassess actual practice if a human routinely follows recommendations affecting a sole trader. |
| 3. Systematic monitoring | **No on current facts** | The brief describes commodity searches and report runs, not systematic monitoring of people's behavior or location. |
| 4. Sensitive data or data of a highly personal nature | **Not identified; possible incidental exposure** | No such data is intended or found in reviewed records. Search/news results could contain it, so test and document filtering. |
| 5. Large-scale processing | **No for the current MVP; future scale unknown** | The brief reports 14 runs by one author and synthetic company data. The size, duration and geographic spread of any production processing are not established. |
| 6. Matching or combining datasets | **Conditional / likely if personal data is present** | The agent combines supplier/contract records with public web/news material. No personal data is confirmed in the company records, but identifiable sole-trader or contact details could be matched into a report. |
| 7. Data concerning vulnerable data subjects | **No indication** | The intended users and affected parties are business suppliers; the brief identifies no children or other vulnerable groups. Reassess if the subject group changes. |
| 8. Innovative use of technology or organisational solution | **Likely yes** | The system integrates generative AI, embeddings, web search and automated report generation in procurement analysis. Record the exact processing and risk context rather than treating AI use alone as an automatic DPIA conclusion. |
| 9. Processing that prevents people from exercising a right or using a service/contract | **No on current facts** | The system does not control access to a service or contract for a person. Unknown data locations and the lack of a rights workflow create response friction, but do not by themselves show that the processing prevents a person from exercising a right. |

**DPIA conclusion:** Criterion 8 likely applies, and criterion 6 may apply if personal data is matched across supplier records and search results. If both are confirmed for production, the two-criteria screen points toward a DPIA; given the missing scope, actual personal-data presence and vendor-flow facts, treat the outcome as **TBD — legal review**, and complete the screening before deployment rather than concluding that no DPIA is needed.

### Data subject rights friction

- **Access (Article 15):** A request could require searching local run files, prompts/logs, report PDFs, Notion, email, GitHub fixtures and vendor-held copies. No person-based index or documented request workflow is described, so a complete and timely response is not demonstrated.
- **Erasure (Article 17):** Local files can be deleted manually, but no automated deletion exists; copies may remain in GitHub history, Notion/email, provider logs or backups with unknown retention. The design does not demonstrate a way to locate, erase or instruct processors to erase all applicable copies within the response period, subject to the right's exceptions.
- **Objection (Article 21):** The system has no documented process for receiving or routing an objection to processing based on legitimate interests. If the controller adopts Article 6(1)(f), it must be able to assess and respond to objections and stop the relevant processing where required.
- **Rectification (Article 16):** Source claims may be wrong or outdated, and no correction workflow for a person mentioned in a report is documented. A reviewer can ignore a report or start another run, but that does not establish a process to correct retained copies or notify recipients where required.

**Current capability:** Based on the brief, the system cannot yet demonstrate timely, end-to-end handling of access, erasure, objection or rectification requests across all copies and vendors. The controller should define a request channel, identity/record search process, response owner, processor instructions, and deletion/correction evidence before production.

### Sources

- [GDPR, Regulation (EU) 2016/679 on EUR-Lex (Articles 9, 15–17, 21–22 and 35)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/)
- [EDPB: DPIA criteria for small businesses](https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en)
- [Court of Justice of the EU, C-634/21, SCHUFA (Article 22 and significant reliance on automated outputs)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62021CJ0634)

## Phase 5: Law stacking check

- **AI Act cross-check:** Phase 2 classified the stated procurement use as not apparently prohibited or Annex III high-risk, with Article 50 transparency obligations to assess; Article 50 user notice/output marking and Article 4 AI-literacy measures add requirements that are distinct from the GDPR lawful-basis, rights and DPIA analysis. ([AI Act, Articles 4 and 50](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727))
- **ePrivacy check:** The brief does not describe cookies, tracking pixels, or other access to/store of information on a user's device; therefore Article 5(3) consent is **not shown to be triggered**, but the Gradio/browser implementation should be checked before deployment for non-essential terminal storage/access. Sending a report by user click is not, by itself, evidence that the cookie-consent rule applies; the confidentiality of the email communication and any personal data in its content still need appropriate handling. ([ePrivacy Directive, Articles 5(1) and 5(3)](https://eur-lex.europa.eu/legal-content/EN/TXT/ALL/?uri=CELEX:32002L0058))
- **Data Act check:** The system uses no connected-product or IoT data. It does use cloud services, but the brief identifies no cloud-switching or porting activity; **currently N/A on the known facts**. If a customer requests switching/export between cloud or other data-processing services, assess the Data Act's Chapter VI obligations and the actual service contracts. ([Data Act, Chapter VI](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854))

## Phase 6: GDPR compliance memo

**To:** Data Protection Officer, Bakery Foods Inc. *(fictional client; if none, Legal Counsel)*  
**From:** Project consultant  
**Date:** 19 November 2026  
**Subject:** First-pass GDPR review — Procurement Risk & Mitigation Agent

### Bottom line: Proceed with conditions

Do not use the current prototype with real supplier or contact-person data in production until the data flows, lawful bases, vendor terms, retention and rights processes are confirmed. The prototype has no real client or production users and uses synthetic company records, but real public search-result contact details remain in a historical run file and public regression-test files; whether they identify natural persons is not yet confirmed.

### Top three actions

1. **Immediately — Developer/repository owner:** Replace real contact details in test fixtures with synthetic placeholders, remove them from the active public repository, and assess whether repository history can be cleaned. Confirm whether the historical details identify people and whether the run/test publication needs further remediation. Keep real personal data out of test and demo materials.
2. **Before any production data flows — Bakery DPO/Legal and developer:** Map each personal-data flow and recipient, confirm controller/processor roles, execute Article 28 terms where the developer or a vendor acts as processor, and verify locations, subprocessors and any Chapter V transfer mechanism. The controller should document a lawful basis for each purpose; if relying on legitimate interests, complete the LIA and assess compatibility with the original collection purpose. Minimise or redact personal data that is not needed.
3. **Before launch — Bakery DPO with product team:** Complete and document a DPIA screening. If personal data is matched across supplier records and web results alongside the system's innovative AI processing, carry out a DPIA before deployment. Set retention periods and a workable access, correction, erasure and objection process across local files, reports and vendors; train users to treat automatically saved reports as unreviewed drafts.

### Residual risks

Even after these actions, public-source information may be incomplete or misleading, and people may not expect their information to appear in a commercial procurement report. Vendor retention, support access and onward transfers may remain difficult to verify. Human review may not prevent a report from influencing a decision about a sole trader, particularly if reviewers routinely rely on its recommendations.

### Caveat

This is an educational, first-pass assessment based on the supplied brief. It is not a legal opinion, a completed DPIA, or a certification. Bakery Foods Inc. and its company data are fictional. A qualified privacy lawyer or the client's DPO should confirm the analysis before any real-person data is used in production.

## Reinforce: Accountability evidence and legal-review preparation

The GDPR accountability principle means the controller must be able to demonstrate compliance, not only describe intended controls (Articles 5(2) and 24). This register reflects documents evidenced in the project materials reviewed for this lab; “not evidenced” means the materials do not establish that the document exists, not that no vendor may have one.

### Accountability evidence register

| Documentation a regulator may request | Status in this project | What exists / what is missing |
|---|---|---|
| Data inventory and data-flow map | **Partial — draft exists** | The updated data processing brief and Phase 1 inventory describe categories, purposes, recipients, storage and unknowns. They are not verified against every deployed configuration or vendor payload. |
| Records of processing activities (Article 30) | **Not evidenced** | No formal controller or processor RoPA is identified. Determine whether the Article 30(5) small-organisation exception applies; recurring or risky processing may still require a record. |
| Controller/processor role determination and responsibility allocation | **Partial — draft exists** | Phase 2 is a first-pass role map. Actual contracts, controller instructions and any Article 26 arrangement have not been confirmed. |
| Data Processing Agreements and subprocessor terms (Article 28) | **Not evidenced** | No client DPA or vendor DPAs are documented in the project materials. Collect and review the applicable agreements before any production personal data flows. |
| Lawful-basis decisions and Legitimate Interests Assessments | **Partial — preliminary analysis only** | Phase 3 includes candidate LIAs, but their necessity and balancing conclusions remain TBD; there is no approved LIA or final basis decision for each purpose. |
| Purpose-compatibility assessment (Article 6(4)) | **Not evidenced as a completed assessment** | Phase 1 flags possible reuse of web, supplier and policy information for AI reporting/testing, but no controller-approved compatibility analysis is documented. |
| Privacy information for data subjects (Articles 13/14) | **Not evidenced** | No notice covering directly collected or indirectly sourced data, recipients, retention, rights and lawful basis is identified. Assess Article 14 information for data obtained from public sources. |
| Retention and deletion schedule | **Not evidenced** | The inventory records that local files lack automatic expiry and provider periods are unknown; it does not set approved retention periods or prove deletion across copies and backups. |
| DPIA and prior screening (Article 35) | **Partial — screening exists; full DPIA not evidenced** | Phase 4 screens the nine criteria and leaves the production result TBD. Complete and approve a DPIA before deployment if the controller concludes processing is likely to result in high risk. |
| International-transfer assessment and mechanism | **Not evidenced** | Vendor locations and transfers remain unknown; no adequacy decision, SCCs, transfer assessment or other mechanism is documented. |
| Security measures and access-control evidence (Article 32) | **Partial / not verified** | The brief reports a redaction control and regression test, but account access, vendor controls, permissions, backups, encryption and security policies are not evidenced here. Test fixtures themselves still contain real public contact values. |
| Data-subject request procedure and request log | **Not evidenced** | No process is documented for finding, correcting, exporting or erasing data across local files, GitHub, Notion, email and vendors, or for handling objections. |
| Personal-data breach response plan and incident record (Articles 33/34) | **Not evidenced** | No procedure for triage, documenting incidents, notifying the supervisory authority within the applicable period, or informing affected people where required is identified. |
| Consent records | **Not applicable on the current assessment; no consent basis proposed** | If a future purpose relies on consent, document the information presented, affirmative choice, date, scope and withdrawal mechanism. |
| Vendor and data-transfer register | **Partial — names and gaps listed** | The brief names services, but contracting entities, account plans, locations, subprocessors, retention and transfer terms remain to be verified. |

### TBD data flow for legal review: public web/news details in AI-assisted reports

**Question for counsel:** May the controller use identifiable details in public search/news results to draft and substantiate procurement-risk reports, send selected text to an LLM, and retain quotes in run files, reports and downstream tools? The answer may differ between the author's current testing/publication and a future bakery deployment.

**Facts counsel would need:**

- Who is the controller for each stage, and who determines the report purpose and recipients?
- Which people can be identified (named individuals, sole traders, supplier contacts), what fields appear, and whether any Article 9 data could be included?
- Which sources are used, how the data was originally published/collected, what notices or expectations apply, and whether indirect-source transparency under Article 14 is required or an exception is available?
- Exactly what is removed before the LLM call, what may remain (including names), what the model/API and other vendors receive, and whether providers use or retain the payload for their own purposes?
- Where prompts, logs, reports and backups are processed/stored; retention periods; subprocessors; access; and any international-transfer safeguards.
- How the report is used in practice, whether a sole trader could be affected, how meaningful the human review is, and what access/objection/erasure route exists.
- What lawful basis is proposed, whether the original purpose is compatible, and whether a LIA or DPIA is needed.

**Preparation the project can provide without exposing additional personal data:**

1. A field-level flow diagram showing Tavily/GDELT results, local redaction, model prompts, logs, report/PDF, Notion, email, GitHub and OneDrive.
2. Synthetic examples of raw and sanitized search results, model payloads, stored traces and report passages; do not send real names or contact details in the legal-prep pack.
3. The redaction code, regression-test results, known misses (such as national-format phone numbers), and a record of the historical run/test-fixture exposure and remediation status.
4. The vendor/account list, applicable contract/DPA links, data-region and retention settings, subprocessor details, access permissions and transfer documents collected from each provider.
5. A short intended-use description covering report recipients, supplier recommendations, human review, expected production volume, and a proposed retention/deletion plan.

**Source:** [GDPR, Regulation (EU) 2016/679 on EUR-Lex (Articles 5(2), 24, 28, 30, 32–35 and 13–14)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/).

## Stretch: Data protection by design checklist

**Highest-risk candidate:** processing potentially identifiable people in web/news results through the LLM, reports, run files and public test fixtures. The brief does not confirm that every item is personal data, but names remain after contact-detail redaction and historical contact values remain in artifacts.

| Design principle | Current state of your system | Pass / Fail / Unknown |
|---|---|---|
| Data minimisation | Emails and some phone numbers are stripped before prompts and saved outputs, but names remain, a national-format phone may pass, and real contact values remain in historical/test artifacts. | **Fail** — remove or pseudonymise names and other identifiers unless necessary; close redaction gaps and replace real test values. |
| Purpose binding | Data moves from public search results into AI-assisted claims, stored reports and regression tests; the brief does not show technical purpose restrictions or approved compatibility assessments. | **Fail** — define permitted uses, separate test data from live data, and prevent personal data from entering prompts/reports/tests unless specifically approved. |
| Access controls | Run files sync to OneDrive and tests are in a public GitHub repository; permissions for Notion, n8n and vendor access are not confirmed. | **Fail** — remove real contact values from public artifacts/history where feasible, restrict repositories and report destinations, and document least-privilege access. |
| Retention enforcement | No automatic deletion or anonymisation is described; provider retention is unknown and deleted GitHub files may remain in history. | **Fail** — set retention periods and automated deletion/anonymisation across local files and vendor copies; verify backup and history deletion behavior. |
| Subject rights workflow | No end-to-end process is documented for finding or erasing personal data across prompts, reports, GitHub, Notion, email and vendors. | **Fail** — implement an intake, identity-check, search, correction/erasure, processor-instruction and response-record process that meets the applicable one-month response period. |
| Incident response | No documented detection, escalation, breach log or notification procedure is identified. | **Fail** — document triage and escalation, preserve evidence, assess risk, and enable the controller to meet the applicable 72-hour supervisory-authority notification deadline when required. |

