# Data processing brief - Menohelp

**For:** a Data Protection Officer who has never seen the project · **Date:** 26 Nov 2026 · **Not legal advice.** Items marked ⚖️ need confirmation by counsel.

**System.** Menohelp is my bootcamp build project (code: `course work/week-6/proj-menopause-insights`, public GitHub repo). A woman uploads her own health data and gets a plain-language report on whether her cycle pattern looks like perimenopause, what may help, and what to raise with a doctor. It runs locally as a prototype. It is not deployed and has no real users. For this audit, the client is the **fictional** Wechselweise Coaching GmbH (Germany), which would offer Menohelp to its customers and coaches. This is the same scenario as my EU AI Act self-audit.

**Does it process personal data?** Yes, and almost all of it is **health data** (Art 4(15), Art 9). The pseudonymous `user_id` and the missing name don't make it anonymous: an exact age, dated cycle starts and dated blood draws single a person out.

## 1. What personal data

| Group | Fields |
|---|---|
| **Cycle log** (CSV/JSON, e.g. a Clue `measurements.json` export) | Cycle start dates, cycle length, period length, flow, optional age and `user_id`. A Clue export also holds everything else she logged (sex, mood, pain, pill use). The code keeps only `period` entries, but the whole file reaches the server first. |
| **Blood test PDF** (optional) | The PDF holds name, address, date of birth, lab number and every result, including infection serology. Code extracts **only** an allow-list of analytes (hormones, thyroid, etc.), the draw date, the cycle day and the age computed from the date of birth. Everything else is never extracted. |
| **Questionnaire** (optional) | Age, hormonal contraception or HRT, hysterectomy/ovary removal, last period, ratings for 14 body systems (including **mood** and **sexuality/libido**), and one free-text box "What bothers you most?" (200 characters). |
| **Derived (inferred) data** | Cycle statistics and flags, a triage category, case tags (e.g. "young"), age-norm positions (e.g. "AMH very low for age 30"), candidate explanations (e.g. "early change, discuss with a gynaecologist"), and the report text. This is **profiling** (Art 4(4)) of health. |
| **Contact data** | The email address the report is sent to (hers, or a third party such as her doctor). |
| **Technical data** | IP address and request logs at the host; Streamlit session state while the browser tab is open. |
| **Not personal data** | Licensed coaching PDFs and instruction chunks in the RAG store. |

## 2. Where it comes from
Directly from the woman, who exports it from her cycle app and her lab report. In coach use (planned Sprint 2), the **coach** uploads it on the client's behalf. Demo data: two Kaggle datasets (one CC BY-NC 4.0, one CC0), a synthetic persona, and one showcase report the README describes as built on **real data**.

## 3. What it is used for
1. Calculate cycle statistics and flags (code only).
2. Read blood values from the PDF (code only).
3. Combine cycle, labs and symptoms into findings and a triage category (code only).
4. Send findings, lab values, symptom ratings, age and the free text to **OpenAI** to write the report.
5. Show the report on screen; optionally **email** it via Resend.
6. Planned: coaches use the report to prepare consultations; pilot feedback forms.

## 4. Who processes it
My code (FastAPI + LangGraph + Streamlit), **OpenAI** (text generation and embeddings of fixed retrieval queries), **Resend** (email), the planned host (**Render** and/or **Streamlit Community Cloud**). **Supabase** stores only the coaching material and receives no user data.

## 5. Where it is stored and processed
- **My server:** in memory only, deleted after **1 hour** (`TTL_SECONDS` in `app/api/store.py`), max 20 datasets. No database, no logs.
- **OpenAI:** US processing by default; the API keeps inputs and outputs for **up to 30 days** for abuse monitoring unless zero data retention is approved.
- **Resend:** US company; sending region and log retention not yet configured (unknown).
- **Hosting:** not chosen. Streamlit Community Cloud runs in the US; Render offers a Frankfurt region.
- **GitHub (US):** the public repo holds the showcase report and its chart.

## 6. Does it decide anything about people?
It makes **no decision** and nobody acts on its output automatically. But it **evaluates** a woman's health and can tell a woman under 40 that her values point to an early change worth checking. **No human reviews the report** before she reads it; only automatic number and wording checks run. In coach use, a human (the coach) reads it before a consultation.

---

## CFU 1 - Recognize

| Question | Answer |
|---|---|
| **Personal data categories** | Health (cycle, labs, symptoms, surgery, medication), sex life (libido and painful-sex ratings, the raw Clue export), age, contact (email), technical (IP), and inferred health attributes. |
| **Art 9 present?** | **Yes, at the core.** Health data in every input, and data concerning **sex life** in the symptom ratings and Clue export. |
| **Art 9 inferable?** | Yes. The output infers reproductive status (perimenopause, possibly premature ovarian insufficiency), fertility (low egg reserve) and mental health (low mood red flags). Serology in the lab PDF (e.g. hepatitis) would reveal more, but the allow-list never extracts it. |
| **Crosses an EU border?** | **Yes.** OpenAI (US), Resend (US by default), Streamlit Cloud (US) if used, and GitHub (US) for the public showcase report. Only my own code and the in-memory store could stay in the EU. |
