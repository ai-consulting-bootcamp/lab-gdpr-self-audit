# LAB | Audit your own project — GDPR lens · Editorial research agent (Project 3)

A first-pass GDPR self-audit of the Project 3 agent, a LangGraph research assistant for independent bookshops. It is based on the real code (commit `3939562`) and 20 saved runs.

## File map

| File | Content |
|---|---|
| [`lab_proof.md`](lab_proof.md) | **Start here.** Workflow export, runs performed today (repo scan, tests), evidence, output, limitations |
| [`data_processing_brief_editorial_agent.md`](data_processing_brief_editorial_agent.md) | Kick-off: one-page data processing brief for a DPO |
| [`gdpr_self_audit_editorial_agent.md`](gdpr_self_audit_editorial_agent.md) | CFU 1; Phase 1 inventory (one row per purpose, retention known/estimated/unknown); Phase 2 role map with DPA/transfer status; Phase 3 lawful bases + three-part LIA; Phase 4 Art. 9, Art. 22, nine EDPB criteria, rights; Phase 5 law stacking; CFU 4 accountability test |
| [`compliance_memo_dpo_editorial_agent.md`](compliance_memo_dpo_editorial_agent.md) | Phase 6: memo to legal counsel (389 words), with a "what this memo is not" disclaimer |
| [`proof/`](proof/) | Read-only scan script and the logs of today's runs |

**Conclusion:** **proceed with conditions.** The agent processes personal data of authors and of third persons; inferable Art. 9 data has been stored and published. There is no customer data and Art. 22 does not apply. Three conditions:
- Gemini on a paid tier, or no retrieved text sent to it;
- remove the public evidence files;
- write the accountability pack before any pilot.

## Status

| Item | Status (17 Nov 2026) |
|---|---|
| Brief, audit, memo, proof | **Prepared** (tutor draft; the student must review and defend it) |
| Project 3 code | **Not modified** |
| GitHub | Folder added to a fork of `ai-consulting-bootcamp/lab-gdpr-self-audit`; pull request opened 18 Nov 2026 |
| Submitted on the portal / accepted | **No / No** |
| Optional Reinforce / Stretch | Not done (the accountability test is included because it is CFU 4) |

**Tags:** **[V]** verified · **[D]** declared · **[A]** inference or assumption · **[NC]** not checked.

*This is not legal advice, not a DPIA and not a certification.*
