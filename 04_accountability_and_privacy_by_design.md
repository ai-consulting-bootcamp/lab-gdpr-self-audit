# Accountability check and privacy by design: AI Use Case Identifier

Reinforce and stretch tasks. Friedrich Tschoepke · 23 November 2026

## Accountability: what a regulator could ask for

| Document | Exists? | Note |
|---|---|---|
| Record of processing activities (Article 30) | No | Small businesses are exempt only if processing is occasional; regular research runs are not. |
| Data processing agreement with OpenAI | Unknown | Part of OpenAI's terms; acceptance not archived. |
| Agreement or role statement for Tavily | No | Tavily states it is controller of its index; my role towards it not documented. |
| Legitimate interests assessment | Draft | In the audit worksheet, Phase 3. Needs to be filed as a standalone record. |
| DPIA or DPIA screening | Draft | Screening in the worksheet, Phase 4. |
| Privacy notice | No | No website notice; no notice for contacts. |
| Retention schedule | No | Run files kept without limit. |
| Procedure for access and erasure requests | No | |
| Breach response procedure | No | |
| Source traceability | Yes | Every claim in a brief is labelled documented or assumption, with links. |
| Technical documentation | Yes | README and architecture notes. |

**Entirely missing:** record of processing, privacy notice, retention schedule, rights procedure, breach procedure.

## Preparing the legal review: outreach to contacts in `lead.json`

What counsel needs to know to advise quickly:

- How contacts enter `lead.json`: typed in by me after finding them on a company website, or given to me directly (business card, event).
- Which channels I want to use: email, phone, LinkedIn message.
- Whether any contact has given consent, and how I would record it.
- Whether contacts are reached in their role (generic company inbox or personal work address).
- The planned frequency and content of follow-ups.

With these facts prepared, the question narrows to one point: which channels § 7 UWG allows without prior consent for this kind of first contact.

## Privacy by design checklist: research step (collect, send to OpenAI, store)

| Design principle | Current state | Status |
|---|---|---|
| Data minimisation | Full page texts, job postings and register snippets go to OpenAI and into `state.json` with all names and contact data. | Fail |
| Purpose binding | Data stays on the laptop and is used only for the brief, but nothing technical prevents reuse, for example for outreach. | Unknown |
| Access controls | Single user, files on a personal laptop; disk encryption not documented. | Unknown |
| Retention enforcement | No deletion. | Fail |
| Subject rights workflow | Files can be searched and deleted locally within 30 days, but there is no procedure and no list of where copies are. | Unknown |
| Incident response | No breach procedure. | Fail |

**What needs to change:**

- **Minimisation:** add a filter in the research node that removes phone numbers, email addresses, dates and residence details from snippets before they are stored or sent to the model.
- **Purpose binding:** keep `lead.json` out of the research output folder and write it only after a documented decision to contact.
- **Access:** confirm full-disk encryption on the laptop and note it in the record of processing.
- **Retention:** a cleanup script that deletes `outputs/` folders older than six months, run monthly.
- **Rights workflow:** a one-page procedure listing the copies (`outputs/`, OpenAI up to 30 days, Tavily index) and a template reply.
- **Incident response:** a short procedure naming what counts as a breach (lost laptop, leaked API key with access to logs) and the 72-hour notification route to the state data protection authority.
