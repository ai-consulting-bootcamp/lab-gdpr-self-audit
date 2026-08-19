# Self-Audit Report: Board Game Concierge

**Author:** Mudit Airan  
**Project name:** Board Game Concierge  
**Project github URL:** https://github.com/zuzubes/Board-game-concierge  
**Description:** Telegram-based board game concierge that explains rules, answers follow-up questions, gives strategy tips, and recommends games from a local catalog.

## Data Processing Brief

Board Game Concierge is a Telegram-based assistant for a regular board game group. The system processes Telegram message content, Telegram account identifiers, usernames or display names if present, conversation history in the active session, and the game preferences or constraints users state in chat. It also processes imported rulebook text, local masterlist CSV data, and query text sent to third-party search and AI vendors when the bot generates answers, tips, or recommendations. The system is designed to help users get through setup faster by explaining rules, answering follow-up questions, giving strategy tips, and recommending games from the local catalog.

The main data source is the user directly through Telegram. Additional data comes from imported rulebooks, the local catalog, and external search or AI APIs used by the backend. Data is used for rule explanation, question answering, recommendation ranking, fallback search, and short-lived session continuity. According to the README, the backend uses OpenAI, Pinecone, SerpApi, Serper, and Tavily, and the Telegram workflow is orchestrated in n8n. 

The system does not appear to make legal or similarly significant decisions about people. Its recommendations are about games, not about the users themselves. The main GDPR question is therefore not automated decision-making, but whether the chat content and identifiers are collected, shared with vendors, retained, and disclosed in a way that matches the bot's actual operation. 

## Phase 1: Personal Data Inventory

| Data category | Source | Purpose(s) | Retention period (known/estimated) | Crosses EU border? |
|---|---|---|---|---|
| Telegram user ID / chat ID | User via Telegram | Session routing, replying to the correct user, basic conversation continuity | Unknown; likely until session reset or platform retention | Yes, likely if vendors are outside the EEA |
| Telegram username / display name | User via Telegram | Personalizing replies, identifying the requester in chat logs | Unknown | Yes, likely if vendors are outside the EEA |
| Message text and follow-up questions | User via Telegram | Rule explanation, tips, recommendations, chat history, intent tracking | Unknown; in-memory session state is documented, but storage policy is not | Yes, likely if external AI/search APIs are used |
| Board-game preferences stated in chat | User via Telegram | Recommendation filtering by player count, time, complexity, and style | Unknown | Yes, likely if sent to external APIs |
| Conversation context / pending intent | System derived from user input | Carrying context across messages | In-memory only per README, but not formally documented | Possibly, if any vendor call includes context | 
| Imported rulebook text | Project team / source PDFs | Grounded rule explanations and report generation | Stored in the repo and Pinecone index; retention not formally specified | Yes, if Pinecone is hosted outside the EEA |
| Masterlist CSV data | Project team / local files | Recommendation candidate filtering and ranking | Stored locally; retention tied to project files | Possibly, if deployed or synced through cloud services |

Private note: The personal data risk comes from Telegram content and identifiers, not from the board-game domain itself.

## Phase 2: Role Map

| Entity | Role (controller / processor / joint controller) | Processing activity | DPA in place? |
|---|---|---|---|
| Your client / project operator | Controller | Decides the purpose of the concierge, the data it uses, and the operational retention rules | No evidence of one |
| You / your team | Processor during development, or controller if you independently decide purposes and means | Build, test, and maintain the system; may access logs or payloads during implementation | No evidence of one |
| Telegram | Independent controller for its platform; recipient for bot traffic | Delivers user messages, chat metadata, and account identifiers to the bot | Platform terms only; not documented in repo |
| OpenAI API | Processor or vendor, subject to contract terms | Embeddings and chat synthesis | Unknown; needs DPA or equivalent terms if personal data is sent |
| Pinecone | Processor or vendor, subject to contract terms | Vector storage and retrieval for rulebook chunks | Unknown; needs DPA or equivalent terms if personal data is sent |
| SerpApi / Serper / Tavily | External service providers; role depends on their service terms | Live search fallback for tips | Unknown; transfer and role need contract review |
| n8n hosting layer | Processor if hosted by n8n; internal tooling if self-hosted | Orchestration of Telegram workflow and message routing | Unknown; needs vendor review if hosted externally |

Private note: I treat the project owner as the main controller because the repo decides the purposes and means of the processing. The only role question that remains genuinely unresolved from the README is whether external vendors are processors or independent controllers, which depends on their contract terms and whether they reuse prompts for their own purposes.

## Phase 3: Lawful Basis Assessment

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| Answering user questions about board games | Legitimate interests | The bot only processes the user’s message to provide the requested concierge function; a contract basis is weaker because this is an informal utility, not a binding service contract | Yes |
| Recommending games from the local catalog | Legitimate interests | Ranking games by stated preferences is core to the product and uses limited, low-risk preference data | Yes |
| Maintaining short-lived chat context | Legitimate interests | Session continuity is necessary for coherent follow-up responses and is less intrusive than persistent profiles | Yes |
| Storing vectors / embeddings for retrieval | Legitimate interests | Retrieval-augmented answering needs a searchable memory layer, but the retention and deletion design must be documented | Yes |
| Sending prompts to external AI/search vendors | TBD — legal review | The operational need is clear, but the actual lawful basis and transfer terms depend on the vendor contract and the amount of personal data sent | Yes |

Private note: I did not choose consent as the main basis because the bot is a functional assistant, not a consent-driven marketing or optional analytics flow.

### Legitimate Interests Assessment

For the four processing purposes where legitimate interests is proposed, the LIA can be stated as follows:

1. **Answering user questions about board games**
   - Legitimate interest: provide a responsive concierge service to users who explicitly ask for help.
   - Necessity: the bot cannot answer the request without processing the message content.
   - Balancing: the privacy impact is limited if messages are used only for the reply and short-lived session handling.

2. **Recommending games from the local catalog**
   - Legitimate interest: help users choose a suitable game from the existing catalog.
   - Necessity: player count, time, and complexity filters are needed to make the recommendation useful.
   - Balancing: the data is low sensitivity, but the system should still avoid building persistent user profiles.

3. **Maintaining short-lived chat context**
   - Legitimate interest: keep the conversation coherent across follow-up questions.
   - Necessity: without session context, the bot would repeatedly lose the active game or request.
   - Balancing: short-lived context is less intrusive than long-term storage, provided it is actually deleted or expires quickly.

4. **Storing vectors / embeddings for retrieval**
   - Legitimate interest: enable rulebook search and grounded answers.
   - Necessity: retrieval infrastructure is required for the product design described in the README.
   - Balancing: this is acceptable only if deletion, retention, and vendor access are tightly controlled and documented.

## Phase 4: Risk and Rights Analysis

**Special category data (Article 9):**  
The project does not appear to intentionally process special-category data. That said, users could still type sensitive information into Telegram messages, and the chatbot could infer something sensitive from free-text prompts. The safer position is to treat special-category data as possible by accident, not as part of the intended design, and to block or minimize it rather than rely on a formal Article 9 condition.

**Automated decision-making (Article 22):**  
The system does not make decisions with legal or similarly significant effects on people. It recommends board games and explains rules; it does not approve, reject, score, or sanction users. Article 22 should therefore not be the main issue, although the project should still avoid presenting recommendations as if they were authoritative decisions about the user.

**DPIA trigger:**  
This is a borderline case rather than an obvious DPIA trigger. The system uses chat content, third-party vendors, retrieval tooling, and possibly cross-border transfers, but it does not obviously do large-scale profiling, monitoring, or special-category processing. My view is that a full DPIA is not clearly mandatory from the current description, but a lightweight documented risk assessment is still warranted before launch.

**Data subject rights friction:**  
The hardest rights request will be erasure, because the system may store chat-derived context in memory, vectors in Pinecone, and vendor-side request logs. Access requests are also awkward because the same user input may be replicated across workflow logs and vendor systems. Objection to legitimate interests is the main rights concern for ongoing processing, so the project should have a clear suppression and deletion path.

## Phase 5: Law Stacking Check

**AI Act cross-check:** The system is best treated as a limited-risk chatbot-style service. The key issue is Article 50 transparency: if the AI nature is not obvious from the Telegram context and the bot’s own wording, the user should be told clearly that they are interacting with AI-generated assistance. The platform label alone is helpful, but it should not be the only disclosure point.

**ePrivacy check:** No cookies, pixels, or browser-based tracking are described in the README. Based on the current architecture, ePrivacy is probably not the main issue unless a web front end or tracking layer is added later.

**Data Act check:** N/A. The project does not involve connected product data, IoT device data, or cloud switching obligations.

## Phase 6: Compliance Memo

**To:** Data Protection Officer / legal counsel  
**Subject:** GDPR assessment of Board Game Concierge

Bottom line: **proceed with conditions.** The Board Game Concierge can likely run on a legitimate-interests basis, but only if the team documents its data flows, clarifies vendor roles, and implements a deletion and disclosure process before wider use.

Top three actions:
1. Publish a privacy notice and retention summary that explains which Telegram identifiers, message content, session context, and vendor payloads are processed.
2. Put DPAs or equivalent controller/processor terms in place with OpenAI, Pinecone, n8n hosting, and any search provider that receives user text, then confirm the transfer mechanism for any EEA export.
3. Add an AI disclosure and a deletion workflow covering chat history, embeddings, workflow logs, and any cached vendor responses before launch.

Residual risks remain even after those steps. First, vendor-side retention may outlast the local session state, especially if logs or telemetry are kept for service improvement. Second, erasure may be incomplete if embeddings, backups, or downstream caches cannot be fully removed on request. Third, users may still submit sensitive or special-category information into the bot even if the product never asks for it, which creates avoidable exposure.

The practical recommendation is to treat the current build as a narrow pilot, not as a fully compliance-hardened production service. If the client wants to keep the current architecture, the next legal check should confirm the lawful basis for each processing purpose, whether any vendor is acting as an independent controller, and whether Article 50 disclosure is obvious from the overall interface rather than only from the bot label.

What this memo is not: a legal opinion, a DPIA, or a certification. Legal counsel should confirm the final lawful basis, transfer mechanism, retention design, and disclosure wording before deployment.

## Reinforce

### Accountability Check

| Document | Exists? | Notes |
|---|---|---|
| DPA | No evidence found | Needs vendor review |
| LIA | No evidence found | Required if legitimate interests is the chosen basis |
| DPIA | No evidence found | Recommended as a documented pre-launch assessment |
| Privacy notice | No evidence found | Missing from the repo |
| Retention schedule | No evidence found | Session and vendor retention are undocumented |
| RoPA | No evidence found | Not documented in the repository |

### Lawyer Follow-Up

The main open question for counsel is whether any vendor receives user text only for processing on instruction, or whether one or more vendors reuse that data for their own purposes. Counsel should also confirm whether prompt text ever includes personal data beyond the user’s request, because that determines both the transfer analysis and whether the current retention setup is defensible.

## Stretch: Data Protection by Design Checklist

| Design principle | Current state of your system | Pass / Fail / Unknown |
|---|---|---|
| Data minimisation: only the minimum necessary data is collected | The bot appears to process only the user’s Telegram message and basic chat context, but logging and vendor payload scope are not documented | Unknown |
| Purpose binding: data is technically restricted to the stated purpose | The main purposes are clear, but no formal technical restriction is documented | Fail |
| Access controls: access is limited to those who need it | Not documented in the repo | Unknown |
| Retention enforcement: automated deletion or anonymisation is in place | No deletion mechanism is described | Fail |
| Subject rights workflow: system can support an access or erasure request within 30 days | No workflow is documented | Fail |
| Incident response: breach detection and 72-hour notification process is documented | Not documented in the repo | Fail |

For the failed items, the project needs a privacy notice, vendor inventory, deletion routine for session data and vectors, and a basic incident response procedure before it is defensible as a production system.
