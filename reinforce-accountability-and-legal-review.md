# Reinforce — the accountability file, and preparing the legal question

## 1. What a regulator would ask for, and what exists

The accountability principle in Article 5(2) is not "did you behave well", it is "can you
demonstrate it". Below is every document an inspection would reasonably ask for, ticked against what
this project actually has.

| Document | Exists? | Where it is, or what would have to be written |
|---|---|---|
| **Records of processing activities** (Art 30) | ❌ | Phase 1 of this audit is the first inventory ever produced. Art 30(5) exempts organisations under 250 staff *unless* processing is non-occasional — scanning is the product, so the exemption does not apply |
| **DPA with OpenAI** (Art 28) | ❌ | Available off the shelf from the vendor; nobody has accepted it |
| **DPA with Pinecone** | ❌ | Same |
| **DPA with n8n / Notion** | ❌ | Only needed if delivery is used with real client data |
| **Transfer mechanism + TIA** (Ch. V) | ❌ | Four US recipients: OpenAI, Pinecone, Notion, GitHub |
| **Legitimate Interests Assessment** | ❌ → now partial | Phase 3 of this audit is the first written LIA, and it concludes the necessity limb currently fails |
| **DPIA, or a recorded Art 35(1) threshold assessment** | ❌ | Three EDPB criteria apply; the assessment must be written down even if it concludes no DPIA is required |
| **Privacy notice / Art 14 reasoning** | ❌ | Data is not obtained from data subjects, so either notify or record why that is disproportionate |
| **Retention schedule** | ❌ | And unenforceable today — `store.py` has no deletion path to attach one to |
| **Breach detection and 72-hour notification procedure** | ❌ | No detection, no owner, no timeline |
| **Provenance records for every finding** | ✅ | URL, retrieval timestamp and hash per finding; **zero provenance violations across 64 findings** |
| **Measured evaluation of system behaviour** | ✅ | `eval/results.md`, five runs, failures published rather than hidden |
| **Architecture and data-flow documentation** | ✅ | `docs/architecture.md` — genuinely usable as the basis for a RoPA |

**Two out of thirteen, and the two that exist were built for accuracy rather than for compliance.**
That is the honest headline. It is also a reason for optimism rather than despair: the provenance
contract is precisely the artefact regulators find hardest to get from AI systems, and it already
exists. The missing items are paperwork and one code change, not a rebuild.

**The pattern worth naming.** Everything present is about whether the system's *output* is true.
Everything absent is about whether its *processing* is lawful. Those are different questions and I
only ever asked the first one.

## 2. Preparing the `TBD — legal review` question properly

The flow I flagged is **P3, the persistent cross-company vendor corpus** — designed, not yet built,
intended to hold vendor AI-feature announcements and changelogs across all scans so the system can
answer "did this vendor ship AI into this product, and when".

**What a lawyer actually needs to advise on it**, and what I can prepare in advance so the
conversation takes twenty minutes rather than two meetings:

| What they need | What I can hand them now |
|---|---|
| What personal data would actually be in it | A sample of ten real vendor changelogs and announcements, marked up for names, bylines and quotes — evidence, not my estimate of how much personal data is in them |
| Whether it is a new purpose or compatible with the original one | The Art 6(4) factors applied honestly: the link between purposes (both are AI-adoption research), the context of collection (published vendor marketing), the nature of the data (professional, low sensitivity), the consequences (none for the individual), and the safeguards available (name stripping, aggregation) |
| Whether the data could be minimised out of scope entirely | A concrete answer: yes, and I should test it first — the corpus needs *product, feature, date, source*, and it is plausible that no personal data is needed at all. If so, the legal question disappears rather than being answered |
| Retention and deletion | A written proposal, since indefinite retention is the design assumption today and that is exactly what a lawyer will challenge |
| Who the controller would be | Depends on the release model — me if I ship it, the adviser's firm if they self-host. Prepared as a short either/or with the consequences of each |

**The single most useful thing I can do before that conversation is the minimisation test.** If the
corpus works with product and date fields alone, there is no personal data, no compatibility
assessment and no retention argument. A lawyer's time is best spent on the question that survives
that test — not on one I could have engineered away myself.
