# Data processing brief: AI Use Case Identifier

For a Data Protection Officer who has never seen the project. Friedrich Tschoepke · 23 November 2026 · Code state: commit `d99573f` (13 November 2026).

## What the system is

A command-line research agent the builder uses to prepare his own first meetings with small and mid-sized companies as an AI consultant. He enters a company name and website. The system collects public information about the company, has OpenAI models describe how the company works, suggests three places where AI could help, and writes a brief with meeting questions. The detailed system description is in the EU AI Act self-audit (system brief of 16 November 2026).

## Does it process personal data?

**Yes, but only incidentally and in small amounts.** The system targets companies, not people. It never searches for a person by name. Personal data still enters in three ways:

1. **Inside public sources about the company.** Homepage, "about" page, careers page and job postings name managing directors, founders and HR contact persons, sometimes with direct phone numbers and email addresses. News articles name and quote people. Entries from the German company register sites (Unternehmensregister, Bundesanzeiger, Handelsregister) name directors and authorised signatories.
2. **Contact details typed in by the builder.** Optional command-line fields for a contact person's name, email and city are saved to a separate file (`lead.json`). They are not used in the analysis.
3. **In the outputs.** The brief can repeat names from the sources. The run file (`state.json`) keeps every collected text snippet in full.

No person is profiled, scored or ranked. The 0–10 "AI potential" rating applies to work steps of the company.

## Where the data comes from

| Source | Personal data in it | How it is obtained |
|---|---|---|
| Company website (home, about, careers, up to 5 job postings) | Names, roles, contact details of staff | Direct download from the builder's machine |
| Tavily web search: news (last 365 days), register sites, job ads (up to 16 results) | Names, roles; in register entries possibly date of birth and place of residence of directors | Tavily API, US company |
| Builder's own input | Contact name, email, city | Typed in at the command line |

## What it is used for

- **P1 Meeting preparation:** describe the company and suggest AI use cases for a first conversation.
- **P2 Traceability:** keep the run file so every claim in the brief can be traced back to its source.
- **P3 Sales follow-up:** keep a contact person's details next to the brief (`lead.json`).
- **P4 Planned, not built:** a public web form (lead magnet) where a company owner enters website, name, email and phone and receives a short report automatically.

## Who processes it

| Party | What it receives |
|---|---|
| The builder (sole consultant) | Everything, on his laptop |
| OpenAI | All collected text snippets, including any names, in several model calls; process steps for the image prompt |
| Tavily | Search queries containing only the company name; returns result texts that can contain personal data |
| Pinecone | Only the built-in library of 51 reference use cases. No company or personal data |

## Where it is stored and processed

- **Builder's laptop (Germany):** `outputs/<company>/` holds `report.md`, `state.json`, the diagram and, if entered, `lead.json`. The folder is excluded from Git. There is no deletion rule.
- **Public GitHub repository:** one sample brief (Ankerstein). Checked on 23 November 2026: it names no individuals. The run file of that sample is not published.
- **OpenAI:** EU customer data handled by OpenAI Ireland Limited under OpenAI's data processing addendum, with US parent and sub-processors. API inputs and outputs are kept up to 30 days for abuse monitoring.
- **Tavily:** US. Tavily describes itself as controller of its search index.

## Decisions about people

None. The output is preparation material for the builder. No decision about any person follows from it, and the builder reads every brief before a meeting. The planned lead magnet would send a report to an outsider without prior review, but that report also concerns a company, not a person.
