# Data processing brief: Stups

**System:** Stups, a personal evening suggestion agent (n8n workflow `Stups v6`)

**Prepared for:** Data Protection Officer or legal counsel

**Date:** 19 August 2026

**Status:** first pass, prepared by the system's builder, not a legal opinion

---

## 1. What the system does

Stups runs automatically every evening at 17:30. It reads Hamburg weather, branches to an outdoor or indoor path, scrapes six public event sources, passes the results with a stored personal preference profile to a large language model, and sends two evening suggestions to a single Telegram chat. No human reviews the message before it is sent. There is one recipient, the builder. It is not offered to the public.

## 2. Recognize: does the system process personal data? (CFU 1)

**Recognition statement.** Yes. Stups processes personal data in two distinct streams, one about the recipient and one about third parties. The system was not obviously a personal data system at a glance, which is the point of recognising it explicitly rather than assuming it. This conclusion is justified, not asserted.

**Stream A: data about the recipient.** A Telegram chat ID is a persistent identifier tied to a specific account, and therefore to an identifiable person under Article 4(1). It is hardcoded in the workflow alongside a detailed lifestyle profile about the same person.

**Stream B: data about third parties.** The scraped listings contain names of performers, musicians, comedians and directors appearing at Hamburg venues: identifiable living people with no relationship to the system and no knowledge of it. Stream B is the one most likely to be overlooked, because it was not deliberately collected. Incidental collection is still collection.

## 3. What personal data is processed

| Stream | Data |
|---|---|
| A | Telegram chat ID (direct identifier, redacted in this repository as `[TELEGRAM_CHAT_ID]`) |
| A | Location at city level: Hamburg, Germany |
| A | Dietary preferences and aversions (leans Spanish and European, seafood, sushi, steak, tapas; dislikes miso and most ramen; avoids coriander led cuisines) |
| A | Financial data: an evening budget of roughly 20 to 30 euros, and a dining budget of 35 to 45 euros |
| A | Physical activity data: running range of six to seven kilometres, gym, swimming, cycling, stand up paddleboarding |
| A | Stated preferences about media, humour, and what the person finds restorative |
| A | Aspirations: fencing, wave surfing, cooking classes |
| A | Inferred: an evening availability pattern, derived from a fixed 17:30 daily trigger with a local weeknight constraint |
| B | Names of artists, performers, directors and other individuals in event and cinema listings, together with the venue, date and time at which they will be present |

## 4. Where the data comes from

Stream A was entered directly by the data subject, who is also the builder, and sits in plain text inside the n8n node parameters. Stream B is scraped from six public sources (the Ticketmaster Discovery API, hamburg.com music and sports pages, stadtparkopenair.de, filmraum.net, abaton.de, kinopolis.de), without notice to the individuals named. Weather comes from OpenWeatherMap and is not personal data on its own.

## 5. What the data is used for

Each purpose is listed separately, since purpose limitation applies per activity.

1. Selecting an indoor or outdoor branch, using weather.
2. Retrieving and parsing tonight's events in Hamburg, using scraped third party data.
3. Generating a personalised evening suggestion, combining the preference profile with the event data.
4. Delivering the suggestion to a named individual, using the Telegram chat ID.
5. Debugging and development, using retained execution logs.

Purpose 5 was never designed. It exists because n8n retains full execution payloads by default.

**Incompatible purpose flag.** The Stream B listings were published so the public could find and attend performances. Stups repurposes them as input to automated profiling and sends them to a US model provider. That is a different purpose from the one they were published for, and it is the clearest purpose limitation issue in the system.

## 6. Who processes the data

| Party | What it processes |
|---|---|
| The builder (system owner) | Everything; determines purposes and means |
| Ironhack | Hosts the n8n instance; stores execution history containing full payloads |
| OpenAI | Receives the full personal preference profile and the scraped event data in two nodes (`Event Extractor` and the `AI Agent`) |
| Telegram | Receives the generated message and the recipient's chat ID |
| Ticketmaster | Returns event data; receives no personal data from Stups |
| OpenWeatherMap and the five scraped websites | Receive no personal data from Stups |

A previously connected DeepSeek node processed the full Stream A profile during development; it has been disconnected. A second DeepSeek node remains in a branch not connected to the trigger.

## 7. Where data is stored and processed

- **n8n execution history:** on the Ironhack hosted instance. Hosting region is not documented and has not been verified by the builder.
- **OpenAI:** United States. No EU data residency option has been configured.
- **Telegram:** distributed infrastructure operated outside the EEA. No adequacy decision applies to the operator.
- **DeepSeek, historically:** servers in China during the development period.
- **Application storage:** none. The workflow contains no database, no Data Table, and no file writes. Nothing persists except the execution logs.

At least three of these flows leave the EEA.

## 8. Does the system make or assist decisions affecting people?

The system ranks, filters and recommends, end to end, with no human review before delivery. For the recipient the output is an evening suggestion, carrying no legal or similarly significant effect, so Article 22 is very unlikely to be engaged (analysed in Phase 4, not assumed here). It also implicitly selects which artists and events are surfaced. No individual suffers a significant effect from that, but the selection is automated and unexplained.

## 9. Open questions for the audit

- The hosting region of the Ironhack n8n instance is unverified and must be confirmed. This is the one open fact the builder cannot resolve alone.
- Whether the fitness and restorative activity statements amount to health data under Article 9 is arguable and is flagged for legal review.

Execution log retention was an open question in an earlier draft. It is now resolved: the instance prunes execution history after a maximum of 14 days (`pruning.enabled: true`, `maxAge: 336 hours`). It is recorded here as closed.
