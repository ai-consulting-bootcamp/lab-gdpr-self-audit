# Reinforce — Accountability test

## Documentation a regulator could ask for

| Document | Exists? | Notes |
|---|---|---|
| Records of processing activities (Art. 30) | ❌ No | This audit is the closest thing. A formal ROPA would need to be maintained by the controller (OEM), with our processing activities listed. |
| Data Processing Agreement — Onyx ↔ OEM (Art. 28) | ❌ No | Blocking gap. Must be executed before any personal data flows. |
| Sub-processor agreements — OpenAI, cloud host | ❌ No | Required by the DPA. OpenAI publishes a standard DPA for API customers; it has not been executed or reviewed. |
| Transfer Impact Assessment / SCCs / DPF reliance | ❌ No | Data crosses to the US on every LLM call. No transfer mechanism documented. |
| Legitimate Interests Assessment (LIA) | ❌ No (drafted in this audit, not formalised) | Phase 3 contains three LIAs. They need to be extracted into standalone documents, reviewed by counsel, and signed off. |
| Data Protection Impact Assessment (DPIA) | ❌ No | Triggered by at least two EDPB criteria. Must be completed before production. |
| Privacy notice for data subjects (Art. 13/14) | ❌ No | Designers and report recipients are not informed of processing. The OEM's employee privacy notice may partially cover this, but we have not verified. |
| Retention schedule | ❌ No | No defined retention period for any data category. |
| Data subject rights procedure | ❌ No | No documented process for handling access, erasure, or objection requests. |
| Breach notification procedure (Art. 33/34) | ❌ No | No documented process for detecting a breach and notifying within 72 hours. |
| AI Act transparency notice (Art. 50) | ❌ No (drafted in the AI Act audit stretch, not implemented) | Overlaps with but does not replace the GDPR privacy notice. |

**Score: 0 of 11 exist.** The system has no compliance documentation at all. This is expected for
a course project — but it means the answer to the accountability test is unambiguous: we could
not demonstrate compliance to a regulator using the documentation we currently have.

The good news is structural: the *architecture* already does many of the right things (human
oversight, version traceability, confidence disclosure, honest declining). What is missing is
entirely in the documentation and contractual layer. Building the documents is work; redesigning
the system is not required.

## Preparing the hardest TBD for a legal conversation

The TBD I would take to a lawyer first: **whether the OEM's existing employee privacy notice
covers processing by RegGuard-Mini, or whether a supplementary notice is needed.**

What the lawyer would need from me to advise efficiently:

1. **The OEM's current employee privacy notice** — to check whether it already covers "workplace
   tools that process employee names, typed input, and interaction history using third-party AI
   services with international data transfers." Most enterprise privacy notices cover "IT systems
   used in the course of employment" generically, but the specifics (LLM inference, US transfer,
   indefinite retention of typed questions) may not be within what an employee would reasonably
   expect from that generic language.

2. **Our data processing brief** (file `00` in this repo) — so the lawyer sees exactly what
   personal data flows where.

3. **OpenAI's current API data-use terms and DPA** — to confirm what OpenAI does and does not
   do with inference inputs, and what transfer mechanism they offer.

4. **A clear statement of what we want the answer to be** — we want the OEM's existing notice to
   suffice, supplemented by a tool-specific transparency note in the interface. The lawyer's job
   is to tell us whether that is defensible or whether a formal notice update is required.

5. **The version-history data sample** — showing what work-pattern data is incidentally created,
   so the lawyer can assess whether it crosses the line into employee monitoring that would
   require a separate lawful basis or works-council consultation (relevant in Germany under
   § 87(1)(6) BetrVG).

The last point is specific to our likely first customers (German OEMs). Works-council consultation
on IT systems that monitor employee behaviour is a co-determination right under German law, and
it is separate from GDPR. A tool that creates a timeline of which designer made how many
iterations and when they worked is exactly the kind of system a works council will want to review.
This is not a GDPR requirement, but a deployment blocker in practice, and the lawyer should know
about it from the start.
