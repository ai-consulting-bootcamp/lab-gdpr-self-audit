# GDPR Audit Worksheet — School Book Order Bot (Project 3)

## Phase 1: Personal data inventory

| Data category | Source | Purpose(s) | Retention period | Crosses EU border? |
|---|---|---|---|---|
| Telegram/WhatsApp chat_id | School, via bot | a, b, d, e | **Assumed: indefinite — not currently defined.** No deletion/archival policy exists in the Google Sheet. Flagged as a gap. | No (deployments run on separate infrastructure) |
| Order content (school, class, book titles) | School, direct message | a, b, c, d, e | **Assumed: indefinite**, same as above — this is also the dataset purpose (e) queries against, which is part of why the purpose-drift flag matters. | No |
| Photo uploads (incidental content) | School, direct message | a only | **Assumed: not persisted** — images are processed transiently through the vision model and not stored as files; only extracted order text is retained. **This assumption should be verified against actual n8n workflow behavior before relying on it.** | No |

**Purpose-drift flag:** Order content originally collected to fulfill purposes (a)–(d) is now also used for purpose (e), a conversational Q&A feature added after the fact. Flagged for legal review under Phase 3.

## Phase 2: Role map

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| Book-order operator (father / India business; Anand / Germany operator) | Controller | Determines purposes and means of processing (what data is collected, how it's used) | N/A — is the controller |
| Anand (developer/operator) | Processor for India instance if operating on behalf of father's business; Controller for Germany instance if operating independently | Builds and maintains the workflow, has direct data access | **TBD — no formal DPA currently in place between developer and business owner; flag for legal review.** |
| OpenAI API | Processor | Parses text/image order content to extract structured order data | **TBD — verify enrollment under OpenAI's standard Data Processing Addendum (DPA); confirm whether it includes SCCs for any non-EEA processing.** |
| Google (Sheets / Workspace) | Processor | Stores catalogue and order data | **TBD — Google Workspace/Cloud terms typically include a standard DPA, but enrollment and region settings must be confirmed.** |
| Telegram / WhatsApp (Meta) | Processor (transport); WhatsApp Business API may carry separate controller obligations for Meta's own metadata use | Transmits messages between school and bot | **TBD — flag, especially for WhatsApp Business API metadata handling, which is contractually distinct from Telegram's bot API.** |

**International transfer mechanism:**
- India deployment: no transfer mechanism needed at present — no shared infrastructure, no EU personal data enters the India stack.
- Germany deployment (once live): if OpenAI or Google process EU personal data outside the EEA, a transfer mechanism (most likely **Standard Contractual Clauses**, via each vendor's standard DPA) is required. **This is currently unverified and should be confirmed before go-live.**

## Phase 3: Lawful basis assessment

| Purpose | Proposed lawful basis | Justification | Flag for legal review? |
|---|---|---|---|
| (a) Parse individual order | Contract, Art. 6(1)(b) | Processing chat_id and order content is necessary to perform the service the school requested | No |
| (b) Match against catalogue | Contract, Art. 6(1)(b) | Necessary step to fulfill the order request | No |
| (c) Consolidate orders for publisher | Legitimate interests, Art. 6(1)(f) | Operational efficiency of bulk ordering; not strictly "necessary" to any single school's contract, so contract basis doesn't fully cover it | **Yes — LIA required (below)** |
| (d) Status replies to schools | Contract, Art. 6(1)(b) | Part of delivering the requested service | No |
| (e) NL Q&A over historical data | Legitimate interests, Art. 6(1)(f) | Operator convenience; not part of the original service to schools | **Yes — LIA required; also flagged under purpose limitation in Phase 1** |

**LIA — Purpose (c), order consolidation:**
1. *Legitimate interest:* Yes — reducing per-school ordering overhead and getting better publisher pricing through bulk consolidation is a concrete, real business need.
2. *Necessary:* Largely yes, though a less intrusive approach (consolidating only order quantities/titles, stripped of school-identifying detail, at the point of sending to the publisher) may reduce what's exposed to that third party. Worth considering.
3. *Override test:* Low impact on individuals — schools' interest in not having their order aggregated is minimal, and the publisher-facing output likely doesn't need to expose the originating school's contact details at all. **Provisional pass, but confirm the publisher-facing export doesn't leak more identifying detail than necessary.**

**LIA — Purpose (e), Q&A over historical data:**
1. *Legitimate interest:* Plausible — operational visibility for the business — but weaker than (c), since this is convenience rather than order fulfillment.
2. *Necessary:* Unclear — the same visibility could likely be achieved through structured reports rather than open-ended natural-language querying of historical personal data.
3. *Override test:* **Cannot confidently complete this part.** Schools did not know their order history would later be queried conversationally by an LLM-backed feature. **Mark TBD — legal review**, and treat this as the highest-priority open item in the whole audit.

## Phase 4: Risk and rights analysis

**Special category data (Art. 9):** No special-category data is intentionally collected. Incidental exposure is possible via handwritten photo uploads (e.g., a name that implies religion, or other unintended content), but this is assessed as low-probability and low-volume given current use. No Art. 9 condition is currently invoked; none is expected to be needed unless photo content handling changes.

**Automated decision-making (Art. 22):** No. Catalogue matching and order consolidation don't produce legal or similarly significant effects on individuals, and no fully automated decision is made about a person without the possibility of human involvement. The one open item — whether "mark fulfilled" happens without human review — doesn't rise to an Art. 22 concern but is still a process gap worth closing.

**DPIA trigger (EDPB nine criteria):** At current scale, the system likely does not trigger a mandatory DPIA. None of evaluation/scoring of people, systematic monitoring, special-category data at scale, or vulnerable-people processing clearly apply. The closest criterion is **large-scale processing**, which does not currently apply given the small number of schools involved, but **should be re-evaluated once the Germany deployment scales past a handful of schools**, since crossing that threshold would likely bring a second criterion (large-scale + purpose (e)'s profiling-adjacent querying) into play, triggering the "two or more criteria" DPIA requirement.

**Data subject rights friction:**
- *Right of access:* Low friction — order data is structured in Sheets and could be exported per school on request.
- *Right to erasure:* Higher friction — because retention is currently undefined (Phase 1), there's no clear mechanism to identify and delete a specific school's historical data, especially once it's part of the aggregate dataset purpose (e) queries against.
- *Right to object to profiling:* Low relevance today since purpose (e) is operator-facing analysis rather than profiling of the schools themselves, but this could shift if the Q&A feature starts surfacing school-level patterns (e.g., "which schools order late every year").

## Phase 5: Law stacking check

- **AI Act cross-check:** Per prior assessment, the system falls into the **minimal risk** tier with an **Article 50 transparency obligation** (disclosure that AI is used to process orders). GDPR's purpose-limitation and lawful-basis requirements are not superseded by this — the two obligations run in parallel; AI Act transparency doesn't substitute for a lawful basis under GDPR Art. 6.
- **ePrivacy check:** No cookies or tracking pixels are involved. The system does use the content of electronic communications (WhatsApp/Telegram messages) for a purpose the sender directly initiated (placing an order), which is materially different from unsolicited marketing messaging. **Flag:** if any broadcast or reminder messages are ever sent to schools that they did not directly prompt, ePrivacy consent requirements would apply and are not currently addressed.
- **Data Act check:** N/A — no connected product data, IoT data, or cloud-switching scenario involved.
