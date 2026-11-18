# Compliance memo — Editorial research agent

**To:** Legal counsel for *La Insumisa* (no DPO appointed) · **From:** Jaime Garate Marquerie, AI compliance consultant · **Date:** 17 Nov 2026
**Re:** GDPR first-pass assessment of the editorial research agent (Project 3, commit `3939562`)

**Bottom line: PROCEED WITH CONDITIONS.** The agent processes personal data of authors and of people mentioned in public sources. The core purpose is defensible under legitimate interests, but two current practices must stop first.

The agent sends author names, publisher texts and web snippets to Tavily and Google Gemini, saves full results locally and publishes them in a public GitHub repository. Our review of the code and of 20 saved runs found:
- **sensitive information about a real third person** (political militancy, imprisonment) in seven saved files;
- **Gemini used on its free tier**, where Google's terms allow it to reuse submitted content to improve its products.

There is no customer data and no decision about people, so Article 22 does not apply.

**Top three actions, in this order:**

1. **Before the next real run:** move Gemini to a paid, billed project covered by Google's data processing terms, or stop sending retrieved web text to it. Check Tavily's role, data retention and transfer tool, and record the result.
2. **This week:** remove the evidence and dossier files from the public repository, including its git history. Replace them with redacted or synthetic samples. Locally, keep only URLs and the fields used, delete raw snippets, and set a retention period (we suggest 90 days for test runs).
3. **Before any pilot with other bookshops:**
   - write the accountability pack: record of processing, legitimate-interests assessment, Article 14 information or a documented exemption, and DPIA screening;
   - add a way to exclude a person on request;
   - prepare a processor agreement for each bookshop.

**Residual risks that remain after these actions:**

- **Incidental sensitive data.** Web sources will keep returning sensitive details about real people. Filtering reduces the risk; it cannot guarantee zero.
- **Inaccuracy.** The LLM can attribute wrong editions or themes to an author's work. That is an accuracy issue (Article 5(1)(d)) that human checking only partly controls.
- **Copies beyond our control.** Copies already cloned or forked from the public repository, and content already sent to the free tier, cannot be recalled.

**What this memo is not.** It is not a legal opinion, not a DPIA and not a certification of compliance. It rests on a technical review of a bootcamp prototype and public provider terms (17 November 2026). Please obtain legal advice before relying on it for compliance decisions.
