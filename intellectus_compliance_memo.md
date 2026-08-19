# Compliance recommendation memo

**To:** Data Protection Officer / legal counsel, Intellectus client  
**From:** Paola Hintze, Intellectus project  
**Subject:** GDPR conditions for an Intellectus pilot

**Bottom line — proceed with conditions.** The bounded public-data MVP may continue for controlled testing, but Intellectus should not accept private client documents or sensitive information until the production data flow, contracts, DPIA and operational controls are complete.

Intellectus converts intake and bounded public research into an organisation-level diagnostic draft. Personal data can still enter through free text and public evidence, including names, professional roles, quotations and contact details. The demonstrated repository does not contain private client data and does not evidence a production document-upload boundary or active external AI provider. It also does not establish hosting countries, vendor DPAs, retention, rights handling or production access controls. A consultant must review every output before client use; the current use does not make legal or similarly significant decisions about individuals.

The client should take three actions in sequence:

1. **Fix the processing boundary before data flows.** Confirm controller/processor roles; document each purpose, data-subject group and lawful basis; execute an Article 28 DPA; map n8n, hosting, storage, logs and any model provider; and approve subprocessors and any EEA transfer mechanism. Keep private-document upload and external model processing disabled until this is signed off.
2. **Complete a full DPIA before the private-document pilot.** The intended scenario combines innovative AI-supported analysis with client and public datasets and may involve vulnerable beneficiaries or sensitive information. Record necessity, proportionality, Article 9 conditions, transfer risks, consultation and residual-risk decisions. Exclude sensitive data unless its specific legal condition and need are demonstrated.
3. **Implement and test operational safeguards.** Add an authenticated gateway, least-privilege access, input warnings and redaction, source-to-output lineage, fact/inference labels, auditable consultant approval, metadata-only logs, case-based retention and cascade deletion. Publish appropriate privacy information and test access, correction, erasure, objection and incident-escalation procedures before the pilot.

Residual risks remain: public information may be stale or taken out of context; free text may unexpectedly reveal sensitive data; generated inferences may be inaccurate or stigmatising; and overseas vendor or subprocessor access may create transfer and rights-enforcement risk. Human review reduces but does not eliminate these risks.

This memo is a first-pass advisory assessment. It is **not a legal opinion, a DPIA or a certification**. The client must engage qualified legal counsel before relying on it for compliance decisions.
