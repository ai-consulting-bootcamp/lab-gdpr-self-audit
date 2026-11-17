# GDPR Audit — Data Processing Brief

**System:** Career Intelligence Agent  
**Industry:** HR Technology / Career Development  
**Development status:** Functional MVP using synthetic candidate profiles  
**Intended use:** Personal career guidance for individual jobseekers

## 1. Personal Data Processed

The Career Intelligence Agent processes information about a candidate's professional background and career preferences.

This may include a name or display name, professional experience, employment history, education, qualifications, skills, preferred occupations, career level, location preferences and preferred working arrangements.

The system also generates personal assessments, including job-matching scores, recommended opportunities, potential qualification gaps and positions requiring further review. These inferred results may also constitute personal data when linked to an identifiable individual.

The current MVP has been demonstrated with synthetic profiles. However, the same information would be personal data when submitted by real users.

The application does not intentionally request special-category data, such as health information, religious beliefs or ethnic origin. Nevertheless, users could potentially include sensitive information in free-text profile fields.

## 2. Data Sources

Candidate information is entered directly by the user through the Streamlit interface. Users can review and correct the profile before initiating the analysis.

Additional information comes from external sources:

- Arbeitnow and Himalayas provide current job advertisements.
- ESCO provides occupational and skills classifications.
- Tavily supports company research.
- Selected publications provide labour-market information retrieved through Pinecone.

These external sources are used to enrich the analysis rather than to obtain private candidate records.

## 3. Processing Purposes

The system processes candidate information for three main purposes:

1. **Job discovery:** Identify vacancies relevant to the user's career interests and preferences.
2. **Matching and recommendation:** Compare the candidate's documented experience and qualifications with job requirements and produce explainable matching scores.
3. **Career intelligence and reporting:** Provide contextual labour-market insights and generate downloadable reports.

The application does not automatically submit job applications or make hiring decisions on behalf of employers.

## 4. Processing Entities

The application uses Python, LangGraph and Streamlit to process profile information, retrieve vacancies and calculate matching scores.

External services are used for specific functions. OpenAI may process candidate-related context and retrieved evidence when optional AI-generated career intelligence is enabled. Pinecone retrieves relevant passages from the labour-market knowledge base.

Tavily and ESCO receive research-related queries. Their exact exposure to personal information, if any, requires verification against the implemented API requests.

## 5. Storage and International Transfers

The MVP runs locally and can generate Markdown, JSON and PDF reports. Candidate information is also handled during the active Streamlit session.

The project does not yet establish a formal retention and deletion policy for real user information.

The hosting regions, processing locations and applicable international transfer safeguards of external services have not been fully verified. Consequently, transfers outside the European Economic Area cannot currently be ruled out.

These points require further investigation before production deployment.

## 6. Automated Assessment and Human Review

The system automatically evaluates and ranks job opportunities using weighted matching criteria and additional qualification checks.

Users review their profile before starting the workflow and can examine the completed recommendations, explanations and source references.

A high matching score does not automatically qualify a position as recommended. Jobs with important unresolved requirements may be flagged for review.

The user remains responsible for deciding whether to apply for a position. The system does not make legally binding employment decisions, and there is no employer-side automated candidate rejection.

**Preliminary conclusion:** The current synthetic-data MVP has limited personal data exposure. A production version processing real candidate information would fall within the GDPR's scope and require a documented privacy and data-processing framework.


## Phase 1: Personal Data Inventory

**Scope:** The current MVP uses synthetic candidate profiles. The assessment below considers how the system would process personal data when used by real jobseekers.

| Data category | Source | Purpose(s) | Retention period (known/estimated) | Crosses EU border? |
|---|---|---|---|---|
| Name, display name and candidate ID | User input | Identify the candidate within the application and associate results with the correct profile | Active session and potentially locally saved reports; no formal retention policy defined | No for local-only processing in the EU; future hosting location TBD |
| Professional experience, employment history and skills | User input | Evaluate suitability for job opportunities and calculate matching scores | Active session and potentially locally saved reports; no formal retention policy defined | Potentially, if candidate-related information is transmitted to OpenAI; processing region not verified |
| Professional experience, qualifications and skills | User input | Generate personalized career intelligence and explain recommendations | Active session and generated reports; external service retention TBD | Potentially yes, through optional OpenAI processing; transfer mechanism TBD |
| Education and professional qualifications | User input | Assess qualification alignment with job requirements | Active session and potentially locally saved reports; no formal retention policy defined | Potentially, depending on optional external AI processing |
| Preferred job roles and career interests | User input | Generate relevant job-search queries and retrieve vacancies | Active session and potentially locally saved reports; no formal retention policy defined | Potentially, through external job APIs; provider processing locations not verified |
| Location, seniority and working preferences | User input | Filter vacancies and assess preference alignment | Active session and potentially locally saved reports; no formal retention policy defined | Potentially, depending on information transmitted in API requests |
| Matching scores, recommendations and review flags | Generated by the matching algorithm | Support individual career decisions and explain suitability assessments | Active session and potentially locally saved reports; no formal retention policy defined | Potentially, if assessment results are included in optional OpenAI requests |
| Candidate profiles and generated report content | User input and system-generated output | Provide downloadable reports in PDF, Markdown and JSON | Saved locally when exported; deletion and retention policy not established | Not necessarily during local export; potentially through optional external AI processing |
| Free-text profile information, potentially including sensitive data | User input | Describe professional background and support matching and analysis | Active session and potentially locally saved reports; no formal retention policy defined | Potentially, depending on external processing; special-category data must be addressed separately |



## Phase 2: GDPR Role Map

**Scope:** The current MVP uses synthetic candidate profiles. The following role assessment considers a future commercial deployment processing real personal data. All unverified relationships require legal and contractual review.

| Entity | Role (controller / processor / joint controller) | Processing activity | DPA in place? |
|---|---|---|---|
| **My company (Career Intelligence Agent provider)** | **Controller** | Determines the purposes and essential means of processing candidate profiles, career preferences, matching scores, recommendations and generated reports. | N/A — Controller; DPAs required with applicable processors. |
| **Me / development team** | **Part of the controller organization** | Develops, operates, maintains and tests the application. May access personal data where necessary for support or troubleshooting. | N/A if acting within the same organization; separate contractual assessment if operating as an external service provider. |
| **OpenAI** | **Processor (provisional)** | Processes candidate-related information and retrieved evidence when optional AI-generated career intelligence is enabled. | TBD — Verify applicable DPA and international transfer safeguards before production use. |
| **Pinecone** | **Role depends on actual data processing** | Stores and retrieves labour-market research. Storage of identifiable candidate profiles is not part of the documented MVP design. | TBD — Determine whether personal data or personal-data-derived queries are transmitted and whether a DPA is required. |
| **Tavily** | **TBD — vendor review** | Processes company research queries and associated request metadata. Candidate profiles are not intentionally sent in full. | TBD — Assess personal data exposure, contractual role and applicable DPA requirements. |
| **ESCO** | **TBD — data flow review** | Provides standardized occupational and skills information through API queries. | TBD — Assess whether queries or technical metadata constitute personal data. |
| **Arbeitnow** | **TBD — data flow review** | Provides job advertisements in response to job-search requests. | TBD — Assess whether search terms or technical metadata contain personal data and determine the provider's role. |
| **Himalayas** | **TBD — data flow review** | Provides remote job advertisements in response to job-search requests. | TBD — Assess whether search terms or technical metadata contain personal data and determine the provider's role. |

### International Data Transfers

The exact processing regions of the external services have not been fully verified.

Where personal data is transferred outside the European Economic Area (EEA), the controller must identify an applicable GDPR Chapter V transfer mechanism, such as:

- An adequacy decision under Article 45;
- Standard Contractual Clauses (SCCs) under Article 46, with supplementary measures where necessary;
- Another legally valid transfer mechanism, where applicable.

**Current status:** TBD — Vendor and legal review required.

### Preliminary Conclusion

My company would act as the primary GDPR controller for the intended B2C service.

OpenAI is the most relevant prospective processor because optional AI-generated analysis may involve candidate-related information.

Other vendors must be assessed individually based on the personal data actually transmitted and their contractual processing roles.

No joint-controller relationship has currently been established.

Before processing real candidate data, applicable processor agreements under GDPR Article 28 and international transfer safeguards must be verified.


## Phase 3: Lawful Basis Assessment

**Scope:** Prospective commercial deployment of the Career Intelligence Agent with real candidate data. The current MVP uses synthetic profiles.

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| **1. Candidate profile collection and validation** | Article 6(1)(b) — Contract | Collecting relevant professional experience, skills, education and preferences is necessary to provide the personalized career-matching service requested by the user. | **Yes** — Confirm contractual necessity and data minimization. |
| **2. Job discovery and filtering** | Article 6(1)(b) — Contract | Processing career interests and search preferences is necessary to identify relevant vacancies through external job APIs. | **Yes** — Verify which personal data, if any, is transmitted to API providers. |
| **3. Job matching, scoring and recommendations** | Article 6(1)(b) — Contract | Comparing candidate qualifications with job requirements is an essential function of the requested career guidance service. | **Yes** — Review proportionality, profiling safeguards and transparency. |
| **4. Optional AI-generated career intelligence** | Article 6(1)(a) — Consent (provisional) | Users may voluntarily request additional AI-generated analysis involving candidate-related information processed through OpenAI. | **Yes** — Confirm the appropriate basis and implement valid, documented consent if consent is selected. |
| **5. Report generation and user-requested export** | Article 6(1)(b) — Contract | Generating and providing the requested PDF, Markdown or JSON report is part of delivering the service. | **Yes** — Define necessary storage, retention and deletion procedures. |
| **6. Service security and technical troubleshooting** | Article 6(1)(f) — Legitimate Interests (provisional) | Limited processing of technical logs or request metadata may be necessary to maintain service security and reliability. | **Yes** — Complete and document a Legitimate Interests Assessment (LIA). |
| **7. Handling GDPR rights requests** | Article 6(1)(c) — Legal Obligation | Processing information necessary to respond to access, correction or deletion requests supports compliance with legal obligations under the GDPR. | **No**, for the general basis; implementation details require review. |

### Legitimate Interests Assessment (LIA)

**Purpose:** Service security and technical troubleshooting.

**1. Purpose Test — Is the interest legitimate?**

Yes, provisionally. The company has a legitimate interest in protecting the application against unauthorized access, detecting technical failures and maintaining operational security.

**2. Necessity Test — Is the processing necessary?**

Potentially. Limited technical logs may be necessary to investigate incidents and maintain service reliability.

However, storing complete candidate profiles or full career reports in technical logs would generally be unnecessary. Data minimization, restricted access and short retention periods should be prioritized.

**3. Balancing Test — Do individual rights override the interest?**

The privacy impact could be limited if logs contain minimal information, are securely stored and are automatically deleted.

However, the current MVP does not have a documented production logging and retention policy. The balancing assessment cannot therefore be completed confidently.

**LIA conclusion:** TBD — legal review.

Article 6(1)(f) should not be treated as confirmed until the necessity and balancing tests are documented.

### Additional Legal Considerations

**Special-category data (Article 9):**

The system does not intentionally request sensitive personal data. However, users may include such information in free-text fields.

An Article 6 lawful basis alone is insufficient for processing special-category data. A separate Article 9 condition would also be required.

The preferred approach is to minimize or prevent unnecessary collection of such information.

**Third-party processing:**

Sending personal data to OpenAI or another external processor does not automatically create a separate lawful basis.

The processing must remain covered by the relevant purpose and its lawful basis. Applicable Data Processing Agreements and international transfer safeguards must be assessed separately.

**Purpose limitation:**

Candidate information is collected for personalized career guidance.

Using it later for employer recruitment databases, unrelated marketing, model training or other secondary purposes would require a separate purpose and lawful-basis assessment.

### Preliminary Conclusion

The core functionality may rely on Article 6(1)(b), provided that the processing is objectively necessary to deliver a clearly defined contractual service.

Optional AI analysis could rely on Article 6(1)(a), subject to valid, informed and withdrawable consent.

Legitimate interests may be appropriate for limited security-related processing, but a completed LIA is required.

**Overall status:** Proposed lawful bases identified; production compliance remains subject to legal review.


## Phase 4: Risk and Rights Analysis

### 4.1 Special Category Data (Article 9)

The Career Intelligence Agent does not intentionally collect special-category data such as health information, religious beliefs, ethnicity, political opinions or trade union membership. However, users could disclose such information in free-text profile fields, and certain sensitive attributes might be indirectly inferred from employment histories or other contextual information.

The current MVP does not have a verified mechanism for detecting or removing such information. Before production deployment, the application should discourage unnecessary sensitive-data input and implement appropriate data minimization and filtering measures. If special-category processing becomes necessary, a valid Article 9 exception must be identified in addition to an Article 6 lawful basis.

### 4.2 Automated Decision-Making (Article 22)

The system automatically evaluates candidate profiles, calculates matching scores, ranks vacancies and flags qualifications requiring verification.

However, it does not make hiring decisions or automatically accept or reject applicants. Users independently review the results and decide whether to pursue an opportunity. Therefore, Article 22 does not appear to apply to the current intended use because no solely automated decision producing legal or similarly significant effects has been identified.

Nevertheless, the system should maintain transparent scoring explanations and allow users to correct their information. Any future employer-facing applicant selection functionality would require a new Article 22 assessment.

### 4.3 Data Protection Impact Assessment (DPIA)

The EDPB criteria indicate the following potential risks:

| EDPB criterion | Assessment | Explanation |
|---|---|---|
| Evaluation or scoring | **Yes** | The system automatically scores individuals against job requirements. |
| Automated decisions with legal or similarly significant effects | **Not identified** | The system provides career advice rather than binding employment decisions. |
| Systematic monitoring | **No evidence** | The MVP does not continuously monitor user behaviour. |
| Sensitive data or highly personal data | **Potentially** | Sensitive information could appear in free-text profiles, although it is not intentionally requested. |
| Large-scale processing | **No, currently** | The MVP uses a small number of synthetic candidate profiles. |
| Matching or combining datasets | **Uncertain** | Candidate information is compared with public job advertisements, but this does not necessarily constitute the matching of separate personal-data datasets contemplated by the criterion. |
| Vulnerable individuals | **Not established** | The intended users are general jobseekers, although individual circumstances may create vulnerability. |
| Innovative technology | **Potentially yes** | The system combines automated profiling with AI-generated career analysis. |
| Preventing individuals from exercising rights or accessing services | **No evidence** | The application does not control access to employment opportunities or prevent users from exercising their rights. |

**DPIA conclusion:**

At least one criterion clearly applies: evaluation or scoring. Innovative technology may provide a second criterion, depending on the production context.

Under EDPB guidance, two or more criteria generally indicate that a DPIA is likely to be necessary, but this is not an automatic legal rule. A documented assessment under GDPR Article 35 should therefore be completed before processing real candidate data.

Potential international transfers should also be assessed as an additional privacy risk.

**Current status:** DPIA screening required before production deployment; formal DPIA obligation TBD — legal/DPO review.

### 4.4 Data Subject Rights Friction

The following GDPR rights could create operational challenges:

| Data subject right | Potential challenge | Current capability / required action |
|---|---|---|
| **Right of access (Article 15)** | Users may request their original profile data, inferred scores, reports and relevant processing information. | Reports can be exported, but a complete personal-data access procedure is not documented. |
| **Right to rectification (Article 16)** | Incorrect experience or qualifications may produce misleading recommendations. | Users can edit profiles before execution; correction and regeneration procedures for stored results require definition. |
| **Right to erasure (Article 17)** | Personal information may exist in saved reports, logs and external processing systems. | No documented end-to-end deletion procedure or retention policy exists. |
| **Right to object (Article 21)** | Users may object to processing based on legitimate interests, including relevant profiling. | No formal objection-handling mechanism is documented. Applicability depends on the selected lawful basis. |
| **Right to data portability (Article 20)** | Users may want to transfer information they provided to another service. | JSON export offers a useful technical foundation, but the complete portability scope and process need assessment. |

**Conclusion:**

The application already provides some technical foundations for transparency, correction and data export.

However, formal procedures for access, deletion, objections and timely responses have not been established. Before production use, the controller should implement and document these procedures, including coordination with external processors.

---

## Phase 5: Law Stacking Check

### AI Act Cross-Check

**Provisional risk tier: Limited Risk / Transparency.** The current B2C system falls outside Annex III, point 4(a), because it supports jobseekers rather than employer-led applicant selection; applicable Article 50 transparency and AI-content marking requirements must be assessed separately from GDPR obligations.

### ePrivacy Check

The MVP does not intentionally implement advertising trackers or behavioural analytics, but its actual browser storage and cookie behaviour has not been audited. Any non-essential cookies or similar tracking technologies would require an assessment under applicable ePrivacy rules, including consent where required.

### Data Act Check

**Not directly relevant to the current MVP:** The system does not process connected-product or IoT data and does not currently offer a cloud-switching service. Applicability should be reassessed if the commercial product or service model changes.

---

## Phase 6: GDPR Compliance Memo

**To:** Data Protection Officer, Career Intelligence Agent  
**From:** AI and Data Protection Consultant  
**Date:** 17 November 2026  
**Subject:** Preliminary GDPR Compliance Assessment

### Recommendation: Proceed with Conditions

The Career Intelligence Agent may continue as a controlled prototype using synthetic candidate data. However, production deployment with real user profiles should not proceed until the organization establishes a documented and GDPR-compliant data-processing framework.

The system evaluates professional experience, qualifications and career preferences to recommend suitable vacancies. Although users retain control over application decisions, the automated matching scores and inferred qualifications constitute personal assessments when linked to identifiable individuals.

The MVP includes explainable recommendations, profile review and report exports. Nevertheless, several privacy safeguards required for production use remain incomplete or unverified.

### Top Three Recommended Actions

**1. Establish lawful processing and data governance**

Document the purpose and lawful basis of each processing activity under Article 6. Verify the necessity of candidate data collection, establish appropriate privacy notices, define retention and deletion periods, and implement procedures for responding to data subject requests. Optional AI analysis requires a clearly documented lawful basis, while any reliance on legitimate interests must be supported by an assessment.

**2. Verify third-party processing and international transfers**

Determine exactly which candidate-related information is transmitted to OpenAI and other external services. Verify controller and processor responsibilities, establish required Data Processing Agreements under Article 28, and assess any international transfers under GDPR Chapter V. Commercial processing should only begin once the necessary contractual and technical safeguards are confirmed.

**3. Complete risk assessment and strengthen technical safeguards**

Conduct a documented DPIA screening under Article 35, considering automated scoring and innovative AI processing. Complete a DPIA if the assessment identifies likely high risk. Introduce safeguards against unnecessary sensitive-data collection and expand testing for incorrect or systematically unfair matching outcomes.

### Residual Risks

Even after these actions, three concerns remain:

- **Recommendation reliability:** Incorrect scores may influence important career decisions despite transparent explanations.
- **Sensitive-data exposure:** Users may unintentionally include Article 9 information in free-text fields.
- **Third-party dependency:** External providers may change their processing arrangements, service locations or contractual conditions.

These risks require continuing monitoring and periodic reassessment.

### Limitations

This memorandum is a preliminary advisory assessment of the current MVP and its proposed commercial use.

It is **not a legal opinion, completed DPIA, conformity assessment or compliance certification**. Qualified legal counsel and the Data Protection Officer should verify the conclusions before production deployment.
