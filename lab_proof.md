# Lab Proof: GDPR Audit of Your Own Project (Fix My Process, Project 3)

**Author:** Ayhan Demir · Ironhack AI Consulting & Integration Bootcamp · 17 Nov 2026
**System audited:** Fix My Process, my Project 3 
**Result in one line:** **proceed with conditions.** Legitimate interests covers all 9 purposes, a DPIA is required, and no real employee data should enter the system until DPAs, transfer safeguards and input filtering are in place.

## Start here

| Phase | File | Outcome |
|---|---|---|
| Input | [00_data_processing_brief.md](00_data_processing_brief.md) | My data processing brief: data, sources, purposes, processors, decisions |
| 1. Personal data inventory | [01_data_inventory.md](01_data_inventory.md) | 13 rows (one per data category and purpose), no retention period anywhere, 3 repurposing flags; highest risk: colleague and customer data pasted into free text |
| 2. Role map | [02_role_map.md](02_role_map.md) | Kleinanzeigen controller, me processor, 9 vendor processors, 2 independent controllers; no DPAs; US transfers need DPF or SCCs |
| 3. Lawful basis | [03_lawful_basis.md](03_lawful_basis.md) | Legitimate interests for all 9 purposes (consent ruled out at work); LIA passes with conditions; feedback and pasted third-party data TBD, legal review |
| 4. Risk and rights | [04_risk_and_rights.md](04_risk_and_rights.md) | No Art. 9 condition fits, so filter it out; Art. 22 not triggered; 2 EDPB criteria, so DPIA required; access, erasure and objection not supported in time |
| 5. Law stacking | [05_law_stacking.md](05_law_stacking.md) | AI Act: not high-risk today (hypothesis); ePrivacy: session ID exempt; Data Act: N/A |
| 6. Compliance memo | [06_compliance_memo.md](06_compliance_memo.md) | To the DPO: proceed with conditions, 3 sequenced actions, 3 residual risks (367 words) |
| Stretch | [07_privacy_by_design_checklist.md](07_privacy_by_design_checklist.md) | Free-text problem description: 5 Fail, 1 Unknown, each with the change needed |

## Top three actions

1. Sign DPAs and secure every US transfer before any real data flows.
2. Run a DPIA before the pilot, with a retention schedule and a privacy notice.
3. Filter names and customer details before the LLM call, and lock the purpose: no evaluation of teams or individuals.

## Method

- Worked from the data processing brief only, not from the repo or workflow export.
- Checked one current legal fact: the EU-US Data Privacy Framework adequacy decision is still in force, with an appeal pending at the CJEU ([02_role_map.md](02_role_map.md#sources)).
- Followed the lab template's tables and limits; Phase 4 written as short paragraphs.

## Limitations

- DPF certification of each US vendor not verified; the role map says "DPF if certified, otherwise SCCs".
- The n8n host (Ironhack) and GNews locations are not documented in the brief.
- The retention periods (90 days for cases, 30 for error records) are my proposal.

## Assumptions

- The system is a prototype with fictional internal documents; the audit assumes a pilot with real Kleinanzeigen employees.
- Law checked as of 17 Nov 2026.
- This is a course assessment, not a legal opinion, DPIA or certification.
