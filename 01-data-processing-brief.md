# Data Processing Brief — School Book Order Bot (Project 3)

Prepared for: Data Protection Officer / legal counsel review
Prepared by: Anand Narasipuram

## 1. Personal data processed
Yes. The system processes:
- **Telegram/WhatsApp chat identifiers** (online identifiers, Art. 4(1) GDPR) — used to route and attribute orders to a specific school contact.
- **Order content linked to an identifiable sender** — school name, class, requested books — tied to the chat identifier above.
- **Incidental content in photo-based orders** — handwritten order photos may contain names, phone numbers, or other handwriting beyond the book list itself. This content is not intentionally extracted or stored, but it is processed transiently by the vision model when the image is parsed.

No special-category data (Art. 9) is intentionally collected. Residual risk of incidental special-category exposure via photo uploads is assessed as low but non-zero.

## 2. Source of data
Directly from schools, submitted via text or photo message over WhatsApp/Telegram. No third-party sourcing, no purchased lists, no pre-existing company database.

## 3. Purposes (listed separately per Art. 5(1)(b) purpose limitation)
- (a) Parsing an individual incoming order
- (b) Matching parsed items against the book catalogue
- (c) Consolidating orders across schools into publisher-level bulk orders
- (d) Generating status replies to a school on request
- (e) Natural-language Q&A over historical order data, for the operator (father)

**Purpose-drift flag:** Purpose (e) was not part of the original order-intake design — historical order data collected for purposes (a)–(d) is now being queried conversationally for a use case that wasn't contemplated when that data was first collected. This is flagged for legal review rather than assumed compatible.

## 4. Processors / entities involved
- n8n (workflow orchestration)
- OpenAI API — GPT-4o / GPT-4o-mini (text and image parsing)
- Google Sheets (catalogue storage, order storage)
- Telegram / WhatsApp (message transport)

## 5. Storage and processing location
Two separate deployments, on separate infrastructure, with **no shared backend or data flow between them**:
- **India** — live. Schools and operator (father, Shirdi Hicon) based in India.
- **Germany** — planned. Currently in discussion with prospective schools; no live school data yet. Operator is based in Germany (EU).

Because infrastructure is not shared, the India deployment does not, at present, constitute an international transfer of EU personal data. The Germany deployment, once live, brings the system within GDPR's territorial scope independently of the India deployment's status.

**Open item:** exact processing region for the OpenAI API calls and Google Workspace/Sheets tenancy has not been confirmed and should be verified before the Germany deployment goes live, since OpenAI processing outside the EEA would itself constitute an international transfer requiring a transfer mechanism (see Phase 2).

## 6. Automated decision-making affecting people
No. Catalogue matching, price lookup, and order consolidation are operational steps, not decisions about people with legal or similarly significant effect (Art. 22 does not apply).

**Open item:** confirm whether the "mark fulfilled" step in the publisher-consolidation branch is reviewed by a human before the order is reported as sent, or whether it auto-marks. If auto-marked, this is a process gap worth naming even though it doesn't rise to an Art. 22 issue.
