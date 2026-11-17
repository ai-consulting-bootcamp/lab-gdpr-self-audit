# Stretch — Data protection by design checklist

**Highest-risk activity:** adverse media research and reporting (P3/P4): named individuals and criminal allegations, processed by an LLM and stored.

| Design principle | Current state of the system | Pass / Fail / Unknown |
|---|---|---|
| **Data minimisation** | Full article text and LLM narrative go into state, prompts, LangSmith and the report, including individuals' names | **Fail** |
| **Purpose binding** | Traces are planned for reuse as an evaluation dataset; reports reused in slides, screenshots and portfolio | **Fail** |
| **Access controls** | Streamlit uses one shared `APP_PASSWORD` (can be empty); API key; reports in a plain local folder; no record of who ran which check | **Fail** |
| **Retention enforcement** | No deletion anywhere; "an audit trail must never overwrite itself" is a design rule | **Fail** |
| **Subject rights workflow** | Reports indexed by company, not person; no correction route; immutable by design | **Fail** |
| **Incident response** | Nothing documented. Possible exposure points: public GitHub repo, LangSmith, the shared Ironhack key | **Unknown** |

**What needs to change:**
- **Minimisation:** the synthesis step outputs company-level findings and a `company_role` field (already planned). Person names are kept only when the person *is* the subject, e.g. a sanctioned owner. Mask names before traces are stored.
- **Purpose binding:** turn LangSmith off for production runs, or mask inputs and outputs. Build evaluation sets from synthetic or anonymised cases. Use anonymised reports in portfolio material.
- **Access controls:** individual logins per user, a log of who triggered each run, and reports stored in the client's document system instead of a folder.
- **Retention:** an automated job that deletes reports after the vendor decision plus the legally required period. Keep a minimal screening record (date, lists checked, result) longer for the audit trail.
- **Subject rights:** a search across reports by person name, and a correction mechanism that **appends** a correction to the audit trail rather than overwriting it. That resolves the clash with "never overwrite".
- **Incident response:** a one-page breach procedure covering key rotation, the GitHub history clean-up and the 72-hour notification. Get processors' notification duties into the DPAs.
