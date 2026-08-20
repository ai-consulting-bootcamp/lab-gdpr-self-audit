# Data processing brief — Whizbiz (Messenger Accountant)

**System:** Whizbiz — a Telegram bot back-office assistant for German sole proprietors (Einzelunternehmer)
**Author:** Vittal Navale · **Date:** 19 August 2026
**Written for:** a Data Protection Officer who has never seen this project

---

## What the system does

Whizbiz lives inside Telegram. An owner forwards a photographed receipt and GPT-4o Vision extracts
vendor, amount, VAT rate, date and category into a German-format (EÜR) expense sheet, filing the
image to Google Drive. The owner types a short order instruction ("invoice Anna, €45, delivery
Friday") and GPT-4o-mini classifies it, fills a Google Docs invoice template, exports a PDF, books a
Google Calendar entry, and logs the sale as income. The owner asks a free-text question ("how did I
do this month?") and the bot reads the sheets back and reports revenue vs. profit. An optional daily
briefing uses GPT-4o with web search for a general news headline (no personal data involved in that
one call).

## What personal data does the system process?

- **Telegram identifiers** — user ID, chat ID, username, display name (present on every message).
- **Free-text message content** typed by the owner, which can incidentally contain names, order
  details, or other identifiable information about the owner or third parties.
- **Receipt photographs** — the whole image, unfiltered. A photograph can incidentally reveal
  special-category data (Article 9) about the owner: a pharmacy or clinic receipt (health), a
  place-of-worship donation (religious belief), a union-office receipt (trade union membership).
  Nothing in the workflow inspects or restricts this before sending it to the vision model.
- **Extracted expense fields** — vendor, date, gross/net/VAT amount, category, receipt link.
- **Customer name and postal address** (`Kunde`, `Addresse`) — typed by the owner about a third
  party (their own customer) for invoicing purposes.
- **Order/delivery details** — dates, amounts, invoice numbers.
- **Aggregated revenue and profit figures**, derived from the above.

## Where does that data come from?

All of it is submitted directly by the owner through Telegram — either typed or photographed. No
data is imported from an existing company database or purchased from a third-party source. The one
exception is the customer data (name, address): the owner obtained it from their own customer
directly, but Whizbiz never interacts with that customer and receives the data second-hand, from the
owner.

## What is the data used for? (each purpose listed separately)

1. **Routing and session identification** — Telegram identifiers, to reply to the right chat.
2. **Receipt/expense extraction** — vision-model processing of receipt photographs into structured
   bookkeeping fields.
3. **Statutory bookkeeping (EÜR)** — writing extracted fields to a German tax-compliant expense
   sheet, retained under German tax law.
4. **Invoicing** — using customer name/address and order details to generate a legally compliant
   German invoice.
5. **Calendar scheduling** — booking delivery dates against the owner's calendar.
6. **Profit reporting** — reading back income/expense data to answer the owner's questions and to
   run the scheduled daily digest.
7. **Archival** — storing the original receipt image in Google Drive after extraction.

Purposes 3 and 4 rest on a legal basis distinct from the others (see Phase 3); each is listed
separately because purpose limitation applies per processing activity, not per data category.

## Who processes it?

- **Whizbiz / me (the builder)** — orchestrates the n8n workflow; this is the point at which every
  category of data is read and routed.
- **OpenAI (GPT-4o, GPT-4o-mini)** — receives the receipt photograph and free-text messages for
  extraction/classification. A sub-processor, US-based.
- **Google (Sheets, Drive, Calendar, Docs)** — stores the structured bookkeeping data, the receipt
  image, the invoice PDF, and the calendar event. A sub-processor, US-based (Google Workspace/Cloud).
- **Telegram** — transports every message, photo and file between the owner and the workflow. Not a
  neutral pipe: it is an independent controller for the messaging layer (Telegram FZ-LLC, Dubai).
- **n8n (orchestration host)** — executes the workflow and holds execution logs. **Production
  hosting location is not yet established** — the current build has only run on a development/shared
  instance; this is a known gap, not a design decision.
- **QuickChart.io** — renders revenue/expense chart images from aggregated (non-personal) figures
  only.

## Where is the data stored and processed?

- Google Workspace (Sheets/Drive/Calendar/Docs) — US-headquartered provider; region of the specific
  workspace instance not yet confirmed.
- OpenAI API — US.
- Telegram — data transits Telegram's infrastructure (Dubai-based operator, not EU-adequate).
- n8n execution environment — **not yet established for production**; currently a
  development/bootcamp-shared instance.

No component of the current build runs on EU-only infrastructure. This is a genuine gap, not a
simplification for this brief.

## Does the system make or assist in any decision that affects people?

The receipt extractor and intent classifier make automated categorisation decisions (e.g., "this
expense belongs in category X", "this message is an order for €45"), but these are transactional
categorisation decisions, not decisions with legal or similarly significant effects on a person.
Every output lands back in the owner's own chat, where the owner reads it before it is acted on
further (e.g., before an invoice is sent to a customer) — human review is structurally present
because the owner is the one operating the bot, though there is no separate, formal
confirm/cancel gate (one was built and rolled back before the MVP deadline — see
`Learning.md`/`Project-Planning-Checklist.md` in the project repo). No profiling, scoring or ranking
of any data subject occurs.

## Confirmation: this system does process personal data

This is not a "no personal data" system. It processes the owner's own personal data (as the direct
Telegram user), and — more importantly — it processes a third category of data subject who never
interacts with the product at all: **the owner's own customers**, named and addressed on invoices and
income records, with no notice and no route to exercise their rights. That distinction, and the
unfiltered receipt-photo pathway to Article 9 data, are the two facts that drive the rest of this
audit.
