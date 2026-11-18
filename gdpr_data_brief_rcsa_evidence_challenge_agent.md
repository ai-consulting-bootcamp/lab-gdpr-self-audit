# GDPR Audit — Data Processing Brief

**System:** RCSA Evidence & Challenge Agent
**Industry:** Banking / Financial Services — Operational Risk Management
**Development status:** Functional MVP using synthetic data only
**Intended use:** Supporting a bank's Risk and Control Self-Assessment (RCSA) for business processes

## 1. Personal Data Processed
The system assesses business processes, risks and controls, not individuals. However, in a real bank several data elements would relate to identifiable people:
- **Process owners and assessors:** name, role, department and possibly business email, linked to each RCSA answer (applicable or not, justification, control described).
- **Loss event and near-miss records:** reporter name, employees involved, customer or account references, amounts, dates and free-text descriptions of what happened.
- **System-generated results linked to people:** challenge flags such as "owner marked risk as not applicable, but a loss event exists". When linked to a named owner, these flags are personal data about that person's assessment.

Loss event narratives may contain sensitive information, for example a workplace injury (health data) or suspected **internal fraud** by an employee (data relating to criminal offences). The application does not ask for such data, but it can appear in free text.

KRI values are normally aggregated (counts, rates, volumes) and are not expected to identify individuals.

The current MVP uses only synthetic processes, loss events and KRIs.

## 2. Data Sources
- Process descriptions and RCSA answers are entered by the process owner.
- The previous RCSA for the process comes from the bank's RCSA records.
- Loss events and KRIs come from the bank's internal loss database and KRI reporting.
- An operational risk library provides risk categories.

There is no internet research, no news search and no external data about people.

## 3. Processing Purposes
1. **Risk identification:** suggest possible operational risks for each process step.
2. **Evidence-based challenge:** compare owners' answers with loss events and KRIs and flag contradictions.
3. **Rating and reporting:** estimate inherent risk, control effectiveness and residual risk, and produce an RCSA report for the second-line risk function.

The system is not designed to evaluate employees' performance or conduct.

## 4. Processing Entities
The application uses Python and LangGraph to run the workflow.

**OpenAI** (via API) processes the process description, the owner's answers and relevant loss event text to suggest risks, check contradictions and write the report. Loss event text may therefore be sent to OpenAI.

No vector database or search API receives bank data in the current design.

## 5. Storage and International Transfers
The MVP runs locally. Input data and generated reports are stored as local files.

There is no formal retention and deletion policy for real data yet, and no access control or user accounts beyond the local machine.

OpenAI is a US-based provider. The processing location, data retention settings and transfer safeguards (EU–US Data Privacy Framework or Standard Contractual Clauses, Data Processing Addendum) have not been verified for this project. **Transfers outside the EEA therefore cannot be ruled out.**

## 6. Automated Assessment and Human Review
The system automatically suggests risks, calculates indicative ratings and flags contradictions.

The process owner must answer every suggested risk and can explain or reject a challenge. A second-line operational risk manager is intended to review the report before ratings are accepted. In the MVP, this final approval is not enforced or logged.

The system makes no decisions about individuals, but challenge results linked to named owners could be misused to judge their work.

**Preliminary conclusion:** The synthetic-data MVP processes no real personal data. A production version in a bank would process employee and possibly customer data, including possibly sensitive loss-event narratives, and would fall under the GDPR. It would require a documented privacy and data-processing framework before go-live.
