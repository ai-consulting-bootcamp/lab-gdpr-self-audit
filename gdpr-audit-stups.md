# GDPR audit worksheet: Stups

**System:** Stups, personal evening suggestion agent (n8n workflow `Stups v6`)

**Companion document:** `data-processing-brief.md`

**Date:** 19 August 2026

**Status:** first pass by the system's builder. Not a legal opinion.

Throughout this document, "Stream A" means personal data about the recipient of the suggestions, and "Stream B" means personal data about third parties appearing in scraped event listings. Both are defined in the data processing brief.

---

## Phase 1: Personal data inventory

Retention has two layers, and they must be read together:

- **Workflow definition:** the preference profile and the Telegram chat ID are hardcoded into node parameters. They persist for as long as the workflow exists. No expiry.
- **Execution history:** the n8n instance runs `pruning.enabled: true`, `maxAge: 336 hours`, `maxCount: 10000`. Full payloads are stored (`storage.success: all`, `storage.error: all`), so every run writes the complete profile and chat ID to a SQLite file, deleted after a maximum of 14 days.

| # | Data category | Source | Purpose | Retention | Crosses EU border? |
|---|---|---|---|---|---|
| 1 | Telegram chat ID | Entered directly by the data subject into the Telegram node | Deliver the suggestion to a named recipient | Indefinite in workflow; 14 days in execution logs; indefinite in Telegram chat history | Yes. Telegram operates outside the EEA |
| 2 | Telegram chat ID | As above | Debugging and development via retained execution logs | 14 days | Undetermined. Instance hosting region unverified |
| 3 | Location, city level (Hamburg, DE) | Entered directly into the OpenWeatherMap node | Weather retrieval and indoor / outdoor branch selection | Indefinite in workflow; 14 days in logs | No. Sent as a bare city name, not linked to any identifier |
| 4 | Dietary preferences and aversions | Entered directly by the data subject into the agent prompt | Generate a personalised evening suggestion | Indefinite in workflow; 14 days in logs | Yes. OpenAI, United States |
| 5 | Financial data (20 to 30 euro evening budget, 35 to 45 euro dining budget) | As above | Generate a personalised evening suggestion | As above | Yes. OpenAI, United States |
| 6 | Physical activity data (running range six to seven kilometres, gym, swimming, cycling, paddleboarding) | As above | Generate a personalised evening suggestion | As above | Yes. OpenAI, United States |
| 7 | Media, humour and restorative preference statements | As above | Generate a personalised evening suggestion | As above | Yes. OpenAI, United States |
| 8 | Aspirations (fencing, wave surfing, cooking classes) | As above | Generate a personalised evening suggestion | As above | Yes. OpenAI, United States |
| 9 | Inferred evening availability pattern | Derived from system design: a fixed 17:30 daily trigger with a local weeknight constraint | Timing of delivery | Not stored as a discrete field. Implicit in the workflow | No |
| 10 | Names of artists, performers and directors in event listings (Stream B) | Scraped from Ticketmaster API, hamburg.com, stadtparkopenair.de, filmraum.net, abaton.de, kinopolis.de | Parse and extract tonight's events | 14 days in logs | Yes. OpenAI, United States (`Event Extractor` node) |
| 11 | Names of artists, performers and directors, with venue, date and time (Stream B) | As above | Input to an automated recommendation that ranks and selects between them | 14 days in logs | Yes. OpenAI, United States (`AI Agent` node) |
| 12 | Generated suggestion text, containing both Stream A and Stream B data | Produced by OpenAI | Delivery to the recipient | 14 days in logs; indefinite in the Telegram conversation | Yes. Telegram, outside the EEA |

### Incompatible purpose flag

**Rows 10 and 11.** The event listings were published by venues, promoters and ticketing platforms so that the public could find and attend performances. Stups repurposes them as input to an automated profiling and recommendation system, and transmits them to a large language model provider in the United States.

This is a different purpose from the one for which the data was made available. Article 6(4) compatibility is not obviously satisfied: the individuals named have no relationship with the controller, received no notice, and would not reasonably expect their name and appearance schedule to be processed this way. No compatibility assessment has been carried out.

### Historical processing flag

During development, the complete Stream A profile in rows 4 to 8 was transmitted to DeepSeek, whose servers are in China. The Berlin data protection authority has publicly found DeepSeek's transfers to China to be in breach of Article 46(1) GDPR, on the basis that China has no adequacy decision and no appropriate safeguards were demonstrated.

The node has since been disconnected and replaced with OpenAI. GDPR contains no exemption for testing, so this remains a past processing activity carried out without a valid transfer mechanism. It is recorded here rather than removed.

---

## Phase 2: Role map

### A note on the client role

This lab template assumes an external client. Stups has none. It is a personal project with one recipient, who is also the builder. This produces an unusual structure that must be stated rather than glossed over:

- For **Stream A**, the builder is simultaneously the controller and the sole data subject. Self determination does not remove controller obligations towards the processors in the chain, and it does not remove the transfer rules in Chapter V.
- For **Stream B**, the builder is a controller processing data about people who are not him, who have not been informed, and who have no way to reach him.

Stream B is where the controller obligations actually bite. The household exemption in Article 2(2)(c) is sometimes raised for purely personal projects. It is not relied on here, because the exemption is read narrowly and does not sit comfortably with systematic collection of third party data from six external sources.

### Role map table

| Entity | Role | Processing activity | DPA in place? | Transfer mechanism |
|---|---|---|---|---|
| Builder / system owner | Controller (and, for Stream A only, also the data subject) | Determines all purposes and means | N/A | N/A |
| External client | None. No client exists | N/A | N/A | N/A |
| Ironhack (n8n host) | Processor | Hosts the self hosted Docker instance; stores full execution payloads in SQLite for up to 14 days | **No.** No DPA has been requested or signed | Undetermined. Hosting region unverified, so it cannot be established whether a transfer occurs at all |
| OpenAI (contracting entity OpenAI Ireland Ltd; processing in the US) | **Sub-processor**, engaged via Ironhack, not by the builder | Receives the full Stream A profile and Stream B event data in the `Event Extractor` and `AI Agent` nodes | **No DPA between the builder and OpenAI, and none is possible.** The API credential belongs to Ironhack, so Ironhack is OpenAI's customer. Any DPA runs between Ironhack and OpenAI | SCCs Module 2 and OpenAI's active EU to US Data Privacy Framework certification may apply to Ironhack's account. The builder cannot verify this and cannot rely on it. Default API processing is not EU resident |
| Telegram | `TBD — legal review`. Arguably an independent controller for its own platform data and a processor for message transit | Receives the chat ID and the generated message; retains the conversation indefinitely | **No** | None identified. No adequacy decision covers the operator |
| DeepSeek (historical) | Processor during development | Received the full Stream A profile | **No** | **None.** Transfer to China without adequacy or safeguards |
| Ticketmaster | Independent controller of its own event data. Source, not processor | Returns event listings. Receives no personal data from Stups | N/A | N/A. Data flows inbound only |
| hamburg.com, stadtparkopenair.de, filmraum.net, abaton.de, kinopolis.de | Independent controllers. Sources, not processors | Scraped. Receive no personal data from Stups | N/A | N/A. Data flows inbound only |
| OpenWeatherMap | Out of scope | Receives a bare city name. No personal data | N/A | N/A |

### DPA gaps

Three controller to processor relationships exist. **Zero have a Data Processing Agreement in force.**

1. **Ironhack.** The most overlooked. A hosting provider storing full execution payloads is a processor under Article 28, and Article 28(3) requires a written contract. None exists, and the builder cannot state the hosting country.
2. **OpenAI, as a sub-processor.** The builder uses an API credential issued by Ironhack. He is therefore not OpenAI's customer and cannot accept, inspect or rely on OpenAI's DPA. Three separate problems follow:
   - Article 28(2): a processor may not engage a sub-processor without the controller's authorisation. Ironhack selected OpenAI; the builder never authorised it and was not asked.
   - Article 28(4): Ironhack must bind OpenAI by contract on terms equivalent to its own. The builder cannot verify that this happened.
   - Purpose mismatch: even a well drafted Ironhack to OpenAI DPA would cover Ironhack's purposes as a training provider. The Stream B scraping of named individuals is the builder's own purpose and falls outside it.

   The builder's working assumption was that Ironhack had probably handled this. Article 5(2) requires the controller to demonstrate compliance, not to assume it upstream.
3. **Telegram.** No DPA, and no realistic route to obtaining one for a consumer messaging platform. The correct answer here may be to change the delivery channel rather than to paper the relationship.

### Residual node risk

`DeepSeek Chat Model1` remains present in the workflow, connected to `Event Extractor1` in a branch that is not wired to the trigger. The credential also remains on the instance. The node processes nothing today, but it is one connection away from resuming an unlawful transfer, and it will appear in any exported workflow JSON.

---

## Phase 3: Lawful basis assessment

### Table

| # | Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|---|
| 1 | Weather retrieval and indoor / outdoor branch selection | N/A, no personal data | A bare city name is sent with no identifier attached, so no lawful basis is required | No |
| 2 | Generate a personalised evening suggestion from the recipient's own profile (Stream A) | Consent, Article 6(1)(a) | The data subject entered his own preferences directly for this single stated purpose and can withdraw at any time by disabling the workflow | No |
| 3 | Deliver the suggestion to the recipient via Telegram (Stream A) | Consent, Article 6(1)(a) | The recipient supplied his own chat ID for the purpose of receiving these messages | No, on the basis. Yes on the transfer, see below |
| 4 | Retrieve and parse event listings containing named individuals (Stream B) | Legitimate interests, Article 6(1)(f) | Extracting what is on tonight from published listings is a minimal use of already public professional information; LIA below | Yes |
| 5 | Use named individuals' events as input to an automated ranking and recommendation (Stream B) | `TBD — legal review` | Repurposing public listings into automated profiling input, with a transfer to the US and no notice to the individuals, is not clearly covered by any Article 6 basis; LIA below fails part two | Yes |
| 6 | Retain full execution payloads for debugging (Streams A and B) | `TBD — legal review` | This purpose was never designed or documented; it exists because the platform defaults to storing complete payloads, and no basis was ever considered | Yes |

### Why consent works for Stream A and nothing else does

Consent is often the weakest basis, because in most systems it is neither freely given nor specific. Here it is unusually clean: the data subject is also the controller, so there is no imbalance of power, no bundling, and no ambiguity about what he agreed to. Withdrawal is a single click.

Two honest caveats. Consent under Article 7 must be demonstrable, and no consent record exists, only the fact that the person typed his own preferences in. And consent does not cure an unlawful international transfer. Article 49(1)(a) does allow explicit consent as a transfer derogation, but it is intended for occasional transfers, not a scheduled daily flow, so it is not relied on here.

### Legitimate Interests Assessment: Purpose 4, parsing event listings

**Part one: is the interest legitimate?**

Yes. The concrete need is to know which cultural events are happening in Hamburg tonight, so that a suggestion can reference something real rather than inventing it. The data involved is professional information already published by the individuals' own promoters and venues, precisely so that the public will see it. Reading a public listings page is an ordinary and expected use.

**Part two: is the processing necessary?**

Yes, but only in a narrow form. There is no way to know what is on tonight without reading listings, and performer names are structurally inseparable from event listings, since the name usually *is* the event. So collecting them is unavoidable.

The current implementation is broader than necessary, however. Full page HTML is fetched and converted, then passed wholesale to a language model, rather than extracting only the event title, date, venue and time first. The `Event Extractor` node receives far more than the minimum. So the purpose is necessary but the method is not minimised.

**Part three: does the individual's interest override?**

On balance, no, for this purpose. A performer whose gig is advertised publicly has a low expectation of privacy in the fact that the gig is happening. The privacy impact of one person reading that listing is close to nil. There is no sensitive inference, no contact, no decision about the performer, and no publication.

Two factors pull the other way and must be recorded. The individuals received no notice and have no practical way to object, since they do not know the system exists. And their names are transmitted to a US provider under a sub-processor arrangement the controller cannot verify, which is a transfer they never contemplated.

**Conclusion:** legitimate interests is available for Purpose 4, conditional on two fixes: minimise extraction to the event fields actually needed before any model call, and establish a documented transfer mechanism. Without those, the LIA passes on principle and fails on execution.

### Legitimate Interests Assessment: Purpose 5, automated ranking

**Part one: is the interest legitimate?** Yes, weakly. Producing a useful personalised suggestion is a genuine, if modest, private interest.

**Part two: is the processing necessary?** **No.** A suggestion could be generated from event titles, dates and venues without the system needing to weigh named individuals against one another, and without their names leaving the EEA. A less intrusive route plainly exists. This part of the test fails.

**Part three: does the individual's interest override?** Not reached, because part two already fails. Recorded for completeness: the impact remains low, but the individuals are being ranked by an automated system, with no notice, no transparency about the logic, and no route to object.

**Conclusion:** `TBD — legal review`. The LIA cannot be completed with confidence in favour of the controller. Per the lab's own instruction, this is marked for review rather than guessed. The practical fix is to strip personal names before the ranking step, at which point the question disappears rather than needing a legal answer.

### Purpose 6: the undesigned purpose

Retaining full execution payloads is processing, and it needs a basis like any other. None was chosen, because the purpose was never recognised as one. `storage.success: all` and `storage.error: all` are platform defaults.

For Stream A, consent could arguably be extended to cover it, but only if the data subject actually knows it is happening, which he did not until this audit. For Stream B, no basis has been identified. Legitimate interests in debugging is arguable but has not been assessed.

Marked `TBD — legal review`. The straightforward remedy is technical rather than legal: reduce payload storage so that the personal data is never written in the first place.

---

## Phase 4: Risk and rights analysis

### 4.1 Article 9: is any special category data involved?

The instinct is to answer no and move on. That instinct should be resisted, because two categories in the Stream A profile sit close to the line and one of them is genuinely arguable.

**Dietary data: not special category.** The profile records a lean towards Spanish and European food, seafood, sushi, steak and tapas, a dislike of miso and most ramen, and avoidance of coriander led cuisines. Dietary information *can* reveal religious belief (halal, kosher) or philosophical belief (veganism), which would engage Article 9. It does not here. The pattern is omnivorous with no religious or philosophical exclusions, and the coriander aversion is a taste preference, a well documented one with a genetic component, not a marker of ethnicity or religion. This is stated explicitly because it is exactly the kind of field a careless audit would either miss or over-classify.

**Financial data: not special category.** Budget ranges are ordinary personal data. Article 9 has no financial category. They still warrant care, but not Article 9 care.

**Physical activity data: arguable.** Article 4(15) defines health data as data related to physical or mental health that reveals information about health status, and Recital 35 reads it broadly. The CJEU has also taken an expansive view of indirect revelation of special category data. Against that:

- A stated running range of six to seven kilometres does reveal a cardiovascular fitness baseline. It says something about the body, not just about a hobby.
- The line "physical activity restores me, not mental" is a self description of how the person recovers. It edges towards a statement about mental wellbeing rather than a leisure preference.

For the defence: none of this discloses a condition, diagnosis, treatment or impairment. Recreational capability is not health status, and reading Article 9 so broadly that "I go to the gym" becomes health data would make the category unworkable.

**Conclusion:** probably not Article 9, but not confidently enough to dismiss. Marked `TBD — legal review`. Two consequences follow regardless of the answer. First, for Stream A the point is largely contained, because Article 9(2)(a) explicit consent is available and the data subject is the controller. Second, it is not contained for the transfer: if this data is special category, sending it to a US sub-processor the controller cannot verify moves from a documentation gap to a materially higher risk.

### 4.2 Article 22: automated decision making

Article 22(1) requires three elements. Each is tested rather than assumed.

| Element | Present? | Reasoning |
|---|---|---|
| A decision | Yes | The system selects two specific suggestions from a larger candidate set and discards the rest |
| Based solely on automated processing | **Yes** | There is no human review step between the model output and the Telegram send. Nobody approves the message |
| Legal effects or similarly significant effects | **No** | An evening suggestion does not approach the threshold set by credit, employment, insurance or access to services |

**Conclusion: Article 22 is not engaged**, because the third element fails. This holds for Stream B as well: a performer's event proceeds whether or not the system recommends it, so no significant effect lands on them either.

That is the legal answer. The design fact behind it still deserves recording. Fully automated output with no human check is a quality risk even where it is not a compliance one, and this system has already demonstrated it: during development the agent proposed events that had already taken place. A wrong date reaches the recipient unreviewed. That is not an Article 22 problem, but it is the reason the Article 22 answer should be *argued* rather than waved through.

### 4.3 DPIA screening against the EDPB criteria

The EDPB guidance (WP248 rev.01) lists nine criteria, with two or more normally indicating that a DPIA is required.

| # | Criterion | Met? | Note |
|---|---|---|---|
| 1 | Evaluation or scoring, including profiling | **Yes** | A stored preference profile drives an automated ranking of candidate events |
| 2 | Automated decision with legal or similarly significant effect | No | Established in 4.2 |
| 3 | Systematic monitoring | Partial | Collection is systematic and scheduled daily, but it observes public listings, not individuals' behaviour |
| 4 | Sensitive data or data of a highly personal nature | **Yes** | This criterion is broader than Article 9. Financial ranges, physical activity and a restoration self description qualify as highly personal even if 4.1 resolves against Article 9 |
| 5 | Large scale | No | One recipient. A small daily volume of third party names |
| 6 | Matching or combining datasets | **Yes** | Weather, six independent event sources and a personal profile are combined in a single model call |
| 7 | Vulnerable data subjects | No | No indication |
| 8 | Innovative use or new technology | **Yes** | An LLM agent with autonomous tool selection |
| 9 | Processing prevents exercise of a right or use of a service | No | Not applicable |

**Four criteria clearly met, one partial.** On a mechanical reading of the guidance, that indicates a DPIA.

The honest answer is more qualified. Article 35(1) sets the actual test: processing likely to result in a **high risk** to rights and freedoms. With a single adult data subject who is also the controller, and a low volume of already public third party names, the real world risk is not high. The criteria count is inflated by factors that are about system design rather than exposure.

**Conclusion:** a full Article 35 DPIA is not mandatory on these facts, but the screening result should be documented rather than assumed away, and the position must be revisited the moment either of two things changes: a second recipient is added, or the system stops being personal. At that point the scale criterion flips and the assessment changes with it. `TBD — legal review` on the formal threshold; the screening itself is complete and recorded here, which is what accountability under Article 5(2) requires.

### 4.4 Data subject rights friction

**Stream A: rights intact in theory, unfulfillable in practice.**

| Right | Status |
|---|---|
| Article 15, access | The builder can read his own workflow, but the execution logs live in a SQLite database on an instance he does not administer. He could not produce a complete copy of his own data without asking Ironhack |
| Article 17, erasure | He can delete the workflow. He cannot verify deletion from OpenAI's retained API logs, cannot force deletion of the Ironhack execution history ahead of the 14 day prune, and cannot delete the message history held on Telegram's side |
| Article 7(3), withdrawal of consent | Genuinely simple. Deactivate the workflow. This one works |
| Article 20, portability | Available in principle, never exercised, no mechanism built |

The pattern: every right he can satisfy alone, he can satisfy easily. Every right that requires a processor to act, he cannot satisfy at all, because no DPA obliges any of them to help him.

**Stream B: rights are not merely difficult, they are structurally unavailable.**

- **Article 14, notice.** Never given. The disproportionate effort exemption in Article 14(5)(b) is the one exemption here with a real chance of applying, since contacting every performer scraped daily is plainly disproportionate. But the exemption is conditional: it requires appropriate compensating measures, expressly including making the information publicly available. No such measure exists. The exemption has not been assessed, and cannot currently be relied on.
- **Article 21, objection.** No route. The individuals do not know the system exists and have no way to find out.
- **Article 15, access.** If a performer did write, the builder has no process for locating their name across the execution history and no means of identifying them reliably.

**This is the sharpest finding in the audit.** For a person whose data Stups processes without their knowledge, every right in Chapter III is formally available and practically inaccessible.

### 4.5 Security and confidentiality risks (Article 32)

| Risk | Severity | Detail |
|---|---|---|
| Full payload logging | High | `storage.success: all` writes the complete profile and chat ID to disk in plain text on every run, for up to 14 days |
| Shared multi-tenant instance | High | The instance is shared across a cohort. The instance owner has full access to execution data. The builder has never established who else does |
| No audit logging | Medium | The community licence provides no audit log, no log streaming and no SSO. If data were accessed improperly, there would be no record. This is an Article 5(2) accountability gap as much as a security one |
| Exposed API credential | Medium | A Ticketmaster API key was exposed in plaintext during development and has not been rotated |
| Dormant DeepSeek node | Medium | Documented in Phase 2. One connection away from resuming a transfer to China |
| Hosting region unverified | Undetermined | Cannot be scored, because it is unknown whether execution data leaves the EEA at rest. The inability to answer this is itself the finding |

---

## Phase 5: Law stacking check

GDPR is not the only regime touching this system. Four others were screened. Two engage, two do not.

| Regime | Engages? | Bottom line |
|---|---|---|
| EU AI Act (Reg. 2024/1689, as amended by the Digital Omnibus in force 27 July 2026) | **Partly** | Not high risk. Transparency duties apply, with one dated deadline |
| ePrivacy Directive / German TDDDG | No, on current design | Would engage immediately if a second recipient were added |
| Data Act (Reg. 2023/2854) | No | Not a connected product; no IoT or related service data |
| Database right (Dir. 96/9/EC, German UrhG §87b) and site terms | `TBD` | Daily systematic extraction from six sources is not a data protection question, but it is a legal one |

### 5.1 AI Act: risk tier

**Not prohibited.** No Article 5 practice is present. No emotion recognition, no biometric categorisation, no social scoring, no untargeted facial image scraping.

**Not high risk.** Annex III lists eight areas: biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, and justice. A leisure suggestion for one adult falls in none of them. Worth noting that the timing question is moot anyway: the Digital Omnibus deferred stand alone Annex III obligations from 2 August 2026 to **2 December 2027**, and embedded product obligations to 2 August 2028.

**Limited risk, transparency tier.** This is where Stups actually sits.

### 5.2 AI Act: does the personal use carve out apply?

Article 2(10) disapplies the Regulation to obligations of **deployers** who are natural persons using AI systems in a purely personal non professional activity. The instinct is to claim it and stop. Three reasons not to.

**First, it covers deployer obligations only, not provider obligations.** The builder did not merely use a system someone else supplied. He built it. Under Article 3(11), putting into service includes supply of a system for **own use** for its intended purpose, which makes him a provider as well as a deployer. Article 2(10) does not reach that role.

**Second, the Commission's guidance reads the exception narrowly.** It is not a general escape hatch for hobby projects.

**Third, and most awkwardly, the activity is arguably not non professional.** Stups is coursework in a paid bootcamp undertaken to enable a career move into AI consulting, and it is being published on a public GitHub repository as a portfolio artefact. A system built to demonstrate professional competence, published to advance a career, is a strained fit for "purely personal non professional".

**Consistency note.** Phase 2 declined to rely on the GDPR household exemption in Article 2(2)(c). Claiming the AI Act personal use carve out here would look inconsistent, so the reasoning is set out rather than assumed. The two tests are different: Article 2(2)(c) GDPR turns on whether the processing has a purely personal character given that third party data is systematically collected, while Article 2(10) AI Act turns on whether the *activity* is professional. Both, on these facts, resolve the same way. Neither carve out is relied on.

### 5.3 AI Act: the obligations that actually apply

| Provision | Applies? | Detail |
|---|---|---|
| Article 50(1), disclose that the user is interacting with AI | No | The obligation lifts where it is obvious to a reasonably informed person. A Telegram bot messaging its own author qualifies |
| Article 50(2), machine readable marking of synthetic content | **Yes, from 2 December 2026** | Stups generates synthetic text. Article 50 applies from 2 August 2026, but Article 50(2) does not bite on systems already on the market at that date until 2 December 2026. Stups predates the cutoff, so it is a legacy system with a deadline |
| Article 50(4), disclosure of AI generated text published to inform the public | No | Nothing is published. Output goes to one private chat |
| Article 4, AI literacy | Yes, in substance | Applicable since 2 February 2025. Low bar, and this audit is itself evidence of it |

**The one concrete AI Act action: no output marking exists today, and Article 50(2) attaches on 2 December 2026.** That date sits inside the life of this project, so it belongs in the memo rather than in a footnote.

### 5.4 ePrivacy and TDDDG

**Not engaged on the current design**, for three reasons.

- §25 TDDDG (implementing Article 5(3) ePrivacy) governs storing or reading information on an end user's terminal equipment. Stups is a server side scraper. Where scraped sites set cookies, the obligation runs from those sites to the builder's own device, not from the builder to anyone.
- Article 13 ePrivacy on unsolicited communications targets direct marketing. Stups sends no marketing, and sends only to the person who set it up.
- Article 5(1) confidentiality of communications is not implicated by a sender messaging himself.

**The trigger to watch:** the moment Stups sends to any recipient other than its builder, Article 13 ePrivacy and §7 UWG on unsolicited electronic communication engage at once, and consent becomes a live requirement rather than a formality. Combined with the Phase 4 finding that adding a second recipient also flips the DPIA scale criterion, this is the single change that most alters the compliance picture.

### 5.5 Data Act

**Not engaged.** Regulation 2023/2854 applies mainly to connected products and related services, and to data processing service providers on cloud switching. Stups is neither. It generates no product or IoT data, and the switching obligations in Chapter VI fall on the cloud provider, not on a user of one.

### 5.6 The non data protection exposure: scraping

This falls outside a GDPR lens, which is precisely why it is easy to miss and worth stating.

Stups performs automated daily extraction from six sources: the Ticketmaster API and five websites scraped without a documented API agreement. Two issues follow.

- **Terms of service.** Most listings sites prohibit automated extraction. No source's terms have been reviewed. Ticketmaster is accessed through its official API, so that one is likely fine, subject to the licence terms.
- **Sui generis database right.** Directive 96/9/EC, implemented in German law at UrhG §87b, protects a database maker against repeated and systematic extraction of substantial parts. Daily scheduled extraction from a curated event database is the fact pattern the right was written for.

Marked `TBD`. The realistic exposure for one hobby project is low, but the audit should not pretend the question was asked and answered when it was not.

---

## Phase 6: Compliance memo

**To:** System owner, Stups
**From:** Internal audit, first pass
**Date:** 19 August 2026
**Re:** GDPR and adjacent regulatory position

### Bottom line

Stups is lawful in intent and non compliant in execution. The processing of the owner's own data rests on solid consent. Everything downstream of that consent fails, because three processors handle personal data and none is bound by any contract. The system also processes named performers scraped from six sources, people who do not know it exists and cannot reach it. That second stream, not the owner's own profile, is where the real exposure sits.

Nothing here suggests high risk to anyone. The gap is documentation and design, not harm. It would nonetheless not survive a regulator's first three questions.

### Three actions, in order

**1. Reduce what is written down (this week, no legal input needed).** Switch n8n execution storage from full payloads to errors only. Today every run writes the complete profile and chat ID to disk in plaintext for fourteen days, serving a purpose nobody chose. In the same pass, delete the dormant DeepSeek node and rotate the exposed Ticketmaster key.

**2. Own the OpenAI relationship (this month).** The API credential belongs to Ironhack, so the owner is not OpenAI's customer and cannot accept its DPA, verify its terms, or rely on its transfer safeguards. Open a direct account, accept the DPA, and replace the credential. This converts an unverifiable sub-processor chain into a documented controller to processor relationship.

**3. Strip names before the model call (next iteration).** Extract event title, date, venue and time, then discard performer names before any ranking. This closes the failed legitimate interests test on automated ranking and removes most of Stream B from scope entirely. It is cheaper than defending the processing.

### Residual risks after all three

Telegram remains unaddressed: no DPA, no transfer mechanism, no realistic route to either. Changing channel is the honest fix. Ironhack's hosting region is still unverified, and that question has not been answered. No Article 14 notice reaches Stream B individuals. AI Act Article 50(2) output marking becomes binding on **2 December 2026**. Database rights across the six scraped sources remain unassessed.

### What this memo is not

Not a legal opinion. Written by the system's builder, who is neither a lawyer nor independent. Items marked `TBD — legal review` are flagged because they require qualified advice, not because they are unresolved details. A DPIA screening was performed and documented; a full Article 35 DPIA was not.

---

## CFU 4: Accountability test

Article 5(2) makes the controller responsible for demonstrating compliance, not merely achieving it. The test is simple: if a regulator asked tomorrow, what could be produced? The gap between what exists and what would be asked for is itself the finding.

| A regulator would ask for | Exists today? | If not, what stands in |
|---|---|---|
| Record of processing activities (Article 30) | **No** | This audit and its brief are the closest thing, produced after the fact |
| Lawful basis, documented per purpose | **Partial** | Written for the first time in Phase 3 of this audit, not before |
| Consent record (Article 7(1)) | **No** | Only the fact that the owner typed his own preferences in. No timestamp, no logged act |
| DPA with each processor (Article 28) | **No** | None of the three. This is the central finding |
| Record of the international transfers and their mechanism | **No** | Transfers happen; no mechanism is documented for any of them |
| DPIA, or a documented reason one was not required | **Now partial** | Phase 4 screening exists as of today. Nothing existed before |
| Article 14 notice to Stream B individuals | **No** | Never given. No reliance on the disproportionate effort exemption assessed |
| Record of a past transfer to DeepSeek | **Now yes** | Documented in this audit. Was not recorded when it happened |
| Audit log of who accessed execution data | **No, and impossible** | The community licence provides none. The gap cannot be closed on this instance |

**The pattern.** Before this audit, the answer to almost every regulator question was nothing. After it, several answers become "see the audit." That is real progress on accountability, and it is also the point: accountability is a documentation discipline, and the system had none until it was audited. A working system that breaks no visible rules can still fail Article 5(2) entirely, because doing the right thing and being able to show it are different obligations.

One honest limit. This audit was written by the system's builder. Article 5(2) accountability is strongest when the evidence is independent. A self audit is a start, not a substitute for it.
