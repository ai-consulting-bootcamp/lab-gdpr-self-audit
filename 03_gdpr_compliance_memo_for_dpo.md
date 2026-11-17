# Phase 6 · Compliance memo

**To:** Data Protection Officer, [Bootcamp] Career Services (pilot client)
**From:** Nicolò Marseu
**Re:** GDPR first-pass review of the Application Prep Agent
**Date:** 17 November 2026

**Bottom line: proceed with conditions.** The design is privacy-friendly at its core (no candidate data in the knowledge base, no training on CVs), but CVs currently linger in places they shouldn't and the contract chain isn't in place yet.

**What the tool does with personal data**

Coaches upload a CV and a job link. The CV text goes to OpenAI, which produces a fit score, CV edits, a cover letter and interview notes, and the report is emailed back. You are the controller and I am your processor. US transfer plus scoring of people means a DPIA is needed before the pilot.

**Top three actions, in order**

1. **Sign the contracts before any real CV is uploaded.** That means a processing agreement between us, OpenAI's Data Processing Addendum on a dedicated API project (ideally with EU data residency, which also turns off OpenAI's 30-day retention), and confirmation from Ironhack of where the workflow server is hosted. Until then, test only with fictional CVs.
2. **Stop the tool keeping copies.** Turn off run history for successful runs (keep failed runs for 7 days), move email from a personal Gmail account to a provider with a DPA, self-host the web fonts, and correct the "nothing is stored" claim.
3. **Run a short DPIA and update your candidate privacy notice.** Tell candidates their CV is analysed by AI via OpenAI, explain the score and how to contest it, and ask them to remove photos and sensitive details first. Agree in writing that the score is never used to select or rank candidates.

**Residual risks, even after these steps**

- **Sensitive data will still slip through.** Some candidates will upload CVs with photos, health gaps or other special-category details, and the instructions only reduce this.
- **Transfer law can shift.** If the EU data-residency option isn't available for our account, the transfer rests on standard contractual clauses, and the US framework is under appeal at the EU's top court.
- **The score can be misused.** Once coaches see a number, there's pressure to rank candidates with it. That would make it a high-risk system under the AI Act and an automated-decision problem under GDPR.

**What this memo is not:** a legal opinion, a DPIA or a certification. It is a first-pass assessment. Please involve legal counsel before relying on it for compliance decisions.
