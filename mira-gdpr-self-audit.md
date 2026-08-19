# MIRA — GDPR Self-Audit

**Student:** Marija Kavaliauskaite

**Project:** MIRA Project 3 (V4 Brand World and shared platform services)

**Assessment date:** 19 August 2026

**Status:** Educational first-pass audit; not a legal opinion, DPIA, certification, or claim of GDPR compliance.

## Scope and evidence boundary

This self-audit applies the GDPR lens to the actual MIRA Project 3 implementation. It reuses the earlier MIRA GDPR audit where the legal analysis remains relevant and checks technical statements against the Project 3 repository at commit `c6d9b61`. Primary implementation evidence is the MIRA system brief, AI/data inventory, audit architecture, environment-variable template, Drizzle schema, and owner-scoped server routes. MIRA V3 remains active but data-isolated; this report focuses on V4 and shared authentication, database, model, image, and storage services. Production deployment, operating legal entity, user population, processing scale, vendor legal entities/regions, contracts, retention, and operational policies are not evidenced and remain **TBD — legal review**.

## Data processing brief

MIRA is a private authenticated application that processes personal data; this is confirmed by its OAuth user table and its owner-linked journey records. The user supplies account identity data; quick context about a business, audience, intended feeling, and moodboard purpose; date and place of birth with optional time; recognition and creative-discovery answers; a creative brief; optional inspiration imagery and explanation; and selection/refinement instructions. The system generates messages, a structured Creative DNA record, campaign prompts, visual directions, and a final five-image moodboard. These are personal data where they relate to an identifiable user or depicted person and may contain inferred attributes.

Data come directly from the authenticated user, from the OAuth provider, and from AI-generated derivations. The purposes are authentication/account access, personalised creative synthesis, campaign/image generation, storage and retrieval of the user's work, and service security. Inputs and outputs are processed by the React/Express/tRPC application, MySQL/TiDB, Forge-backed chat completions (`gpt-5-mini` in the verified V4 services), Forge ImageService (`MODEL_GPT_IMAGE_2`), and Forge/S3-backed object storage. Birth-city lookup may use a platform map/geocoding service; its exact provider and role are **TBD — legal review**.

The code shows persistent structured records and private object storage, but production regions, cross-border access, backup locations, vendor training use, and retention periods are **TBD — legal review**. MIRA automates creative recommendations and imagery, not employment, credit, healthcare, legal, or similarly significant decisions. A user selects and refines creative directions; no Article 22-significant decision is evidenced.

## Phase 1 — Personal data inventory

| Data category | Source | Purpose(s) — one row per purpose | Retention period (known/estimated) | Crosses EU border? |
| --- | --- | --- | --- | --- |
| OAuth identifier, name, email, login method, sign-in timestamps | OAuth provider and user | Authenticate the user and maintain owner-scoped access | Session cookie code permits up to one year; database-record retention is **TBD — legal review** | **TBD — legal review** |
| Session cookie/token and OAuth state data | OAuth/platform service and application | Maintain an authenticated session and prevent login CSRF | OAuth-state cookie: ten minutes in code; session token: up to one year in code | **TBD — legal review** |
| Business/audience/purpose context and creative brief | User directly | Personalise Creative DNA and creative direction | **TBD — legal review** | **TBD — legal review** |
| Date, city, country, timezone, and optional time of birth | User directly; city lookup may enrich location/timezone | Supply V4 journey context and Creative DNA source data | **TBD — legal review** | **TBD — legal review** |
| Recognition and creative-discovery answers; conversation messages | User directly and Forge chat service | Generate bounded follow-up questions and synthesise Creative DNA | **TBD — legal review** | **TBD — legal review** |
| Optional inspiration image, filename/type/storage key, explanation, and signed-access data | User directly | Provide optional visual evidence for creative synthesis | **TBD — legal review** | **TBD — legal review** |
| Creative DNA, campaign plan/prompts, selections, preserve/avoid instructions | Inferred or generated from user inputs | Produce and refine personalised editorial directions | **TBD — legal review** | **TBD — legal review** |
| Generated visual sets and final five-image moodboard | Forge ImageService using derived prompts | Deliver the requested creative campaign output | **TBD — legal review** | **TBD — legal review** |
| Technical identifiers and service/security events, if retained by platform services | Application/platform interaction | Authentication security, abuse prevention, and fault diagnosis | Collection and retention are **TBD — legal review** | **TBD — legal review** |

No reuse for advertising, analytics, or general model training is verified. Any such reuse would be a new purpose requiring compatibility, transparency, and lawful-basis assessment before activation. V4 stores birth details even though no active V4 Human Design or numerology calculation is implemented; necessity for creative synthesis is therefore unresolved and should be reduced or justified.

## Phase 2 — Role map

| Entity | Role (controller / processor / joint controller) | Processing activity | DPA in place? | Transfer mechanism |
| --- | --- | --- | --- | --- |
| MIRA product owner / operating legal entity | Likely controller | Determines the purposes and essential means of the MIRA service | Not applicable internally; controller identity is **TBD — legal review** | Not applicable |
| Marija / Project 3 team | Acts for the controller in the evidenced build; a separate processor role depends on the operating arrangement | Builds and operates private staging and handles project data under the controller's authority | **TBD — legal review** | **TBD — legal review** |
| Manus OAuth/platform | Likely processor for authentication; any independent purposes require separate role analysis | OAuth identity, session, and platform authentication | **TBD — legal review** | **TBD — legal review** |
| MySQL/TiDB hosting provider | Processor if it hosts MIRA records on instructions | Stores users, journeys, messages, Creative DNA, and visual-set state | **TBD — legal review** | **TBD — legal review** |
| Forge chat-completion service | Processor if it uses prompts only on MIRA's instructions | Adaptive questions and structured Creative DNA synthesis | **TBD — legal review** | **TBD — legal review** |
| Forge ImageService | Processor if it uses prompts/images only on MIRA's instructions | Generates visual directions and moodboard images | **TBD — legal review** | **TBD — legal review** |
| Forge storage gateway / S3 provider | Processor | Stores uploaded and generated image objects; issues signed access | **TBD — legal review** | **TBD — legal review** |
| Map/geocoding service, if active for birth-city lookup | Processor or independent controller depending on service terms | Resolves city/place data and timezone | **TBD — legal review** | **TBD — legal review** |

Every entity acting as processor needs an Article 28 DPA. A vendor that reuses prompts or images for its own model training or service-improvement purposes may be an independent or joint controller for that processing rather than a processor. Vendor terms, legal entities, subprocessors, processing regions, adequacy coverage, SCCs, and supplementary measures are all **TBD — legal review**.

## Phase 3 — Lawful basis assessment

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
| --- | --- | --- | --- |
| Authenticate the user and maintain owner-scoped account access | Contract | Identity and session processing appear objectively necessary to provide the private service the user requests. | Confirm controller, terms, and whether a persistent account is necessary: **TBD — legal review** |
| Collect business/creative context and answers; generate Creative DNA | Contract | These inputs and inferences are integral to the requested personalised creative-direction service, subject to minimisation. | Confirm scope and necessity of every field: **TBD — legal review** |
| Generate, store, and display campaign plans, visual directions, and the moodboard | Contract | Processing is required to create and deliver the core output selected by the user. | Retention after delivery is **TBD — legal review** |
| Process an optional inspiration image and explanation | Contract | The user deliberately selects an optional feature to personalise the requested output; a no-upload route must remain available. | Incidental Article 9/third-party content and vendor image use: **TBD — legal review** |
| Collect and use detailed birth data as creative context | Contract proposed, but necessity is not established | The code stores the fields, but no active V4 numerology or Human Design calculation is implemented, so necessity for contract performance is unproven. | **Yes — TBD — legal review**; minimise or remove unless evidence establishes necessity |
| Maintain proportionate security and diagnostic records, if collected | Legitimate interests | Protecting accounts and the service can be a legitimate interest if logging is necessary, proportionate, and expected. | **Yes — TBD — legal review** pending the LIA and actual logging inventory |

An interface label or recorded product consent does not by itself choose the GDPR Article 6 basis. If an image or free text contains Article 9 data, an additional Article 9 condition is required independently of Article 6: **TBD — legal review**.

### Legitimate Interests Assessment — service security and diagnostics

1. **Purpose test — is the interest legitimate?** MIRA has a concrete interest in protecting authenticated accounts, preventing abuse, investigating failures, and maintaining availability. This is lawful and sufficiently specific in principle, but the controller must document the exact events and threats covered.
2. **Necessity test — is processing necessary?** Minimal authentication, error, access, and security events may be necessary because account misuse and service failures cannot be managed reliably without evidence. Less intrusive measures must be tested: omit content and full prompts from logs, pseudonymise identifiers, restrict access, redact payloads, and use short purpose-based retention.
3. **Balancing test — do individual interests override?** Users expect reasonable security logs in a private authenticated service, but they do not reasonably expect intimate free text, birth details, or images to appear in diagnostic logs. The balance may favour MIRA only with minimisation, access controls, short retention, notice, and an objection assessment; actual logging and safeguards are not evidenced, so the final conclusion is **TBD — legal review**.

## Phase 4 — Risk and rights analysis

### Special-category data — Article 9

MIRA does not request Article 9 data as a defined input. Free text, birth context, inspiration imagery, or Creative DNA may nevertheless reveal or infer health, ethnicity, political or religious beliefs, sexual orientation, or other protected information. A photograph is not automatically biometric data; Article 9 biometric data arise where specific technical processing is used for unique identification, which is not evidenced here.

MIRA should avoid sensitive inference, warn against unnecessary sensitive or third-party submissions, and define isolation/deletion handling. No Article 9 condition is established for incidental or inferred special-category data: **TBD — legal review**.

### Automated decision-making — Article 22

Article 22 does not appear to apply. MIRA generates creative synthesis and imagery and allows the user to select/refine directions, but no solely automated decision producing legal or similarly significant effects is evidenced. This must be reassessed if outputs later rank people, determine access to services, or drive consequential employment, credit, health, or similar decisions.

### EDPB DPIA trigger assessment

| Criterion | Assessment for MIRA |
| --- | --- |
| Evaluation or scoring | **Appears relevant:** Creative DNA evaluates and structures personal creative attributes. |
| Automated decisions with legal/similarly significant effects | **Not evidenced.** |
| Systematic monitoring | **Not evidenced.** |
| Special-category or highly personal data at scale | Highly personal or incidental sensitive data are possible; scale is **TBD — legal review**. |
| Large-scale processing | **TBD — legal review**; private staging does not establish production scale. |
| Matching or combining datasets | **Not evidenced** for V4; vendor-side matching is **TBD — legal review**. |
| Vulnerable data subjects | **Not evidenced**; target-user ages and exclusions are **TBD — legal review**. |
| Innovative technology | **Applies:** structured generative-AI inference and image generation are innovative processing. |
| Cross-border processing that may impede rights exercise | Locations, subprocessors, and rights support are **TBD — legal review**. |

Evaluation/scoring and innovative technology appear to meet two criteria, with highly personal data also plausible. A pre-deployment DPIA is strongly recommended. Whether Article 35 legally requires it depends on scale, final purposes, geography, and the competent supervisory authority's list: **TBD — legal review**.

### Data-subject-rights friction

**Access and portability:** owner predicates make user-level retrieval technically plausible, but no complete export workflow is evidenced. A response would need account fields, raw answers, messages, images, Creative DNA/inferences, prompts/provenance where personal, generated outputs, and processor-held copies in a commonly usable format.

**Erasure:** database foreign keys provide some cascade behaviour, and V3 has soft-deletion/revocation logic, but an end-to-end V4 erasure workflow covering object storage, generated/derived assets, vendor copies, caches, and backups is not evidenced. **Rectification:** factual inputs and misleading inferences need correction or regeneration routes; the code's owner-scoped editing/refinement features do not prove a GDPR rectification process. **Objection:** any legitimate-interest security/logging processing needs an intake and balancing workflow. Current ability to meet one-month rights deadlines is **TBD — legal review**.

## Phase 5 — Law stacking check

- **AI Act:** MIRA was previously assessed as limited risk / transparency rather than Annex III high risk. AI interaction disclosure, AI literacy, machine-readable marking of synthetic outputs, and context-appropriate disclosure for generated/manipulated imagery may add AI-specific duties alongside GDPR.
- **ePrivacy:** authentication and OAuth-state cookies are implemented and appear functionally necessary; the session cookie may persist for up to one year. No analytics or marketing trackers are evidenced. Exemption, duration, notice, and any other device storage/access are **TBD — legal review** under applicable national ePrivacy law.
- **Data Act:** no connected product or IoT data are evidenced. Cloud/data-processing-service switching rules may affect MIRA's infrastructure contracts, but material applicability to MIRA's role and services is **TBD — legal review**.

## Phase 6 — Compliance memo

**To:** MIRA Data Protection Officer / legal counsel

**From:** Privacy audit team

**Subject:** Project 3 pre-deployment GDPR assessment

### Bottom line

**PROCEED WITH CONDITIONS.** MIRA's private, owner-scoped creative workflow can progress, but production processing should not begin until data necessity, vendor terms and transfers, retention, rights operations, and the DPIA decision are documented.

### Top three actions

**1. Finalise the processing record and minimise the V4 journey.** Map every OAuth field, questionnaire answer, birth field, message, image, Creative DNA attribute, prompt, visual output, log, and storage location to one explicit purpose and Article 6 basis. Remove exact birth time, city, country, or timezone unless product evidence shows they are necessary: the implementation stores them, while no active V4 numerology or Human Design calculation is verified. Approve purpose-specific retention and publish layered notices at account creation, free-text entry, and image upload.

**2. Close the processor and transfer gap before live data flows.** Identify the legal entities, roles, regions, subprocessors, training/reuse terms, and deletion behaviour for Manus OAuth/platform, MySQL/TiDB hosting, Forge chat, Forge ImageService, S3-backed storage, and any geocoding service. Execute Article 28 DPAs where appropriate. For non-EEA access, record adequacy or SCCs, complete the necessary transfer assessment, and require support for access, erasure, incidents, audits, and subprocessor changes.

**3. Complete a DPIA and prove operational rights.** Assess Creative DNA evaluation, innovative generative AI, highly personal free text, birth context, and imagery against actual scale and the relevant supervisory-authority list. Test a full access export and V4 erasure across database rows, object storage, derived assets, provider copies, caches, and backups. Document owners, one-month response tracking, security logging limits, and breach escalation.

### Residual risks

Free text or images may still reveal third-party or Article 9 data, and Creative DNA may produce unwanted sensitive or stereotyped inferences. Processor deletion may lag in backups or derived systems. Vendor regions, subprocessors, and transfer arrangements may change after review and therefore require continuing monitoring.

### What this memo is not

This educational memo is **not a legal opinion, a DPIA, a certification, or evidence that MIRA is GDPR compliant**. The controller must engage qualified legal counsel before relying on it for compliance decisions.

## Reinforce — Accountability documentation inventory

| Documentation or evidence | Current state | Finding / next step |
| --- | --- | --- |
| Technical architecture and data/AI inventory | EXISTS | Project repository documents implemented services, data classes, and known deployment limits. |
| Database schema and owner-scoped access evidence | EXISTS | Drizzle schema and server queries link records to authenticated owners; retain test evidence. |
| Consent records for V3 image upload/analysis | EXISTS, outside primary V4 scope | Useful design precedent; does not establish V4 Article 6/9 compliance. |
| Records of processing activities (RoPA) | MISSING | Create a controller-approved record covering purposes, categories, recipients, transfers, retention, and safeguards. |
| Privacy notice and just-in-time notices | MISSING / not evidenced | Draft and version notices for account, free text, birth data, uploads, inference, and providers. |
| Article 28 DPAs and subprocessor inventory | MISSING / not evidenced | Obtain executed agreements and current subprocessor lists for each processor. |
| International-transfer register and assessment | MISSING / not evidenced | Record regions, remote access, adequacy/SCC mechanism, and supplementary measures. |
| Retention and deletion schedule | MISSING | Approve per-purpose periods, backup rotation, legal holds, and tested enforcement. |
| LIA for security/diagnostic processing | DRAFTED IN THIS AUDIT | Validate against actual logs and approve or select another lawful basis. |
| DPIA | MISSING | Complete before production or document with counsel why Article 35 does not require one. |
| Data-subject-rights procedure and test evidence | MISSING | Define intake, identity verification, search/export, correction, erasure, vendor propagation, and deadlines. |
| Incident-response and breach-notification plan | MISSING / not evidenced | Define detection, roles, risk assessment, processor escalation, documentation, and 72-hour decision path. |

### Revisited legal-review issue — international transfers

To resolve the repeated transfer **TBD — legal review**, counsel needs: each vendor's exact contracting entity; controller and processor establishments; production hosting and backup regions; locations of support/remote access; complete subprocessor lists; categories and volumes sent to each service; whether prompts/images are retained or used for training; DPA and security terms; deletion behaviour; and the intended transfer mechanism. The project team can prepare an architecture diagram, vendor questionnaire, data samples by field (not real user data), configuration screenshots, contract copies, and a region/subprocessor matrix. Counsel can then assess adequacy, SCC modules, transfer-impact risks, supplementary measures, and notice language efficiently.

## Stretch — Privacy by design for Creative DNA synthesis

Creative DNA synthesis is the highest-risk V4 activity because it combines identity-linked business context, birth details, intimate free text, optional visual evidence, and AI inference.

| Design principle | Current state of the system | Pass / Fail / Unknown | Required change |
| --- | --- | --- | --- |
| Data minimisation | Structured prompts are bounded, but detailed birth data are stored without an active V4 numerology/Human Design calculation. | FAIL | Remove or make unnecessary birth fields optional unless documented necessity and user value are established. |
| Purpose binding | V4 tables are separate and inputs feed a defined creative flow; vendor reuse/training restrictions are not evidenced. | UNKNOWN | Enforce purpose tags/configuration and contractual no-reuse controls; document any new purpose. |
| Access controls | Protected tRPC procedures and owner predicates are implemented; production IAM, staff access, and audit logging are not evidenced. | UNKNOWN | Document roles, least privilege, staff/vendor access, review cadence, and access logs. |
| Retention enforcement | Persistent records/object assets exist; no approved automated V4 deletion or anonymisation schedule is evidenced. | FAIL | Implement per-purpose expiry and tested deletion across database, objects, vendors, caches, and backups. |
| Subject-rights workflow | Owner-scoped retrieval helps, but no complete access/export/erasure workflow or one-month tracking is evidenced. | FAIL | Build and test request intake, export, correction, erasure, vendor propagation, and deadline monitoring. |
| Incident response | Application safeguards exist, but no documented breach detection and GDPR 72-hour notification process is evidenced. | UNKNOWN | Adopt and rehearse an incident plan with processor escalation and notification decision records. |

## Evidence consulted

- Official `lab-gdpr-self-audit` instructions and rubric.
- Completed `lab-gdpr-privacy-audit-mira` audit pack and optional controls.
- MIRA Project 3 repository at commit `c6d9b61`: `README.md`, `MIRA_SYSTEM_BRIEF_FOR_PEER_AUDIT.md`, `docs/MIRA_AI_AND_DATA_INVENTORY.md`, `docs/MIRA_ARCHITECTURE_FOR_AUDIT.md`, `docs/ENVIRONMENT_VARIABLES.md`, `drizzle/schema.ts`, authentication/cookie code, and owner-scoped V3/V4 database routes.
