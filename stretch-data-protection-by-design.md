# Stretch — data protection by design checklist

**Highest-risk processing activity:** ingestion of whole fetched pages into the `scan-<company>`
namespace — chunked, embedded via OpenAI, stored in Pinecone. This is the activity that turns a
system researching organisations into one holding personal data about individuals.

| Design principle | Current state | Verdict |
|---|---|---|
| **Data minimisation** — only the minimum necessary data is collected | Whole pages are fetched, chunked and embedded. The evidence gate only ever uses the validated passage plus its provenance metadata, so the surplus is never read | **Fail** |
| **Purpose binding** — data is technically restricted to the stated purpose | Two namespaces share one index. Nothing technically prevents scan data being read for the vendor-corpus purpose; the separation is a naming convention, not a control | **Fail** |
| **Access controls** — access is limited to those who need it | The UI binds to 127.0.0.1 with no accounts, so local access is inherently limited. But the Pinecone index is reachable by anyone holding the API key, and there is no per-namespace restriction | **Unknown** — adequate locally, undefined at the vendor |
| **Retention enforcement** — automated deletion or anonymisation | `store.py` contains no deletion path at all: no vector delete, no namespace purge, no TTL. Retention today is "forever, by omission" | **Fail** |
| **Subject rights workflow** — access or erasure answerable within 30 days | Vectors are keyed by company, not person; there is no way to find or remove one individual's data, and no deletion primitive to call even if there were | **Fail** |
| **Incident response** — breach detection and 72-hour notification documented | No detection, no named owner, no documented procedure | **Fail** |

**Score: 0 pass, 5 fail, 1 unknown.**

**What would need to change, in dependency order.** The five failures are not five projects — four of
them collapse into one change and one document.

**Change the ingestion contract.** Store the validated passage, its URL, retrieval timestamp and
hash; cache the whole page only for the life of the scan and discard it at the end. This fixes
minimisation directly and shrinks everything downstream: less data stored means less to delete, less
to search for a rights request, and less to lose in a breach.

**Add the deletion primitives the store never had.** A vector delete, a namespace purge, and a TTL on
`scan-<company>`. Retention enforcement and the erasure half of subject rights both depend on this
and cannot be fixed by policy.

**Add a person-name index or accept the limit honestly.** With passages rather than pages, the
residual personal data is small enough that a scan-level purge is a credible answer to an erasure
request. If that is the answer, it should be written down as the answer rather than left as an
unexamined gap.

**Separate the namespaces properly**, with distinct indexes or credentials, so purpose binding is
enforced by the infrastructure rather than by a naming convention I remember to respect.

**Write the incident procedure.** One page: what counts as a breach here (most plausibly an exposed
Pinecone or OpenAI key), who notices, who decides, and the 72-hour clock. This is the only item on
the list that is pure documentation — and the only one that has to exist before, not after, the
thing it describes happens.
