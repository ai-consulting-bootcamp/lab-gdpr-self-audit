# Lab proof — Audit your own project (GDPR lens)

**Student:** Pieter Albrecht
**System audited:** my Project 3, the Vendor Due-Diligence Agent (LangGraph, GLEIF + KvK + OpenSanctions + Tavily, gpt-4o-mini, Streamlit / FastAPI / n8n front ends)

This is the entry point for the reviewer. Each section below links to the supporting file.

## 1. Workflow

```
Project 3 docs + code ──► Data processing brief ──► CFU 1 Recognize
                                                         │
     Phase 1 Inventory ◄─────────────────────────────────┘
          │  (purpose-drift flags)
          ▼
     Phase 2 Role map (DPAs, transfers) ──► Phase 3 Lawful basis + LIA
          │
          ▼
     Phase 4 Risk & rights (Art. 9/10, Art. 22, DPIA, rights) ──► Phase 5 Law stacking
          │
          ▼
     CFU 4 Accountability test ──► Phase 6 Compliance memo ──► Reinforce + Stretch
```

## 2. One run: input → evidence → output

**Input:** a real test run from 12 November: `python main.py "ASML"` (from the 5-company test).

**Evidence it produced:** the report rated ASML **Medium, Onboard with conditions** because of the red flag *"Former employee jailed for sharing trade secrets with Russia"*. In fact ASML was the *victim*. The run shows, in one report:
- **personal data about a third party** (the ex-employee and the criminal conviction): **Art. 10 data** pulled in by a system whose input was just a company name;
- **an accuracy failure** (Art. 5(1)(d)): the company's role was mislabelled, and the design has no correction route (Art. 16);
- **storage everywhere:** state → OpenAI prompt → LangSmith trace (US) → saved report, with no retention rule.

This run is what moved my answer to "does the system process personal data?" from *"barely, it's about companies"* to **"yes, including criminal-offence data"**.

**Final output:** [compliance memo](compliance_memo_Vendor_DD_Agent.md). **Proceed with conditions.** Actions: (1) own LLM account + DPA, tracing off/EU, clean the public repo → (2) Art. 10 legal opinion + DPIA → (3) company-level findings with role labels, reviewer sign-off, correction route, retention rule.

## 3. Failure / limitation I hit

- **The shortcuts I took while building were exactly the GDPR gaps:** the bootcamp OpenAI key (no DPA of my own), LangSmith tracing every prompt "because it's useful for the demo", reports in a public repo, and "never overwrite the audit trail" with no thought about rectification.
- **Unverified facts.** I didn't confirm where n8n, Streamlit and the API run, or LangSmith's region; I assumed local and US default. Whether old reports are in the public repo needs `git ls-files`: the `.gitignore` only covers `reports/*_2026-*.md`, not `reports/archive/`, `notes/` or `screenshots/`.
- **Art. 10 can't be settled without a lawyer:** which Dutch exception, if any, covers screening *suppliers* for criminal conduct.

## 4. Supporting files

- [data_processing_brief.md](data_processing_brief.md) — one-page brief for a DPO
- [GDPR_Audit_Vendor_DD_Agent_Pieter_Albrecht.md](GDPR_Audit_Vendor_DD_Agent_Pieter_Albrecht.md) — CFU 1, Phases 1–5, CFU 4 accountability test
- [compliance_memo_Vendor_DD_Agent.md](compliance_memo_Vendor_DD_Agent.md) — Phase 6 memo to the client's DPO
- [reinforce_accountability_and_legal_review_prep.md](reinforce_accountability_and_legal_review_prep.md) — document inventory + Art. 10 legal-review prep
- [stretch_privacy_by_design_checklist.md](stretch_privacy_by_design_checklist.md) — data protection by design checklist
