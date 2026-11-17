# Verify, Reinforce and Stretch

## CFU 4 / Reinforce: accountability test

*Could I demonstrate compliance to a regulator using only the documentation the project has today?* **No.**

The repository describes the data flows well: the README, architecture diagram and grounding section. But none of the formal GDPR records exist.

| Document a regulator could ask for | Exists? | Note |
|---|---|---|
| Record of processing activities (Art. 30) | ❌ | The brief in file 01 is a starting point |
| Privacy notice (Art. 13) | ❌ | The form only says "Nothing you submit is stored", which is inaccurate |
| DPA with the client (me as processor) | ❌ | Needed for the coach set-up |
| DPA with OpenAI | ❌ / unknown | Standard addendum available; not confirmed as accepted |
| DPA with the n8n host (Ironhack) | ❌ | Course instance, no contract |
| DPA with the email provider | ❌ | Not available for a personal Gmail account |
| Transfer impact assessment (US transfer) | ❌ | Needed if relying on SCCs |
| Legitimate Interests Assessment | ⚠️ Draft | In file 02, Phase 3 (P5) |
| DPIA | ❌ | Required before the client pilot |
| Retention schedule | ❌ | No retention is defined anywhere; tool defaults apply |
| Data subject request procedure | ❌ | No contact address or process |
| Breach response procedure (72 hours) | ❌ | — |
| Technical description of data flows | ✅ | README, workflow export, file 01 |

**Entirely missing:** everything except the technical description. The project documents *how it works*, not *why it's lawful*.

## Reinforce: revisiting one TBD

**TBD: the lawful basis for P1 in the coach set-up**, i.e. whether the career service may send an enrolled candidate's CV to the tool. A lawyer would need:

- the client's **enrolment contract and current candidate privacy notice**, to see whether AI-assisted career support is already covered;
- **how CVs reach coaches today** (collected at enrolment, or sent per application), to test purpose compatibility under Art. 6(4);
- whether using the tool is **optional for candidates**;
- the **data-flow diagram and processor list** (file 01 and the role map);
- OpenAI's **DPA and residency status**;
- the **score logic**, and confirmation it won't drive selection.

All of this can be prepared in advance, which turns a vague "is this OK?" into a 30-minute review.

## Stretch: data protection by design checklist

**Highest-risk activity:** sending full CV text to the OpenAI API, and keeping the results.

| Design principle | Current state | Pass / Fail / Unknown |
|---|---|---|
| Data minimisation | The entire CV, including contact details and any photo-page text, is sent in up to 5 LLM calls. Name, phone and address aren't needed for the analysis | **Fail** |
| Purpose binding | CV data never enters the knowledge base or training, and research APIs get only the company name | **Pass** |
| Access controls | n8n access is limited to course accounts on Ironhack's instance (exact roles unknown). The Gmail Sent folder is accessible to anyone with the sender account | **Unknown** |
| Retention enforcement | No deletion anywhere: n8n keeps executions by default and Gmail keeps Sent mail | **Fail** |
| Subject rights workflow | No contact route; manual search only | **Fail** |
| Incident response | No breach process documented | **Fail** |

**What needs to change:**

- **Minimisation:** add a Code node after "Extract CV Text" that strips email addresses, phone numbers and postal addresses (simple pattern matching) before any LLM call. Add a prompt rule to ignore personal characteristics.
- **Access:** request the role list from Ironhack, and use a dedicated sender account, not a personal one.
- **Retention:** turn off saving of successful executions, keep error executions for 7 days, and use an email provider without a stored Sent copy.
- **Rights:** publish a contact email and a short procedure (find by email address, delete executions, confirm within 30 days).
- **Incidents:** write a one-page breach procedure covering who checks, who decides, and who notifies the supervisory authority within 72 hours.
