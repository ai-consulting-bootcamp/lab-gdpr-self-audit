# Advisory memo: Model Intake Brief

**To:** Data Protection Officer or Legal Counsel, prospective client organisation  
**From:** Sergii Rostovskyi, project owner and consultant  
**Date:** 17 November 2026  
**Subject:** Conditions for further use of the educational prototype

Proceed with conditions: the local educational prototype can continue with offline fixtures and screened non-personal documents, but unreviewed personal-data flows and client deployment should remain on hold until the controls below are evidenced.

The owner confirms individual local use, public model documentation only, and no real client data. The application assesses documentation about models rather than making decisions about people. Nevertheless, public sources may contain identifiable authors, contacts or repository handles. Our local synthetic check demonstrated that a contact email survives into the prepared assessment prompt. We intercepted that request locally; no personal information was transmitted during the test. The code also disables response storage, but this does not establish zero retention across the service.

First, restrict and minimise inputs before further unreviewed live use. Keep private documents and special-category information outside the permitted workflow, remove unnecessary identifiers before API dispatch, and check reports before saving or sharing them. Tighten source-domain and redirect controls. Retest with synthetic examples and retain evidence that prohibited content cannot reach downstream services.

Second, establish the contractual and legal foundation before any personal-data transfer. Identify the relevant vendor entities, confirm applicable processing agreements and subprocessors, and verify processing locations, retention settings and transfer mechanisms. Complete a purpose-specific legitimate interests assessment and determine the appropriate transparency arrangements. Public availability and an API subscription do not resolve these questions.

Third, make accountability operational before external or client use. Approve a retention schedule, assign a rights-request contact, and rehearse access, correction and deletion across exports and vendors. Document incident assessment and notification responsibilities. Record a DPIA screening decision and check the applicable national mandatory list; the present evidence does not establish that a full DPIA is mandatory, but expanded use may change that conclusion.

Residual risks remain: redaction can miss identifiers or sensitive context; vendor retention and overseas access may remain outside direct technical control; downloaded or shared reports can persist after local deletion. Human reviewers must also check misleading findings before relying on them.

This memo is not a legal opinion, a DPIA or a compliance certification. Engage qualified legal counsel before relying on this assessment for compliance decisions. The accompanying worksheet distinguishes observed controls, unresolved facts and proposed changes.
