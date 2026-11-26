# GDPR audit worksheet - Menohelp (Phases 1-5)

Builds on [`01-data-processing-brief-menohelp.md`](./01-data-processing-brief-menohelp.md). Client: Wechselweise Coaching GmbH (**fictional**). Legal baseline: GDPR as in force; the proposed Digital Omnibus changes to GDPR are not relied on. **Not legal advice.** ⚖️ = needs counsel.

## Phase 1: Personal data inventory

One row per purpose (purpose limitation applies per processing activity).

| # | Data category | Source | Purpose | Retention (known / estimated) | Crosses EU border? |
|---|---|---|---|---|---|
| 1 | Cycle log (dates, lengths, flow, age); full Clue export on arrival | The woman (export from her cycle app) | P1 Calculate cycle stats and flags | **Known:** 1 h in memory on my server; Streamlit session while the tab is open | No, if hosted in the EU. Yes on Streamlit Cloud (US) |
| 2 | Cycle stats and flags (derived) | My code | P3 Write the report via OpenAI | **Known:** 1 h on my server. **Estimated:** up to 30 days at OpenAI | **Yes** (OpenAI, US) |
| 3 | Lab PDF (name, address, DOB, all results) | The woman (lab report) | P2 Extract allow-listed values | **Known:** PDF bytes are not stored by my API; held in Streamlit session memory while the tab is open | Depends on host |
| 4 | Allow-listed lab values, draw date, cycle day, age | Parsed in code, confirmed by the woman | P1 Flags against printed ranges and age norms | **Known:** 1 h in memory | Depends on host |
| 5 | Same lab values | As above | P3 Write the report via OpenAI | **Estimated:** up to 30 days at OpenAI | **Yes** |
| 6 | Questionnaire (symptoms incl. mood and sexuality, HRT, surgery, free text) | The woman | P1 Triage and findings (code) | **Known:** session only | Depends on host |
| 7 | Same questionnaire, incl. free text | The woman | P3 Write the report via OpenAI | **Estimated:** up to 30 days at OpenAI | **Yes** |
| 8 | Report text + chart (inferred health attributes) | OpenAI + my code | P4 Show on screen | Session only | Depends on host |
| 9 | Report + recipient email address | The woman types the address | P4 Email delivery via Resend | **Unknown:** Resend log retention not set; recipient inbox indefinitely | **Yes** (Resend, US default) |
| 10 | Report of a coaching client | Coach uploads client data | P5 Coach prepares a consultation (planned) | **Unknown:** depends on what the coach keeps | Yes (as rows 2, 5, 7) |
| 11 | Pilot feedback (ratings, comments) | Pilot participants | P6 Evaluate the pilot (planned) | **Estimated:** end of pilot + 3 months | Depends on form tool |
| 12 | Run metadata (run id, timestamp, prompt version, check results; **no health values**) | My code | P7 Security, incident investigation, abuse prevention | **Proposed:** 6 months (not built yet) | No, if hosted in the EU |
| 13 | IP address, request logs | Hosting provider | P7 Security, rate limiting | **Unknown:** host default | Depends on host |
| 14 | Showcase report built on a real person's data | Development data | P8 Public demo in the GitHub repo, slides, recording | **Indefinite**: public, forkable, in Git history | **Yes** (GitHub, US) |
| 15 | Kaggle cycle datasets | Kaggle publishers | P8 Demo data | Indefinite in repo | Yes (GitHub) |

### Purpose-limitation flags 🚩

| Flag | What changed | Assessment |
|---|---|---|
| **A. Clue / lab data re-purposed** | Collected by the cycle app (tracking) and the lab (medical care). Menohelp uses it for perimenopause analysis. | **Not a breach in itself:** the woman brings her own copy, so Menohelp is a **new collection** with its own purpose and needs its own basis and notice. It cannot rely on Clue's or the lab's consent. Minimisation issue: the whole Clue export (incl. sex life) arrives when only `period` rows are needed. |
| **B. Coaching client data fed to AI** | A coach's client shared data for coaching. Uploading it to Menohelp adds AI processing and a US transfer. | **New processing activity.** It needs the client's explicit consent for this step, not just the coaching contract. |
| **C. Real data → public showcase** 🔴 | The "real data" report (cycle, blood values, symptoms of one woman, incl. her AMH for her age) was generated for testing and is now **published** in a public repo, slides and a recording. | **Incompatible further use** unless that person explicitly consented to publication. The household exemption does not cover publishing to an open audience (CJEU *Lindqvist*, C-101/01). Fix now: confirm whose data it is and her written consent, or replace it with synthetic data and purge Git history. **TBD - legal review** if consent exists but was informal. |
| **D. Kaggle research data → product demo** | Published for research, one set under CC BY-NC. | If the rows are real survey data, using them in a commercial product is further processing (Art 6(4)) and breaks the NC licence. Confirm they are synthetic or anonymous. **TBD - legal review.** |
| **E. Temptation: reports → product improvement** | Not built. Tuning prompts on pilot reports, or training the dropped prediction model on user data. | **Not permitted** under the report consent. Needs a separate, optional consent, or synthetic data only. |

## Phase 2: Role map

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| **Wechselweise Coaching GmbH** (client) | **Controller** | Decides to offer Menohelp to customers and coaches, why and on what terms (P1-P7) | n/a (it is the controller). Needs an Art 28 DPA **with me**. |
| **Freelance coaches** (Sprint 2) | **Joint controller** with Wechselweise, or separate controller per client ⚖️ | Upload client data, read the report, use it in sessions (P5) | **No.** If joint: an Art 26 arrangement. If coaches are employees, they are part of the controller. **TBD - legal review.** |
| **Me / my team (Ben Mayer)** | **Processor** for Wechselweise when I host and run Menohelp for them. **Controller** for my own development and demo use (P8), and controller of the showcase report | Build, host and operate the pipeline | **No.** Art 28 DPA with Wechselweise needed before any customer data flows. Note: in the AI Act self-audit I am the *provider*. AI Act and GDPR roles don't map 1:1. |
| **OpenAI** (Ireland Ltd for EEA customers; processing by OpenAI, L.L.C., US) | **Sub-processor** | Generates report text; embeds fixed retrieval queries (P3) | **Not executed** ⚖️ (OpenAI offers a standard DPA; I have not signed it). Wechselweise must authorise it as a sub-processor (Art 28(2)). |
| **Resend** (US) | **Sub-processor** | Sends the report email (P4) | **Not executed.** Resend offers a DPA. |
| **Hosting** (Render or Streamlit Community Cloud) | **Sub-processor** | Runs the app; request logs (P7) | **Not executed**; host not chosen. |
| **Supabase** | **Not a processor today** (no user data). Becomes a sub-processor if accounts and stored reports are added (GTM plan) | Stores coaching chunks | Not needed now; required before persistence. |
| **GitHub** (US) | Hosting for my public repo; for the showcase report I am the controller who published it | P8 | n/a. The fix is removal, not a DPA. |
| **Cycle app, lab, Kaggle publishers** | **Independent controllers** of their own copies | Original collection | n/a. No data flows from them to Menohelp. |
| **Report recipient** (her doctor, by email) | **Independent controller** (doctor) or household use | Receives the report at the woman's request | n/a |

### International transfers

| Flow | Mechanism today | Recommended |
|---|---|---|
| → OpenAI (US) | **None documented.** Possible: EU-US Data Privacy Framework (Art 45) *only if* the receiving OpenAI entity is on the active DPF list ⚖️; otherwise SCCs Module 3 (processor → sub-processor) in OpenAI's DPA + a transfer impact assessment | **Avoid the transfer:** OpenAI EU data residency with zero data retention ⚖️ (availability per project to confirm). Otherwise DPF/SCCs + TIA. |
| → Resend (US) | None documented | EU sending region if available for the domain ⚖️, else DPF/SCCs + TIA |
| → Host | None | Choose an EU region (e.g. Render Frankfurt). Avoid Streamlit Community Cloud for real users. |
| → GitHub (showcase) | None, and none can fix a public publication | Remove the data |

## Phase 3: Lawful basis assessment

Every purpose that touches health data needs **two** bases: one from Art 6 and a condition from Art 9(2). For a consumer wellness service, the only realistic Art 9 condition is **9(2)(a) explicit consent**. 9(2)(h) (health care) needs a health professional under a secrecy duty (Art 9(3)); coaches generally aren't one.

| Purpose | Proposed basis (Art 6 + Art 9) | One-line justification | Legal review? |
|---|---|---|---|
| **P1** Cycle stats, lab flags, triage (code) | **6(1)(b)** contract + **9(2)(a)** explicit consent | She asked for a report, and the analysis is the service itself; the Art 9 condition must be explicit consent. | No |
| **P2** Parse the full lab PDF | **6(1)(b)** + **9(2)(a)** | Reading the PDF is necessary to extract her values; the allow-list keeps the rest out. | No |
| **P3** Send findings, labs, symptoms and free text to OpenAI | **6(1)(b)** + **9(2)(a)**; consent must name the US provider and the transfer | Writing the text is part of the service; she must know an external AI provider sees her values. | **Yes:** whether one consent can cover both analysis and transfer, and the transfer mechanism ⚖️ |
| **P4** Email the report | **6(1)(b)** at her request + **9(2)(a)** | She chooses to send it; Art 32 security still applies to the channel. | No |
| **P5** Coach prepares a consultation | **6(1)(b)** coaching contract + **9(2)(a)** collected by the coach | Separate, unbundled consent; the client must be able to refuse and still be coached (Art 7(4)). | **TBD - legal review** (coach role; 9(2)(h) if the coach is a licensed health professional) |
| **P6** Pilot feedback | **6(1)(a)** consent | Optional and separate from the report; keep health values out of the form. | No |
| **P7** Metadata-only run log, abuse prevention, request logs | **6(1)(f)** legitimate interests (LIA below) | Needed to investigate a harmful report or an attack; contains no health values. | No, if the log really holds none. DPO to confirm. |
| **P8** Showcase report with real data, public | **6(1)(a) + 9(2)(a)** explicit consent of that person, **or no basis** | Publishing someone's health data needs her explicit agreement; nothing else fits. | **TBD - legal review** |
| **P8** Kaggle demo data | **6(1)(f)** if not anonymous ⚖️; none needed if synthetic | Licence and Art 6(4) compatibility decide it. | **TBD - legal review** |

**Why not legitimate interests or consent for P1-P4 under Art 6?** Contract fits: the processing is objectively necessary to deliver the report she ordered (EDPB Guidelines 2/2019). Art 6 consent would also work but adds nothing, since Art 9 consent is needed anyway.

### Legitimate interests assessment: P7 (metadata run log and security logs)

| Test | Finding |
|---|---|
| **1. Legitimate interest?** | **Yes.** If a woman says a report told her something harmful, the controller must be able to reconstruct which sources, prompt version and guardrail result produced it (Art 5(2) accountability, Art 32 security). Rate-limiting and request logs prevent abuse of the email feature. |
| **2. Necessary?** | **Yes, in minimised form.** Without any log, an incident can't be investigated. The less intrusive option is chosen: run id, timestamp, model and prompt versions, retrieved chunk ids, check results, retry count. **No health values, no report text, no email address.** IP logs kept at host minimum. |
| **3. Balancing?** | **Passes.** The log can't be linked to a named person, holds no health data, and has a 6-month limit. Women expect a health service to investigate complaints. Risk to them is low, the benefit (safety) is high. They must be told in the privacy notice and can object (Art 21). |
| **Result** | Legitimate interests apply. If the design ever adds health values or report text to the log, the LIA fails and must be redone. |

## Phase 4: Risk and rights analysis

**Special category data (Art 9).**
Health data is the core input, and data concerning **sex life** sits in the symptom ratings and the raw Clue export. The output infers more: reproductive status, a possibly low egg reserve, low-mood red flags. The applicable condition is **Art 9(2)(a) explicit consent**, which today **does not exist**: upload starts processing at once. Germany adds specific safeguards for special-category data (§22(2) BDSG) ⚖️.

**Automated decision-making (Art 22).**
Art 22 **does not apply**: Menohelp makes no decision about the woman. No one grants or refuses her anything because of the report, and she decides what to do with it. It **is profiling** of health, though, and no human reviews the text before she reads it. That makes **accuracy (Art 5(1)(d))** and transparency the real duties. Safeguards in place: code computes every number, a checker blocks mismatched numbers, a guardrail blocks diagnoses and dose advice, and every report says "not medical advice". **Watch-out:** if Wechselweise ever used the report to accept or refuse clients, or to price a programme, Art 22 and Art 22(4) (special-category data) would apply.

**DPIA trigger (EDPB WP248 criteria).**

| # | Criterion | Applies? |
|---|---|---|
| 1 | Evaluation or scoring | ✅ Profiles health ("cycle irregular", "low for age") |
| 2 | Automated decision with legal/similar effect | ❌ No decision |
| 3 | Systematic monitoring | ❌ One-off upload (⚠️ if accounts keep data over time) |
| 4 | Sensitive data or highly personal data | ✅ Health and sex life |
| 5 | Large scale | ❌ Pilot of 5-8 women (⚠️ at launch) |
| 6 | Matching or combining datasets | ✅ Cycle app + lab report + questionnaire, combined by design |
| 7 | Vulnerable data subjects | ⚠️ Women worried about symptoms, some with low mood; coach-client imbalance |
| 8 | Innovative technology | ✅ LLM-written health text |
| 9 | Processing prevents exercise of rights or use of a service | ❌ |

**Four criteria apply clearly, one partly, so a DPIA is required (Art 35) before any real user's data is processed.**

**Data subject rights friction.**

| Right | Friction | Can the current design respond in time? |
|---|---|---|
| **Information (Art 13)** | The UI says **"Nothing is stored"**. True for my server after 1 h, but OpenAI may keep inputs for 30 days, Resend keeps logs, and the host logs requests. "The LLM never sees raw data" overstates it too: lab values, symptoms, age and free text do go to OpenAI. | **No.** There is no privacy notice, and the existing wording misleads. |
| **Access (Art 15)** | No accounts and no stored data, so after 1 h there is nothing to give, which is good. But I can't find her prompts at OpenAI either: they aren't tagged per person. | **Partly.** Answer is "we hold nothing, OpenAI may hold X for 30 days". That answer must be documented and true. |
| **Erasure (Art 17)** | Automatic on my side. Not possible on request at OpenAI within 30 days without zero data retention. An emailed report can't be recalled. The public showcase report survives in forks and Git history. | **Partly.** No training on user data, so no model-unlearning problem. ZDR closes the OpenAI gap. |
| **Rectification (Art 16)** | Misread lab values: she confirms each value before the report (good). Wrong statements in the AI text: she can only regenerate. | **Yes**, within the session. |
| **Withdraw consent / object to profiling (Art 7(3), Art 21)** | Under consent, she simply stops; under P7 (LI), she can object to logging. In coach use, refusing must not cost her the coaching. | **Yes** for individuals. **No** process yet for coach clients. |

## Phase 5: Law stacking check

- **AI Act cross-check:** **Limited risk** (Art 50), with an open high-risk route if Menohelp counts as MDR/IVDR medical-device software (Art 6(1) + Annex I) ⚖️, as in my AI Act self-audit. It adds duties GDPR doesn't have: **machine-readable marking** of AI-generated reports (Art 50(2)), an AI disclosure, and **AI literacy** for coaches (Art 4). GDPR already requires the transparency, accuracy and DPIA work.
- **ePrivacy check:** No analytics, pixels or marketing email today. Streamlit's session cookie and websocket are strictly necessary, so they are exempt from consent (ePrivacy Art 5(3), German §25(2) TDDDG). **Two flags:** (1) confirm Resend **open/click tracking is off**: a tracking pixel in a health-report email would need consent; (2) a Sprint 3 landing page with analytics would need a consent banner.
- **Data Act check:** **N/A today.** A cycle-tracking app isn't a connected product. It would become relevant if wearable import (temperature, heart rate) returns. Then the Data Act's user access right could even be the lawful route to get that data. Cloud switching (Ch. VI) is a contract lever when Wechselweise picks a host.
