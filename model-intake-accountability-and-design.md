# Model Intake Brief: accountability and privacy by design

## Reinforce: documentation register

Statuses describe the situation at assessment, not promises. Owner: Sergii Rostovskyi; a prospective client must appoint its own accountable owner. “Created in this lab” means an assessment draft, not operational implementation.

| Record a regulator could request | Exists? | Evidence or missing step |
|---|---|---|
| System purpose, architecture and limitations | Yes | Source README and USER_GUIDE; [E1 in evidence register](model-intake-evidence-and-sources.md) |
| Data inventory, recipients and purpose map | Created in this lab | Processing brief and worksheet; validate against actual live traffic |
| Records of processing activities (Art. 30) | No completed operational record evidenced | Use this inventory as input; assess Art. 30 applicability/exceptions and complete required fields |
| Applicable DPAs and processor/subprocessor authorisations | Not documented | Owner arranged none; review whether accepted standard terms already incorporate a DPA and preserve proof |
| Regions, international-transfer mechanism and assessment | Unknown / missing | Verify entities, routes, support access, adequacy scope or SCCs plus assessment |
| Purpose-specific LIA and lawful-basis approval | No approved record | Provisional LIA drafts here remain **TBD — legal review** |
| DPIA screening and national mandatory-list check | Partial, created here | Screening exists; location/national list and owner decision unresolved |
| Full DPIA / prior consultation | Not done; conditional | Required only if applicable high-risk threshold/list is met; no automatic exemption because it is a prototype |
| Privacy notice and indirect-collection information/exception record | No | Owner confirms no notice; determine duties and provide specific notice or justified exception |
| Retention schedule and deletion evidence | No | Proposed periods are recommendations; implement and test them |
| Rights request log and response procedure | No | Set contact, identity-check standard, search locations, recipient coordination and deadlines |
| Security/access-control record | Partial technical controls | HTTPS, domain controls, secret-file ignore rules and quote checks exist; endpoint encryption, access permissions and backup policy unverified |
| Breach register and incident response | No | Document detection, containment and risk assessment; record all personal-data breaches |
| Browser storage/telemetry inventory and consent evidence | Unknown | No runtime capture; classify necessary storage and disable/gate non-essential collection |
| Human review and training record | User guidance only | No enforced approval history; preserve reviewer actions if used in procurement |
| Source accuracy, model version and audit evidence | Partial | Source commit and synthetic evidence included; live completeness and ongoing accuracy not established |

Notification design must distinguish controller notice to the authority within 72 hours of awareness unless risk is unlikely, processor notice to its controller without undue delay, and communication to individuals where high risk requires it. A privacy incident is not automatically a reportable breach; document the decision. Rights handling targets one calendar month, with applicable extension and notification rules. [L1, L5]

## Reinforce: legal-review preparation for one unresolved flow

**Flow:** Jina-extracted public author/contact text → local assessment prompt → OpenAI → downloaded report. **Question:** can any retained personal attribution satisfy necessity and balancing under P1–P3, and on what documented vendor/transfer terms?

Prepare the following for counsel without including real private content in the public lab:

1. A minimised source example showing original publication purpose, publisher, data subject, collection date and whether the individual supplied the information.
2. The exact fields needed for the checklist, alternatives such as corporate attribution or manual review, and the synthetic payload showing the present gap.
3. Controller establishment, intended audience, frequency, scale, whether sole developers/children or sensitive information can appear, and intended report distribution.
4. Actual API account holder/entity, accepted contract/DPA versions, subprocessor list, processing/support regions, retention settings and deletion capabilities.
5. Proposed notice or Article 14 exception reasoning, retention schedule, objection/suppression process, transfer analysis and a change-of-purpose assessment.

**Decision pending:** **TBD — legal review**. Until resolved, keep the flow non-personal and do not describe the candidate LIA as approved.

## Stretch: highest-risk activity design checklist

Activity: uncontrolled extracted public text entering the external LLM and later exports. This is the largest identified privacy exposure in this prototype, not a claim of statutory high-risk classification. Status assesses readiness for personal-data use; “Unknown” means evidence is absent.

| Design principle | Current state of your system | Pass / Fail / Unknown | Required change |
|---|---|---|---|
| Data minimisation: only minimum necessary data | Contact survives synthetic outbound-payload probe; truncation is not redaction | Fail | Minimise sections and identifiers before dispatch; verify with synthetic cases |
| Purpose binding: technical restriction to stated purpose | Fixed checklist narrows output, but raw sources can include unrelated personal text | Fail | Enforce source/content policy and reject private/sensitive inputs |
| Access controls: need-to-know access | Single local user confirmed; filesystem, backups and vendor access unverified | Unknown | Verify device access, file permissions and vendor support controls |
| Retention enforcement: automated deletion/anonymisation | No export expiry; `store: false` is not end-to-end deletion | Fail | Apply approved schedule, clear session/browser state, test vendor deletion |
| Subject rights workflow: timely access/erasure | No coordinated workflow or rehearsal | Fail | Assign contact and run a synthetic request exercise within one calendar month |
| Incident response: detection and 72-hour process | No documented playbook or breach register | Fail | Define detection, escalation, risk assessment and applicable notifications |

The lab's “30 days” wording is treated as a planning prompt; the legal default is one calendar month. These changes are recommendations only; the application source was not modified.
