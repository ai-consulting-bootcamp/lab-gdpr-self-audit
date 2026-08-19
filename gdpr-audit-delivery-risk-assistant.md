# GDPR Audit — AI Delivery Risk Assistant
**Project:** `delivery-risk-assistant` (github.com/akansha27nov/delivery-risk-assistant)

**Auditor:** Akansha Verma

**Date:** 19 August 2026

**Status of this document:** First-pass compliance assessment for a consulting portfolio exercise. Not a legal opinion, DPIA, or certification.

---

## Data Processing Brief

*Written for a Data Protection Officer who has never seen this project.*

**What the system does:** The AI Delivery Risk Assistant ingests project artefacts (sprint reports, ticket exports, standup transcripts, Slack threads, retro notes, stakeholder and exec emails), retrieves the most relevant evidence for a set of fixed "risk angles," and uses an LLM to extract up to three cited delivery risks per run. High-severity or contradictory findings are routed to a human for approval before they reach a report.

**What personal data does it process?**
- Full names and roles of team members, stakeholders, and external partners, appearing directly in ingested source text (e.g. standup transcripts name a scrum master and three engineers by name; a stakeholder email names a product lead).
- Free-text workplace communications authored by identifiable individuals — standup remarks, Slack messages, retro comments, status emails.
- Inferred/derived signals about individuals: workload strain, capacity, morale, and at least one **explicit attrition/retention signal** ("I'm honestly starting to look around at other roles"), attributed to a named person in the source transcript.
- Performance-adjacent signals: who is blocked, who owns an unassigned remediation ticket, who made a status claim that later contradicts the underlying evidence.

This is personal data under Art. 4(1) GDPR — it relates to identified, identifiable natural persons (team members, named in text, with role and employer context attached).

**Where does the data come from?** In the current repo, the `knowledge_base/` corpus (`atlas` and `nova` projects) is explicitly documented as **synthetic/fabricated demo data** (README: "Data Notes"). However, the system is architected for **live, ongoing production use**: the Streamlit UI has a live document-upload flow into an existing project namespace, a FastAPI endpoint (`POST /run-audit`) is deployed on Render, and an n8n workflow triggers a real scheduled run every Thursday. In a real deployment, the equivalent inputs would be genuine internal sprint reports, ticket exports, Slack exports, and emails belonging to a client's employees — i.e., real personal data, sourced from the client's own tooling (Jira/ticket systems, Slack, email, meeting transcripts) rather than collected directly from the data subjects for this purpose.

**What is the data used for?**
1. Semantic retrieval and evidence ranking (vectorising and storing text chunks).
2. LLM-based extraction of delivery risks, including per-person-adjacent signals (capacity, morale, attrition).
3. Severity classification and routing to human review.
4. Generation and distribution of a leadership-facing report (Markdown, Notion, Telegram).

**Who processes it?**
- The system itself (ingestion, chunking, retrieval, orchestration — `src/`).
- **OpenAI** — embeddings (`text-embedding-3-small`) and structured risk extraction (`gpt-4o-mini`).
- **Pinecone** — vector database storing embedded chunks, namespaced per project.
- **Cohere** — reranking of candidate evidence (`rerank-v3.5`).
- **Telegram** (Bot API) — human-in-the-loop approval alerts for high-severity/contradictory findings.
- **Notion**, via **n8n** — scheduled delivery of the aggregated report to a workspace.
- **Render** — hosts the live FastAPI backend (`delivery-risk-api.onrender.com`).

That is six distinct third parties touching personal data before a human ever reviews it.

**Where is data stored/processed?** Not confirmed for any vendor in the current repo/config. `.env.example` and `config.py` set API keys and model names but do not pin a data region for Pinecone, OpenAI, or Cohere, and Render's hosting region is not documented. **This is a TBD that must be resolved before any real client data touches the system.**

**Does the system make or assist in a decision affecting people?** Yes, indirectly. It scores and evaluates project (and implicitly team/individual) risk, and it explicitly extracts individual-level signals such as workload and attrition risk from named employees' own words. It does **not** take automated action against an individual (e.g. no automatic HR action), and severity-1 findings and contradictions are routed to a **human-in-the-loop** approval gate (Telegram) before reaching a report — this is a genuine, code-enforced safeguard (`graph.py`, `evaluate_severity` → `route_to_hitl`). Whether this fully avoids Art. 22 is analysed in Phase 4 below; either way it clearly triggers DPIA-relevance criteria (see Phase 4).

**Confirmation: this system does process personal data.** It is not limited to anonymised or purely operational data — the "no personal data" exemption does not apply, because named individuals and their workplace conduct/sentiment are directly present in source text and directly inform system outputs, even though final reports currently anonymise to role-level language (e.g. "the single QA engineer") rather than naming individuals.

---

## Phase 1: Personal Data Inventory

| Data category | Source | Purpose(s) | Retention (known/estimated) | Crosses EU border? |
|---|---|---|---|---|
| Full name + role (e.g. "Priya Nair, Scrum Master") | Standup transcripts, sprint reports, emails | Attribution/context for risk extraction | Indefinite — no deletion logic in `ingestion.py`/`embedding.py`; vectors persist in Pinecone until manually cleared | Yes (see Phase 2) |
| Full name + role, external party (e.g. "David Cho, Product Lead, Rewards Partner Co.") | Stakeholder emails | Evidence for scope/status risk extraction | Same as above | Yes |
| Verbatim workplace communications (standup remarks, Slack messages, retro comments) | `knowledge_base/*.txt`, `.md`, live uploads | Chunked, embedded, and retrieved as evidence | Indefinite in Pinecone; no TTL configured | Yes |
| Verbatim workplace communications | *(same as above)* | Sent to OpenAI for LLM risk extraction (per-request, not stored by the pipeline itself) | Governed by OpenAI's own API data retention policy, not the project's — TBD, needs verification | Yes |
| Inferred attrition/wellbeing signal, attributed to a named individual | Standup transcript ("I'm honestly starting to look around at other roles") | Retained as a citable evidence chunk that can be retrieved and cited by the LLM as grounding for a risk | Indefinite in Pinecone unless manually purged | Yes |
| Ownership/accountability signals (who owns an unassigned SEV-1 ticket, who made a status claim that contradicts evidence) | Ticket exports, incident postmortems, exec status emails | Contradiction detection, severity routing | Indefinite | Yes |
| Reviewer identity (Telegram chat ID / approver) | `.env` `TELEGRAM_CHAT_ID`, HITL approval events | Routing high-severity approvals to a specific human | Held by Telegram indefinitely per their retention policy — not controlled by this project | Yes (Telegram infrastructure is not EU-only) |

**Flag — purpose limitation:** Standup transcripts, Slack messages, and retro notes were created by employees for internal team coordination and process improvement. Feeding them into an automated, cross-project risk-scoring and evidence-retrieval system — which surfaces individual capacity/attrition signals to leadership via a separate reporting channel (Notion, Telegram) — is very likely a **different, incompatible purpose** from why that data was originally generated. This is the single most important gap in the project and should be flagged prominently in the client memo (Phase 6).

---

## Phase 2: Role Map

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| Client (hypothetical, e.g. an engineering org deploying this) | Controller | Determines purpose (delivery risk monitoring) and means (which docs are ingested, who receives reports) | N/A — client is the controller, not a processor relationship |
| Akansha / project owner (in a real engagement) | Processor (on client's behalf) or joint controller if reused across engagements | Operates the pipeline, configures retrieval/reporting | **No DPA exists in the current repo.** Would be required before any live client engagement. |
| OpenAI | Processor | Embeddings + risk extraction on submitted text | Not evidenced in repo. OpenAI does offer a standard DPA — **not yet executed/confirmed for this project.** |
| Pinecone | Processor (sub-processor) | Stores vector embeddings + underlying text metadata, namespaced per project | Not evidenced. Pinecone offers a DPA — **not confirmed.** |
| Cohere | Processor (sub-processor) | Reranks candidate evidence chunks (receives chunk text) | Not evidenced. **Not confirmed.** |
| Telegram | Processor (sub-processor) — arguably borderline, since Telegram also acts with its own purposes as a comms platform | Delivers HITL approval alerts containing risk summaries | Telegram does not offer a standard enterprise DPA in the way OpenAI/Pinecone/Cohere do — **this is a real gap, not just a TBD.** |
| Notion (via n8n) | Processor (sub-processor) | Stores the final aggregated report | Not evidenced. Notion offers a DPA — **not confirmed.** |
| Render | Processor (sub-processor, infrastructure) | Hosts the live FastAPI backend that receives and processes requests | Not evidenced. Render offers a DPA — **not confirmed.** |

**International transfers:** Every third party above (OpenAI, Pinecone, Cohere, Telegram, Notion, Render) is a US or non-EU-headquartered service. Unless each is explicitly configured to an EU processing region (several of them, e.g. Pinecone and Render, do offer EU regions as a paid/config option), personal data will leave the EEA on **every single pipeline run.** Transfer mechanism status: **TBD for all six vendors** — this needs to be resolved via each vendor's Standard Contractual Clauses (SCCs) and region settings, not assumed.

---

## Phase 3: Lawful Basis Assessment

| Purpose | Proposed lawful basis | Justification | Flag for legal review? |
|---|---|---|---|
| Ingesting sprint/ticket/comms data to extract delivery risks | Legitimate interests (Art. 6(1)(f)) | Employer has a plausible operational interest in delivery-risk visibility | **Yes** — LIA required (below); balancing test is not obviously in the employer's favor given the individual-level sentiment data involved |
| Retaining chunked employee communications in a vector database for repeated retrieval | Legitimate interests, *tentatively* | Needed for the retrieval architecture to function | **Yes — TBD, legal review.** Necessity is questionable: full-corpus retention with no TTL is broader than needed for weekly risk scoring |
| Surfacing an individual attrition/wellbeing signal to leadership via Notion/Telegram | Legitimate interests, *contested* | Arguable business interest in retention risk visibility | **Yes — TBD, legal review.** This is the highest-risk purpose in the whole system (see LIA below) |
| Sending team members' names and communications to third-party LLM/rerank vendors (OpenAI, Cohere) | Legitimate interests, contingent on DPAs | Necessary sub-processing to run the pipeline | **Yes**, contingent on DPAs/SCCs actually being executed — currently blocked |

### Legitimate Interests Assessment — for "surfacing individual attrition/wellbeing signals to leadership"

1. **Is the interest legitimate?** Plausibly yes — reducing unplanned attrition and identifying team strain is a real, understandable business need for a delivery organisation.
2. **Is the processing necessary?** Weak. A less intrusive alternative clearly exists: the system could flag "team capacity risk" at a **team level** (as the current sample reports already do — "the single QA engineer," not by name) without retaining or being capable of retrieving verbatim, person-attributed sentiment about wanting to leave. The fact that the underlying evidence chunk (with the named individual and their exact words) remains retrievable via the "Forensic Evidence Inspector" feature undermines necessity — the system keeps more identifiable, sensitive detail than the stated purpose requires.
3. **Does the individual's interest override?** Likely yes for this specific processing activity. An employee raising a private capacity/retention concern with their scrum master in a standup has a reasonable expectation that it stays within that immediate relationship — not that it becomes a permanently retrievable, cross-tool evidence artefact feeding an automated risk system reporting to leadership. This is the kind of processing an employee would be surprised and unhappy to learn about.

**Conclusion: mark this purpose TBD — legal review, and treat it as the highest-priority open item in the client memo.**

---

## Phase 4: Risk and Rights Analysis

**Special category data (Art. 9):** No health, biometric, political, religious, sexual orientation, ethnic origin, or trade union data is present in the current corpus, and none is directly solicited by the system's prompts (`RISK_ANGLES` in `config.py` target blockers, scope, capacity/morale, incidents, and status accuracy — not protected characteristics). However, free-text ingestion of unstructured workplace communications creates a **realistic risk that special-category data could appear incidentally** (e.g. a Slack message mentioning a medical leave, a religious holiday request affecting sprint capacity). Nothing in the pipeline currently detects or excludes this before embedding and LLM processing.

**Automated decision-making (Art. 22):** The system does not itself take action against an individual (no automatic HR action, no automatic report distribution of unapproved findings — the n8n/Notion design explicitly labels unapproved findings "Pending human review" rather than presenting them as settled fact, per `n8n_notion_justification.md`). SEV-1 and contradiction findings route through a human-in-the-loop Telegram approval gate before reaching a report. This human review is a genuine, code-level safeguard and likely means the system falls short of "a decision based solely on automated processing" for Art. 22 purposes. That said, it clearly constitutes **profiling** under Art. 4(4) (automated evaluation of aspects relating to a natural person — their workload, reliability, and attrition risk), and profiling triggers DPIA relevance regardless of whether Art. 22's stricter regime applies.

**DPIA trigger — EDPB nine criteria applied:**
- Evaluation or scoring of people — **applies** (capacity/attrition/reliability signals).
- Automated decision-making with significant effect — borderline/partial (human review exists, but the underlying evaluation is automated).
- Systematic monitoring — **applies** (the n8n weekly Thursday cron trigger makes this recurring, scheduled surveillance of team communications, not a one-off analysis).
- Special category data at scale — not currently, but realistic incidental risk (see above).
- Large-scale processing — not yet, at demo scale; would very plausibly become large-scale in a real multi-team client deployment.
- Matching/combining datasets — **applies** (tickets + Slack + email + transcripts are cross-referenced specifically to detect contradictions between them).
- Vulnerable data subjects — no.
- Innovative technology — **applies** (LLM-based automated evaluation of employee-generated text is exactly the kind of use the EDPB flags here).
- Cross-border transfer preventing rights exercise — plausible, given six non-EU-default vendors.

**At least four of the nine criteria plausibly apply (evaluation/scoring, systematic monitoring, matching/combining datasets, innovative technology) — a DPIA is required before any real deployment**, not just recommended.

**Data subject rights friction:**
- **Right of access:** An employee asking "what does this system know about me" would require reconstructing every chunk across Pinecone (and any residual OpenAI/Cohere processing logs) that mentions them — the architecture has no person-indexed lookup; chunks are indexed by project namespace and content, not by data subject. **Not currently supportable in a timely way.**
- **Right to erasure:** Deleting one person's mentions would require identifying every chunk containing them across the vector index and any generated report artefacts already sent to Notion/Telegram — no such deletion tooling exists today. **Not currently supportable.**
- **Right to object to profiling:** Since individual capacity/attrition signals feed into evaluation used in leadership reporting, an employee has a plausible basis to object. The system has no mechanism to exclude a specific person's data from future risk extraction. **Not currently supportable.**

---

## Elevated Finding: Attrition Signal — Design Intent vs. Implementation Gap

**Severity:** Blocking (for any deployment touching real employee data)

**Context:** The repo's own README documents the attrition/retention signal as a deliberately planted test case in the corpus — not an incidental artefact of the sample data. It is described as "single-source — tests that the assistant doesn't fabricate corroboration, and handles people-sensitive content responsibly." That framing matters: it confirms the system was built and evaluated specifically against this scenario, which means any real deployment on genuine employee communications will encounter the identical pattern by design, not by chance. This elevates the finding from "sensitive data happens to be present" to "the system's stated design goal for handling sensitive data is not currently met."

**Description:** The pipeline passes the retrieval half of its own test — it correctly surfaces the cited signal without fabricating corroborating evidence. It fails the "handles it responsibly" half. Per the Phase 1 inventory and the Stretch checklist above, the underlying source text (not a role-level summary of it) is embedded verbatim, retained indefinitely with no TTL, retrievable by any query rather than being bound to the "capacity/morale" risk angle it was extracted for, and remains accessible via the Forensic Evidence Inspector back to the named individual's exact words. The final leadership-facing report does anonymise to role-level language ("the single QA engineer"), but the evidence chain underneath it does not — meaning responsible handling currently exists only at the last-mile output layer, not throughout the pipeline.

**Recommended action:** Before this pattern can be described as "responsible handling" in any client-facing material, the architecture needs at minimum: (1) purpose-bound retrieval, so person-attributed sentiment chunks are not retrievable outside the specific risk angle they were extracted for; (2) a distinct, shorter retention/TTL policy for chunks flagged as containing person-attributed sentiment, separate from operational data like ticket status; (3) restricting the Forensic Evidence Inspector's ability to surface verbatim named-individual quotes — even to the approving human — without a documented justification for why the role-level summary is insufficient for that approval decision.

**Escalation needed?** Yes — to whoever owns the go/no-go decision on a real pilot, before this project is pitched as "citation-gated" or "responsible by design," since that framing currently holds true only at the report layer, not the retrieval layer.

---

## Phase 5: Law Stacking Check

- **AI Act cross-check:** If deployed in a real organisation to evaluate employees' workload, reliability, or retention risk, this system is a strong candidate for the **EU AI Act's Annex III high-risk classification for employment** (monitoring/evaluating performance and behaviour of workers) — this is the same classification lens Akansha is applying in the HR Tech Compliance Shield project, and it applies with force here too, even though this project was not originally scoped as an "HR" tool. If high-risk, the AI Act would add obligations GDPR does not on its own require: a documented risk-management system, technical documentation, logging/traceability (LangSmith-style tracing would help here), human oversight design documentation, and accuracy/robustness testing — beyond GDPR's lawful-basis and rights framework.
- **ePrivacy check:** No cookies, tracking pixels, or device-level data collection are used by this system (it is a backend pipeline plus a Streamlit dashboard, not a consumer-facing site with tracking). ePrivacy's consent requirement does not appear to apply. N/A.
- **Data Act check:** No connected product, IoT, or cloud-switching data involved. N/A.

---

## Phase 6: Compliance Memo

**To:** Data Protection Officer / Legal Counsel
**From:** Akansha Verma
**Re:** GDPR first-pass assessment — AI Delivery Risk Assistant
**Date:** 18 August 2026

**Bottom line: Proceed with conditions.** The architecture's citation-gating and human-in-the-loop severity routing are genuine, code-enforced safeguards — but the system currently processes named individuals' workplace communications, including an explicit employee-attrition signal, with no data-subject rights tooling, no confirmed sub-processor DPAs, and no confirmed EU data residency — notably, the attrition-signal gap addressed in condition 3 is blocking-severity, not optional, and is what keeps this recommendation at "proceed with conditions" rather than "stop." It should not touch real employee data until the conditions below are addressed.

**Top three actions:**
1. **Establish DPAs and confirm EU processing regions with all five external processors (OpenAI, Pinecone, Cohere, Notion, Render) before any live client data is ingested.** Telegram is a distinct problem — it does not offer a standard enterprise DPA, so an alternative HITL notification channel (e.g. Slack or email via a vendor with an executable DPA) should be evaluated before production use.
2. **Complete a full DPIA before deployment.** This system triggers at least four EDPB criteria (evaluation/scoring of people, systematic monitoring, dataset matching, innovative technology) — a DPIA is not optional here.
3. **Redesign the individual-level attrition/wellbeing signal handling before it reaches production.** The Legitimate Interests Assessment for this specific purpose does not clearly favor the employer. Recommend restricting the system to team-level signals only (which the current output reports already do reasonably well) and either excluding individually-attributable sentiment chunks from retrieval entirely, or gating them behind a much narrower, explicitly-scoped lawful basis with a documented necessity case. (See "Elevated Finding" above — this is the same gap the project's own test corpus was designed to catch, and it currently isn't caught.)

**Residual risks, even if all three actions are taken:**
- **Purpose limitation risk persists.** Standup and Slack data was generated for team coordination, not automated risk scoring; even with a valid lawful basis, employees may reasonably object that this is a different purpose than the one they understood when they spoke or wrote.
- **Rights-exercise infeasibility.** Access and erasure requests are not currently supportable in a timely way, because chunks are indexed by content/project, not by data subject — this is an architectural gap, not just a documentation gap, and will take real engineering effort to fix.
- **Incidental special-category data.** Free-text ingestion of unstructured communications creates an ongoing, low-probability but real risk that Article 9 data appears in the corpus without detection.

*This memo is not a legal opinion, a DPIA, or a certification. Please engage legal counsel before relying on this assessment for any compliance decision.*

---

## Reinforce — Accountability Test

**Could you demonstrate compliance to a regulator using only what currently exists in the repo?** No.

| Documentation a regulator could request | Exists? |
|---|---|
| DPA with OpenAI | ✗ Not evidenced |
| DPA with Pinecone | ✗ Not evidenced |
| DPA with Cohere | ✗ Not evidenced |
| DPA/alternative safeguard with Telegram | ✗ Not evidenced, and Telegram may not offer one |
| DPA with Notion | ✗ Not evidenced |
| DPA with Render | ✗ Not evidenced |
| Legitimate Interests Assessment (LIA) | ✗ Did not exist before this audit; drafted above for one purpose only |
| DPIA | ✗ Does not exist |
| Privacy notice to affected employees | ✗ Does not exist — employees whose standups/emails are ingested appear to have no visibility that this system exists |
| Retention schedule | ✗ No TTL or deletion policy configured anywhere in `src/` |
| Records of Processing Activities (Art. 30) | ✗ Does not exist (this audit is the closest starting point) |

**What's entirely missing:** everything except the technical safeguards baked into the code itself (citation gating, HITL routing, contradiction detection). The engineering discipline is real; the compliance paperwork and rights infrastructure is currently zero.

**Revisiting a TBD:** The LIA for "surfacing individual attrition signals to leadership" was marked TBD — legal review. What a lawyer would actually need to advise on it: (1) the exact retention period currently in effect in Pinecone (undefined — needs to be measured, not estimated); (2) whether the client's employment contracts or works council agreements (relevant given the DACH market context) already address monitoring of internal communications; (3) whether a narrower, team-level-only design would still meet the client's actual business need, which would remove the need for this LIA entirely. Preparing a concrete answer to (3) — i.e., building the team-level-only alternative — is something that can be done now, before the legal conversation, and would substantially de-risk the rest of the audit.

---

## Stretch — Data Protection by Design Checklist

**Highest-risk processing activity:** Retaining and making individually-retrievable an employee's verbatim attrition/wellbeing statement, sourced from a standup transcript, for use in an automated cross-tool risk-reporting pipeline.

| Design principle | Current state | Pass/Fail/Unknown |
|---|---|---|
| Data minimisation | Full verbatim transcript is chunked and embedded; no filtering removes person-attributed sentiment before storage | **Fail** |
| Purpose binding | No technical control restricts a stored chunk to only the "capacity/morale" risk angle it was intended for — any chunk is retrievable for any query | **Fail** |
| Access controls | Not evidenced in repo — no auth layer visible on the Streamlit app or the FastAPI `/run-audit` endpoint beyond what Render provides by default | **Unknown / likely Fail** |
| Retention enforcement | No TTL, no scheduled deletion, no anonymisation step anywhere in `ingestion.py`, `chunking.py`, or `embedding.py` | **Fail** |
| Subject rights workflow | No person-indexed lookup exists; a 30-day access/erasure response is not currently achievable | **Fail** |
| Incident response | No breach-detection or 72-hour notification process is documented for this project | **Fail** |

**What would need to change:** Add a lightweight person-tagging step at ingestion (flagging which chunks mention which named individuals) to make access/erasure technically feasible; set an explicit TTL on Pinecone vectors and re-embed only current source docs; add authentication to the FastAPI endpoint before any real deployment; and write a one-page incident-response runbook covering the six external processors, since a breach at any one of them (e.g. Pinecone) would expose employee communications data. None of this is large engineering effort individually, but none of it exists today, and all of it is a precondition for moving past "demo with synthetic data" into "real client pilot."
