# GDPR self-audit — Editorial research agent (Project 3)

**Basis:** [`data_processing_brief_editorial_agent.md`](data_processing_brief_editorial_agent.md); code at commit `3939562`; the 20 saved runs (10–13 Nov 2026).
**Tags:** **[V]** verified in code or run files · **[D]** declared in project docs · **[A]** inference or assumption · **[NC]** not checked.
**Scope note:** the founder is building the agent **for his own future business**. That is a professional activity, so the household exemption (Art. 2(2)(c)) does not apply [A, strong]. The GDPR applies even though the project is a prototype.

## CFU 1 — Recognize

- **Categories:**
  - identity and professional or biographical data of authors;
  - data about third persons mentioned in books and articles;
  - social-media profile URLs;
  - free-text queries;
  - LLM-generated statements about authors' works.
- **Art. 9:** inferable, incidental and not targeted. Political opinions, and possibly health data, of a real person described in a non-fiction book appear in retrieved snippets saved in 7 evidence files [V].
- **EU border:** **likely**. Each run sends author names and retrieved text to US-based providers (Tavily, Google) [A]. A provider's nationality alone does not prove a transfer. Hosting regions and mechanisms are not documented [NC].

## Phase 1 — Personal data inventory (one row per purpose)

| Data category | Source | Purpose | Retention (known / estimated / unknown) | Crosses EU border? |
|---|---|---|---|---|
| Author name, bibliographic data | Bookseller input; Open Library; Google Books | F1 Research the author's works | Local evidence: **unknown** (no rule; kept since 10 Nov) [V]. Providers' logs: **unknown** [NC] | Likely: Open Library and Google (USA) [A] |
| Author biography, interviews, press, social URLs | Tavily web results | F1 Research and context | **Unknown** (no rule) [V] | Likely: Tavily, USA [V company; region NC] |
| Same data + publisher page text (≤ 4,000 chars) + snippets | Retrieved sources | **F2** Gemini describes and judges books | At Google: free tier, content **used to improve Google products**; duration **unknown** [V terms / NC duration] | Likely [A] |
| Third persons (incl. inferable Art. 9 data) in snippets | Tavily results | Not a purpose: **incidental** to F1/F2 | **Unknown**; stored in full in evidence JSON [V] | Likely [A] |
| All of the above | Agent output | F3 Local audit trail (JSON + dossier) | **Unknown**, indefinite [V] | No (laptop) [A] |
| All of the above | Agent output | **F4 Public demo / portfolio on GitHub** | **Unknown**; also in git history and any forks [V] | GitHub (USA) [A] |
| Bookseller's free-text query | Bookseller | F1, and sent to Tavily | Same as F3/F4 [V] | Likely [A] |
| (Planned) other bookshops' profiles and queries | Pilot bookshops | F5 Pilot [D] | **Unknown** | Unknown |

**Purpose-limitation flags (the most common failure mode):**
- **F4.** Texts published by newspapers and publishers to inform readers are **republished in bulk on GitHub** for a portfolio. This includes snippets about a third person in a sensitive context. It is a new purpose and hard to reconcile with the original publication context (Art. 6(4) test not done).
- **F2 (free tier).** Sending retrieved text to Google's **unpaid** service means Google may reuse it for **its own** product improvement. That further use was never part of the bookshop's purpose.

## Phase 2 — Role map

| Entity | Role (GDPR) | Processing activity | DPA in place? |
|---|---|---|---|
| **Client** = the founder as *La Insumisa* (the user) | **Controller** [A, strong] | Decides why authors are researched and which tools to use | n/a |
| **You / your team** = the same founder as builder; Codex and Claude as development tools | Same controller. Codex/Claude read the public repo during development [A] | Building, testing, storing runs | No (developer tool terms only) [NC] |
| **Google — Gemini API, free tier** | **Independent controller** for its own reuse of content under the unpaid terms [V terms]; **processor** only on Paid Services under Google's data processing terms [A] | Generation; product improvement | **No DPA for the free tier** [V: terms] |
| **Tavily** (AlphaAI Technologies Inc., USA) | **TBD.** Processor for API queries or independent controller. Tavily calls itself controller of its search index [V docs] | Web search on queries containing names | **Not found** [NC] |
| **Google Books API** | Likely independent controller (public API, key-based) [A] | ISBN lookup | No [NC] |
| **Open Library / Internet Archive** | Independent controller of its own logs [A] | Author and ISBN lookup | No; none offered for the public API [A] |
| **GitHub** (Microsoft) | Hosting provider for content the founder **chose to publish**. The founder is controller of the publication [A] | Public hosting of evidence | GitHub's standard terms only [NC] |
| **Future pilot bookshops** [D] | Each bookshop = controller. The founder = **processor** if he runs the agent for them (Art. 28 DPA needed) | Research for their catalogue | Not drafted |

**International transfers:** none documented [NC].
- If Tavily or Google process the data in the US, the founder needs either an adequacy route (EU–US Data Privacy Framework, **only** if the recipient is certified — not checked here) or SCCs.
- The DPF is valid but under appeal (C‑703/25 P).

## Phase 3 — Lawful basis assessment (Art. 6)

| Purpose | Proposed basis | One-line justification | Legal review? |
|---|---|---|---|
| F1 Research authors' works | **6(1)(f) legitimate interests** | Booksellers have a clear interest in researching published authors' professional output; the data is public and low-impact. LIA below | No, for authors' professional data. **Yes** for incidental third-person / Art. 9 data |
| F2 Gemini description and judging | 6(1)(f) **only on a paid tier with Google as processor**; on the free tier **`TBD — legal review`** | Disclosure to a provider that reuses the content for its own purposes weighs against the balancing test | **Yes** |
| F3 Local audit trail | 6(1)(f) | Traceability and debugging are legitimate. Necessity requires minimised storage (URLs + short extracts) and a retention limit | No, once minimised |
| F4 Public GitHub publication | **`TBD — legal review`** (likely no adequate basis as it stands) | A portfolio interest does not need real third-person snippets; redacted or synthetic samples would do | **Yes** |
| F5 Pilot | `TBD — legal review` | Roles, contracts and data are not yet defined | **Yes** |

**LIA for F1 and F2 (three-part test)**

1. **Legitimate interest?** Yes. The concrete need is deciding which of an author's books suit the shop, with sources. This is a lawful commercial interest linked to the freedom to conduct a business.
2. **Necessary?** Partly.
   - The author's name and bibliographic data are necessary: Open Library searches by author.
   - **Not necessary:** storing full web snippets, biographies of third persons and social-profile URLs. Sending them to a provider that reuses them is not necessary either.
   - Less intrusive options: keep only URLs and the fields used, filter non-bibliographic text, and use a paid, no-reuse LLM tier.
3. **Balancing?** For authors in their **professional capacity**, the balance favours the bookshop: published works, low impact, and research by booksellers is reasonably expected. For **third persons in sensitive contexts**, and for reuse by Google, it does **not**.

**Result:** F1 passes once minimised. F2 passes only with a paid tier. F4 fails as it stands → `TBD — legal review`.

## Phase 4 — Risk and rights

**Special category data (Art. 9).** Present incidentally. Retrieved text about a real person (a non-fiction subject) reveals political militancy, imprisonment and torture. It is stored in 7 evidence files and published on GitHub [V].
- A possible condition is 9(2)(e), data *manifestly made public by the data subject*, if that person made the facts public herself. That is a legal judgement → **`TBD — legal review`**.
- **The safer design:** do not persist or publish raw snippets.

**Automated decision-making (Art. 22).** Not engaged [A, strong].
- The agent judges **books** against a shop profile. It does not decide about people, and there is no legal or similarly significant effect on an author.
- The human review is only the planned workflow ("El librero decide"). It is not enforced or logged [V]. That matters for quality and for the AI Act, not for Art. 22.

**DPIA trigger (nine EDPB criteria).**

| # | Criterion | Applies? |
|---|---|---|
| 1 | Evaluation or scoring | No, of people (books are scored) |
| 2 | Automated decisions with legal or similar effect | No |
| 3 | Systematic monitoring | No |
| 4 | Sensitive data | Incidental only |
| 5 | Large scale | No: 20 runs, 1 author [V] |
| 6 | **Matching or combining datasets** | **Yes**: web + Open Library + Google Books + publisher pages about the same author [V] |
| 7 | Vulnerable data subjects | No |
| 8 | **Innovative technology** | **Yes**: LLM judge |
| 9 | Prevents exercising a right | No |

Two criteria apply: under the course's rule of thumb a DPIA would be *generally required*. **A risk-based reading points the other way:** public figures in a professional context, at very small scale, make a "likely high risk" (Art. 35(1)) doubtful.
- **Position:** do a documented **DPIA screening** now.
- Do a **full DPIA before the pilot**, or earlier if Art. 9 text keeps being stored. → `TBD — legal review` on whether a full DPIA is mandatory today.

**Data subject rights friction.**
- **Access (Art. 15):** feasible. Evidence is plain JSON, searchable by name [V]. No procedure exists [NC].
- **Erasure (Art. 17):** local files can be deleted. **Not feasible** for copies in the public git history and forks, or content already sent to Gemini's free tier.
- **Objection (Art. 21, needed because 6(1)(f) is the basis):** there is **no way to exclude a person** from future runs (no blocklist) [V: no such feature].
- **Information (Art. 14):** authors were never told. Art. 14(5)(b) (disproportionate effort) may apply, but it requires documenting that assessment and publishing the information, e.g. on the shop's website → `TBD — legal review`.
- **Timely response (one month):** not possible today for erasure. Possible for access once a procedure exists.

## Phase 5 — Law stacking

- **AI Act cross-check:** **minimal risk, provisional.** The agent is not Art. 5, not Annex III and not Annex I. There is an open Art. 50(2) question on marking the synopsis written by Gemini. Art. 4 (AI literacy) applies once the system is in service. The AI Act adds the transparency duty, which GDPR does not cover. The recruitment high-risk regime **does not apply** to this agent.
- **ePrivacy check:** **N/A.** It is a command-line tool: no cookies, tracking, device access or electronic-communications content [V].
- **Data Act check:** **N/A.** No connected product, IoT data or cloud-switching question.

## CFU 4 — Accountability test: could we show compliance to a regulator today?

| Document | Exists? | Evidence |
|---|---|---|
| Record of processing (ROPA, Art. 30) | **No** | Nothing in the repo [V: no GDPR/privacy file found]. The <250-employee exemption is doubtful if processing is regular or includes Art. 9 data |
| Privacy notice / Art. 14 assessment | **No** | [V] |
| LIA | **No** (drafted for the first time in this lab) | — |
| DPIA or DPIA screening | **No** (screening drafted in this lab) | — |
| DPAs (Google paid, Tavily, future pilot) | **No** | Free-tier terms only [V] |
| Transfer assessment / mechanism | **No** | [NC] |
| Retention schedule | **No** | Evidence kept since 10 Nov, no rule [V] |
| Security measures | **Partial** | `.env` is in `.gitignore`; API keys are redacted in error messages (`graph.py` l. 85) [V]. The Google Books key travels in the URL [V] |
| Breach procedure (72 h) | **No** | [V] |
| Record of the human decision | **No** | [V] |

**Verdict:** **no.** Apart from partial security measures, the project could not demonstrate compliance with its current documentation. What exists is technical evidence (tests and run logs), not accountability documentation.
