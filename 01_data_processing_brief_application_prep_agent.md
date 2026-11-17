# Kick-off · Data processing brief: Application Prep Agent

*For a Data Protection Officer who has never seen the project. System audited: my Project 3, [github.com/nmarseu/Project-3-Marseu](https://github.com/nmarseu/Project-3-Marseu). All facts below were checked against the workflow export (`workflow/application_prep_agent.json`), not just the README.*

**Does the system process personal data?** **Yes.** Its core input is a CV, which is personal data by definition. "No personal data" is not an available conclusion.

## 1. What personal data it processes

- **Contact data:** the email address typed into the form (where the report is sent), plus the name, phone number and postal address that CVs normally contain.
- **CV content:** work history, employers, job titles, education, dates (from which age can be estimated), languages, skills. CVs may also contain a photo, date of birth, nationality, marital status, or health, disability, religion or union information, depending on what the candidate chooses to include.
- **Free text from the candidate:** "Extra achievements" (up to 15,000 characters about their results and experience).
- **Generated data about the candidate:** a fit score from 0 to 100, each job requirement labelled strong, partial or gap, rewritten CV bullets, a cover letter and interview notes. These are inferences about the person's suitability for a job.
- **Third parties (incidental):** a pasted job description can name a recruiter or hiring manager. CVs can name references or former managers.
- **Technical data:** visitor IP addresses on the form and landing page. Both load Google Fonts from Google's servers.

## 2. Where it comes from

Directly from the person filling in the form: the job seeker, or a career coach submitting on a candidate's behalf. The system adds public company information (web search, company pages, news), which is about companies, not people.

## 3. What it's used for (separate purposes)

1. **Generate the application pack** (job parsing, fit analysis, CV fixes, cover letter, interview prep).
2. **Fit-score gate:** below 50, the system automatically sends a short "weak match" note instead of the full pack.
3. **Fact-check** the draft against the CV and sources.
4. **Deliver** the report by email.
5. **Operate and debug** the workflow (n8n execution history).

## 4. Who processes it

| Service | What it receives |
|---|---|
| n8n (instance hosted by Ironhack) | Everything: form data, CV file, every intermediate result |
| OpenAI API (`gpt-4o-mini`) | Full CV text, extra achievements and job text, in up to five calls per run |
| Gmail (SMTP, sender account) | Recipient email address and the full report |
| Google Fonts | Visitor IP addresses |
| Jina Reader | The job posting URL only |
| Tavily, NewsAPI | The company name only |
| Pinecone + OpenAI embeddings | A fixed query string only. No candidate data is ever embedded or stored in the knowledge base |

## 5. Where it's stored and processed

- **n8n:** Ironhack-hosted; server location **unknown**. Execution data is kept by default, because the workflow doesn't switch it off.
- **OpenAI:** US-based processing by default. API content may be retained for up to 30 days for abuse monitoring.
- **Gmail:** Google servers; a copy of every report stays in the sender's Sent folder indefinitely.
- **Nothing is stored in a project database.** Pinecone holds only the writing guidelines.

## 6. Does it make or assist decisions about people?

**Yes, it assists, through scoring.** The fit score evaluates a person against a job's requirements, and the system itself makes one automatic decision: full pack or short note. Nobody reviews that before the email goes out.

The decisions that matter (whether to apply, what to send) stay with the candidate. The system doesn't decide who gets a job. But if a coach or recruiter used the score to decide whom to support or put forward, it would directly influence decisions about people.
