# Compliance Advisory Memo

**To:** Data Protection Officer / Legal Counsel
**From:** Anand Narasipuram, Project 3 — School Book Order Bot
**Re:** GDPR first-pass assessment ahead of Germany deployment

## Bottom line
**Proceed with conditions.** The current India deployment carries limited GDPR exposure given the lack of shared infrastructure with any EU processing, but the planned Germany deployment brings the system fully within GDPR's scope, and three specific gaps should be closed before any EU school's data is processed live.

## Top three actions

1. **Establish Data Processing Agreements with OpenAI and Google before the Germany deployment goes live.** Confirm both vendors' standard DPAs are in force for the account/tenant actually used, and confirm whether any processing occurs outside the EEA — if so, verify Standard Contractual Clauses are in place under the same agreements.

2. **Resolve the lawful basis for purpose (e) — natural-language Q&A over historical order data — before relying on it in the EU deployment.** This purpose was not part of the original data collection and the Legitimate Interests Assessment could not be confidently completed (see Phase 3). Legal counsel should determine whether this requires a separate lawful basis, a revised privacy notice to schools, or exclusion from the EU rollout until resolved.

3. **Define a retention policy for order data and chat identifiers**, currently undefined and held indefinitely. This is both a standalone Art. 5(1)(e) storage-limitation gap and a prerequisite for being able to respond to erasure requests in a timely way once the Germany deployment has EU data subjects.

## Residual risks (remain even if the above are addressed)

- **Incidental personal data in photo uploads.** Even with retention and DPA gaps closed, handwritten order photos may incidentally contain personal data beyond the book order itself. This risk is low-probability but not eliminated by any of the three actions above.
- **Scale-triggered DPIA requirement.** The system does not currently trigger a mandatory DPIA, but this should be re-evaluated once the Germany deployment grows past a handful of schools — large-scale processing combined with purpose (e)'s profiling-adjacent querying could jointly trigger the two-criteria DPIA threshold.
- **WhatsApp Business API metadata handling** sits partly outside this system's direct control, since Meta may process certain metadata under its own terms as a separate controller. This should be reviewed as part of vendor DPA work but may not be fully resolvable through contract alone.

## What this memo is not
This is a first-pass, non-expert assessment intended to identify gaps and prioritize next steps. It is not a legal opinion, not a completed DPIA, and not a certification of compliance. Legal counsel should be engaged before any of the above is relied upon for a compliance decision, particularly regarding purpose (e) and the international transfer question.
