# GDPR compliance memo: Programme Research Agent

**To:** Legal counsel, Unioptt (no DPO appointed yet) · **From:** Elif Yurdakul, AI consultant · **Re:** First-pass GDPR assessment before launch with real students

**Bottom line: Proceed with conditions.** The prototype is low-risk because it uses a synthetic student, but launching it for real Unioptt students, many of them minors, needs contracts, documentation and a few design changes first.

**What we found.** The agent researches public university pages and compares a student's grades, language level and budget with a programme's requirements. It makes no decisions and processes no sensitive data, and it does not train any AI model. The risks sit elsewhere: student profiles collected for matching would be reused for a new purpose, page text containing university staff names goes to US AI services, none of the seven external services has a data processing agreement in place, and reports cannot yet be found or deleted per student.

**Top three actions, in order:**
1. **Before any real student data flows:** accept data processing agreements with OpenAI, Pinecone, Airtable, n8n, Tavily and Jina; confirm each US vendor's transfer mechanism; replace the ngrok tunnel and Telegram delivery with Unioptt's own EU-hosted backend. Keep the student description sent to the AI with each page at today's three fields (school type, curriculum, citizenship; no name, grades or budget) and lock this with a test; strip staff names and emails from page text before the AI call.
2. **Before launch:** carry out a DPIA, ideally for the whole Unioptt platform (minors and psychometric data already require one), including a documented test that reusing the matching profile for readiness reports is compatible with its original purpose.
3. **At launch:** update the privacy notice and the parental consent text to cover this feature; let students request a report without sharing their profile; store reports per student with a retention period (e.g. 12 months) and a working access and deletion route.

**Residual risks (even with these steps):**
- **Wrong facts:** a student may give up on a programme because of an outdated or misread requirement. Sources and statuses reduce this risk but cannot remove it.
- **Vendor dependency:** the AI and search vendors are US-based; a change in their terms or a legal challenge to the EU–US framework could force a quick vendor switch.
- **Minors:** age and parental consent are self-declared in Unioptt today, so some under-18 users may use the feature without valid consent.

**What this memo is not.** It is not a legal opinion, not a DPIA and not a certification. Points marked "legal review" in the audit, especially the lawful basis for minors' data, must be confirmed by counsel before relying on this assessment.

*(≈ 390 words)*