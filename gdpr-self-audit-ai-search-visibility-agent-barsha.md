# GDPR Self-Audit - AI Search Visibility Agent

**Auditor:** Barsha Mishra
**System audited:** AI Search Visibility Agent (my Project 3, Ironhack AI Consulting & Integration Bootcamp)
**Project repo:** https://github.com/barsha-mishra/ai-search-visibility-agent
**Related work:** my EU AI Act self-audit of the same system (minimal risk, with a possible Article 50(2) duty)
**Date:** 17 November 2026
**Status:** First-pass assessment for a classroom lab. This is not legal advice.

---

## Kick-off - Data processing brief

*Written for a Data Protection Officer who has never seen the project.*

**Does the system process personal data at all?**
**Yes, but only a small amount, and mostly as a side effect.** The system is built to analyse **companies**: brands, their Google rankings, and how often AI assistants mention them. Most of the data is therefore company data, which GDPR does not cover. However, personal data enters the system in four places:
1. the **email address** of the person who requests the report
2. **names of people** in news articles and search results (journalists, authors, CEOs and spokespeople, reviewers, influencers)
3. **brand names that are also people**, for example a freelancer or personal brand entered as "brand" or "competitor"
4. **technical data** such as the requester's IP address, which the form host and the email image service may log

So "no personal data" would be the wrong conclusion. GDPR applies, but at low intensity.

**What personal data does it process?**
- Recipient email address, typed into the form
- Names and professional details of people mentioned in news articles (NewsAPI), Google search snippets (Serper) and AI answers (OpenAI)
- Article text that describes people, e.g. "CEO X resigns"
- Names of natural persons if a personal brand is analysed
- Technical data: IP address and timestamps in n8n execution logs and hosting logs (probable, not yet verified)
- The generated report, which can repeat any of the above

The system does **not** infer attributes about people. The scores are about brands.

**Where does the data come from?**
- **Directly from the user:** the form (brand, competitors, country, search questions, email).
- **From third-party sources:** Serper (Google results), NewsAPI (news articles), and OpenAI (AI-generated answers about the brands).
- **Not from company databases:** no customer database is used. The RAG knowledge base (Pinecone) contains only public SEO and AI-search guideline documents.

**What is the data used for?** One purpose each:
1. Delivering the report to the requester by email
2. Measuring brand visibility on Google and in AI answers, and collecting brand news
3. Generating the written report with an LLM
4. Fact-checking the report (LangGraph service)
5. Running and troubleshooting the workflow (execution logs)
6. *Planned, not built:* weekly scheduled runs and a results history in Google Sheets

**Who processes it?**
- My n8n workflow
- OpenAI (AI answer check, report writing, fact-checking)
- Serper and NewsAPI (they receive search queries containing brand names)
- Render (hosts the fact-checker)
- Gmail SMTP (sends the email; currently a **personal Gmail account**)
- QuickChart (receives chart data, i.e. brand scores, and the recipient's IP when the image loads)
- Pinecone (stores guideline documents only, no user data)

**Where is it stored and processed?**
- **Mostly in the US:** OpenAI, Serper, NewsAPI, Render, Google and QuickChart are US-based or US-hosted. Pinecone's region is not configured for the EU.
- **n8n execution data:** stored in **n8n Cloud** (n8n GmbH, a German company; the hosting region is documented by n8n and should be verified as EU) with the **default execution-saving settings**. No retention period is defined.
- **Reports:** stored as Markdown files and in the recipient's inbox.

**Does it make or assist decisions about people?**
**No.** It ranks and scores **brands**, not people, and it recommends SEO actions. A human (the marketing lead) reads the report and decides what to do. The only edge case is a personal brand: the system would then score one person's online visibility. That still has no legal or similarly significant effect on them.

---

## CFU 1 - Recognize

- **Categories of personal data present:**
  - contact data (recipient email)
  - identity and professional data of third parties (names, roles, quotes in news and search results)
  - content about people (news text)
  - technical data (IP addresses, timestamps)
- **Special-category data (Article 9):** **not intended and not inferred.** However, news articles about named people can incidentally contain health, political or religious information, for example "CEO steps down for health reasons" or a founder's political donations. If those pass the relevance filter, they could end up in the report.
- **Does data cross an EU border?** **Yes.** Every run sends data to US-based services: OpenAI, Serper, NewsAPI, Render, Google (Gmail) and QuickChart.

---

## Phase 1 - Personal data inventory

| Data category | Source | Purpose(s) | Retention period (known/estimated) | Crosses EU border? |
|---|---|---|---|---|
| Recipient email address | User, via n8n form | P1: deliver the report | n8n logs: **undefined** (default saving). Sent mail: kept in the Gmail "Sent" folder indefinitely | Yes (Gmail, US). n8n Cloud is run by a German company (verify the hosting region) |
| Recipient email address | Same | P5: troubleshooting (execution logs) | **Undefined** | Yes |
| Recipient email address | Same | P6 (planned): weekly reports and history log | Not built yet | ⚠️ **Purpose change flag** (see below) |
| Names and roles of people in news | NewsAPI | P2: brand news; P3: report writing | Not stored by me after the run, except in n8n logs (**undefined**) and the report | Yes (NewsAPI and OpenAI, US) |
| Names of people in search snippets | Serper (Google results) | P2: Google visibility | n8n logs (**undefined**) | Yes (Serper, US) |
| Names of people in AI answers | OpenAI | P2: AI visibility; P3: report writing | n8n logs (**undefined**). OpenAI API data is retained by OpenAI for up to 30 days for abuse monitoring, per its API policy *(verify the current terms)* | Yes (OpenAI, US) |
| Report content (can contain all of the above) | Generated by OpenAI | P1: delivery; P4: fact-checking | Recipient's inbox (controlled by the recipient); Render (**unknown** if logged) | Yes (OpenAI, Render, Gmail) |
| Brand name = natural person (personal brand) | User, via form | P2: visibility measurement | n8n logs (**undefined**) | Yes |
| IP address and timestamps | Requester's browser and email client | P5: operations (hosting logs); image loading (QuickChart) | Per the vendors' log policies (**unknown**) | Yes (QuickChart, US) |

**⚠️ Purpose-change flags**
1. **News articles and search snippets were written for journalism and publishing.** My system reuses the names in them for **commercial competitor analysis**. This is a secondary use of public data, so it needs its own lawful basis (Phase 3), and people's names are not even needed for the purpose.
2. **The recipient email was collected to send one report.** Reusing it for **weekly scheduled reports** or storing it in a **Google Sheets history** (planned features) would be a new purpose. That is only acceptable if the user explicitly asks for recurring reports.

---

## Phase 2 - Role map

**Prototype today:** I run everything myself, so I am the **only controller**.
**Production (as assumed for the memo):** a client, e.g. an SEO agency or a brand's marketing team, uses my agent as a service.

| Entity | Role (controller / processor / joint controller) | Processing activity | DPA in place? |
|---|---|---|---|
| **Client** (e.g. BrightCart GmbH, fictional) | **Controller** | Decides to analyse its brand and competitors, and receives the report | No contract exists yet |
| **Me (Barsha)** | **Processor** for the client: I run the workflow on the client's instructions. **Controller** for my own operations (account, invoicing, and the prototype today) | Runs the n8n workflow, the APIs and delivery | ❌ **DPA needed** between the client and me (Art. 28) |
| **OpenAI** (LLM API) | **Sub-processor** | AI answer check, report writing, fact-checking | ⚠️ OpenAI offers a DPA for API customers. **Not confirmed as signed.** |
| **Serper** | **Sub-processor** for my queries *(TBD: may act as an independent controller for its own search index)* | Google search results | ❌ **Unknown** |
| **NewsAPI** | **Sub-processor** for my queries *(TBD, as for Serper)* | News articles about the brands | ❌ **Unknown** |
| **Render** | **Sub-processor** | Hosts the fact-checker (receives the report and key facts) | ⚠️ DPA available. **Not confirmed.** |
| **Google (Gmail SMTP)** | **Sub-processor** | Sends the report | ❌ **No DPA.** A personal Gmail account has no data processing agreement. A business account (Google Workspace) is needed. |
| **n8n Cloud** (n8n GmbH, Germany) | **Sub-processor** | Workflow execution and logs | ⚠️ DPA available. **Not confirmed.** |
| **QuickChart** | Sub-processor only for IP addresses (receives brand scores, not names) | Chart images in the email | ❌ **Unknown.** Could be replaced by an embedded chart. |
| **Pinecone** | **Not a processor of personal data** | Stores public guideline documents only | Not needed for personal data |

**International transfers:** all US vendors receive data from the EU. Mechanism:
- the **EU-US Data Privacy Framework (adequacy decision)** for vendors that are certified (check each one on the DPF list)
- otherwise **Standard Contractual Clauses** (controller-to-processor or processor-to-processor module) plus a transfer impact assessment

**Status today: not checked for any vendor.**

---

## Phase 3 - Lawful basis assessment

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| P1: Deliver the report by email | **Contract (Art. 6(1)(b))** | The user requests the report, and sending it to their email is necessary to provide the service. *(If the email belongs to an employee of a client company, the client relies on legitimate interests and I act as processor.)* | No |
| P2: Measure visibility and collect brand news (incidental names of people) | **Legitimate interests (Art. 6(1)(f))** | Competitive brand analysis is a normal business interest. The names are only incidental (see LIA below). | ⚠️ Yes, confirm Art. 14 information duties |
| P3: Generate the report with OpenAI | **Legitimate interests (Art. 6(1)(f))** | Same data and interest as P2. The LLM is the means of writing the report. | No, if the minimisation below is applied |
| P4: Fact-check the report (Render) | **Legitimate interests (Art. 6(1)(f))** | Checking accuracy protects both the client and the people named. | No |
| P5: Execution logs for troubleshooting | **Legitimate interests (Art. 6(1)(f))** | Running a reliable service needs short-term logs. | No, if retention is limited |
| P6 (planned): Weekly reports and history log | **Contract (Art. 6(1)(b))** if the user subscribes to recurring reports; otherwise **no valid basis** | The email must not be reused without the user asking for recurring reports. | ⚠️ Yes, decide before building |
| Personal brands (a person entered as "brand") | **TBD - legal review** | Measuring one person's online visibility is closer to profiling an individual than to brand analysis. | ✅ **Yes** |

**Legitimate Interests Assessment (P2–P5: brand analysis with incidental personal data)**

1. **Is the interest legitimate?** **Yes.** The client needs to know how visible its brand is on Google and in AI answers compared with competitors, to plan marketing. This is a lawful, concrete business interest.
2. **Is the processing necessary?** **Only partly, as currently built.** Brand-level data is necessary. **People's names are not**: the analysis works on brand mentions, rankings and headlines. A less intrusive design exists: **remove author names and personal details from news and snippets before they are sent to OpenAI**, and exclude personal brands. With that change, the remaining personal data is minimal.
3. **Do the individual's interests override?** **No, once minimised.** The data is public and professional (journalists, executives). It is used for analysis of companies, not of the people, and no decisions are made about them. Expected impact is low. Without minimisation, people would not reasonably expect their names to be sent to several US AI and API services for a competitor report, so the balance is weaker.

**Result:** legitimate interests is **valid for P2–P5 on the condition that names are removed (minimisation) and log retention is limited**. Article 14 (informing people whose data comes from third parties) likely falls under the **disproportionate-effort exception (Art. 14(5)(b))**, because I cannot contact every journalist named. This must be documented, and the LIA must be published or available on request. **This is flagged for legal review.**

---

## Phase 4 - Risk and rights analysis

**Special category data (Article 9)**
The system does not collect or infer special-category data. However, news text about named executives can incidentally contain health, political or religious information, and that could be copied into a report. No Article 9 condition clearly applies: "manifestly made public by the data subject" (Art. 9(2)(e)) does not fit journalist reporting about someone. So the safe approach is to **remove person-level details before the LLM step** and instruct the report writer not to mention individuals' personal circumstances.

**Automated decision-making (Article 22)**
**No.** The system scores and ranks **brands**, not people, and only recommends SEO actions. A marketing lead reads the report and decides what to do. Even for a personal brand, a visibility score has no legal or similarly significant effect on that person. So Article 22 does not apply, and no Article 22 safeguards are required.

**DPIA trigger (EDPB nine criteria)**

| Criterion | Applies? |
|---|---|
| Evaluation or scoring of people | ❌ No. It scores brands. ⚠️ Partial edge case: personal brands |
| Automated decision with significant effects | ❌ No |
| Systematic monitoring | ❌ No, for now. ⚠️ The planned weekly runs would monitor brands, not people |
| Special category data at scale | ❌ No |
| Large-scale processing | ❌ No. A few emails and incidental names per run |
| Matching or combining datasets | ✅ Yes, Google + AI answers + news are combined (though about brands) |
| Vulnerable data subjects | ❌ No |
| Innovative technology | ✅ Yes, an LLM agent with RAG and an LLM fact-checker |
| Transfers preventing rights exercise | ❌ No |

**Result:** two criteria apply on paper, but both concern **company data**, and the personal data involved is minimal and incidental. My assessment is that **a full DPIA is not required**, but a **written DPIA screening note** should document this reasoning. If personal-brand analysis or the weekly monitoring is added, I would re-screen. **This should be confirmed by a DPO.**

**Data subject rights friction**
- **Right of access (Art. 15):** a requester could ask what is stored about them. n8n executions are saved by default and searchable by email, so I *could* answer, but there is **no documented process**, and the data also sits with vendors. **Partly supported.**
- **Right to erasure (Art. 17):** I can delete n8n executions, but **not** emails already sent, data OpenAI keeps for up to 30 days, or vendor logs. **Partly supported, with known limits.**
- **Right to object (Art. 21):** a journalist or executive could object to their name being processed. There is no way to exclude a specific person today. **Not supported** until name-stripping is built, which would make the point largely irrelevant.

---

## Phase 5 - Law stacking check

| Law | Check |
|---|---|
| **AI Act** | **Minimal risk** (see my AI Act self-audit), with a **possible Article 50(2)** duty to mark AI-generated report text. The AI Act adds two things GDPR doesn't cover: **AI-generated content marking** and **AI literacy (Art. 4)**. Neither is about personal data. |
| **ePrivacy** | **Mostly not triggered.** The system sets no tracking cookies or pixels and doesn't read the content of anyone's communications. One flag: the **QuickChart image** in the email loads from an external server, which reveals the recipient's IP and the open time to QuickChart. That is not tracking by me, but it is avoidable. Embed the chart as an attachment instead. |
| **Data Act** | **Not applicable.** There is no connected product or IoT data. Cloud switching rules would only matter if a client wanted to move the service between cloud providers. |

---

## Phase 6 - Compliance memo

**To:** Data Protection Officer, BrightCart GmbH (fictional client)
**From:** Barsha Mishra, AI Consultant
**Date:** 17 November 2026
**Re:** GDPR review - AI Search Visibility Agent

**Bottom line: Proceed with conditions.** The agent mainly analyses companies, not people, so the privacy risk is low. However, it currently sends small amounts of personal data to US services without contracts, clear retention or a privacy notice, and that must be fixed before client use.

**What personal data is involved:** your team member's email address, and names of people that appear in news articles and search results (journalists, executives). The system makes no decisions about any person.

**Top three actions, in this order**

1. **Put contracts in place before any client data flows.** Sign a data processing agreement between BrightCart and me, and accept or sign DPAs with OpenAI, Render, n8n and the news and search providers. Check each US vendor's Data Privacy Framework certification, and use Standard Contractual Clauses where it is missing. Replace the personal Gmail sender with a business email service covered by a DPA.
2. **Remove what isn't needed.** Before data reaches the AI model, strip journalists' and individuals' names and personal details from news and search results. Do not use the tool to analyse individuals' "personal brands". Set n8n execution logs to delete automatically after 14 days.
3. **Document and inform.** Add a short privacy notice to the request form. Create a record of processing, the written legitimate interests assessment, and a DPIA screening note explaining why a full DPIA is not needed. Do not reuse the email address for weekly reports unless the user subscribes.

**Residual risks, even after these steps**

- **The AI may name people anyway.** OpenAI's answers can mention executives or founders from the model's own knowledge, and name-stripping cannot fully control this.
- **US vendor retention and access.** OpenAI keeps API data for a limited period for abuse monitoring, and US authorities' access remains a legal risk, especially if the Data Privacy Framework is struck down.
- **Sent reports are out of our control.** Once delivered, reports can be forwarded, and erasure requests cannot reach copies in recipients' inboxes.

**What this memo is not:** this is a first-pass consulting assessment. It is not a legal opinion, not a DPIA and not a certification. Please have legal counsel confirm the lawful-basis choices, especially for legitimate interests and Article 14 information duties, before relying on it for compliance decisions.

---

## CFU 4 - Verify: the accountability test

**Could I demonstrate compliance to a regulator using only my current project documentation?** **No.**

| Document a regulator could ask for | Exists? | Note |
|---|---|---|
| System and architecture description | ✅ Yes | README, workflow diagram, `stack_decision.md` |
| List of data sources | ✅ Partly | README lists the APIs. `rag_docs/sources.md` lists the RAG documents. |
| Record of processing activities (Art. 30) | ❌ Missing | |
| Privacy notice (Art. 13/14) | ❌ Missing | The form has no notice |
| Legitimate interests assessment | ❌ Missing | First draft is in this audit |
| DPIA or DPIA screening note | ❌ Missing | First reasoning is in this audit |
| DPAs with vendors | ❌ Missing / unconfirmed | |
| Transfer mechanism records (DPF / SCCs) | ❌ Missing | |
| Retention schedule | ❌ Missing | n8n uses default settings |
| Data subject request procedure | ❌ Missing | |
| Breach response procedure (72 hours) | ❌ Missing | |

**What this tells me:** my documentation explains *how the system works* very well, but nothing explains *how personal data is protected*. Accountability (Art. 5(2)) means the controller must be able to **show** compliance, and right now I could only describe it.

---

## Reinforce

**Revisiting a TBD: personal brands**
To advise on whether my agent may analyse a person's "personal brand" (e.g. a freelance consultant), a lawyer would need:
- the exact use case (who requests it, and whether the person is told)
- what data is collected about the person and how long it is kept
- whether results could affect the person's business, e.g. a client choosing between freelancers
- whether I could detect personal names in the form and block or warn

**What I could prepare in advance:** a one-page data flow for a personal-brand run, example outputs, and a proposed form warning. In practice, the simplest path is to **exclude personal brands** from the service's intended use.

---

## Stretch - Data protection by design checklist

**Highest-risk processing activity:** collecting news and search data and sending it, including people's names, to OpenAI for report writing.

| Design principle | Current state of my system | Pass / Fail / Unknown |
|---|---|---|
| Data minimisation | Full news text and snippets, including author names, are sent to OpenAI | **Fail** |
| Purpose binding | Data is only used to build the report, but nothing technically prevents reuse (e.g. the planned history log) | **Fail** |
| Access controls | Only I can access n8n, Render and the API keys. Keys are in n8n credentials, not in code. | **Pass** (prototype) |
| Retention enforcement | n8n default execution saving, no automatic deletion | **Fail** |
| Subject rights workflow | No documented process. Executions are searchable manually. | **Unknown** |
| Incident response | No breach detection or 72-hour notification process | **Fail** |

**What needs to change:**
- Add a "remove personal names" step (a code node) before the OpenAI calls.
- Keep the planned history log to brand-level data only, with no emails.
- Set n8n execution data to auto-delete after 14 days, and stop saving successful executions.
- Write a one-page data subject request procedure: search n8n by email, delete it, and request deletion from vendors.
- Write a short breach plan: who checks the vendor status pages and n8n alerts, and how the client's DPO is told within 24 hours, so the client can meet the 72-hour deadline.
