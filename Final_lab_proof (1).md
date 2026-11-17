# Lab Proof — GDPR Audit of Project 3 Interview Preparation Agent

**Reviewer entry point:** [GDPR audit, data map, role map, lawful bases, risks and client memo](gdpr_audit_ai_interview_preparation_agent.md)

## Workflow / code evidence

- **Reported workflow:** n8n form → CV and job description → RAG / LLM processing → interview preparation report → Notion.
- **Services reported:** OpenAI GPT-4o-mini, Pinecone, Tavily, NewsAPI, Notion.
- **Workflow export:** **Not attached / not independently verified.** Add a sanitised n8n `.json` export here if required by the instructor.

## One run / query and input

- **Input type:** CV upload and job description. The project owner reports a consent/permission request before the CV check; verify the n8n gate and prompt wording in the workflow export.
- **Original input:** The report indicates a CV and a Siemens-related SaaS product management job description were processed, but the exact submitted CV, job description and consent record have **not** been supplied. Do not reconstruct or invent them.
- **Evidence produced:** The project owner recovered and supplied an earlier report with identifier `RPT-20261112-3688`. See [sample output — Siemens interview report](sample_output_siemens_interview_report.md). **No n8n execution screenshot or log has been supplied**, so this is output evidence, not a verified execution trace.
- **Final output:** [Recovered Siemens interview preparation report](sample_output_siemens_interview_report.md), containing company overview, job requirements, CV-to-job matching, evidence gaps, five interview questions, three STAR examples and recommendations. Supplied by the project owner; original run not independently verified.

## One failure / limitation

The recovered report contains STAR examples mentioning ExampleCloud Software, DemoTech Solutions, a 22% feature-adoption increase and a 15% customer-satisfaction increase. The source CV is unavailable, so these claims are **unverified** and may be AI-generated embellishments; user verification is required before relying on them. Data retention, deletion across vendors, and processing regions remain unverified.

## Audit result

**Proceed with conditions.** See the [full audit and 300–400-word client memo](gdpr_audit_ai_interview_preparation_agent.md).
