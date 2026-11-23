# GDPR audit worksheet: AI Use Case Identifier

Friedrich Tschoepke · 23 November 2026 · Builds on `01_data_processing_brief_ai_use_case_identifier.md`. Not legal advice.

**Working assumption:** the builder is the only user and the system has so far run on test cases and a few prospects, not under a client contract. He acts as a sole trader without employees and has no data protection officer.

## CFU 1 – Recognize

- **Categories present:** identity and professional role (names, job titles), professional contact data (phone, email), register data (possibly date of birth, place of residence of directors), quotes and statements in news, contact data entered by the builder.
- **Special categories (Article 9):** not collected on purpose. Can slip in through sources: a news item on a founder's illness, works council or union roles, an inclusive employer describing staff with disabilities. The system draws no inference about individuals.
- **EU border:** yes. Text snippets go to OpenAI (Ireland, US parent); search results come through Tavily (US).

---

## Phase 1: Personal data inventory

| Data category | Source | Purpose | Retention (known/estimated) | Crosses EU border? |
|---|---|---|---|---|
| Names and roles of company staff | Company website, job postings | P1 Meeting preparation | Local: no limit. OpenAI: up to 30 days | Yes (OpenAI) |
| Same | Same | P2 Traceability (`state.json`) | No limit | Collected via US services; stored locally |
| Professional contact data of HR contacts (phone, email) | Job postings, careers page | P1 (not needed) | No limit | Yes (OpenAI) |
| Directors' names, possibly date of birth and residence | Register sites via Tavily | P1 Company profile (size, founding, legal form) | No limit locally; Tavily: own retention | Yes (Tavily, OpenAI) |
| Names and quotes of people in news | Tavily news search | P1 Recent developments | No limit locally | Yes |
| Contact name, email, city | Typed in by the builder | P3 Sales follow-up (`lead.json`) | No limit | No |
| Planned: name, email, phone of requester | Web form | P4a Deliver the report | To be defined | Depends on hosting |
| Same | Same | P4b Marketing follow-up | To be defined | Depends on hosting |

**Purpose changes (flagged):**

1. **Job postings** were published to recruit staff. The system reuses them, including the named HR contacts, to analyse the company for sales preparation. Using the content about the company is compatible (Article 6(4): public business information, low sensitivity, people in their professional role). The HR contacts' names and numbers are not needed for that purpose and should be dropped.
2. **Register entries** are published for legal transparency and creditor protection. Using the company facts (founding year, legal form, size) is compatible. Personal details of directors beyond name and role are not needed.
3. **Planned lead magnet:** contact data collected to deliver a report would be reused for sales follow-up. That is a separate purpose and needs its own basis and, for emails, consent.

## Phase 2: Role map

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| Analysed company | None (data source, not a client) | – | Not needed |
| Friedrich Tschoepke (sole trader) | Controller | Decides why and how all data is processed | – |
| OpenAI (OpenAI Ireland Limited for EEA data) | Processor | Model calls on collected snippets; image generation | **Unknown.** OpenAI's DPA forms part of its services agreement; acceptance must be checked and archived. Transfer to US: **TBD – verify** mechanism in the current DPA (Data Privacy Framework or SCCs). |
| Tavily (AlphaAI Technologies Inc., US) | Independent controller of its search index; processor for the builder's queries **TBD – legal review** | Search; returns third-party content | **No.** No standard DPA known. Queries contain only company names, so the personal data reaching Tavily from the builder is minimal. |
| Pinecone | None for personal data | Stores the reference library | Not needed |
| GitHub (Microsoft) | Not relevant | Hosts code and one sample without personal data | Not needed |
| Planned: web host and email service for the lead magnet | Processors | Form, delivery | Needed before launch |

## Phase 3: Lawful basis assessment

| Purpose | Proposed lawful basis | One-line justification | Legal review? |
|---|---|---|---|
| P1 Meeting preparation | Legitimate interests (6(1)(f)) | Personal data is incidental to analysing a company from public sources; no consent is possible from people the builder does not know. | No, if minimised |
| P2 Traceability | Legitimate interests | Showing where each claim comes from protects the client and the analysed company from errors; needs a time limit. | No |
| P3 Sales follow-up (`lead.json`) | Legitimate interests for storing (Recital 47) | Keeping a business contact for a planned conversation is an expected use. **Emailing** that contact for marketing needs prior consent under German law (§ 7 UWG) whatever the GDPR basis. | **Yes** |
| P4a Lead magnet: deliver report | Contract (6(1)(b)) | The person asks for the report; email is needed to send it. | No |
| P4b Lead magnet: marketing follow-up | Consent (6(1)(a)) | Separate, unticked checkbox; required anyway by § 7 UWG for emails. | Yes |

**Legitimate interests assessment for P1:**

1. **Legitimate interest?** Yes. Preparing an informed first conversation with a business is a normal commercial interest and also serves the company, which gets a better-prepared consultant.
2. **Necessary?** Only partly. The analysis needs facts about the company, not about individuals. Names of directors help to know whom one meets; HR contact names, phone numbers, dates of birth and residence are not needed. A less intrusive way exists: remove these before the model call and before storage.
3. **Balancing?** With minimisation, the people concerned are named only in their public professional role, the data is low in sensitivity, the volume is small, and no decision about them follows. People in management roles can expect their company to be researched. Without minimisation, the indefinite storage of unneeded contact data and register details tips the balance the wrong way.

**Result:** legitimate interests hold for P1 and P2 **on condition of minimisation and a retention limit**.

## Phase 4: Risk and rights analysis

**Special category data (Article 9).** Not sought and not inferred. It can arrive by chance in news or company pages, for example an inclusive employer describing staff with disabilities or a report on a founder's illness. No Article 9(2) condition fits this processing, so such content must not be used. The practical safeguard is a prompt rule and a review step: drop health, union or religious details about individuals before they reach the brief.

**Automated decision-making (Article 22).** Does not apply. The system makes no decision about any person. Its only rating concerns company work steps, and the builder reads every brief before using it. The planned lead magnet changes nothing here: the report still concerns a company.

**DPIA trigger (EDPB criteria).**

| Criterion | Applies? | Note |
|---|---|---|
| 1 Evaluation or scoring of people | No | Scores work steps, not persons. |
| 2 Automated decision with significant effect | No | |
| 3 Systematic monitoring | No | One-off research per company. |
| 4 Sensitive or highly personal data | No | Only by accident. |
| 5 Large scale | No | A few companies a month, few names each. |
| 6 Matching or combining datasets | Partly | Website, news and register data are merged into one profile; the personal data in it is incidental. |
| 7 Vulnerable data subjects | No | |
| 8 Innovative technology | Yes | Language models analyse collected data. |
| 9 Prevents exercise of a right or access to a service | No | |

One clear criterion and one partial: **a DPIA is not generally required.** Record this screening and repeat it if the lead magnet or a client version is built.

**Data subject rights friction.**

- **Information (Article 14):** people named in sources are not told. For incidental names, the exemption for disproportionate effort (Article 14(5)(b)) is arguable but must be documented. For contacts in `lead.json`, information is due at the first contact at the latest (Article 14(3)(b)). **Not supported today:** no privacy notice exists.
- **Access (Article 15):** a named director asks what is held. Possible within 30 days by searching `outputs/` for the name, but there is no procedure and no inventory.
- **Erasure (Article 17):** local files can be deleted at once. OpenAI's copies expire after up to 30 days; Tavily's index is outside the builder's control.
- **Objection to direct marketing (Article 21(2)):** absolute. Requires a suppression list once outreach starts; none exists.

## Phase 5: Law stacking check

- **AI Act:** limited risk (Article 50(2), see EU AI Act self-audit). Adds machine-readable marking of the generated brief and image, and AI literacy (Article 4). Neither is a GDPR duty.
- **ePrivacy:** the command-line tool uses no cookies or tracking. Outreach by email to contacts from `lead.json` falls under the ePrivacy rules on unsolicited communication, in Germany § 7 UWG: prior consent is required, also between businesses. **Not satisfied today**, because no consent is recorded. The planned lead-magnet website would need consent under § 25 TDDDG for any analytics or third-party content.
- **Data Act:** not applicable. No connected products, no cloud switching.

## CFU 4 – Verify (accountability test)

Could the builder demonstrate compliance to a regulator with today's documentation? **No.** What exists: README, architecture notes, and source labels in every brief. Missing: see the accountability list in `04_accountability_and_privacy_by_design.md`.

## Sources

- [OpenAI, Data controls in the OpenAI platform](https://developers.openai.com/api/docs/guides/your-data)
- [OpenAI, Data Processing Addendum](https://openai.com/policies/data-processing-addendum/)
- [Tavily, Search index and the right to be forgotten](https://docs.tavily.com/documentation/Right-To-Be-Forgotten)
- [Tavily, Privacy and security](https://help.tavily.com/articles/6781493822-data-retention)
- [Tavily, Privacy policy](https://tavily.com/privacy)
- EDPB-endorsed WP29 Guidelines on DPIA (WP248 rev.01)
- Code: `app/run.py` (contact fields, `lead.json`), `app/tools/search.py` (queries, register domains), `app/nodes/research.py` (pages fetched), `app/nodes/report.py` (`state.json`)
