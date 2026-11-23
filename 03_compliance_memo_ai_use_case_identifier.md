# Compliance memo: AI Use Case Identifier

**To:** External legal counsel (the business has no data protection officer)
**From:** Friedrich Tschoepke, AI consultant and builder of the system
**Date:** 23 November 2026
**Re:** GDPR readiness of the research agent before use with real prospects

**Bottom line: proceed with conditions.** The system targets companies, not people, but it collects and keeps more personal data from public sources than it needs, without a deletion rule or any of the records GDPR expects.

**What the system does with personal data.** For each company it reads the website, job postings, news and register entries. These name managing directors, HR contacts with direct phone numbers, and sometimes directors' dates of birth. All of this goes to OpenAI and is saved without time limit on my laptop. No person is scored or decided about. A DPIA screening shows one clear criterion (new technology), so a full DPIA is not needed now.

**Top three actions, in this order:**

1. **Before the next real prospect: collect less.** Remove phone numbers, email addresses, dates of birth and residence from the collected text before it reaches OpenAI or the run file. Keep names and roles of management only. Stop saving contact persons in `lead.json` until action 3 is done.
2. **Within two weeks: set limits and contracts.** Delete run files six months after the first meeting unless a client engagement follows, and automate this. Accept and archive OpenAI's data processing addendum and confirm its transfer mechanism. Note that Tavily acts as controller of its own index and receives only company names from me.
3. **Before any outreach or the planned web form: write the paperwork.** A record of processing activities, the legitimate interests assessment in this audit, a privacy notice on my website, and a short notice for contacts at first contact. No marketing emails without recorded consent; the web form needs a separate, unticked consent box for follow-up.

**Residual risks after these steps:**

- **Copies outside my control.** OpenAI keeps inputs for up to 30 days. Tavily keeps its own index. I cannot honour an erasure request there.
- **Unexpected content.** Web sources can contain health or union details about individuals. Filters and my review reduce this risk but cannot rule it out.
- **Unnamed people.** People named in sources are not informed individually. Relying on the disproportionate-effort exemption is defensible but contestable.

**What this memo is not.** It is not a legal opinion, not a DPIA and not a certification. It is a first-pass self-assessment by the builder. Please confirm in particular the lawful basis for outreach to contacts and Tavily's role before I rely on it.
