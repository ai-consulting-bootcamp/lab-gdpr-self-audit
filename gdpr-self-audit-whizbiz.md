# GDPR self-audit — Whizbiz: Messenger Accountant

**Author (builder and auditor):** Vittal Navale · **Date:** 19 August 2026 · **Basis:** Regulation (EU) 2016/679

Brief this audit is built from: [`data-processing-brief.md`](./data-processing-brief.md).

---

## CFU 1 — Recognize

**Categories of personal data present:** Telegram identifiers, free-text message content, receipt
photographs, extracted expense fields, customer name/address, order/delivery details, aggregated
revenue figures.

**Special-category data (Article 9):** Not collected by design, but **inferable** from unfiltered
receipt photographs — a pharmacy, clinic, place-of-worship or union receipt can reveal health,
religious belief or trade-union membership. Nothing in the current build inspects or restricts this.

**Cross-border flows:** Yes, on every transaction. OpenAI (US), Google Workspace (US), and Telegram
(Dubai, no EU adequacy decision) all receive personal data as part of the normal processing path.

---

## Phase 1: Personal data inventory

| Data category | Source | Purpose(s) | Retention period | Crosses EU border? |
|---|---|---|---|---|
| Telegram identifiers (user ID, chat ID, username) | Telegram, every message | Routing replies; session identification | Undefined — **TBD** | Yes — Telegram |
| Free-text message content | Typed by owner | Intent classification; invoice/calendar creation | Undefined — **TBD** | Yes — OpenAI, Telegram |
| Receipt photographs | Sent by owner | Vision extraction; archival copy in Drive | Undefined — likely indefinite | Yes — OpenAI, Google, Telegram |
| Extracted expense fields | Derived from photograph | EÜR bookkeeping, VAT record | 10 years (German tax law, §147 AO) | Yes — Google Sheets |
| Customer name & address (`Kunde`, `Addresse`) | Typed by owner about a third party | Invoice creation; income sheet; calendar entry | Undefined — likely indefinite | Yes — Google, OpenAI, Telegram |
| Order/delivery details | Derived from instruction | Invoicing, scheduling, revenue reporting | Undefined — **TBD** | Yes — Google |
| Aggregated revenue/profit figures | Derived from sheets | Owner-facing reporting; daily digest | Tied to underlying records | Yes — Google, OpenAI |

**Purpose-limitation flag:** the receipt photograph is collected for one purpose (expense
extraction) but is **also retained afterward** in Google Drive as an archival copy — a second,
separate purpose (archival/audit trail) that is not currently distinguished from the extraction
purpose, disclosed to the owner, or covered by its own retention rule. This is the clearest
purpose-limitation risk in the system and should be treated as its own row, not folded into
"extraction."

---

## Phase 2: Role map

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| Subscribing owner (client) | **Controller** — decides to record their own and their customers' data | Everything the bot does on their behalf | N/A (they are the controller, not a processor) |
| Me / Whizbiz (builder) | **Processor** on the subscription model, though I determine much of the technical means | Receipt extraction, bookkeeping, invoicing, storage, reporting | **No — none exists.** No Article 28 contract with any subscriber |
| OpenAI (GPT-4o, GPT-4o-mini) | Sub-processor | Vision extraction, intent classification | **No** — no DPA reviewed/signed, no transfer mechanism documented |
| Google (Sheets/Drive/Calendar/Docs) | Sub-processor | Bookkeeping storage, image archival, invoice generation, calendar | **No** — Google's standard DPA exists as a clickthrough but has not been reviewed or accepted as part of this build |
| Telegram | Independent controller for the messaging layer | Transports every message/photo/file | **Not obtainable in practice** — a consumer messaging app will not sign an Article 28 agreement with a small vendor; this is a disclosure obligation, not a contract to chase |
| n8n host | Sub-processor (orchestration) | Executes workflow, holds execution data | **No**, and **production host is not yet established** |

**International transfers:** three separate exports leave the EEA on the main path of every
transaction — OpenAI, Google, Telegram. For OpenAI and Google, the mechanism would be the EU–US Data
Privacy Framework where the specific entity is certified, otherwise Standard Contractual Clauses plus
a transfer impact assessment. **Neither has been confirmed or documented for this build.** Telegram is
the hardest case: no EU establishment, no adequacy decision, and no realistic path to an Article 28
agreement — the only honest mitigation is disclosure to subscribers, not a paper fix.

---

## Phase 3: Lawful basis assessment

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| Statutory bookkeeping (EÜR expense/income records) | Legal obligation (Art. 6(1)(c)) | German tax law (§147 AO) requires these records to be kept — the basis is the law itself | No |
| Receipt extraction (the vision-model call itself) | Contract (Art. 6(1)(b)) | Necessary to perform the subscribed bookkeeping service the owner signed up for | No |
| Invoicing (owner's own transaction with their customer) | Contract (Art. 6(1)(b)) — between owner and Whizbiz | Necessary to deliver the invoicing feature the owner subscribed for | No |
| Processing the **customer's** name/address on that invoice | **TBD — legal review** | The lawful basis sits with the *owner's* relationship to their own customer (their contract or legitimate interest in invoicing them), not with Whizbiz directly — Whizbiz's role here needs its own basis as processor, and the product currently supplies no Article 13/14 notice to that customer | **Yes** |
| Receipt image archival in Drive (beyond the extraction itself) | **TBD — legal review** | Possibly legitimate interest (audit trail) or folded into the legal-obligation basis for bookkeeping, but this has never been decided or documented as a separate purpose | **Yes** |
| Calendar booking of delivery dates | Contract (Art. 6(1)(b)) | Necessary to deliver the scheduling feature | No |
| Profit reporting / daily digest | Contract (Art. 6(1)(b)) | Necessary to deliver the reporting feature the owner subscribed for | No |
| Special-category data incidentally captured in receipt photos | **TBD — legal review** | No Article 9(2) condition currently applies or has been sought | **Yes** |

### Legitimate Interests Assessment — receipt image archival (the one purpose where LIA was considered)

1. **Is the interest legitimate?** Keeping an archival image alongside the extracted record supports
   dispute resolution and audit trail credibility — a concrete, plausible business need.
2. **Is the processing necessary?** Arguably not fully — the extracted structured fields already
   satisfy the statutory bookkeeping purpose; keeping the *whole image* indefinitely is a broader
   retention than the stated purpose requires, and a shorter retention (e.g., image deleted once the
   extraction is confirmed correct, or kept only for the same period as the ledger row it supports)
   would be less intrusive.
3. **Does the individual's interest override?** Given the risk that some images incidentally contain
   Article 9 data, and that there is no filtering or shortened retention, this weighs toward the
   individual. **I cannot complete this LIA with confidence — marking TBD, legal review.**

---

## Phase 4: Risk and rights analysis

**Special category data (Article 9).** Yes, inferable and unmitigated. A pharmacy, clinic,
place-of-worship or trade-union receipt reveals health, religious, or union data about the owner, and
the vision model receives the whole photograph with no pre-filter. No Article 9(2) condition
currently applies — explicit consent could in principle be sought for the owner's *own* data, but has
never been asked for, and could never cover data incidentally captured about anyone else.

**Automated decision-making (Article 22).** The system produces automated categorisations (expense
category, order intent) but not decisions with legal or similarly significant effects on a person.
Every output returns to the owner's own chat, where the owner reads and can correct it before it has
any downstream effect on a third party (e.g., before an invoice is actually sent). Article 22 is not
engaged, but this reasoning depends on the owner reliably acting as that check — the rolled-back
confirm/cancel gate would have made this explicit rather than implicit, and its absence is a real gap
even though it does not trigger Article 22 itself.

**DPIA trigger.** Applying the EDPB's nine criteria: **(1) special-category data at scale** — plausible
across a subscriber base, though unmitigated by design rather than by volume; **(2) matching or
combining datasets** — receipts, invoices, calendar and reports are joined per user; **(3) innovative
technology** — vision-model extraction plus LLM-based routing. Three criteria plausibly apply; two is
the EDPB's usual threshold. **A DPIA is very likely required before onboarding real subscribers, and
none has been conducted.**

**Data subject rights friction.** The hardest right to support is **the customer's right to access or
object** — a person named on an invoice has no relationship with Whizbiz, no notice that their data is
held, and no lookup mechanism exists to find or delete their record if they asked. The owner's own
**right of access** to their AI-processed data is comparatively easy (the sheets are directly
readable), but there is no per-record deletion path distinguishing statutory records (must be kept 10
years) from operational copies (chat history, Drive images, calendar entries) that should not be.

---

## Phase 5: Law stacking check

**AI Act cross-check.** Whizbiz is not a high-risk system under Annex III (no employment, credit,
law-enforcement or similar listed use case) — it is closer to a general business-automation tool, likely
outside the high-risk regime as currently scoped, though this is a hypothesis, not a completed
walkthrough of the compliance checker. It does not impose obligations GDPR doesn't already require for
this system; transparency about AI involvement (Article 50-type disclosure) is the main incremental
duty, and the product currently gives no explicit AI-processing notice to the owner.

**ePrivacy check.** No cookies, tracking pixels, or device-level tracking are used — Telegram is the
sole channel, and Telegram's own terms, not ePrivacy, govern the messaging layer itself. ePrivacy's
consent requirement is not currently engaged by this build.

**Data Act check.** N/A — no connected product, IoT device, or cloud-switching scenario is involved.

---

## CFU 4 — Verify: the accountability test

**Could I demonstrate compliance to a regulator using only the documentation this project currently
has?** No. There is no DPA with any subscriber, no processor agreement with OpenAI or Google reviewed
for this use, no transfer mechanism documented for any of the three cross-border flows, no DPIA, no
privacy notice (for the owner or their customers), and no retention schedule. The n8n workflow export
and the pitch/planning documents describe the system honestly, but none of them are compliance
artefacts — they would not answer a regulator's questions about lawful basis, transfers, or rights
handling. This gap is the direct input to the compliance memo below.
