# GDPR Self-Audit — Should-Cost Benchmarking Agent
**Auditor:** Jay Ramamoorthi
**Subject system:** Autonomous Should-Cost Benchmarking Agent (Project 3 capstone)

## Data Processing Brief

**What personal data does the system process?** None. The system's inputs are: a free-text part description (e.g., "a cylindrical steel shaft with a threaded end"), a material description, part weight, stock utilization fraction, source and destination business addresses (factory/plant locations, not personal residences), annual production quantity, and boolean feature flags (holes, threads, heat treatment, surface finish, welding). None of these fields identify, describe, or relate to an individual person. Source/destination addresses are used exclusively as geocoding inputs for freight-distance calculation — they are plant/facility locations, not addresses of individuals, and no name, contact, or identifying detail about any person accompanies them anywhere in the pipeline.

**Where does the data come from?** Directly from the user submitting a part specification (via an n8n form or direct API call) at the time of each request. No existing company database, CRM, HR system, or third-party personal-data source is queried or referenced anywhere in the system.

**What is the data used for?** A single purpose: calculating a should-cost estimate for a manufactured part (material cost, process/labor cost, freight cost, overhead) and generating a report and live spreadsheet reflecting that estimate.

**Who processes it?** The system's own LangGraph pipeline; OpenAI (LLM calls for classification and narrative generation); Pinecone (vector storage/retrieval for the RAG corpus); CommodityPriceAPI (live material pricing); OpenCage (geocoding); Google Sheets API and Notion API (report delivery).

**Where is data stored and processed?** Processing runs via OpenAI and Pinecone's infrastructure (both US-based providers); the finished report is delivered to Google Sheets and Notion (also US-based providers). No self-hosted EU storage layer exists in the current MVP.

**Does the system make or assist in any decision that affects people?** No. The output is a should-cost estimate about a physical part, used by a human buyer as one input into a supplier negotiation. It does not score, rank, evaluate, or make any determination about any individual — not the buyer, not a supplier's staff, not any third party.

**Explicit confirmation: this system does not process personal data.** This conclusion is justified, not assumed — see the Phase 1 inventory below, which walks through every data category the system actually handles and confirms none identifies or relates to an individual.

---

## Phase 1: Personal Data Inventory

| Data category | Source | Purpose(s) | Retention period | Crosses EU border? |
|---|---|---|---|---|
| Part description (free text) | User-submitted at request time | Shape/material classification, process planning | Not persisted beyond the request/response cycle in the core pipeline; if logged for debugging, retention is undefined — **flagged as a gap, see Phase 4** | N/A — not personal data |
| Material description | User-submitted | Material classification, pricing lookup | Same as above | N/A — not personal data |
| Part weight, utilization fraction, feature flags | User-submitted | Cost/cycle-time calculation | Same as above | N/A — not personal data |
| Source/destination **business** addresses (plant/facility locations) | User-submitted | Freight distance calculation via geocoding | Same as above | N/A — not personal data (facility location, not an individual's address) |
| Annual quantity | User-submitted | Annualized cost total | Same as above | N/A — not personal data |

**Conclusion: no category above constitutes personal data under GDPR's definition** (information relating to an identified or identifiable natural person). Every field describes a part, a material, or a business facility — never a person. No purpose-limitation conflict exists because no personal data is collected in the first place, so there is no original purpose to compare a new use against.

**One caveat surfaced by this exercise, not a personal-data issue but worth noting:** retention period for logged requests (if any logging exists at the infrastructure level — e.g., OpenAI's or Pinecone's own request logs) is undefined in this system's own documentation. This doesn't create GDPR exposure since no personal data is in those logs either, but it's a general data-hygiene gap worth closing regardless.

---

## Phase 2: Role Map

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| Client (procurement team receiving the report) | N/A — not a data controller/processor relationship, since no personal data flows to or from them via this system | Receives the finished cost report | N/A |
| Jay (builder/operator) | N/A — since no personal data is processed, controller/processor classification doesn't meaningfully apply to this system | Operates the pipeline end-to-end | N/A |
| OpenAI | Would be a processor **if** personal data were involved — currently N/A | LLM classification and narrative generation on part/material text | N/A currently; if the system's scope ever expanded to include personal data (see Reinforce), a DPA with OpenAI would become necessary |
| Pinecone, CommodityPriceAPI, OpenCage, Google Sheets, Notion | Same — N/A under current scope | Vector storage, pricing/geocoding lookups, report delivery | N/A currently, same caveat as above |

**International transfers:** Not applicable under GDPR specifically, since no personal data crosses any border in this system — though it's worth noting factually that OpenAI, Pinecone, Google, and Notion are all US-based infrastructure providers, which would become a live GDPR transfer question the moment personal data ever entered this pipeline.

---

## Phase 3: Lawful Basis Assessment

**Not applicable.** GDPR's lawful basis requirement (Article 6) applies to the processing of personal data. Since this system processes no personal data, no lawful basis analysis is required for any current processing activity.

---

## Phase 4: Risk and Rights Analysis

**Special category data (Article 9):** Not present and not inferable. Part descriptions, material specs, and facility addresses carry no plausible path to inferring health, biometric, political, religious, or other special-category information about any person, unlike the chat-sentiment scenario in the peer/partner GDPR lab.

**Automated decision-making (Article 22):** Not applicable. The system doesn't make a decision *about* a person at all — its output is a cost estimate about a part, used by a human as input to a negotiation they conduct themselves. There is no automated decision with legal or similarly significant effect on any individual.

**DPIA trigger:** None of the EDPB's nine criteria apply — no evaluation/scoring of people, no automated decision-making affecting a person, no systematic monitoring of individuals, no special-category data, no large-scale processing of personal data (there is no personal data at all), no vulnerable-population processing, no dataset-matching involving individuals. **A DPIA is not required.**

**Data subject rights friction:** None currently applicable, since there is no personal data for any data subject right (access, erasure, objection to profiling) to attach to. This section is revisited under Reinforce as a forward-looking exercise.

---

## Phase 5: Law Stacking Check

**AI Act cross-check:** Per the linked self-audit, this system is classified **minimal risk** under the AI Act. The AI Act's minimal-risk tier does not impose any obligation GDPR doesn't already require — and since GDPR itself doesn't apply here (no personal data), neither framework currently imposes a compliance obligation on this system.

**ePrivacy check:** No cookies, tracking pixels, device-level data collection, or interception of communications content occur anywhere in this system. Not applicable.

**Data Act check:** No connected product, IoT, or cloud-switching data involved. Not applicable.

---

## Phase 6: Compliance Memo

**To:** Client's Legal Counsel (no dedicated DPO exists for this engagement)
**From:** Jay Ramamoorthi, AI Consulting
**Re:** GDPR assessment — Should-Cost Benchmarking Agent

**Bottom line: Proceed.** This system does not process personal data in its current form, and this conclusion is based on a full review of every data field it collects, not an assumption. No GDPR compliance obligation currently attaches to this system's operation.

**Top three actions:**

1. **Document this conclusion formally**, not just informally understood. Keep a short written record (this audit) showing that "no personal data is processed" was actively verified against every data category the system handles, since a regulator or client's legal team would reasonably expect to see that reasoning, not just a bare assertion.
2. **Define a logging retention policy**, even though it isn't a GDPR requirement here. If any request-level logging exists at the infrastructure or debugging level, document what's kept and for how long — good practice regardless of personal-data status, and it removes ambiguity before any future scope change.
3. **Re-run this assessment before any scope expansion.** If the system's roadmap ever adds named individuals to its inputs or outputs (e.g., a named buyer or supplier contact tied to a specific negotiation record — see the Reinforce section below), this conclusion must be revisited immediately, not assumed to still hold.

**Residual risks:**

- **Scope creep risk.** The single biggest risk to this "no personal data" conclusion isn't a current gap — it's a future one. Any well-intentioned feature addition (e.g., tracking which named buyer requested which report, for the multi-distributor CRM-style features implied by future growth) would immediately reintroduce GDPR obligations that don't exist today.
- **Vendor-level data handling is outside this system's direct control.** Even though no personal data is submitted, the underlying vendors (OpenAI, Pinecone, etc.) process the system's requests on their own US infrastructure — this is a general vendor-dependency risk worth being aware of, even though it doesn't currently create a GDPR obligation for this specific data.

**What this memo is not:** a legal opinion, a DPIA, or a certification. Legal counsel should be engaged before relying on this assessment for any formal compliance decision, particularly if system scope changes.
