# GDPR Audit Pack — TestVet

**Author:** Parisa Dehghani  
**Project:** TestVet — Project 3  
**Audit type:** First-pass GDPR assessment of the student-built prototype  
**Repository reviewed:** https://github.com/Parisa-QA/Project-3  
**Review basis:** Public `master` branch and project documentation/code available on 24 August 2026

## 1. Data-processing brief

TestVet is a Python/LangGraph prototype that evaluates QA testing tools, frameworks, and testing APIs. A user enters a tool name, written QA requirements/context, and optionally a public GitHub repository URL or `owner/repository` slug. TestVet then retrieves GitHub repository and release metadata, searches News API when a key is configured, searches Hacker News through Algolia, loads a local QA evaluation guideline, and produces a structured recommendation such as **Adopt**, **Pilot**, **Reject**, or **More evidence needed**.

The direct input can contain personal data if a user includes a name, email address, employer, colleague reference, or other identifying information in the free-text context. GitHub, news, and Hacker News responses can also contain public usernames, author names, profile links, and text about identifiable people. The code does not intentionally request special-category data, and no LLM API or model-training workflow is visible in the repository. The synthesis currently appears rule-based and keyword-based rather than an LLM decision.

Data originates from the TestVet user, public GitHub APIs, News API, and Hacker News Algolia search. The purposes are: (1) receive and interpret the QA evaluation request; (2) retrieve supporting public evidence; (3) compare evidence with the local QA rubric; and (4) generate a recommendation report. The project code does not show a database, authentication system, analytics service, or automatic deletion process. Storage after a run, hosting location, application logs, and retention are therefore **Unknown — confirm before deployment**. The report is returned to the user interface and sample reports are written locally by the sample-generation script.

TestVet assists an organisational tool-selection decision. It does not appear to score, rank, recommend, or reject natural persons, and no meaningful legal or similarly significant effect on an individual is evident from the repository.

## 2. Recognize: data categories and cross-border flow

- **Direct input:** tool name, QA requirements, and optional repository URL. The free-text field may accidentally contain names, emails, employer information, or other personal data.
- **Public-source metadata:** repository owner/name, description, release data, article titles and descriptions, Hacker News author/title/engagement metadata, and source URLs.
- **Derived data:** criterion scores, risks, confidence, missing evidence, and an organisational recommendation about a software tool.
- **Special-category data:** not intentionally collected. It could appear incidentally in free text or public source content and must be filtered or excluded.
- **Cross-border possibility:** likely. GitHub, News API, and Algolia may process request data or source data outside the EEA. Exact locations and transfer mechanisms are not documented in the repository.

## 3. Phase 1 — Personal-data inventory

| Data category | Source | Purpose(s) | Retention period | Crosses EU border? | Purpose compatibility / gap |
|---|---|---|---|---|---|
| Tool name and QA context | TestVet user | Receive and evaluate the requested QA tool | In memory during run; afterward unknown | Unknown | Compatible with the requested evaluation. Free-text minimisation is missing. |
| Optional GitHub URL or slug | TestVet user | Resolve the public repository | In memory during run; afterward unknown | Likely possible through GitHub API | Compatible if limited to public repositories; do not accept private URLs without a separate assessment. |
| GitHub repository and release metadata | GitHub REST API | Evidence for technical fit, health, security, and maintainability | In memory during run; report retention unknown | Likely possible | Public-source reuse is likely compatible, but source notice and provider terms should be checked. |
| News article metadata | News API, if configured | Supporting evidence about tools and vendors | In memory during run; report/log retention unknown | Unknown; provider location not documented | Use only for the stated evaluation purpose; do not retain full article content unnecessarily. |
| Hacker News author and post metadata | Algolia Hacker News API | Supporting community evidence | In memory during run; report retention unknown | Unknown | Limit output to necessary evidence and avoid unnecessary author profiling. |
| Scores, confidence, risks, and recommendation | TestVet-generated | Explain the tool-selection recommendation | Report retention unknown | Depends on hosting and storage | This is organisational decision support, not a decision about an individual. |

No incompatible secondary purpose or model-training use is visible in the code. However, using free-text inputs or retrieved source data for future analytics, profiling, or model training would be a new purpose and requires a separate compatibility and lawful-basis review.

## 4. Phase 2 — Role map

| Entity | Likely role | Processing activity | DPA status / action |
|---|---|---|---|
| TestVet operator or future business | Controller for TestVet service | Defines purposes, receives inputs, runs workflow, and presents reports | No DPA evidence in repository; publish privacy information and document role. |
| TestVet developer/team | Processor only if acting on another organisation's instructions; otherwise part of controller | Maintains code and may access development data | Define role contractually; do not use real personal data in development without controls. |
| GitHub | Independent controller for its platform; possible processor question for a contracted API use | Supplies public repository/release data and processes API requests | No DPA evidence. Check GitHub terms, privacy information, hosting, and transfer details. |
| News API | Likely independent service provider or processor depending arrangement | Searches and returns article metadata | DPA and international-transfer terms are **TBD — legal review**. |
| Algolia/Hacker News search service | Likely independent service provider or processor depending arrangement | Searches public Hacker News content | DPA and transfer mechanism are **TBD — legal review**. |
| Hosting provider, if deployed | Likely processor | Hosts Gradio app, logs, and generated reports | Provider, region, DPA, SCCs/adequacy, and retention are unknown. |

For any customer deployment where TestVet processes a customer's inputs, the customer may be the controller and TestVet the processor. The exact arrangement depends on who determines the purposes and means. No DPA, SCC, adequacy decision, or processor register is present in the repository.

## 5. Phase 3 — Lawful-basis assessment

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| Receive and process a user's requested evaluation | Contract, if TestVet is offered as a service; otherwise consent for a voluntary prototype | Processing is needed to provide the evaluation the user requested. | Yes — confirm service terms and whether any personal data is necessary. |
| Retrieve public GitHub evidence | Legitimate interests | **LIA:** legitimate interest is evidence-based QA tool evaluation; retrieval is necessary because manual research is the service purpose; the impact should be low when limited to public repository data, but data-subject interests may override if unnecessary profiling or retention occurs. | Yes — document the LIA and source-data limits. |
| Retrieve News API and Hacker News evidence | Legitimate interests | **LIA:** the business interest is researching software-tool suitability; API retrieval is a targeted way to obtain evidence; the balance is more favourable when only relevant public content is used and authors are not profiled. | Yes — provider role and transfer terms are unknown. |
| Generate and display a recommendation report | Contract, where the user requested the report | The report is the requested service output. | Yes — confirm whether the report is stored or shared. |
| Product analytics, persistent logs, or future model training | None selected | These purposes are not documented in the code and must not be assumed to be covered by the evaluation purpose. | **TBD — legal review before enabling.** |

The LIA conclusions above are preliminary. If TestVet is used only by the developer locally and no personal data is entered, the practical processing risk is lower; that does not justify collecting unnecessary personal data in a future deployment.

## 6. Phase 4 — Risk and rights analysis

### Special-category data — Article 9

TestVet does not intentionally collect health, biometric, political, religious, sexual-orientation, ethnic-origin, or trade-union data. The free-text context and retrieved public content could nevertheless contain such information incidentally. The design should minimise free text, avoid storing unnecessary source text, filter sensitive categories where practicable, and treat any actual Article 9 processing as **TBD — legal review** because no Article 9 condition is currently documented.

### Automated decision-making — Article 22

The system generates a recommendation about QA software, not about a natural person. The repository shows no recruitment, credit, employment, benefits, or other individual-impact decision. Article 22 therefore appears unlikely to apply to the current use case. A human user should still review the evidence and recommendation before making a procurement or operational decision; the project should not describe the output as an objective or final decision.

### DPIA trigger

The strongest possible EDPB criteria are innovative technology and matching/combining data from GitHub, news, Hacker News, user context, and a local rubric. Cross-border transfer may also apply. Criteria such as evaluation of people, significant automated decisions, systematic monitoring, large-scale special-category processing, and vulnerable-person processing are not evidenced. A documented DPIA screening is required before deployment; a full DPIA is **TBD — legal review**, especially if the service becomes public, processes customer data at scale, or adds profiling, analytics, or model training.

### Data-subject rights friction

Access and erasure requests would be difficult because the repository has no user identity, account, retention, or deletion workflow. The team may not be able to identify where a person's name appears in free-text inputs, API responses, logs, or saved reports. The right to object may also be relevant if public-source data is used for profiling or persistent analytics. A deployed service needs an intake route, searchable records, retention limits, deletion capability, and a documented response process; the current prototype does not demonstrate these controls.

## 7. Phase 5 — Law-stacking check

- **AI Act:** TestVet does not appear to be a high-risk system because it evaluates software tools rather than people. It may still be an AI-enabled software product depending on the final implementation; keep human review, output transparency, and provider documentation under review.
- **ePrivacy:** No cookies, tracking pixels, device-level tracking, or analytics code is visible in the repository. Gradio or a future host may still set necessary or optional cookies; inspect the deployed configuration and obtain consent where non-essential tracking is used.
- **Data Act:** **N/A on current evidence.** TestVet does not process connected-product or IoT data and does not implement cloud switching. Reassess if those features are added.

## 8. Accountability check

| Evidence a regulator could request | Current status |
|---|---|
| Data-processing brief and data map | Created for this audit; not visible in the project repository. |
| Records of processing activities | Missing. |
| Privacy notice and user-facing data warning | Missing from repository. |
| Retention and deletion schedule | Missing / unknown. |
| DPAs and vendor list | Missing. |
| Transfer assessment, SCCs, or adequacy basis | Missing / unknown. |
| LIA for public-source retrieval | Missing. |
| DPIA screening and, if needed, full DPIA | Missing. |
| Access, erasure, and objection workflow | Missing. |
| Incident response and 72-hour assessment process | Missing. |

## 9. Client recommendation memo

**To:** TestVet project owner and future Data Protection Officer or legal counsel  
**From:** Parisa Dehghani  
**Subject:** First-pass GDPR recommendation for TestVet

### Bottom line: proceed with conditions

TestVet can continue as a local educational prototype because the reviewed code does not intentionally collect sensitive personal data, does not use an LLM API, and does not make decisions about individuals. It should not be opened to external users or real company data until the data flows, vendors, hosting location, retention, and rights workflow are documented. The main risk is not the current scoring logic; it is uncontrolled free-text input, public-source retrieval, and unknown logging or cross-border processing.

### Top three actions

1. **Minimise and control inputs before deployment.** Add a warning not to enter personal or confidential information, validate inputs, restrict repository retrieval to public targets, avoid retaining unnecessary article or author data, and document the exact report fields stored or displayed.
2. **Complete the accountability package.** Identify the host and API providers, confirm their regions and transfer mechanisms, establish DPAs where TestVet acts as a processor, write a privacy notice, record a retention/deletion schedule, and complete an LIA for public-source retrieval plus DPIA screening.
3. **Build rights and governance controls.** Provide an access/erasure/objection contact, define logging and deletion, record incidents, keep a vendor register, and require human review of recommendations. Do not enable analytics, profiling, or model training on submitted or retrieved data without a new purpose and lawful-basis assessment.

### Residual risks

Even after these actions, public sources may contain unexpected sensitive information, providers may change their processing or hosting, and free-text users may bypass warnings. The recommendation can also be over-trusted by a QA lead even when evidence is incomplete. This memo is a first-pass educational assessment, not a legal opinion, DPIA, certification, or guarantee of compliance; legal counsel should validate the final deployment design.

## 10. Data-protection-by-design checklist

| Design principle | Current state | Pass / Fail / Unknown | Required change |
|---|---|---|---|
| Data minimisation | Free-text context accepts unspecified content; public-source fields are broader than strictly necessary | Fail | Restrict input fields, warn against personal data, and return only necessary evidence. |
| Purpose binding | Evaluation purpose is documented; analytics/training purposes are not | Unknown | Prohibit secondary use until separately documented and assessed. |
| Access controls | No authentication or access-control design is documented | Unknown | Define users, permissions, secrets handling, and report access before deployment. |
| Retention enforcement | No deletion or retention mechanism is visible | Fail | Set retention periods and implement deletion/anonymisation. |
| Subject-rights workflow | No access, erasure, or objection process is visible | Fail | Add a contact and searchable deletion/response workflow. |
| Incident response | No breach process is documented | Unknown | Add detection, escalation, records, and 72-hour assessment steps. |

## Sources and evidence

- TestVet repository: https://github.com/Parisa-QA/Project-3
- GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- EDPB automated decision-making and profiling guidance: https://www.edpb.europa.eu/documents/guideline/automated-decision-making-and-profiling_en
- EDPB DPIA guidance: https://www.edpb.europa.eu/documents/guideline/data-protection-impact-assessments-high-risk-processing_en
- EU AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- ePrivacy Directive: https://eur-lex.europa.eu/eli/dir/2002/58/oj/eng
- Data Act: https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng
