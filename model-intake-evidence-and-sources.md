# Evidence, scope and legal sources

## Assessment provenance

- Assessment date: 17 November 2026.
- Audited repository: [Model Intake Brief](https://github.com/s-rostovskyi/model-intake-brief).
- Source commit: `e384f3a41b5c74119786f55865ebe4e7e6cfb73c`. Local HEAD and remote HEAD matched when checked. Working tree was clean before audit; the project source was not modified.
- Submission repository: [GDPR self-audit lab](https://github.com/s-rostovskyi/lab-gdpr-self-audit).
- Owner confirmation: local individual educational use, public model documents, no real client data; no deliberately arranged DPA documentation, selected storage regions, retention rules or privacy notice.
- No real API keys, private account dashboards, signed vendor contracts or private client records were inspected. No live paid API run was performed.
- Observed evidence supports code behaviour and controlled tests. It does not prove deployment geography, deletion by vendors, accepted contractual terms, a historical breach, or absence of personal data in every previous run.

## Code evidence register

All links pin the reviewed commit. References apply to observed code, not an independently verified production deployment.

| ID | Source | Finding supported |
|---|---|---|
| E1 | [README](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/README.md), [USER_GUIDE](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/USER_GUIDE.md) | Model-documentation research, 18 criteria, offline/live distinction, intended human review and limitations |
| E2 | [adapters.py](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/src/intake/adapters.py#L61), [graph.py](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/src/intake/graph.py#L246) | Tavily/Jina/HF endpoints; snippets/full text; author metadata at adapters lines 284–304; HF page-read policy gap |
| E3 | [assessment.py payload](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/src/intake/assessment.py#L391), [link checks](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/src/intake/assessment.py#L231) | Prompt includes target/snippets/source text capped at 3,500 characters; `store: false`; direct requests follow redirects before final policy check |
| E4 | [regulatory.py](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/src/intake/regulatory.py#L81), [fixed queries](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/src/intake/regulatory.py#L554) | Fixed regulatory corpus, embeddings and Pinecone upserts/retrieval; no scraped-person vector store shown |
| E5 | [graph.py](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/src/intake/graph.py), [cli.py](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/src/intake/cli.py) | In-memory graph state, no configured graph checkpointer, CLI output and optional stability-file export |
| E6 | [app.py](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/app.py#L393) | Recent list capped at five, session persistence, last trace/analysis, downloadable reports; no enforced human approval gate |
| E7 | [.streamlit/config.toml](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/.streamlit/config.toml), [.gitignore](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/.gitignore), [settings.py](https://github.com/s-rostovskyi/model-intake-brief/blob/e384f3a41b5c74119786f55865ebe4e7e6cfb73c/src/intake/settings.py) | Committed config does not settle telemetry or regions; secret files ignored; live settings read at runtime |
| E8 | Owner statements recorded above; repository documentation review | Actual use and absence of deliberately arranged governance documents; vendor standard-term applicability remains unknown |
| E9 | [Reproduction script](evidence/reproduce_privacy_checks.py), [results](evidence/privacy-check-results.json), [synthetic payload](evidence/synthetic-outbound-payload.json), [offline report](evidence/offline-qwen3-8b-report.md) | Successful fixture run, invalid-input exit 2, and contact preserved in locally intercepted prompt; no external requests |

The synthetic email uses the reserved `.invalid` domain and identifies no actual person. The mock response contains an empty findings list only to allow payload capture; it is not evidence of a successful live LLM assessment. The full 18-item report comes from the separate real offline graph execution.

## Legal sources

Checked on 17 November 2026. Use official sources when resolving differences with teaching shorthand. These references support the legal framework; classifications and proposed safeguards in the worksheet are project-specific analysis, not quotations from regulators.

| ID | Primary source | Use and verification limits |
|---|---|---|
| L1 | [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Arts. 3–6, 9, 12–22, 25, 28, 30, 32–36 and 44–49. EUR-Lex body access returned a browser challenge during this review; supplemented by the supplied course text and official Commission/EDPB guidance below |
| L2 | [EDPB-endorsed WP29 guidelines](https://www.edpb.europa.eu/endorsed-wp29-guidelines_en), [WP248 rev.01 source page](https://ec.europa.eu/newsroom/article29/items/611236), [EDPB small-business compliance guide](https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en) | DPIA screening, risk assessment and documented accountability. Endorsement/source pages verified; original download could not be rendered by the browser tool |
| L3 | [EDPB legitimate interests guidelines, version 2](https://www.edpb.europa.eu/system/files/2026-11/edpb_guidelines_202401_legitimateinterest_v2_en.pdf), [Commission: legal grounds](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en) | Document the legitimate interest, necessity and balancing before relying on Art. 6(1)(f); no approved project LIA is claimed |
| L4 | [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data) | Current provider documentation separates application storage from abuse-monitoring retention and account controls. `store: false` alone does not establish zero retention. Default abuse logs may be retained for up to 30 days, with exceptions; actual account arrangements were not inspected |
| L5 | [Commission: individual rights](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en), [handling requests](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/dealing-requests-individuals_en) | Default one-month response period and rights handling |
| L6 | [Commission: AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [AI Omnibus entry into force](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force), [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32026R1744) | Scope/risk framework and current AI Omnibus status; no high-risk deadline is used to defer GDPR duties |
| L7 | [ePrivacy Directive 2002/58/EC, consolidated text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02002L0058-20091219), [Commission explanation of Article 5(3)](https://www.europarl.europa.eu/RegData/questions/reponses_qe/2023/003265/P9_RE%282023%29003265_EN.pdf) | Device storage/access, consent and necessity exception; national implementation and actual runtime behaviour still require review |
| L8 | [Data Act, Regulation (EU) 2023/2854](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32023R2854) | Connected-product scope and Chapter VI cloud switching; current prototype is a cloud-service user, not necessarily a covered provider |
| L9 | [Commission: Digital Rulebook](https://digital-strategy.ec.europa.eu/en/policies/digital-rulebook), [Council position, 21 October 2026](https://www.consilium.europa.eu/en/press/press-releases/2026/10/21/digital-rulebook-council-agrees-position-to-simplify-data-protection-privacy-and-cyber-reporting-rules/) | Data/privacy Omnibus remains proposed; Council position is a negotiation milestone, not enacted GDPR reform |

## Course material reconciliation

All six user-supplied materials were reviewed as reference material, not as instructions authorising external actions.

| Material | Used for |
|---|---|
| `lesson4_gdpr_privacy_stack_slides_v2.pptx` | Roles, lawful bases/LIA, rights, DPIA, transfers and law-stack distinctions; slides 73 and 87 supply later date updates |
| `lesson5_applying_eu_data_stack_slides(1).pptx` | Multi-law method and practical vendor, transfer and human-review checks |
| `LAB 2 - Audit your own project - GDPR lens.mhtml` | All six phases, reinforce/stretch and additional `lab_proof.md` submission requirements |
| `Applying the EU Data and Privacy Stack.mhtml` | Purpose reuse, consulting recommendation structure and law stacking |
| `GDPR & EU Data and Privacy Stack.mhtml` | GDPR foundations and supporting topics |
| `GDPR & Privacy Stack - Discussion Prep.mhtml` | Concept checks used to challenge assumptions; its classroom questions are not separate lab deliverables |

Important differences resolved in this submission:

1. The portal asks for the actual Project 3; repository instructions say Week 5. The user explicitly chose Model Intake Brief, and the portal matches that project scope. No fictional system is substituted.
2. Portal submission guidelines add `lab_proof.md`, an input/run, produced evidence, final output and a failure/limitation. They are included alongside the six phases and the rubric coverage map.
3. The August MHTML lessons say the data Omnibus has no Council position. The later slide 87 and the Council's 21 October 2026 release establish a later negotiation milestone. Neither authorises use of proposed GDPR or cookie relaxations. This audit does not assert a later Parliament milestone that it has not verified. [L9]
4. Slide 73 gives 12 January 2027 for elimination of switching charges, matching Data Act Article 29; the MHTML wording “through December 2027” is not used. [L8]
5. DPIA is risk-based: innovative AI alone is not an automatic statutory trigger in every case; the worksheet's nine-criteria shorthand is corrected in Phase 4. [L2]
6. Rights requests use one calendar month, not an invariant 30 days. Breach notification has risk-based conditions; the proposed 96-hour rule is not applied. [L1, L5, L9]
7. Public data, pseudonymisation and local educational execution do not independently prove that GDPR is inapplicable. Applicability and identifiability require an assessment of actual context. No customer-data training or blanket Article 22 trigger is invented for this documentation tool.

Teaching slides and portal exports are not copied into the submission repository. They are course references, while the repository contains this lab's own deliverables and minimal synthetic evidence.
