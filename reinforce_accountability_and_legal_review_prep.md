# Reinforce — Accountability inventory and legal-review prep

## 1. What a regulator could ask for

| Document | Exists? | Notes |
|---|---|---|
| Record of processing activities (Art. 30) | ❌ | The brief's tables are a starting point |
| Privacy notice / Art. 14 information to people named in reports | ❌ | Or a documented "disproportionate effort" assessment (Art. 14(5)(b)) |
| Legitimate interests assessment (LIA) | ❌ | Draft for P3 in the audit, Phase 3 |
| DPIA | ❌ | Required (4 EDPB criteria) |
| Art. 10 legal basis assessment | ❌ | Key open question |
| DPA with LLM provider | ❌ | Bootcamp key belongs to Ironhack's account |
| DPA with LangSmith, Tavily | ❌ | Check terms per plan |
| Transfer impact assessment / transfer mechanism record | ❌ | OpenAI, LangSmith, Tavily (US) |
| Retention schedule | ❌ | Reports kept indefinitely |
| Access / rectification / erasure procedure | ❌ | No index by person, no correction route |
| Breach response procedure | ❌ | Including what's in LangSmith and GitHub |
| Record of human decisions on recommendations | ❌ | Report has no reviewer field |
| Data flow documentation | ✅ | Pipeline doc, README diagram |
| Design rationale | ✅ | `stack_decision.md`, `docs/chunking_decision.md` |
| Per-run audit trail | ✅ | Section 8 of every report + LangSmith trace |
| Data source licences | ⚠️ | OpenSanctions non-commercial only; KvK test data in MVP |

**Entirely missing:** every GDPR-specific document. The project documents *how the agent works* well, but nothing about *whose data it touches and why that's allowed*.

## 2. One TBD revisited: Art. 10 for adverse media (P3)

**What a lawyer needs to know to advise:**
- **Who the controller is:** law firm, notary or payment company. Is it a Wwft institution, and does it screen suppliers under a documented integrity policy?
- **Exactly which criminal-offence data is stored:** names, roles, allegation vs. charge vs. conviction, and for how long.
- **Whether names are needed at all,** or company-level findings are enough.
- **Who sees the reports,** and what decision they feed.
- **Which sources are used** (public reputable news only?), and how accuracy is checked.

**What I can prepare in advance:**
1. A one-page data flow (from the brief) highlighting where named-person data enters and leaves.
2. Two **redacted sample reports**: one company-level only, one with names. Shows the lawyer the minimised option is realistic.
3. The ASML/Heineken test results, as concrete evidence of the accuracy risk.
4. A proposed retention rule and the reviewer sign-off design.
5. The specific question: *"Which UAVG exception (if any) allows a private firm to process criminal-offence data about individuals at its suppliers for integrity screening, and under what conditions?"*
