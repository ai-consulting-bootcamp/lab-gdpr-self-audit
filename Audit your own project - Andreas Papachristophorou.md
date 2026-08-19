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

