# W7D3_LAB_GDPR_Audit your own project
- Week 7 / Day 3
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-08-19
---

## Data Processing Brief

The Proactive Incident Agent is an AI-assisted decision-support system for cruise-company incident, claims, legal, risk, and compliance teams. It is designed to help human reviewers turn messy incident material into a clearer case file. The system does not make final claims decisions, approve or reject claims, decide legal liability, or replace a claims officer. It supports triage, completeness checking, classification, follow-up preparation, and weekly risk reporting.

The system processes personal data because cruise incident and doctor reports can identify real passengers, staff members, witnesses, or other people involved in an incident. The personal data may include passenger names, staff or witness names, cabin or location details, incident date and time, descriptions of what happened, injury details, medical observations, doctor-report content, evidence notes, follow-up questions, and case status. It may also create inferred information, such as severity level, claim-risk level, customer-impact level, missing-information status, high-risk flags, and short explanations for why a case was classified in a certain way. Injury and doctor-report information may be special-category data under GDPR Article 9 because it can reveal health information. For the MVP, the project used pseudonymised sample data rather than real production passenger records.

At production level, the data would mainly come from incident investigation reports and optional doctor reports uploaded into the system interface as PDF or text-based files. In a future production version, the data could also come from existing cruise-company systems, passenger statements, witness statements, vessel investigation notes, reception logs, gangway records, police reports, agent reports, photos, videos, or other operational records. This means some data would be submitted directly by staff, while other data may already exist in company databases or be collected from third parties involved in the incident.

The data is used for several separate purposes. First, the system extracts structured fields from unstructured reports so that a reviewer can see the key facts more clearly. Second, it checks whether required information is missing and generates follow-up questions where needed. Third, if the case is complete enough, it classifies severity, claim risk, and customer impact as Low, Medium, High, or Critical where relevant. Fourth, it flags higher-risk or incomplete cases for human attention. Fifth, it stores audit information about processing steps and LLM calls for traceability, review, and cost control. Sixth, it can generate weekly risk reports showing open cases, incomplete cases, classified incidents, and higher-risk matters for management review.

Several parties or systems process the data. The local Python application, including Streamlit, LangGraph, LangChain, Pydantic, pypdf, and Pandas, processes uploaded reports and structured case information. Airtable, or a future industrial-scale database, stores case records, missing fields, classifications, explanations, and audit logs. The OpenAI API or another LLM API provider may process selected case details when the system classifies complete cases or generates explanations and follow-up questions. Notion may process weekly report content if the weekly risk report is published there. The MVP was built as an individual bootcamp project. In production, the cruise company would likely decide the purpose of the processing and use the output through its claims, legal, risk, compliance, guest services, or vessel operations teams.

The exact storage and processing locations are not fully confirmed and should be marked for legal and technical review before production use. The MVP ran in a development/demo environment and stored structured records in Airtable, with possible weekly reporting to Notion and LLM processing through OpenAI. Because these vendors may process data outside the EEA or use international infrastructure, cross-border transfer checks would be required. In production, the client would need to confirm data hosting regions, vendor Data Processing Agreements, transfer mechanisms such as Standard Contractual Clauses, retention periods, access controls, and whether any personal or health data is sent to the LLM provider.

The system assists decisions that may affect people, but it is designed to keep a human in the loop. It can score or classify incidents by severity, claim risk, and customer impact; recommend follow-up questions; and flag high-risk or incomplete cases. These outputs could influence how quickly a case is escalated, how a claim is reviewed, or what further evidence is requested. However, the MVP does not automatically approve, reject, settle, or deny claims. A human claims officer or reviewer must check the extracted fields, missing-information list, classification, risk flag, explanation, and suggested follow-up questions before any real action is taken. The AI is therefore decision support, not the final decision-maker.

---

## Phase 1: Personal data inventory

For each category of personal data identified in the data processing brief, complete the table below.

| Data category | Source | Purpose(s) | Retention period (known/estimated) | Crosses EU border? |
| --- | --- | --- | --- | --- |
| Passenger identity data, such as passenger name and possibly cabin or booking-related identifiers | Incident investigation reports, doctor reports, and future cruise-company systems | Identify the incident case, connect reports to the correct passenger, support claims review, and allow human follow-up | Unknown for MVP. In production, should follow the cruise company’s claims/legal retention schedule and be deleted or anonymised when no longer needed | Yes / likely. The MVP used Airtable, OpenAI, and possibly Notion, so EEA-to-non-EEA processing or international infrastructure must be checked |
| Staff, witness, or vessel investigation officer information | Incident reports, witness statements, vessel investigation notes, reception logs, and operational records | Understand who reported, witnessed, handled, or investigated the incident; support evidence review and follow-up questions | Unknown for MVP. In production, should follow internal investigation and claims retention rules | Yes / likely. Vendor hosting and transfer mechanisms must be confirmed |
| Incident facts and narrative descriptions about people | Incident investigation reports, passenger statements, witness statements, police reports, agent reports, and operational records | Extract structured case facts, summarise what happened, support severity and claim-risk classification, and prepare weekly risk reporting | Unknown for MVP. In production, should be limited to what is necessary for claims, legal, and risk purposes | Yes / likely. Data may be processed by cloud database, LLM API, and reporting tools |
| Injury and medical information, including doctor-report content | Optional doctor reports, medical notes, injury descriptions in incident reports, and possibly future medical or first-aid records | Assess injury context, classify severity, identify high-risk cases, and support human claims/legal review | Unknown for MVP. In production, should have stricter retention controls because this may be special-category health data under GDPR Article 9 | Yes / likely. This is the most sensitive transfer risk if any health data is sent to an LLM or stored in non-EEA infrastructure |
| Inferred risk and classification outputs, such as severity, claim risk, customer impact, completeness status, and high-risk flags | Generated by the system from incident and doctor-report inputs | Triage cases, prioritise human review, identify incomplete files, support escalation decisions, and create weekly management reporting | Unknown for MVP. In production, should be retained only as long as needed for claims handling, audit, and legal accountability | Yes / likely. Outputs may be stored in Airtable/future database, sent to Notion, or processed by the LLM provider |
| Follow-up questions and explanation text generated by the system | Generated by the local application and/or LLM provider from case details | Help the reviewer request missing information, explain classifications, and support traceability of human review | Unknown for MVP. In production, should be linked to the case retention schedule and reviewed for accuracy | Yes / likely. If generated using an LLM API, selected case details may cross borders |
| Audit logs and LLM call logs, including prompts, selected case details, responses, and token usage | Created by the application during processing and stored in Airtable or a future audit database | Support traceability, review, debugging, accountability, and cost control | Unknown for MVP. In production, should have a defined retention period and avoid storing unnecessary personal or health data in logs | Yes / likely. Logs may contain personal data and may be stored or processed by cloud vendors |

### Purpose change check

Some data may have been originally collected for incident reporting, medical treatment, vessel safety, or claims handling. Using the same data for AI-assisted classification, weekly risk reporting, management dashboards, or model-related audit logs may be a new or expanded purpose. This does not automatically mean it is unlawful, but it must be checked against GDPR purpose limitation, transparency notices, lawful basis, data minimisation, and any original privacy notice given to passengers or staff. The same data might also be further used to train the AI model or build a new predictive model using statistics, econometrics, and actuarial techniques.

**Notes:**

- The highest-risk data category is injury and medical information because it may reveal health data, which is special-category data under GDPR Article 9.
- The MVP used pseudonymised sample data, but a production version would process real passenger, staff, witness, and medical data. This will need to be properly anonymised before being transmitted to the LLM. Storage in the database is necessary for escalation.
- Retention periods are currently unknown and should be marked for legal and technical review by personal injury lawyers with expertise in passenger shipping and maritime law in general, as well as by insurance advisors with maritime insurance expertise.
- Cross-border transfers are likely, or at least possible, because Airtable, OpenAI, and Notion may use international cloud infrastructure. Before production use, confirm the hosting region, Data Processing Agreements, and transfer mechanism. This should be reviewed in the final production model, including whether storage is local or cloud-based and whether reporting uses Notion, email, or another tool with local or cloud hosting.

---

## Phase 2: Role map

Identify every entity that processes personal data in the system and classify its role.

| Entity | Role (controller / processor / joint controller) | Processing activity | DPA in place? |
| --- | --- | --- | --- |
| Cruise company / client using the system in production | Controller | Decides why and how passenger incident, claims, medical, and follow-up data are used. Uses the system for claims triage, legal/risk review, escalation, and weekly reporting. | N/A as controller, but the client must have DPAs with all processors that handle personal data on its behalf. |
| You / your team / consultant building or operating the MVP | Processor, if building or operating the system for the client; | Builds, configures, tests, and may support the system. May access uploaded reports, structured case records, logs, prompts, outputs, and reporting flows during development or support. | Required if handling real client personal data.  |
| OpenAI API or other LLM API provider | Processor or sub-processor, depending on the contract and deployment setup | Processes selected case details, prompts, classification tasks, generated explanations, and follow-up questions when the LLM is called. | Required before any real personal data, especially health data, is sent to the provider. Contract terms, data-use settings, retention, and training opt-out must be confirmed. |
| Airtable or future production database provider | Processor | Stores structured case records, missing fields, classifications, explanations, audit logs, and possibly LLM call logs. | Required before production use with real personal data. Hosting region, access controls, retention, and transfer mechanism must be confirmed. |
| Notion, email, or reporting tool provider, if used for weekly reports | Processor | Stores or distributes weekly risk reports, summaries, high-risk case lists, and management reporting outputs. | Required if reports contain personal data or identifiable case details. If possible, reports should be minimised or anonymised. |

### International transfer check

For any international transfer, note which transfer mechanism applies: adequacy decision, Standard Contractual Clauses (SCCs), or other.

**Notes:**

- The exact transfer position is currently **TBD — legal and technical review**.
- Airtable, OpenAI, Notion, email tools, and cloud hosting may involve processing outside the EEA or access from outside the EEA.
- Before production use, the client should confirm each vendor’s hosting region, DPA, sub-processors, transfer mechanism, security controls, retention settings, and whether data is used for model training.
- If data leaves the EEA and there is no adequacy decision, the likely mechanism would be **Standard Contractual Clauses (SCCs)** plus a transfer-risk assessment.
- Health or injury data should be treated as especially sensitive. Ideally, it should be minimised, pseudonymised, or removed before being sent to any LLM or external reporting tool.

---

## Phase 3: Lawful basis assessment

For each processing purpose, select a lawful basis and justify it.

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
| --- | --- | --- | --- |
| Ingest and structure incident investigation reports and optional doctor reports | Legitimate interests | The client has a legitimate business need to organise incident material for claims handling, safety review, legal risk management, and operational follow-up. | Yes — legal review recommended, especially where medical data is included |
| Identify the correct case and connect reports to the right passenger or incident | Contract / legitimate interests | Processing may be necessary to manage passenger-service obligations and possible claims. | Yes — confirm with legal counsel |
| Check whether required incident information is missing | Legitimate interests | The client needs complete and accurate case files before making claims, legal, risk. | Yes — confirm that the missing-field checks are proportionate and limited to necessary data |
| Generate follow-up questions for vessel staff, investigation officers, claims teams, or other reviewers | Legitimate interests | Follow-up questions help the client collect missing information while evidence is still available and support fair human review. | Yes — especially if questions include or reveal health data |
| Classify severity, claim risk, and customer impact for complete cases | Legitimate interests | The client has a legitimate interest in prioritising incidents, but classifications may influence people and therefore need human review and safeguards. | Yes — legal review recommended because this involves evaluation/scoring |
| Flag high-risk or incomplete cases for human attention | Legitimate interests | Flagging helps the client escalate potentially serious matters to claims, legal, risk, or compliance teams. | Yes — confirm this does not become automated decision-making without meaningful human review |
| Store structured case records, classifications, explanations, and audit logs | Legitimate interests / legal obligation | Storage supports accountability, auditability, claims handling, legal defence, and regulatory or litigation record-keeping. | Yes — retention period and legal basis should be confirmed |
| Generate weekly risk reports for management review | Legitimate interests | Aggregated or minimised reporting helps the client monitor operational risk and recurring incident patterns. | Yes — reports should be minimised or pseudonymised where possible |
| Process injury or medical information from doctor reports | TBD — legal review; likely Article 6 legitimate interests plus a separate Article 9 condition | Health data is special-category data, so Article 6 alone is not enough; the client must identify an Article 9 condition before production use. | Yes — mandatory legal review |
| Use incident data to train or improve an AI model or build a future predictive model | TBD — legal review | This may be a new purpose beyond the original incident/claims purpose and may require a compatibility assessment, updated transparency notice, minimisation, anonymisation, or a different lawful basis. | Yes — mandatory legal review |

### Legitimate Interests Assessment, if applicable

If using legitimate interests, complete the three-part test.

#### 1. Is the interest legitimate?

What is the concrete business need?

**Answer:** The interest is likely legitimate because the cruise company has a real business and legal need to review passenger incidents, manage possible claims, identify incomplete evidence, escalate serious matters, and monitor operational risk. The system supports existing claims, legal, safety, and compliance work rather than creating an unrelated commercial purpose. However, using the data for model training or future predictive analytics may be a separate purpose and should be marked **TBD — legal review**.

#### 2. Is the processing necessary?

Is there a less intrusive way to achieve the same goal?

**Answer:** The processing may be necessary if the system only uses the information needed to structure the case, check missing fields, classify risk for human review, and create audit records. A less intrusive approach would be to minimise the data before LLM processing, remove or mask names where possible, avoid sending full doctor reports to external tools, and use aggregated or anonymise data in weekly reports. The system should not process more medical or identity data than needed for the specific claims and risk-review purpose.

#### 3. Does the individual's interest override?

Does the privacy impact outweigh the benefit?

**Answer:** The individual's interests could override the business interest if the system uses real medical data without strong safeguards, sends identifiable health information to external vendors, produces risk scores that strongly influence claim outcomes, or uses incident data later for AI training without clear notice. The balance is stronger if the system remains human-reviewed, uses pseudonymisation or anonymisation where possible, limits access, keeps logs, has clear retention rules, and does not make automated final decisions. Because passengers may be affected by claim triage or escalation, this balancing test should be reviewed by legal counsel before production use.

**Legal review flag:** - **TBD — legal review required**, especially for health data, automated classification/scoring, cross-border transfers, retention periods, and any future model training or predictive analytics.

---

## Phase 4: Risk and rights analysis

### Special category data, Article 9

Yes. Injury details, doctor-report content, medical observations, treatment notes, and severity descriptions may reveal health data, which is special-category data under GDPR Article 9. The exact Article 9 condition is **TBD — legal review**, but possible candidates may include processing needed for legal claims or another condition confirmed by counsel. Before production use, the client should identify the correct Article 9 condition, minimise health data sent to external vendors, and avoid sending full identifiable doctor reports to an LLM unless this is legally approved and technically protected.

### Automated decision-making, Article 22

The system will not make automated decisions with legal or similarly significant effects by itself. It classifies severity, claim risk, and customer impact, and it can flag high-risk or incomplete cases, but it does not automatically approve, reject, settle, or deny a claim. A human claims officer or reviewer must check the extracted fields, missing-information list, classification, risk flag, explanation, and suggested follow-up questions before any real action is taken. The human reviews  remain on the loop and has oversight. 

To reduce this risk, the system should include safeguards: mandatory human review before action, clear explanations of classifications, audit logs, the ability for a person to challenge or correct an output, and documented instructions that the AI is decision support only.

### DPIA trigger

Several DPIA trigger criteria may apply to a production version of this system. The strongest trigger is **evaluation or scoring of people**, because the system classifies severity, claim risk, customer impact, completeness status, and high-risk flags linked to passenger incidents. **Special category data** may also apply because doctor reports and injury descriptions can contain health data. **Innovative technology** apply because the system uses an LLM-based workflow to assist claims triage and risk review.

Other criteria are possible but need legal and technical review. **Large-scale processing** will apply when the system is used across many vessels, passengers, incidents, or claims over time. **Matching or combining datasets** could apply if incident reports are combined with doctor reports, passenger records, witness statements, police reports, insurance data, or operational logs. **Automated decision-making with significant effects** does not appear to apply because human review remains required.

Because at least two criteria are likely or possible, especially evaluation/scoring plus health data, a **DPIA should be treated as required before production deployment**. The DPIA should review data minimisation, human oversight, LLM/vendor processing, cross-border transfers, retention, access controls, audit logs, and whether outputs could unfairly affect passengers.

### Data subject rights friction

The main rights friction points are the **right of access**, the **right to erasure**, the **right to rectification**, and the **right to object to profiling or risk classification**. A passenger may ask what personal data was processed, what the AI produced about the incident, what prompts or logs were created, and who received the weekly report. The current MVP has useful audit logs, but production use would need a clear subject-rights workflow so the client can find all relevant data across the database, LLM logs, reports, and any exported records within the GDPR response deadline.

---

## Phase 5: Law stacking check

### AI Act cross-check

The system is treated as a **limited-risk / transparency decision-support system.**

### ePrivacy check

The system does not use cookies, tracking pixels, device-level data collection, or electronic-communications monitoring, so ePrivacy is likely **not a major issue for the current version**. 

### Data Act check

The Data Act is likely **not applicable to the current MVP**, because the system does not involve connected product data, IoT device data, smart-ship sensor data, or cloud-switching services.

---

## Phase 6: Compliance memo

### Draft memo

**To:** Data Protection Officer / Legal Counsel
**Subject:** First-pass GDPR compliance assessment for Proactive Incident Agent

**Bottom line:** Proceed with conditions. The Proactive Incident Agent can be developed as a human-reviewed decision-support tool, but it should not be used with real passenger or medical data until GDPR controls, vendor checks, and a DPIA are completed.

The system processes cruise incident reports and optional doctor reports to extract structured case information, identify missing fields, classify severity, claim risk and customer impact, flag higher-risk cases, and support weekly risk reporting. This creates GDPR exposure because the system may process passenger identity data, staff or witness information, incident narratives, inferred risk classifications, audit logs, and health-related information from injury descriptions or doctor reports. Health data is special-category data under GDPR Article 9, so the client must identify both a lawful Article 6 basis and a separate Article 9 condition before production use.

The top three actions are: **(1)** complete a DPIA before deployment, because the system likely involves evaluation/scoring, health data, innovative AI-assisted processing, and possible dataset combination; **(2)** confirm all vendor arrangements before any real personal data flows, including DPAs, hosting regions, sub-processors, transfer mechanisms, retention settings, security controls, and whether data is used for model training; and **(3)** implement privacy-by-design controls, including data minimisation, pseudonymisation or anonymisation before LLM use, strict access controls, clear retention rules, audit logs, and mandatory human review before any claim, legal, escalation, or compensation action.

Residual risks remain even if these actions are completed. First, AI classifications may still be inaccurate or unfairly influence human reviewers. Second, medical and incident data may be difficult to fully remove from logs, reports, backups, or exported records. Third, cross-border vendor processing may create continuing transfer and security risks.

This memo is a first-pass compliance assessment for bootcamp learning purposes. It is not a legal opinion, DPIA, conformity assessment, certification, or final regulatory determination. The client should engage qualified legal counsel before relying on this assessment for production compliance decisions.