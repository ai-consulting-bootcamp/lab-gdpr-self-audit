# Compliance memo

**To:** Data Protection Officer, Wechselweise Coaching GmbH *(fictional client)*
**From:** Ben Mayer
**Date:** 26 November 2026
**Re:** GDPR first-pass assessment of Menohelp before the pilot

**Bottom line: proceed with conditions.** Menohelp's design already keeps health data short-lived and minimised, but no legal or contractual layer exists yet. No customer's data should flow until the three actions below are done.

**What we found.** Menohelp processes health data, and some data about sex life, from every woman who uses it. Cycle logs, blood values and symptom answers are analysed in code. Results, together with blood values and the free-text answer, are sent to OpenAI in the US to write the report. My server deletes everything after one hour. But OpenAI may keep inputs for 30 days, there is no consent step, and the screen tells users "Nothing is stored", which is not accurate. Art 22 does not apply, because the report decides nothing. The system does, however, profile health without human review, so accuracy and transparency carry the weight. Four of the EDPB's nine DPIA criteria apply.

**Top three actions, in order.**
1. **Before any customer data flows: contracts and transfers.** Sign a data processing agreement with me as your processor. Authorise OpenAI, Resend and the host as sub-processors, each with its own DPA. Use OpenAI's EU data residency with zero data retention, an EU host and EU email sending. Where a US flow remains, document the Data Privacy Framework certification or SCCs with a transfer impact assessment.
2. **Before the pilot: explicit consent and an honest notice.** Add an unticked consent step (Art 9(2)(a)) that names OpenAI and the US transfer, and replace "Nothing is stored" with a privacy notice that matches the real data flows. For coach use, decide whether coaches are joint controllers and record it in an Art 26 arrangement.
3. **Before the pilot: a DPIA.** Cover health profiling, combining sources, the vulnerable-user angle and the email channel. Replace open email sending with a download or a verified address.

**Residual risks.**
- **Wrong or alarming text.** No human reviews a report before the woman reads it. Checks catch wrong numbers, not every misleading sentence.
- **Copies outside your control.** Downloaded or forwarded reports can't be recalled or erased.
- **Transfer instability.** The EU-US framework is under legal challenge. Without EU-only processing, a ruling could force a fast switch.

**What this memo is not.** It is not a legal opinion, a DPIA or a certification. Please involve legal counsel before relying on it for compliance decisions.
