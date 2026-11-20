# Phase 4: GDPR Audit Report: Interview Prep Report

**Audited system:** Interview Prep Report (Julia Antunes) · **Auditor:** Ayhan Demir · **Date:** 17 Nov 2026
**Based on:** [Data_Processing_Brief_Interview_Prep_Report.md](./Data_Processing_Brief_Interview_Prep_Report.md), reviewed as the partner's evidence package

## Section 1: System summary

Interview Prep Report is an n8n workflow that helps a job seeker prepare for an interview. The candidate enters a company name, pastes a job posting and gives a CV as a PDF, a public GitHub profile, or both. The workflow researches the company through Tavily and GNews, pulls public repositories from GitHub, and has OpenAI compare the candidate's evidence with the job and write a report on fit, skill gaps and likely questions. The main personal data is the CV and GitHub profile, plus the generated report that evaluates the candidate; rejected submissions can also be logged to Notion.

## Section 2: Data and role map

The personal data is mainly the candidate's: CV, GitHub identity and repositories, and the report's fit and skill-gap assessment. CVs can also hold special-category data (photo, health, religion) and third-party data such as referees. With no client named, I assume Julia runs the tool for the public and is the **controller** (Q1). OpenAI, Tavily, Notion, n8n and the host are **processors** with no DPAs documented; GitHub and GNews are independent controllers. OpenAI, Notion and Tavily are in the US with no transfer mechanism documented; n8n and hosting regions are not stated.

## Section 3: Compliance findings

**Finding 1: Processor contracts (Art. 28)**
**Severity:** Blocking
**Description:** Every processor needs a contract before handling personal data. OpenAI already receives full CV text and n8n stores it, but no DPAs are documented and all integrations run on free or trial plans.
**Recommended action:** Accept or sign DPAs with OpenAI, the n8n host, Notion and Tavily, moving to plans that offer them, before any real CV is processed.
**Escalation needed?** No.

**Finding 2: Lawful basis and transparency (Art. 6, 13)**
**Severity:** Significant
**Description:** No lawful basis or privacy notice is named. A basis plausibly exists (the user's request, Art. 6(1)(b)), but candidates are not told that an AI in the US reads their CV.
**Recommended action:** Record a basis per purpose (contract for (1) to (4) and (7), legitimate interests for (5) and (6)) and show a short privacy notice on the form before upload.
**Escalation needed?** No.

**Finding 3: Minimisation, special-category and third-party data (Art. 5(1)(c), 9, 14)**
**Severity:** Significant
**Description:** The full CV goes to OpenAI, including contact details, date of birth and referees the report does not need, and no Art. 9 condition covers special-category data. Nothing checks that the CV or GitHub profile is the submitter's own, so another person's data can be processed without their knowledge.
**Recommended action:** Strip contact details, date of birth and referees before the LLM call; ask users to remove special-category details; add a confirmation that the CV and profile are their own.
**Escalation needed?** No.

**Finding 4: International transfers (Art. 44 to 46)**
**Severity:** Significant
**Description:** CV text goes to OpenAI in the US; Notion and Tavily are also US-based. No transfer mechanism and no n8n or hosting region is given.
**Recommended action:** Confirm EU-US Data Privacy Framework certification or put SCCs in place for each US processor; host n8n in the EU.
**Escalation needed?** Yes: legal counsel, to confirm the transfer mechanism.

**Finding 5: Storage limitation (Art. 5(1)(e))**
**Severity:** Significant
**Description:** Reports are not stored on purpose, but n8n execution history and the Notion error log can keep CV text with no retention period.
**Recommended action:** Turn off saving of successful executions or prune them after a short period (for example 7 days); limit the Notion log to error type and time, with no CV text.
**Escalation needed?** No.

**Finding 6: DPIA screening (Art. 35)**
**Severity:** Significant
**Description:** LLM-based evaluation of a candidate's fit and skills meets two EDPB indicators (evaluation or scoring, innovative technology). As it serves the candidate and decides nothing about them, a full DPIA may not be needed, but no screening is documented.
**Recommended action:** Document a DPIA screening; if it confirms a high risk, complete a DPIA before launch.
**Escalation needed?** Yes: a data protection adviser, to confirm whether a full DPIA is needed.

## Section 4: Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Gap identified | None named (Finding 2) |
| Purpose limitation respected (no incompatible reuse) | Appears met | All purposes serve the user's request; Notion logging needs limiting (Finding 5) |
| Data minimisation (only necessary data collected) | Gap identified | Full CV to OpenAI (Finding 3) |
| Controller/processor roles mapped and DPAs in place | Gap identified | Roles inferable, no DPAs (Finding 1) |
| International transfer mechanism documented | Gap identified | US processors, no mechanism (Finding 4) |
| DPIA conducted if required | Cannot determine from brief | No screening documented (Finding 6) |
| Article 22 safeguard in place if automated decisions affect people | Appears met | No decision about the candidate; report is advice to the user |
| Privacy notice covers AI processing | Cannot determine from brief | Brief silent; assumed missing (Finding 2) |
| Data subject rights can be operationalised within deadlines | Cannot determine from brief | No accounts or stored reports, but CV copies in logs cannot be found by person without an identifier |

## Section 5: Overall recommendation

**Do not proceed** with real candidate data until Finding 1 is resolved. The design is privacy-friendly in key ways: it stores no reports on purpose, connects to no HR system and decides nothing about the person. But OpenAI and n8n already process full CVs without a processor contract, which the severity guide treats as blocking. Once DPAs are in place, it moves to **proceed with conditions**: lawful basis and privacy notice, CV minimisation, secured US transfers, log retention and a DPIA screening, all before a public launch. Demos with synthetic data or the builder's own CV can continue.

## Section 6: What this report is not

This report is not a legal opinion, not a DPIA and not a certification of compliance. It is a peer review based only on the data processing brief. The client should obtain legal review before relying on this assessment.
