MIRA — GDPR Self-Audit Submission

Student: Elza Paegle
Project: MIRA — AI-assisted personal-brand and photoshoot planning
Track: GDPR | Audit your own Project 3
Assessment date: 18 August 2026
Status: First-pass compliance assessment; not legal advice

Bottom line

Proceed with conditions. MIRA can continue as a controlled prototype, but it should not accept real public users until the team has completed the DPIA, established processor and transfer safeguards, published a privacy notice, and implemented enforceable deletion and data-subject-rights workflows.

File map

File

Contents

mira_data_processing_brief.md

One-page description of MIRA’s personal-data flows, sources, purposes, recipients, storage, transfers, and decision effects

mira_gdpr_audit_worksheet.md

Full Phases 1–5 audit: inventory, roles, lawful bases, LIA, rights and risk analysis, DPIA screening, and law stacking

mira_compliance_memo.md

300–400-word advisory memo with recommendation, three sequenced actions, and residual risks

mira_accountability_checklist.md

Regulator-readiness check identifying what exists and what is missing

mira_data_protection_by_design_checklist.md

Pass/fail/unknown design review of MIRA’s highest-risk activity

Fixed prototype fact pattern

This audit assesses the MIRA MVP as described for Project 3: a user completes a Tally questionnaire, may provide free-text and visual inspiration, and receives an AI-generated Creative DNA/profile, moodboard or visual direction, practical photoshoot plan, and up to five generated images. The prototype workflow uses Tally, n8n Cloud, Google Sheets/Docs, an LLM API, an image-generation service, and a Railway-hosted MIRA application.

Vendor hosting regions, Data Processing Agreements (DPAs), subprocessors, model-training settings, security controls, and deletion configurations were not evidenced in the project materials available for this audit. They are therefore recorded as Unknown — verify before deployment, rather than assumed compliant.

Scope boundary

MIRA is not an employment, education, credit, insurance, law-enforcement, or public-benefits decision system.

It provides creative recommendations to the user and/or photographer; the human remains free to reject or modify every output.

The intended audience is adults. The production service should implement an 18+ rule until risks involving children are separately assessed.

Production data must not be committed to GitHub. The repository should contain only documentation, redacted screenshots, synthetic test data, and code/configuration with secrets removed.

Key legal sources

General Data Protection Regulation — official text

EDPB small-business compliance guide, including DPIA screening

European Commission guidance on EU–US transfers

EU Artificial Intelligence Act — official text
