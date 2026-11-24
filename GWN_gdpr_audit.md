# Green Warehouse Network GDPR Audit

**Scope:** Project-3 Green Warehouse Network MVP, as documented and implemented in the `Project-3` repository.

## Data processing brief

The MVP processes a sample planning dataset containing 24 customer records and 12 candidate warehouse records. The customer CSV contains IDs, place-style names (for example, “Berlin retail”), coordinates, and annual demand. The warehouse CSV contains IDs, location names, coordinates, capacity, fixed cost, and fixed CO₂. The current sample has no names or emails of natural persons, no account identifiers, and no evident special-category attributes. The records should therefore be treated as **potentially personal or pseudonymous logistics data**, not as proven personal data. Precise coordinates can identify a person or household in a real deployment, and the `add_customers` interface allows a caller to submit arbitrary customer names and locations.

The data comes primarily from static, hand-built CSV files. Climatiq-sourced emission factors and an OpenRouteService-derived distance cache supplement those inputs. The application adds user-entered scenario values and natural-language chat text. It also stores chat history, LangGraph thread IDs, scenario events, solver results, and saved scenarios in Streamlit/LangGraph session state. The chat text is sent to the configured OpenAI model for intent extraction and answer/report generation.

The processing purposes are network optimization and scenario analysis, map and report presentation, conversational clarification, and generation of downloadable HTML reports. The system makes a warehouse-allocation recommendation and ranks or selects primary and backup sites. A human operator chooses the objective and reviews the map and report before using the plan; in the MVP, the solver result is not presented as an automatic operational instruction.

The core CSV and solver processing runs in the local application environment. OpenAI receives chat prompts and session/tool information for intent and report functions. The exact OpenAI account region, deployment location, and retention settings are unknown. Streamlit hosting, server location, and database retention are also unknown. The prepared routing-distance and emission caches avoid normal live calls to routing or emissions vendors, although those integrations exist for refresh/cache preparation.

## Phase 1: Personal data inventory

| Data category | Source | Purpose(s) | Retention period (known/estimated) | Crosses EU border? |
|---|---|---|---|---|
| Customer ID, place-style name, coordinates, annual demand | Static `customers.csv`; optional chat-added customer | Optimize primary/backup assignments and map locations | Unknown; session state only in MVP, source CSV unbounded | Locally only in base MVP; may cross EU border through OpenAI if included in prompts |
| Chat prompts and session clarification text | Directly from the user | Intent extraction and conversational scenario assistance | Unknown; session memory in MVP and provider-side retention unknown | Yes, if OpenAI processing occurs outside the EEA |
| Scenario settings and natural-language request history | Chat UI and session state | Scenario replay, explanation, saved scenarios, report generation | Unknown; memory/session lifetime, no deletion workflow documented | Locally only; full session/tool data is sent to OpenAI for report generation |
| Warehouse ID, location name, coordinates, capacity, cost, fixed CO₂ | Static `candidate_sites.csv` | Candidate-site optimization and mapping | Unknown; source file unbounded | Locally in MVP; unknown if exported |
| Solver assignments, KPI values, and generated HTML report | Derived from data and scenarios | Present recommendations and download reports | Unknown; browser/session/report retention; no retention schedule | Locally only in MVP; data may be sent to OpenAI while report wording is generated |
| OpenAI API account/model metadata | OpenAI provider | Authenticate and process chat/report requests | Unknown | Potentially cross-border; location and terms require verification |

**Purpose compatibility:** The static logistics dataset was built for network modeling, and the MVP uses it for that stated purpose. In a real implementation, importing customer records previously collected for customer service or sales, or using the chat and location data for profiling or outreach, would be a new purpose and require purpose-limitation review. The future n8n integration also introduces new notification and export purposes that are not in the current MVP scope.

## Phase 2: Role map

| Entity | Role (controller / processor / joint controller) | Processing activity | DPA in place? |
|---|---|---|---|
| Logistics customer or deploying organization | Controller | Defines objectives and provides network/customer data; approves warehouse decisions | DPA status unknown |
| Project team / application operator | Processor if acting on client instructions; otherwise controller for development and deployment | Hosts, operates, and maintains the app; processes chat and source data | TBD — legal review; processor terms and project role must be documented |
| OpenAI API provider | Processor when processing client-provided chat/session data under an API agreement | Intent parsing, explanations, and report generation | DPA unknown; establish OpenAI API DPA and confirm retained data/API settings before personal data flows |
| Streamlit/hosting provider | Processor if it hosts user or chat data | Dashboard execution, session state, and possible logs | Unknown; require hosting DPA and documented region |
| OpenRouteService / HeiGIT | Likely processor or independent provider; no normal runtime request in the supplied setup | Prepared distance-cache refresh; attribution included | Unknown; cache contents and refresh access should be reviewed |
| Climatiq | Likely processor or independent provider; no normal runtime request in the supplied setup | Emission-factor refresh | Unknown; API terms/DPA and data transmitted should be verified |

For any international transfer, the mechanism is **TBD — legal review**. The OpenAI deployment region and hosting region must be established. Adequacy, EU/UK or US transfer arrangements, or approved Standard Contractual Clauses (SCCs) must be confirmed before regulated personal data is sent outside the EEA. The current sample dataset should not be transmitted to OpenAI unless it is needed for report generation and has been minimized.

## Phase 3: Lawful basis assessment

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| Warehouse network optimization using client-provided location/demand data | Contract or legitimate interests | Contract may apply when direct delivery requires the network plan; otherwise the client must complete an LIA for internal network planning | Yes |
| Natural-language intent extraction and chat assistance | Legitimate interests or contract | The chat is supporting the contracted planning service, but whether it is necessary and privacy-safe remains unconfirmed | Yes |
| Solver result, map, and downloadable report | Contract or legitimate interests | This is a direct output of the planning service, but personal data should be minimized to avoid unrelated uses | Yes |
| Future n8n notifications, Slack/email exports, CRM or ERP integrations | TBD — legal review | Not part of the MVP, and recipients, purposes, and data fields are not yet defined | Yes |
| Development/testing and sample-data analytics | Legitimate interests or consent, depending on test subjects | Re-use of real production data should not be assumed; synthetic/anonymized data is preferred | Yes |

**Three-part LIA, if legitimate interests is retained**

1. **Legitimate interest:** Efficient, resilient warehouse planning has a concrete business need, but it must be linked to the deploying organization's ordinary network-planning service.
2. **Necessity:** Processing is necessary only for the data fields required to calculate distance, demand, and capacity. The chat should not receive broad session data or unrelated personal attributes.
3. **Balancing:** The client's operational benefits may not override individuals' or customers' privacy if precise locations are identifiable, data is sent to a US provider, or chat text is retained. This test cannot be completed confidently with the present information.

**Conclusion:** `TBD — legal review` remains the appropriate status until the controller, contractual role, and the categories of real data are confirmed.

## Phase 4: Risk and rights analysis

### Special category data (Article 9)

No special-category data is evident in the static MVP fields, and the stated output should not infer health, ethnicity, political, religious, sexual, biometric, or trade-union traits. Precise coordinates or arbitrary free-text customer names could nevertheless identify small locations or individuals, and future customer profiling could create inferences. No Article 9 condition is confirmed as satisfied; Article 9 review is required before using such fields or deploying the chat with real personal content.

### Automated decision-making (Article 22)

The model selects warehouse assignments and can influence a major network decision, but it does not currently decide about a person's legal status or similar rights and has meaningful human selection of objective and review of the result. Human intervention is therefore operationally present but not documented as a safeguard. If GWN later assigns real customers, denies service, or triggers individual operational consequences without meaningful review, Article 22 safeguards, contestability, and explanation requirements would need reassessment.

### DPIA trigger

Potential EDPB triggers include innovative technology (LLM orchestration), cross-border LLM or hosting transfers, matching/combining several planning datasets, and evaluation or scoring if customer locations are used to rank or allocate capacity. The MVP does not clearly process special-category data at scale or systematically monitor individuals. Given the uncertain real-data scope and cross-border transfer, a DPIA is prudent before production deployment: if customer records or chat content are identifiable and at least two robust criteria apply, the DPIA becomes a likely requirement.

### Data subject rights friction

Access: The system can display and export saved scenario results, but it has no documented record of a data subject, index, or export workflow linking a person to source and derived records. Erasure: static CSV and session/report copies have no deletion procedure, and chat text may exist in OpenAI or host/provider logs. Objection and restriction: there is no UI or technical mechanism to stop profiling or restrictive processing for a particular person. Rectification: chat-added customer records are retained in scenario state, but no identity-level update or deletion API is documented. The system cannot currently support a timely response within 30 days with confidence.

## Phase 5: Law stacking check

- **AI Act cross-check:** A production GWN application may be limited-risk or could become high-risk if used in a regulated logistics or essential-services context; the current warehouse-planning product is not automatically high-risk on the evidence shown. Human oversight and documented/accurate solver results help address transparency and risk management, but they do not replace AI Act duties if a high-risk use case is later identified.
- **ePrivacy check:** The MVP description identifies Streamlit session state but no cookies, pixels, or persistent device tracking. Consent requirements are not established from this evidence; a production provider or analytics integration may change the result and require a cookie-consent check.
- **Data Act check:** The MVP does not process connected-product or IoT data and has no production cloud-switching workflow. This is N/A for the current version, except for future n8n, ERP/WMS, or machine-generated data integrations.

## Phase 6: Compliance memo

To: Green Warehouse Network Client Legal Counsel / Data Protection Officer

**Bottom line: proceed with conditions.** The deterministic MVP is suitable for controlled, synthetic or genuinely anonymized planning data, but it should not deploy with identifiable customer or chat data until the contractual, transfer, and retention gaps are closed.

Top actions, in sequence: (1) Confirm whether the system is processing personal data and complete a data-flow record listing every real source field, chat field, recipient, region, and retention period. If real people are identifiable, establish the controller/processor roles and execute DPAs with OpenAI and the hosting provider before personal data flows. (2) Conduct a DPIA and make a written Article 6 lawful-basis decision before production use; if legitimate interests is used, document the complete LIA and review Article 22 safeguards and human review. (3) Build minimization and rights controls: remove unnecessary chat context, validate and restrict `add_customers`, disclose OpenAI/hosting transfers, define deletion schedules, and add access, rectification, restriction, and erasure procedures. The MVP also lacks a privacy notice and record of processing activities.

Implementation should begin with synthetic or genuinely anonymized data. Before the real-data pilot, maintain a source-field allowlist, prohibit unnecessary identifiers, and avoid transmitting the full session when only a scenario is required. Add an administrative deletion key, preserve deletion-request evidence, and test source files, session state, reports, provider logs, and exports. The client should designate a privacy owner and define incident and report-release responsibilities.

Human review should remain mandatory for consequential warehouse choices. The review record should identify the operator, the source data used, the model and solver versions, the confirmation of objective, any warnings, and the final business decision. This does not cure GDPR issues, but it strengthens accountability and supports explanation where automated planning assists a larger decision.

Residual risks include uncertain provider locations and retention, arbitrary free-text data being copied into third-party prompts, and future exports or n8n/CRM integrations expanding purpose and recipient scope. Additional operational risk remains from the illustrative nature of fixed costs and emission factors and from decisions made without a documented, accountable business review. This memo is not a legal opinion, a DPIA, or a certification. The client must engage qualified legal counsel and its DPO before relying on this assessment for compliance decisions.

## Reinforce: accountability test

| Documentation / evidence | Status |
|---|---|
| System/data-processing description | **Exists** — README, Spec, and architecture documents |
| Personal data inventory / data-flow brief | **Added by this audit** |
| Data Processing Agreements | **Missing** |
| Legitimate Interests Assessment | **Missing; framework noted as TBD** |
| DPIA | **Missing** |
| Privacy notice / transparency notice | **Missing** |
| Records of Processing Activities | **Missing** |
| Retention and deletion schedule | **Missing** |
| Data subject rights procedure | **Missing** |
| International transfer assessment and SCC/adequacy evidence | **Missing** |
| OpenAI/vendor subprocessor and DPA review | **Missing** |
| Security controls / incident-response and breach-notification plan | **Missing** |

A regulator could show that the project has a technical data inventory and architecture, but could not demonstrate lawful-basis records, DPIA completion, vendor agreements, transfer mechanisms, retention, rights response, or incident handling. The minimum audit evidence should include a controller/processor agreement, DPA, LIA or Article 6 decision, DPIA, privacy notice, RoPA entry, retention schedule, deletion test, rights request workflow, data-transfer register, security policy, and 72-hour breach process.

For the unresolved OpenAI lawful-basis issue, counsel would need the deploying organization's contract with users, the actual fields sent, OpenAI contract/API region, provider retention and training settings, known recipients/subprocessors, server/log retention, and whether users have a genuine choice or are receiving the service under contract.

## Stretch: data protection by design checklist

Highest-risk activity: processing user chat text and any `add_customers` values through OpenAI and storing session/report data.

| Design principle | Current state | Pass / Fail / Unknown |
|---|---|---|
| Data minimisation: only minimum necessary data is collected | Chat sends session/tool context and may include free text; add-customer fields are broad | Unknown |
| Purpose binding: data is technically restricted to the stated purpose | No policy or technical purpose tags for chat/session fields | Fail |
| Access controls: access is limited to those who need it | No documented authentication or role-based access controls in MVP | Unknown |
| Retention enforcement: automated deletion or anonymisation is in place | Streamlit session lifecycle exists, but no deletion policy or provider retention control | Fail |
| Subject rights workflow: access or erasure can be completed within 30 days | No rights request identity lookup or deletion workflow | Fail |
| Incident response: breach detection and 72-hour notification is documented | No documented incident process or escalation owner | Fail |

The system should add field allowlists and redact or reject identifiers, send only scenario data needed for reports, authenticate users, restrict exports and logs, configure provider retention, record processing purposes, implement verified deletion across CSV/session/provider caches, and document a breach triage and notification process.