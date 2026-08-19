# GDPR self-audit — AI Pre-Scan

**System audited:** AI Pre-Scan (Week 5 Project) · **Auditor:** Ugo Ahukannah · **Date:** 19 August 2026
**Companion audit:** the EU AI Act self-audit of the same system classified it **minimal risk**.

> First-pass assessment, not a legal opinion, not a DPIA, not a certification. Anything marked
> **TBD — legal review** is flagged deliberately rather than guessed.

---

## Data processing brief

**Does this system process personal data at all? Yes — and the project documentation says
otherwise.** `docs/proposal.md` states that "the subject of research is the **organisation**, not any
individual — no personal data is collected, and named individuals encountered in sources are not
recorded." That is the design intent. It is not what the implementation does, and the gap between
the two is the substance of this audit.

**What personal data is processed.** Nothing about individuals is *sought*. But the system fetches
whole public pages — careers pages, press releases, product changelogs, news articles — and those
carry names, job titles, direct quotes and author bylines. Those pages are chunked, embedded and
stored. So the categories in scope are: **names and job titles** of employees, executives and
authors; **statements attributed to them**; and the **embeddings derived from that text**, which
remain personal data while the individuals stay identifiable from it. One input can also be personal
data in its own right: a company name typed by the adviser is ordinary business data for a limited
company, but for a sole trader or an eponymous firm it identifies a person.

**Where it comes from.** Entirely third parties, never the data subject: Serper (web search and
domain resolution), a news API, GLEIF for legal-entity identity, and Wikidata. Worth noting that
GLEIF returns *entity* records rather than officer records, so the registry path — the one a reader
would assume is the personal-data source — is the cleanest part of the pipeline.

**What it is used for.** Six purposes, separated in Phase 1: extracting candidate AI systems from
sources; verifying quoted evidence against retrieved passages; a persistent cross-company vendor
corpus (designed, not yet built); optional report delivery to Notion; local scan history; and
evaluation, including two sample reports committed to a public repository.

**Who processes it.** The system itself; **OpenAI** (gpt-4o for extraction, text-embedding-3-small
for embeddings); **Pinecone** (vector index `ai-prescan`, one persistent namespace and one
`scan-<company>` namespace per scan); optionally **n8n and Notion** for delivery; and **GitHub**,
which hosts the evaluation artefacts.

**Where it is stored and processed.** Outside the EEA for every component that matters: OpenAI and
Pinecone are US services, and the repository is on GitHub. Local scan history sits on the operator's
own machine, and the web interface binds to 127.0.0.1 — it is a local tool, not a hosted service,
with no accounts, no analytics and no cookies.

**Does it make or assist decisions about people?** **No.** Its outputs are statements about a
company's software estate. No natural person is scored, ranked or flagged. A human adviser reviews
every report and settles the open questions with the client before anything is acted on, and the
system deliberately stops before the legal step.

---

## CFU 1 — Recognize

**Categories present:** identity data (names), professional data (job titles, employer), content
authored by or attributed to individuals (quotes, bylines), and derived data (embeddings of passages
containing the above). No contact details are sought, though a page fetched whole may contain them.

**Special-category data (Article 9):** not deliberately, and not systematically — but it is
**inferable at the edges**. A news article about a company's diversity programme, a disability
accommodation, or a union negotiation can reveal ethnic origin, health or trade union membership of
named individuals, and such a page would be ingested exactly like any other. There is no filter that
would stop it. The only plausible Article 9 condition here is 9(2)(e), data manifestly made public by
the data subject, which is narrow and would not cover a third party writing about someone.

**Border crossing:** **yes, on the main path.** Every fetched page reaches OpenAI for extraction and
Pinecone for embedding, both US. Delivery to Notion, when used, is a third US transfer. No transfer
mechanism is documented for any of them.

---

## Phase 1: Personal data inventory

One row per purpose, since purpose limitation applies per processing activity.

| # | Data category | Source | Purpose | Retention (known/estimated) | Crosses EU border? |
|---|---|---|---|---|---|
| 1 | Names, titles, quotes, bylines inside fetched pages | Public web via Serper / news API | **P1 — extract candidate AI systems from source text** | Not defined; page text passes through the model per scan | **Yes** — OpenAI (US) |
| 2 | The same text, chunked and embedded | Derived from P1 | **P2 — evidence-gate verification against retrieved passages** | **None. There is no deletion path in `store.py`** — the `scan-<company>` namespace has no TTL and nothing purges it | **Yes** — Pinecone (US), embeddings generated by OpenAI (US) |
| 3 | Vendor announcement and changelog text, including author names | Public web | **P3 — persistent cross-company vendor AI-feature corpus** (designed, not yet built) | Indefinite **by design** — the namespace exists precisely to persist across scans | **Yes** — Pinecone (US) |
| 4 | Quoted evidence carried in the finished report | Derived from P1 | **P4 — optional report delivery and filing** | Indefinite once filed | **Yes** — n8n / Notion (US) |
| 5 | Company name, scan metadata, finished report | Adviser input + system output | **P5 — local scan history (`store_jobs`)** | Indefinite; files persist until manually deleted | No — local disk |
| 6 | Source text and generated reports | Public web | **P6 — evaluation, ground truth, and two sample reports committed to the repo** | Indefinite, and **irreversible in git history** | **Yes** — GitHub (US) |
| 7 | Company name where the company is a sole trader or eponymous firm | Typed by the adviser | P1–P6 as above | As above | Yes |

**Purpose-limitation flag — and it applies to almost every row.** Every source page was published for
a purpose that has nothing to do with this system: a careers page exists to attract applicants, a
press release to announce news, a changelog to inform customers. AI Pre-Scan reuses that content to
infer a company's AI adoption. Reuse of lawfully published data is not automatically unlawful, but
two consequences follow that the project has never addressed:

- Because the data is **not obtained from the data subject**, **Article 14** transparency applies —
  individuals should in principle be told their data is being processed, within a month. The
  disproportionate-effort exemption in Article 14(5)(b) is arguable here and is probably where this
  lands, but it has to be *reasoned and recorded*, not assumed.
- **P3 is the sharpest case**: it lifts content out of a per-company scan and into a persistent,
  cross-company corpus. That is a genuinely different purpose from the one the data was fetched for,
  and it is the row I would put in front of a lawyer first.

**One check that came back clean.** I inspected both sample reports committed to the public
repository (`samples/personio.md`, `samples/ballymaloe-foods.md`) for names, attributed quotes and
titles. There are none: the report format quotes product and vendor evidence, not people. The
exposure in this system is at the **ingestion** layer, not the published-output layer — which is
worth stating precisely, because it changes which fix matters.

---

## Phase 2: Role map

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| **The adviser's firm** (intended user/client) | **Controller** — decides to scan a given company and why | Running scans, receiving and acting on reports | N/A between us today; **needed** if I ever host the tool for her |
| **Me / this project** | **Controller today** — I chose the purposes and means for development and the 12-company evaluation. Would become a **processor** if I hosted it on the adviser's instructions, or drop out entirely if she self-hosts | Development, evaluation, sample generation | — |
| **OpenAI** | **Processor** (gpt-4o extraction, text-embedding-3-small embeddings) | Receives full page text; returns extractions and vectors | **No. Needed.** Plus a Chapter V transfer mechanism |
| **Pinecone** | **Processor** | Stores embeddings and metadata in both namespaces | **No. Needed.** Plus transfer mechanism |
| **Serper** (web search / domain resolution) | **Independent controller** of its own service; we are the recipient of results | Supplies search results | Not a processor relationship — a source. Its terms govern reuse |
| **News API** | **Independent controller** | Supplies article data | As above |
| **GLEIF / Wikidata** | **Independent controllers** — public registries | Entity identity resolution | Not applicable; GLEIF returns entity records, not officers |
| **n8n / Notion** (optional delivery) | **Processors** | Receive and file the finished report | **No. Needed** if delivery is ever used with real client data |
| **GitHub** | **Processor** for the repository | Hosts evaluation artefacts and sample reports | Covered by GitHub's own terms; the transfer question stands |

**Transfers.** OpenAI, Pinecone, Notion and GitHub are all US. The mechanism would be the **EU–US
Data Privacy Framework** where the vendor is certified, otherwise **SCCs plus a transfer impact
assessment**. **None is documented today** — this is a gap, not a judgement that the transfers are
unlawful.

---

## Phase 3: Lawful basis assessment

| Purpose | Proposed basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| P1 — extract candidate systems | **Art 6(1)(f)** legitimate interests | Compliance advisers need a factual inventory before the law can be applied, and the data is already public | No, for reading and quoting |
| P2 — evidence-gate verification | **Art 6(1)(f)** | Checking claims against retrieved text is what stops the system fabricating — a strong interest in accuracy | **Yes** — the basis is sound; the *whole-page, no-retention* implementation is what fails, see the LIA |
| P3 — persistent vendor corpus | **TBD — legal review** | A cross-company, indefinite corpus is a materially different purpose from a single scan and needs an Art 6(4) compatibility assessment | **Yes** |
| P4 — report delivery | **Art 6(1)(f)**, or contract if operated for a client | Filing a report the adviser commissioned | No |
| P5 — local scan history | **Art 6(1)(f)** | Operational necessity: re-open a prior scan without re-running it | No |
| P6 — evaluation and public samples | **Art 6(1)(f)** | Measuring the system honestly is a legitimate interest, and the published samples were verified free of personal data | **Yes** if any future sample carries a name — publication changes the balancing test |

### Legitimate Interests Assessment — P1 and P2 (the core processing)

**1. Is the interest legitimate?** Yes, and concretely. An external adviser cannot apply the AI Act
to a client without knowing which AI systems the client runs, and small companies frequently have no
inventory. Establishing that from public evidence is a real and lawful business need, and the system
is deliberately built to refuse rather than invent when the evidence is absent.

**2. Is the processing necessary?** **Partly — and this is where it fails as built.** Reading public
pages and quoting the passages that evidence a finding is necessary; there is no less intrusive way
to establish what a company publishes about its own tooling. But **storing whole fetched pages,
embedded, indefinitely, in a US vector database** is not necessary to that purpose. The evidence gate
needs the validated passage and its provenance — URL, timestamp, hash — not the page. A less
intrusive design achieving the identical result exists, which is the definition of failing the
necessity limb.

**3. Does the individual's interest override?** **As configured, yes for storage; no for reading.**
An individual named on a careers page has a low expectation of being embedded in a vector store they
have never heard of, held indefinitely, in a third country, with no route to object — and with
Article 9 data ingestible by accident at the edges. Against that: the data is genuinely public, the
processing is not directed at the individual, no decision is made about them, and nothing is
published about them. **Minimise to the validated passage, add retention, and document the
transfers, and the balance tips back in favour of processing.** Until then, P2 should be recorded as
**LI available in principle, not satisfied in practice**.

---

## Phase 4: Risk and rights analysis

**Special category data (Article 9).** Not sought and not systematically present, but ingestible by
accident: a news story about a diversity initiative, a health-related absence, or a union
negotiation would be fetched and embedded like any other page. No Article 9(2) condition sits
comfortably — 9(2)(e), manifestly made public by the data subject, is the only candidate and does not
cover a third party writing about someone. The honest position is that this is unmitigated, and the
mitigation is minimisation at ingestion rather than a condition to rely on.

**Automated decision-making (Article 22).** **Not engaged, and this is the strongest part of the
system's privacy posture.** Article 22 concerns decisions producing legal or similarly significant
effects *on a data subject*. AI Pre-Scan produces statements about companies; no natural person is
scored, ranked, refused or profiled. Human review is structural rather than a safeguard bolted on —
the adviser verifies the report and settles open questions with the client before anything is acted
on, and the system refuses by design to produce legal conclusions at all.

**DPIA trigger.** Applying the EDPB's nine criteria: **innovative technology** applies (LLM
extraction plus vector retrieval); **matching or combining datasets** applies (search, news, registry
and vendor sources are combined per company); **cross-border transfer** arguably applies, since the
transfers are undocumented and a data subject would have no practical route to exercise rights
against them. The other six do not: no evaluation or scoring *of people*, no ADM with significant
effects, no systematic monitoring of individuals, no special-category data at scale, no large-scale
processing, no vulnerable data subjects. **Two to three criteria therefore apply, which crosses the
EDPB's two-criteria threshold.** Given that no individual is targeted, I would not assert that a full
DPIA is mandatory — but the Article 35(1) threshold assessment must be **performed and recorded**,
and on these facts it is more likely than not to conclude that a DPIA is required before any real
client use. **TBD — legal review**, and this is the single most consequential open question.

**Data subject rights friction.** All three of the usual ones bite, and the design cannot currently
serve any of them in time:

- **Access (Art 15).** Embeddings in Pinecone are keyed by company, not by person. There is no way to
  search for "all data about this individual" across scan namespaces, so a request could not be
  answered completely within a month.
- **Erasure (Art 17).** Worse than access: `store.py` has **no deletion path at all**. There is no
  function to remove a vector, a namespace or a page. Erasure would today mean deleting the entire
  index.
- **Objection to profiling (Art 21).** No mechanism exists, and no notice tells anyone the processing
  is happening, so the right cannot be exercised in practice. This links back to the Article 14
  question in Phase 1.

---

## Phase 5: Law stacking check

- **AI Act cross-check.** **Minimal risk** — the companion audit concluded this because every Annex
  III area is defined by its effect on natural persons and this system assesses organisations. It
  still imposes two duties GDPR does not: **Article 4** AI literacy, which applies at every tier
  (softened by Regulation (EU) 2026/1744 from *ensure* to *support*, but not removed), and **Article
  50(1)** disclosure that a user is dealing with an AI system.
- **ePrivacy check.** **Not engaged.** The interface binds to 127.0.0.1 with no accounts, no
  analytics and no cookies, so nothing is stored on or read from a user's terminal equipment under
  Article 5(3). Fetching public pages makes the system a *client* of other sites rather than a party
  setting anything on a user's device. If the tool were ever hosted as a web service, this answer
  changes immediately.
- **Data Act check.** **N/A** — no connected-product data, no IoT, no cloud-switching scenario.

---

## CFU 4 — The accountability test

**Could I demonstrate compliance to a regulator using only the documentation this project has
today? No.** The project is unusually well documented — architecture, provenance contract, evaluation
results, a lessons file, an ethics section — but those are **engineering** records. Accountability
under Article 5(2) needs a different genre of document, and none of it exists:

| Regulator would ask for | Exists? |
|---|---|
| Records of processing activities (Art 30) | **No** — Phase 1 of this audit is the closest thing that has ever existed |
| DPAs with OpenAI, Pinecone, Notion (Art 28) | **No** |
| Transfer mechanism and TIA for US processors (Ch. V) | **No** |
| Documented LIA | **No** — Phase 3 is the first |
| DPIA or a recorded Art 35(1) threshold assessment | **No** |
| Privacy notice / Art 14 reasoning | **No** |
| Retention schedule | **No** — and no deletion path in code to enforce one |
| Breach detection and 72-hour notification procedure | **No** |

The one genuine accountability asset the project does have is its **provenance contract**: every
finding carries a URL, a retrieval timestamp and a hash, with zero provenance violations measured
across 64 findings. That is exactly the kind of evidence a regulator likes, and it exists because it
was built for *accuracy* rather than for compliance. It is worth saying plainly: the system's
engineering discipline is real, and it has simply never been pointed at data protection.
