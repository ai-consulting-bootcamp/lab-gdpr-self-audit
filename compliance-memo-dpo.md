# Compliance memo — AI Pre-Scan (GDPR)

**To:** Data Protection Officer · **From:** Ugo Ahukannah · **Date:** 19 August 2026
**Re:** First-pass GDPR assessment of AI Pre-Scan, ahead of any real client use

**Bottom line: proceed with conditions.** The purpose is legitimate and the system makes no
decisions about people — but it stores personal data we say we do not collect, in a third country,
with no way to delete it. That must be fixed before a single real client scan.

Our documentation states we research organisations, not individuals, and that named individuals are
not recorded. In practice the system fetches whole public pages — careers pages, press releases,
changelogs, news — and chunks and embeds them into a US vector store. Those pages carry names, job
titles and quotes. Nothing filters them, and `store.py` has no deletion path, so an erasure request
could only be met by destroying the index. The basis for reading and quoting public sources is
sound; the *storage* is what fails, because a less intrusive design achieving the same result
exists.

**Three actions, in order.**

1. **Store the validated passage, not the page** — the quoted text plus URL, timestamp and hash,
   which is all the evidence gate needs. Add a deletion path and a retention limit. This fixes the
   necessity limb of our legitimate-interests assessment and makes our privacy claim true rather
   than aspirational.
2. **Record the Article 35(1) threshold assessment before real use.** Three of the EDPB's nine
   criteria apply — innovative technology, combining datasets, undocumented transfers — crossing the
   usual two-criteria threshold. It may conclude no full DPIA is needed since no individual is
   assessed; that conclusion still has to be written down.
3. **Vendor paperwork before data flows** — Article 28 agreements with OpenAI, Pinecone and Notion,
   each with a transfer mechanism: Data Privacy Framework where certified, otherwise standard
   contractual clauses plus a transfer impact assessment.

**Residual risks after all three.** Special-category data stays ingestible by accident — a story
about a health matter or a union dispute is fetched like any other page, and minimisation reduces
that without eliminating it. Article 14 transparency stays unresolved: we process data not obtained
from the data subject, and the disproportionate-effort exemption is arguable but must be reasoned
and recorded. And the persistent cross-company vendor corpus, if built, is a different purpose from
a single scan and needs its own compatibility assessment.

**What this memo is not.** It is not a legal opinion, not a DPIA, and not a certification. Engage
counsel before relying on it for any compliance decision.
