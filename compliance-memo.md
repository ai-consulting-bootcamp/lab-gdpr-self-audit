# Compliance memo — Whizbiz (Messenger Accountant)

**To:** Data Protection Officer / legal counsel (Whizbiz has no DPO yet — addressed to whoever takes
this on before launch)
**From:** Vittal Navale, builder
**Date:** 19 August 2026
**Re:** First-pass GDPR assessment ahead of onboarding paying subscribers

---

**Bottom line: proceed with conditions.** Whizbiz's engineering is sound and its statutory-bookkeeping
purpose has a clean legal basis, but the product currently has no processor agreements, no
international-transfer documentation, and no notice mechanism for the third-party customers whose
data it holds — none of which is expensive to fix, but none of which can be deferred past the first
paying subscriber.

**Top three actions:**

1. **Put an Article 28 agreement in place with every subscribing owner before any external data
   flows**, naming OpenAI, Google, and the n8n host as sub-processors and disclosing Telegram's role
   as an independent, non-EU controller for the messaging layer. Without this, Whizbiz processes
   personal data on subscribers' behalf with no contractual basis at all.
2. **Conduct a DPIA before onboarding real subscribers.** The system plausibly triggers at least two
   of the EDPB's nine criteria — combining datasets per user, and innovative technology (vision
   extraction plus LLM routing) — with a third (special-category data at scale) worth deciding
   explicitly rather than leaving implicit. The DPIA's most useful output will be a decision on
   whether receipt photographs need pre-filtering before they reach the vision model.
3. **Give subscribers a way to meet their own Article 14 obligation to their customers**, whose names
   and addresses Whizbiz stores without their knowledge. This is the finding most likely to make a
   *subscriber* non-compliant without realising it — the fix is model privacy-notice wording and a
   per-customer lookup so an access or deletion request against that data can actually be answered.

**Residual risks that remain even after these three actions:**

- **Telegram itself cannot be contracted with.** Disclosure, not a DPA, is the ceiling here — a
  structural risk that no amount of Whizbiz-side paperwork removes, and subscribers who object to it
  have no in-product alternative today.
- **Receipt photographs can still incidentally carry special-category data** even after a DPIA
  decision — filtering reduces but does not eliminate the chance that a pharmacy or union receipt
  reaches the vision model, and no Article 9 condition currently covers that residual case.
- **Retention is undefined outside the statutory 10-year bookkeeping rule.** Chat history, Drive image
  copies, and calendar entries have no deletion schedule; fixing the DPA and DPIA does not by itself
  produce that schedule, and until it exists, "everything kept forever" remains the likely real-world
  default.

**What this memo is not:** a legal opinion, a DPIA, or a certification of compliance. It is a
first-pass technical/product assessment. Whizbiz should engage legal counsel before relying on it for
any compliance decision, particularly on the three items marked "TBD — legal review" in the full
audit worksheet.
