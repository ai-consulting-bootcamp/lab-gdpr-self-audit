# Lab proof · Audit your own project: GDPR lens

**Start here.** First-pass GDPR assessment of my Project 3, the [Application Prep Agent](https://github.com/nmarseu/Project-3-Marseu): an n8n workflow that turns a CV and a job link into an AI-written application pack, delivered by email.

## Result in one line

**Proceed with conditions.** The core design is privacy-friendly: no candidate data in the knowledge base, no training on CVs, and research APIs get only the company name. But CVs are kept by default in n8n execution history and a Gmail Sent folder, they go to OpenAI in the US with no DPA confirmed, and none of the formal GDPR documentation exists.

## Workflow audited

- Workflow export: [`workflow/application_prep_agent.json`](https://github.com/nmarseu/Project-3-Marseu/blob/main/workflow/application_prep_agent.json) (35 nodes)
- Data processing brief: [`01_data_processing_brief_application_prep_agent.md`](01_data_processing_brief_application_prep_agent.md)

## The run: input → evidence → output

**Input.** The Project 3 workflow export and README. The reference submission is the fictional demo candidate (`sample_inputs/CV_Sofia_Lindqvist.pdf` + `achievement_bank.md`), traced through the workflow node by node. This is a static trace of the export; I did not execute a new run for this audit.

**Evidence produced.** I traced which personal data reaches each node and service, checked against the node parameters in the export, not the README:

| Node / service | What it receives (from the export) | GDPR consequence |
|---|---|---|
| `1. Form Trigger` | Job URL, job text, CV PDF, extra achievements, language, email | Controller collects personal data; form text says "Nothing you submit is stored" |
| `2. Extract CV Text` → 5 OpenAI nodes (`gpt-4o-mini`) | Full CV text + achievements in the parse, fit, report, low-match and fact-check calls | US transfer; OpenAI as processor; DPA and transfer mechanism needed |
| `3. Fetch Job Posting (Jina)` | Job URL only | No personal data |
| `5 / 5b Tavily`, `6 NewsAPI` | `job.company_name` only | No personal data: good minimisation |
| `7b. RAG: Writing Guidelines` | Fixed prompt string | No candidate data embedded or stored: good purpose binding |
| `Good Enough Match?` | Fit score ≥ 50 | Solely automated decision; assessed under Art. 22 as not significant |
| `11b. Send Email` (Gmail SMTP) | Recipient email + full report | Copy kept in Sent folder; no DPA possible on a consumer account |
| Workflow `settings` | Only `executionOrder`, `binaryMode` | Execution data not switched off, so CVs are retained by default |
| `assets/form_custom.css`, `landing/index.html` | `@import` / link to fonts.googleapis.com | Visitor IP sent to Google |

**Final output**

- [`02_gdpr_audit_worksheet_application_prep_agent.md`](02_gdpr_audit_worksheet_application_prep_agent.md): CFU 1, Phases 1–5 (inventory, roles, lawful basis + LIA, risk and rights, law stacking)
- [`03_gdpr_compliance_memo_for_dpo.md`](03_gdpr_compliance_memo_for_dpo.md): Phase 6 memo to the client's DPO (389 words)
- [`04_accountability_check_and_privacy_by_design.md`](04_accountability_check_and_privacy_by_design.md): CFU 4 accountability test, Reinforce, Stretch checklist

## One failure / limitation I hit

**Some of the most important facts sit outside the workflow export, and I couldn't verify them:**
- the **hosting region and retention settings of Ironhack's n8n instance**;
- whether **OpenAI's DPA** has been accepted for my API account;
- whether **EU data residency** is available for it;
- whether the **n8n form sets any cookies**.

The export shows only workflow-level settings. These gaps are marked "unknown" or "TBD" rather than assumed. They affect the transfer analysis and the retention findings.

## Sources

- OpenAI Data Processing Addendum: transfers from OpenAI Ireland under SCCs. [openai.com/policies/data-processing-addendum](https://openai.com/policies/data-processing-addendum/)
- OpenAI, *Introducing data residency in Europe*: in-region API processing with zero data retention for eligible projects. [openai.com](https://openai.com/index/introducing-data-residency-in-europe/)
- OpenAI default 30-day abuse-monitoring retention for API content. [iubenda](https://www.iubenda.com/en/blog/openai-gdpr-compliance/)
- EU–US Data Privacy Framework appeal pending before the CJEU (Latombe v Commission). [IEU Monitoring](https://ieu-monitoring.com/editorial/microsoft-backs-eu-commission-in-eu-court-case-on-transatlantic-data-flows-and-privacy/1244467/)
