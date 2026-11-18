# Fundamentals: Data Processing Brief

**Procurement Risk & Mitigation Agent.** Updated 18 November 2026.

Scope: the brief covers two groups of data. **Group A** is the procurement report data (inputs, results, reports). **Group B** is account and operator data (the author's service accounts, e-mail addresses, logs). Group B is included in scope but kept separate, because it is not an input to the report. The inventory tables below give each category its examples, purpose, destination and status.

| # | Question | Answer |
|---|---|---|
| 1 | What personal data does the system process? | **Confirmed:** none that the system is built to collect. The form has no name or free-text field.<br>**Possible, to verify:** people named in web and news results; a supplier that is a sole trader; job titles in policies that identify someone in a small company; contact details in search results (see inventory A1).<br>**Group B:** the author's account and e-mail data (inventory B1 to B3) |
| 2 | Where does the data come from? | The web form, the company's database, and outside sources (Tavily, GDELT, the European Commission price file) |
| 3 | What is it used for? | Each category's purpose is in the inventory tables. In short: write and check the report, keep spending under the USD 5 limit, save and e-mail the report, and keep records of runs and tests |
| 4 | Who processes it, and what does each service receive? | **Local app** (author's computer): everything; keeps reports in `runs/`.<br>**OpenAI, writing model:** extracted text only: kept search results (title, extract, link, date, after e-mail and phone removal), figures and supplier names from the database, policy passages, instructions. No whole documents or files.<br>**OpenAI, embeddings:** policy passages when loaded, and short fixed search phrases at run time.<br>**Tavily and GDELT:** search words only, built from the product and market. No company documents.<br>**Supabase:** holds the database. The agent reads it and never writes.<br>**n8n** (reported as Ironhack-hosted), **Notion, Gmail:** the finished report; on an e-mail click, also the PDF. No database access. BUILT; live use is author-reported.<br>**Retention at every provider:** NOT DEFINED |
| 5 | Where is it stored and processed? | See "Storage, transfers and retention" below |
| 6 | Does it make or help make a decision that affects people? | It rates how serious each risk is for products and contracts and recommends actions, such as checking a suggested supplier. Everything it rates is an organisation. A human reads every report and no action happens automatically. Whether a decision based on a report could affect a sole trader: TO ASSESS |

### Inventory A: procurement report data
| ID | Category | Examples and possible data subjects | Purpose | Sent to | Stored in | Status |
|---|---|---|---|---|---|---|
| A1 | Web and news results (title, extract, link, date) | A person named in an article; a sole trader or contact on a supplier's web page; an e-mail address or phone number in an extract | Draft report claims. Each claim must carry a word-for-word quote from a kept result, and code checks the quote. Kept results are listed as sources | OpenAI (title and extract after redaction) | Run record and saved report (after redaction); Notion and PDF copies of the report | **Possible.** Details below |
| A2 | Company records: contracts, forecasts, suppliers, ingredients | Supplier names, countries, status notes. A sole-trader supplier would be a person | Calculate exposure and tell the model the facts it may use | OpenAI (figures and supplier names); Supabase (storage) | Supabase; copies in run records and reports | **None found** in the columns checked (`suppliers.csv`: id, name, country, ingredients, status, notes; contracts; forecasts; ingredients; database schema). **To verify:** whether any supplier name is a person's name |
| A3 | Policy documents (25 passages) | Job titles (for example a director who approves). A title could identify one person in a small company | Give the model internal rules to check recommendations against | OpenAI (passages for the model; passages and search phrases for embeddings) | Supabase | **None found** besides job titles; **to verify** |
| A4 | Request form and request number | Product and months. The number is made by the app | Define the run; label its records | Not sent | Run record, usage log | **Not personal** |
| A5 | Market price series | European Commission figures | Compare contract prices with the market | Figures only | Supabase | **Not personal** |

**How contact details are handled (A1).** Search services return text that may contain e-mail addresses or phone numbers. The local app removes them from the title and extract right after the results arrive and before the text goes to OpenAI, a run record or a report. The rule is code (`src/agent/credibility.py`, applied in `src/agent/evidence.py`). It catches e-mail addresses, international-format numbers (+ or 00) and numbers after words such as "phone" or "WhatsApp". A national-format number with no such cue may pass (to verify). Names are not removed. A regression test checks that no contact details reach the model prompt, the report or the run trace.

**What happened before this was added.** Live run 2 (10 to 11 November) stored one company's public business e-mail and phone number in `runs/live-002.json`, a local file. The removal was added after that run. From the records alone I cannot show whether run 2 also sent that text to OpenAI, so assume it may have. A search of `runs/` on 2026-11-18 found contact details in that file only. The same company contact details are also copied into two test files as sample input (`tests/test_evidence_validation.py`, `tests/test_live002_regressions.py`) and are therefore in the public GitHub repository and its history. Replacing them with placeholder values is planned and not done.

### Inventory B: account and operator data
| ID | Category | Examples | Purpose | Status |
|---|---|---|---|---|
| B1 | Service accounts | The author's sign-ins at OpenAI, Tavily, Supabase, Notion, n8n, Gmail; API keys kept in a local `.env` file that is not published | Run the services | Author only. Who else has access: NOT DEFINED |
| B2 | E-mail addresses | Sender: the author's Gmail account. Recipient: set inside n8n | Deliver the report | Recipient's role: NOT DEFINED |
| B3 | Logs and histories | Usage log (request number, model, token counts); run records; n8n execution history; a Notion table of error codes | Control cost; find faults | Contain no names by design. What n8n keeps, for how long and who can see it: NOT DEFINED |

### Storage, transfers and retention
| Item | Confirmed | Not confirmed |
|---|---|---|
| Database | Supabase, region eu-central (read from the dashboard 2026-11-18) | Where backups, logs and support access are handled |
| n8n, Notion, Gmail | Receive the finished report | n8n and Notion region; who can see pages and executions |
| OpenAI, Tavily, GDELT | Receive the text listed in question 4 | Where they process it; retention; training use |
| Local `runs/` and test files | Kept on the author's computer, in a OneDrive folder, so they are also copied to Microsoft's cloud (region not checked) | Whether OneDrive excludes them |
| Public GitHub repository | Holds code, fictional company data, tests (including the two test files above), a sample report PDF and its history | |
| Transfers outside the EU or EEA | None have been assessed | Whether any occur: cannot be ruled out for the vendors above |
| Retention | No code deletes or expires anything; local files and test files stay until the author deletes them; removed files stay in Git history | Provider retention periods: NOT DEFINED |

### Data flow
1. Form to local app to report run (BUILT).
2. Database (read only), then search words to Tavily and GDELT, then results; e-mails and phone numbers removed in the local app (BUILT).
3. Facts, redacted search results and instructions to OpenAI, then draft, then checks, then report saved in `runs/` (BUILT).
4. Policy text to OpenAI (embeddings), then database (BUILT).
5. Report to n8n, then Notion page, automatically after the run and before human review (BUILT).
6. PDF and Notion link to n8n, then Gmail, on click (BUILT).
7. Recorded approver sign-off (PLANNED).

## Note on the MVP
This is a portfolio prototype built by one author as an Ironhack bootcamp project. It runs on the author's computer and has no real client or users. Bakery Foods Inc. and its contracts, forecasts, suppliers, ingredient records and policy documents are **fictional (synthetic data)**. The price series, the web and news content and the search results are real. The 14 live runs were done by the author. Exposure figures are scenario results from those fictional inputs, not a company's real financial impact. Every statement about production use is intended, not real.