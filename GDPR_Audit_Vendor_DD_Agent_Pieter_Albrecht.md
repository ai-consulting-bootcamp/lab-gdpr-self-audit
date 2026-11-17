# GDPR Audit — Vendor Due-Diligence Agent (Project 3)

**Author:** Pieter Albrecht · **Date:** 17 November 2026
**Status:** First-pass consulting assessment, not legal advice. Items marked *TBD — legal review* need a lawyer or DPO.
**Based on:** [data_processing_brief.md](data_processing_brief.md)

**Who is the "client"?** Two phases matter:
- **Now (bootcamp MVP):** I decide what the agent does and run it on real companies, so **I am the controller**.
- **GTM sprint 1 (pilot):** a design-partner law firm or notary runs vendor checks with it. **The firm is the controller**, and I become its **processor** if I host the agent, or just a software supplier if they run it themselves.

The memo is addressed to that pilot firm's DPO.

**Assumptions** (not confirmed): n8n runs locally; LangSmith tracing is on for all runs, default US region; Streamlit and the API run locally.

---

## CFU 1 — Recognize

| Question | Finding |
|---|---|
| **Categories of personal data** | (a) Sole-trader identity and registration data; (b) sanctioned individuals' data (names, aliases, DOB, nationality, listing reason); (c) people named in news (name, role, employer, allegations, charges, convictions); (d) LLM-generated statements about those people; (e) technical data: API key, Streamlit password, local server logs. |
| **Special-category data (Art. 9)?** | **Not targeted, but possible.** News can reveal health, religion or political views; if PEP screening is added (the report template already has a "Sanctions and PEP" heading), political roles enter the system. |
| **Criminal-offence data (Art. 10)?** | **Yes, this is the core risk.** Adverse media is largely about fraud, bribery, money laundering and sanctions evasion, often naming individuals. Art. 10 is stricter than Art. 9: processing is allowed only under official authority or where EU/member-state law authorises it. |
| **Crosses an EU border?** | **Yes.** OpenAI (US), LangSmith (US, assumed), Tavily (US, verify). |

---

## Phase 1 — Personal data inventory

| Data category | Source | Purpose(s) | Retention (known / estimated) | Crosses EU border? |
|---|---|---|---|---|
| Sole-trader name, address, KvK data | User input, KvK, GLEIF | P1 Identify vendor | Indefinite (in reports) | Yes: in prompts to OpenAI, LangSmith traces |
| Sole-trader data | as above | P4 Risk assessment & report | Indefinite | Yes |
| Sanctioned individuals' data | OpenSanctions bulk file | P2 Sanctions screening | Until next download (file replaced); matches kept in reports indefinitely | Matched names go to OpenAI and Tavily (enhanced review) |
| People named in news + allegations / convictions | Tavily (news sites) | P3 Adverse media research | In state during the run; then in reports, LangSmith, possibly `notes/` | Yes: Tavily, OpenAI, LangSmith |
| People named in news + allegations | as above | P4 Risk assessment & report | Indefinite | Yes |
| People named in news + allegations | as above | P5 Audit trail | Indefinite; "never overwrite" by design | No (local), unless committed to GitHub |
| All of the above | Full run traces | **P6 Debugging & evaluation (LangSmith)** ⚠️ | Plan default (verify) | Yes (US) |
| Report extracts with named people | Earlier runs | **P7 Testing, demo, portfolio** ⚠️ | Indefinite; possibly public on GitHub | Yes (GitHub) |
| API key, Streamlit password, local logs | User | Access control | Local only | No |

**⚠️ Purpose drift flags:**
- **P6:** traces are collected to debug, but the build guide plans to reuse them as a **LangSmith evaluation dataset**, which is a new purpose for data about real people.
- **P7:** reports produced as test runs are reused in **slides, screenshots and a public portfolio repo**. The people in them never had any connection to my bootcamp.
- **News articles** were published for journalism and are reused here for **profiling counterparties**. This can be compatible (Art. 6(4)), but it has to be assessed, not assumed.

---

## Phase 2 — Role map

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| Pilot firm (client) | **Controller** | Decides to check vendors and acts on the report | n/a |
| Me (Pieter) | **Controller** now; **processor** in a hosted pilot | Build, run, host, store reports | **No.** Needed with the firm if I host |
| OpenAI | **Processor** (sub-processor in a pilot) | LLM calls with evidence and names | **Not mine.** The API key belongs to Ironhack's account, so any OpenAI DPA is with Ironhack. The client has no contract with OpenAI. |
| LangChain (LangSmith) | Processor | Stores full traces | **No** (verify plan terms) |
| Tavily | Processor for queries | Web/news search | **No** (verify terms) |
| Pinecone | Processor, **no personal data** | Guidance vectors | Not needed for personal data (documented here) |
| n8n | None (assumed local) | Form → API | n/a |
| GLEIF, KvK, OpenSanctions, news publishers | **Independent controllers** (sources) | Publish the data | n/a. OpenSanctions has a **non-commercial licence**: a commercial pilot needs a paid licence (not GDPR, but a blocker) |

**International transfers:**
- **OpenAI (US):** check its EU-US Data Privacy Framework (DPF) certification and the transfer clauses in its DPA, or use an EU data-residency project if the account offers one.
- **LangSmith and Tavily (US):** DPF certification or SCCs + transfer impact assessment, **or** switch tracing to an EU instance / off.
- **For all three:** keep SCCs as a fallback, since the DPF is under appeal at the CJEU (C-703/25 P).

---

## Phase 3 — Lawful basis assessment

| Purpose | Proposed lawful basis | One-line justification | Legal review? |
|---|---|---|---|
| P1 Identify vendor | Legitimate interests (f) | Knowing who you contract with is a basic business need; registry data is public and expected. | No |
| P2 Sanctions screening | Legal obligation (c), fallback (f) | EU sanctions regulations and the Dutch Sanctiewet 1977 forbid making funds available to listed parties; screening is how a firm complies. The regulations prohibit the dealing but don't prescribe screening, hence the fallback. | **Yes** |
| P3 Adverse media research | Legitimate interests (f) **+ an Art. 10 condition** | See LIA below. The Art. 6 basis is workable; the **Art. 10 authorisation for criminal-offence data is the open question**. | **Yes — TBD legal review** |
| P4 Risk assessment & report | Legitimate interests (f) | Turns facts into a decision aid. Acceptable only with human decision-making and accurate attribution. | Yes (accuracy) |
| P5 Audit trail | Legal obligation (c) for sanctions records; (f) otherwise | A firm must be able to show it screened. Doesn't justify indefinite retention of named-person allegations. | Yes (retention) |
| P6 Debugging & eval (LangSmith) | Legitimate interests (f) — **fails as currently set up** | Debugging doesn't need full article texts about real people stored in the US indefinitely; masking or synthetic data would do. | **Yes — TBD** |
| P7 Testing, demo, portfolio | Legitimate interests (f) — **fails as currently set up** | My interest in showing my work is legitimate, but it doesn't need *real* people's alleged offences; anonymised examples achieve the same. | No: fix by anonymising |

**LIA for P3 (adverse media):**
1. **Legitimate interest?** Yes. Avoiding contracts with vendors involved in fraud, corruption or sanctions evasion protects the firm legally and reputationally, and is expected of Wwft-regulated firms.
2. **Necessary?** Partly. Company-level findings are necessary, but **storing individuals' names and allegations usually is not**. The report needs "a 2022 corruption case involving a regional export manager", not the person's name.
3. **Balancing?** Uncertain. The people named don't know about the processing (Art. 14 notice not given) and may be wrongly cast as wrongdoers (proven in testing). With minimisation, role classification and a short retention period the balance can tip in favour of the firm; **today it doesn't.**

→ **TBD — legal review**, mainly because of Art. 10. The Dutch implementing act (UAVG) contains exceptions for criminal data processed by private parties, and a lawyer needs to confirm which, if any, covers adverse-media screening of *suppliers*. Wwft due diligence formally covers *clients*, not suppliers.

---

## Phase 4 — Risk and rights analysis

**Special-category data (Art. 9).** Not targeted, but news articles can reveal health, religion or political views, and the LLM passes them on unfiltered. No Art. 9 condition applies to this use, so such content must be filtered out of findings. If PEP screening is added, political roles become systematic and need their own basis. **Criminal-offence data (Art. 10)** is the bigger issue: it is processed by design and needs explicit legal authorisation (see P3).

**Automated decision-making (Art. 22).** For companies Art. 22 doesn't apply; it protects natural persons only. For **sole traders** it can: a "Do not onboard" from a fully autonomous run, acted on without real review, is a solely automated decision with a significant effect (losing a contract). Today the "human in the loop" is only a sentence in my pitch ("it supports the officer"); the system neither requires nor records a human decision. **Safeguard needed:** a reviewer field and sign-off before any recommendation is final, plus a way for the vendor to respond.

**DPIA trigger (EDPB criteria):**
| # | Criterion | Applies? |
|---|---|---|
| 1 | Evaluation or scoring | ✅ Rates vendors, and indirectly the people linked to them |
| 2 | Automated decision with significant effect | ⚠️ Sole traders only |
| 3 | Systematic monitoring | ❌ now; ✅ once GTM sprint 3's scheduled re-screening is built |
| 4 | Sensitive / criminal-offence data | ✅ Art. 10 data by design |
| 5 | Large scale | ❌ MVP; ⚠️ in a commercial roll-out |
| 6 | Matching or combining datasets | ✅ Registry + sanctions + news + LLM inference |
| 7 | Vulnerable data subjects | ❌ |
| 8 | Innovative technology | ✅ Autonomous LLM agent |
| 9 | Prevents exercising a right / using a service | ⚠️ Sole traders denied a contract |

**4 clear + 3 partial → DPIA required before the pilot.** The Dutch DPA's list of processing that always needs a DPIA also covers blacklists and warning lists (verify the current list), which adverse-media screening comes close to.

**Data subject rights friction:**
- **Access (Art. 15):** a person named in a report asks "what do you hold on me?". Reports are files named by *company*, with no index by person. **Can't answer within 30 days without searching every file by hand.**
- **Rectification (Art. 16):** the ASML and Heineken victims were described as wrongdoers. The design rule "an audit trail must never overwrite itself" **clashes** with correcting inaccurate data. **No correction process exists.**
- **Erasure (Art. 17) and objection (Art. 21):** no retention rule, so data is kept indefinitely across the laptop, LangSmith and possibly GitHub. **Cannot support a timely erasure today.**
- **Information (Art. 14):** people named in news are never told. The "disproportionate effort" exception may apply, but it must be **documented**, which it isn't.

---

## Phase 5 — Law stacking check

- **AI Act:** **minimal risk**. Vendor due diligence isn't in Annex III (not employment, credit scoring of natural persons or law enforcement), and the agent isn't a chatbot facing the public. The only extra duty is **AI literacy (Art. 4)** for users. GPAI duties sit with OpenAI. It adds nothing material beyond GDPR here.
- **ePrivacy:** **mostly N/A.** No tracking cookies or pixels, and no content of electronic communications. Streamlit's session handling is strictly necessary. *Check* that `browser.gatherUsageStats = false` is set in `.streamlit/config.toml`, so Streamlit's own usage telemetry doesn't run in the user's browser.
- **Data Act:** **N/A.** No connected products and no cloud-switching data.

---

## CFU 4 — Verify: the accountability test

*Could I demonstrate compliance to a regulator with the documentation the project has today?* **No.**

**What exists:** the pipeline doc and README (data flows); `stack_decision.md`; per-report "Data limitations" sections and section 8 audit trails; LangSmith traces (evidence of what ran); `.env` keeps keys out of code.

**What is missing:** record of processing activities (Art. 30) · privacy notice / Art. 14 information or a documented exception · LIA · DPIA · Art. 10 legal basis assessment · DPAs with OpenAI (own account), LangSmith and Tavily · transfer impact assessment · retention schedule · rectification and access procedure · breach procedure · record of human decisions · commercial OpenSanctions licence.
