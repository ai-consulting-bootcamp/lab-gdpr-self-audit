# Stups: project overview for the reviewer

This file orients a reader before they open the audit. It is not part of the lab's instructions. It describes the system being audited and shows where each graded item lives.

## What Stups is

Stups is my IronHack Project 3: a personal evening suggestion agent built in n8n. Once a day at 17:30 it reads Hamburg weather, branches to an indoor or outdoor path, scrapes six public event sources, and passes the results together with a stored personal preference profile to a large language model, which writes two evening suggestions. The suggestions are sent to a single Telegram chat. There is one recipient, me, and the system is not offered to the public.

The version audited is `Stups v6`, the version that actually ran. A later `v7` was built but never activated, so it is out of scope.

## Why this system is worth a GDPR audit

At a glance Stups looks like a private hobby tool with no data protection surface. The audit shows it processes personal data in two separate streams:

- **Stream A** is data about me, the recipient: a Telegram chat ID and a detailed lifestyle profile.
- **Stream B** is data about third parties: the names of performers, musicians, comedians and directors scraped from event listings, people who do not know the system exists.

Stream B is the finding most students would miss, and it is where the real controller obligations sit.

## Deliverables and where the graded items are

| File | Contents |
|---|---|
| `data-processing-brief.md` | Kick-off brief. Recognises the data (CFU 1), maps every category across both streams, lists purposes, processors and storage locations |
| `gdpr-audit-stups.md` | The audit worksheet: Phases 1 to 6, plus the CFU 4 accountability test |

Phase map inside the worksheet:

1. Personal data inventory, one row per purpose, two layer retention
2. Role map, controller, processor and sub-processor relationships
3. Lawful basis per purpose, with full three part legitimate interests tests
4. Risk and rights: Article 9, Article 22, DPIA screening, data subject rights, security
5. Law stacking: AI Act tier, ePrivacy, Data Act, database rights
6. Compliance memo: bottom line, three sequenced actions, residual risks

## Headline findings

- Three processors handle personal data. None is bound by a data processing agreement.
- The OpenAI API credential belongs to Ironhack, so OpenAI is a sub-processor I never authorised and cannot contract with directly.
- A development transfer to DeepSeek sent my full profile to China with no valid transfer mechanism. It is documented, not deleted.
- For Stream B individuals, every right in Chapter III is formally available and practically inaccessible.
- One fact I cannot resolve alone: the hosting region of the Ironhack instance is unverified.

## Scope and integrity notes

- The audit is a self assessment by the system's builder. It is not a legal opinion. Items marked `TBD — legal review` need qualified advice.
- The lab's own `instructions.md` and `rubric.md` are left unmodified.
- The Telegram chat ID is redacted as `[TELEGRAM_CHAT_ID]` throughout.
- The workflow JSON is deliberately not committed, because it carries that identifier and credential names.
