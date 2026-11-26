# Verify, Reinforce and Stretch - Menohelp

## CFU 4 - Verify: the accountability test

**Could I demonstrate compliance to a regulator using only what the project has today? No.** The code shows good privacy engineering (stats instead of raw rows, an allow-list lab parser, a 1-hour in-memory store). But the GDPR asks for *documented* compliance (Art 5(2)), and almost none of the paperwork exists.

### Reinforce: the documents a regulator could ask for

| Document | GDPR | Exists? | Notes |
|---|---|---|---|
| Records of processing activities | Art 30 | ❌ | The <250-staff exemption doesn't apply: special-category data is processed. The Phase 1 inventory is a first draft. |
| Privacy notice | Art 13 | ❌ | Only UI captions, and "Nothing is stored" is inaccurate. |
| Consent wording + consent records | Art 7(1), 9(2)(a) | ❌ | No consent step at all. |
| DPA (client ↔ me) | Art 28 | ❌ | |
| DPAs with OpenAI, Resend, host | Art 28(4) | ❌ | Vendor DPAs exist as templates; none executed. |
| Transfer impact assessment | Ch. V, *Schrems II* | ❌ | |
| Joint-controller arrangement (coaches) | Art 26 | ❌ | Role not decided yet. |
| LIA (run log) | Art 6(1)(f) | 🟡 | Drafted in this audit (worksheet, Phase 3). |
| DPIA | Art 35 | ❌ | Risks listed informally in `docs/PROJECT_DRAFT.md` and this audit. |
| Retention schedule | Art 5(1)(e) | 🟡 | Enforced in code (`TTL_SECONDS = 3600`), not written as a policy; vendor retention not covered. |
| Security measures (TOMs) | Art 32 | 🟡 | README privacy section, allow-list parser, tests. No access control on the API, no written TOMs. |
| Breach procedure | Art 33-34 | ❌ | |
| Data subject request procedure | Art 12, 15-22 | ❌ | No contact point. |
| DPO assessment | Art 37 | ❌ | Not large-scale yet; record the reasoning. |
| Evidence of consent for the showcase report | Art 9(2)(a) | ❌ | See flag C in the worksheet. |

**Score: 0 complete, 3 partial, 12 missing.** The gap is documentation, not engineering, so most of it is cheap to fix.

### Reinforce: preparing one `TBD - legal review` (coach role, P5)

A lawyer needs to answer: are freelance coaches joint controllers with Wechselweise, separate controllers, or processors? And can any coach rely on Art 9(2)(h) instead of consent? To make that conversation short, I'd bring:
1. **Contract chain:** the coach agreement (freelance or employed), who pays whom, who chooses to use Menohelp.
2. **Who decides what:** a table of who sets the purpose (consultation prep), the means (Menohelp, OpenAI) and the retention of downloaded reports.
3. **Coach qualifications:** whether any coach is a licensed health professional bound by professional secrecy (e.g. §203 StGB), which matters for 9(2)(h) and 9(3).
4. **Data flow diagram:** client → coach → Menohelp → OpenAI → report → coach's files.
5. **Draft consent text and privacy notice** for coach clients, plus one sample report.

## Stretch: data protection by design checklist

**Highest-risk activity:** P3, sending a woman's findings, lab values, symptom answers and free text to OpenAI to write the report. It combines health data, profiling and a US transfer.

| Design principle | Current state | Pass / Fail / Unknown |
|---|---|---|
| Data minimisation | The model sees computed stats, never raw cycle rows. Name and DOB are dropped from lab PDFs, and only allow-listed values are kept. Still sent: exact age, the free text, sexuality ratings. | **Pass** (refinements below) |
| Purpose binding | In code, data flows only into the report pipeline. At OpenAI, only default API terms apply: no DPA signed, no zero data retention. | **Unknown** |
| Access controls | The UI has one optional shared password. The FastAPI has **no authentication**: anyone holding a 12-character dataset id can read, and `PUT /labs/{id}` can change, that data for up to 1 hour. | **Fail** |
| Retention enforcement | Automatic deletion after 1 h on my server (max 20 datasets). OpenAI keeps data up to 30 days. Streamlit keeps session state until the tab closes. | **Pass** on my side, **Fail** at the vendor |
| Subject rights workflow | No contact point, no procedure, no documented answer to "what do you hold about me?". | **Fail** |
| Incident response | No breach procedure. With no logs, a breach would be hard to detect. A mistyped email address is already a reportable breach. | **Fail** |

**What would need to change.**
- **Minimisation:** send an age band instead of the exact age. Scrub names and contact details from the free text before the prompt, or keep it out of the prompt entirely. Filter a Clue export to `period` rows in the browser before upload.
- **Purpose binding and retention at the vendor:** sign OpenAI's DPA, request zero data retention and EU data residency, and record it in the sub-processor list.
- **Access controls:** don't expose FastAPI publicly; run it in-process or behind the UI with a per-session token. Make lab values read-only after confirmation. Replace the shared password with per-user sign-in once accounts exist.
- **Subject rights:** a privacy contact address and a one-page procedure with templated answers ("we hold nothing after 1 h; OpenAI may hold your prompt for up to 30 days").
- **Incident response:** a one-page breach playbook (who decides, 72-hour clock, Art 34 notice to the woman). Add the metadata-only run log from P7. Replace open email with download or a verified address, which removes the most likely breach.
