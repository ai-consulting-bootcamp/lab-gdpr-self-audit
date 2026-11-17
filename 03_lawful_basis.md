# Phase 3: Lawful Basis Assessment

**System:** Fix My Process (Ironhack Project 3) · **Input:** [00_data_processing_brief.md](00_data_processing_brief.md) · **Lens:** GDPR only · **Date:** 17 Nov 2026

Purpose numbers (1) to (9) follow [section 3 of the brief](00_data_processing_brief.md#3-what-is-the-data-used-for).

| Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|
| (1) Fix report | Legitimate interests, Art. 6(1)(f) | Employer interest in faster processes; employee chooses to submit. Consent avoided: rarely freely given at work (EDPB 05/2020) | No (Yes for pasted third-party data) |
| (2) Compliance flag | Legitimate interests | Prevents non-compliant AI use; the flag is about the use, not the person | No |
| (3) Use-case summary | Legitimate interests | Shows the company which AI use cases to build; needs a privacy notice | Yes: repurposing flag 2 ([Phase 1](01_data_inventory.md)) |
| (4) Red-case Board review | Legitimate interests | Governance control on risky AI use; full problem text is more than the Board needs | Yes: minimisation |
| (5) Status lookup | Legitimate interests | Lets the employee follow their own case | No |
| (6) Tool-adoption feedback | Legitimate interests | Measures adoption, but captures attitudes and may feed department summaries | **TBD: legal review** |
| (7) Quality scoring | Legitimate interests | Quality control of AI output | No |
| (8) Session chat context | Legitimate interests | Technically needed for the chat to work | No |
| (9) Error handling and logs | Legitimate interests (security, Art. 32) | Keeps the system running and secure | No |
| Pasted customer or colleague data | None identified | No basis for sending it to a US LLM; prevent at input | **TBD: legal review** |

Employment context: rely on Art. 6(1)(f) directly; § 26 BDSG carries little weight after CJEU C-34/21.

**Legitimate Interests Assessment, purposes (1) to (5) and (7) to (9)**

1. **Is the interest legitimate?** Yes. Kleinanzeigen needs to cut manual work and keep AI use within its internal AI policy; without a sanctioned route, employees tend to use unapproved tools.
2. **Is the processing necessary?** Partly. The fix needs the problem and the department, not names. Less intrusive options exist and should be used: strip names and customer details before the LLM call, send only the summary to Slack and Notion, and set a retention period.
3. **Does the individual's interest override?** No for the submitting employee, if the options above are applied, a privacy notice is given and the data is never used to judge people: employees expect work input to be processed. Yes for named colleagues and customers, who have no such expectation, which is why their data must be kept out.

Purpose (6) and the planned department summaries: **TBD: legal review**, because the balancing test depends on how the summaries would be used.

## Sources

- EDPB Guidelines 05/2020 on consent (employment context)
- CJEU C-34/21 (30 Mar 2023), employee data and Art. 88 GDPR
