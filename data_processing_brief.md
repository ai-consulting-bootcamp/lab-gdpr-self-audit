# Data processing brief — Vendor Due-Diligence Agent

**Author:** Pieter Albrecht · **Date:** 17 November 2026 · **For:** a Data Protection Officer who has never seen the project

## What the system is

A LangGraph agent (Ironhack Project 3) that takes a **company name** (optional KvK number) and writes a vendor due-diligence report: identity, ownership, sanctions screening, adverse media, red flags, a risk rating (Low / Medium / High) and a recommendation (Onboard / Onboard with conditions / Escalate / Do not onboard). Intended buyer: a compliance officer at a Dutch law firm, notary or payment company checking a new supplier. Triggers: command line (`main.py`), a Streamlit app, a FastAPI endpoint and an n8n form in front of that API.

## Does it process personal data?

**Yes, even though the input is a company.** Four routes bring in data about natural persons:

1. **Sole traders and one-person companies.** For an *eenmanszaak* the company *is* a person; its name, address and registration are personal data.
2. **The OpenSanctions file** (stored locally in `data/sanctions/`) contains thousands of sanctioned **individuals**: names, aliases, dates of birth, nationalities, listing reasons. Every run fuzzy-matches against all of them.
3. **News articles** found by the agent name **executives, employees, suspects and convicted persons**, often with allegations or convictions. Testing produced exactly this: an ASML ex-employee jailed for passing trade secrets, and a Heineken export manager charged with corruption.
4. **LLM-generated text**: summaries and red flags can attribute conduct to named people, and testing showed they can get the role wrong (victim described as wrongdoer).

The RAG corpus in Pinecone (5 public guidance PDFs) contains **no** personal data.

## Where the data comes from

| Source | What | How |
|---|---|---|
| User | Company name, optional KvK number | CLI, Streamlit, API, n8n form |
| GLEIF API | Legal entity data, LEI, parents | Public API, no key |
| KvK Handelsregister API | Dutch registration (**test environment, fictitious data** in the MVP) | API key |
| OpenSanctions | Sanctions collection, entities and persons | Bulk CSV, downloaded locally |
| Tavily | News search results (title, URL, date, snippet, article text) | API, queries chosen by the ReAct agent |
| OpenAI (gpt-4o-mini) | Generated findings, ratings, report prose | API, **Ironhack bootcamp key** |

## Purposes

1. Identify the vendor (entity resolution) · 2. Sanctions screening · 3. Adverse media research · 4. Risk assessment and report writing · 5. Keeping reports as an audit trail · 6. Debugging and evaluation (LangSmith traces) · 7. Testing, demo and portfolio (sample reports, slides, screenshots)

## Who processes it

My code (locally); **OpenAI** (receives news evidence, names and allegations in prompts); **Tavily** (receives search queries, including names of sanctioned parties in enhanced review); **LangSmith** (stores every prompt, tool call and output); Pinecone (guidance only); n8n (passes the company name and returns the result).

## Where it is stored and processed

| Location | What | Retention |
|---|---|---|
| My laptop: `reports/`, `notes/`, `data/sanctions/` | Reports, raw API responses, sanctions file | **No rule; kept indefinitely** |
| Public GitHub repo | Dated reports are git-ignored, but `reports/archive/`, `notes/`, `screenshots/`, `powerpoint_slides/` are not (**to verify**) | Indefinite, public |
| OpenAI (US) | Prompts and outputs | Per OpenAI API policy (typically up to 30 days for abuse monitoring; **verify**) |
| LangSmith (US, *assumed default region*) | Full traces incl. article text | Per plan default (**verify**) |
| Tavily (US, **verify**) | Search queries | Unknown |
| n8n, Streamlit, API | Pass-through | *Assumed local*, no hosting |

## Decisions about people

The system **rates and recommends**; it does not onboard or reject anyone itself. A compliance officer is meant to decide, but **nothing in the system requires or records a human decision.** The run goes from command to saved report with no human step. For a sole trader, a "Do not onboard" recommendation is a decision about a natural person.
