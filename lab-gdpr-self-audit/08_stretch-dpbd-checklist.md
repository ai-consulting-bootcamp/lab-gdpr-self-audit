# Stretch — Data protection by design checklist

## Highest-risk processing activity

**Session continuity: retaining the designer's thread history (typed questions, AI responses,
timestamps) indefinitely for return visits.**

This is the highest-risk activity because it combines the largest volume of personal data, the
longest retention, the most sensitive content (free-text questions that may contain anything),
and the international transfer to the LLM provider — all in one flow.

## Checklist

| Design principle | Current state | Pass / Fail / Unknown |
|---|---|---|
| **Data minimisation:** only the minimum necessary data is collected | Thread history stores every typed question and every AI response in full, including conversational fragments that are not needed for the analytical result. The system does not distinguish between questions that produced a retained result and questions that were exploratory or conversational. | **Fail** |
| **Purpose binding:** data is technically restricted to the stated purpose | No technical control limits the use of thread data to session continuity. The same data is accessible for version comparison, handoff assembly, and — without restriction — any other use the application or deployer implements. No access-control boundary separates "session continuity" from other purposes. | **Fail** |
| **Access controls:** access is limited to those who need it | The designer sees their own threads. No evidence of role-based access controls preventing a manager, admin, or Onyx support staff from accessing thread history. The handoff report lets the designer include selected thread excerpts, which is controlled — but raw thread access is not scoped. | **Unknown** |
| **Retention enforcement:** automated deletion or anonymisation is in place | No retention period is defined. No automated deletion or anonymisation mechanism exists. Data persists until someone manually deletes it. | **Fail** |
| **Subject rights workflow:** system can support an access or erasure request within 30 days | No export function exists for access requests. No erasure path has been designed — deleting a designer's thread history would orphan version references. The 30-day deadline cannot currently be met with confidence. | **Fail** |
| **Incident response:** breach detection and 72-hour notification process is documented | No breach detection mechanism. No notification procedure. No documented process for identifying that thread data has been accessed without authorisation and notifying the controller within 72 hours. | **Fail** |

## What would need to change

**Data minimisation — two changes.**
First, separate the analytical result (the flagged zone, the measurement, the confidence figure)
from the conversational context that produced it. Retain the result; age out the raw question
text after a defined window (e.g. 90 days or programme close, whichever is shorter). Second,
strip or redact free-text content from inference logs on the LLM side — or confirm that the API
provider already does this within a defined period and obtain written confirmation.

**Purpose binding — one architectural change.**
Implement a technical separation between thread data used for session continuity and thread data
available for other functions. In practice: the handoff assembly should pull from saved results
and selected excerpts, not from the raw thread. Analytics or product-improvement queries should
not have access to identifiable thread content without anonymisation.

**Access controls — one scoping decision.**
Define who can see raw thread content: the designer only, or also their team lead, the OEM admin,
and Onyx support? Document the decision, implement it as role-based access, and log access events.
For Onyx support access specifically: require a justification and log it, because we are a
processor and ad-hoc access to personal data must be accountable.

**Retention enforcement — one implementation.**
Set a retention period (recommendation: tied to the vehicle-programme lifecycle, with a hard cap
of 24 months after the last interaction). Implement automated anonymisation: replace the designer
name with a pseudonym, delete raw question text, retain only the structured results. Run
anonymisation on a schedule, not on request.

**Subject rights workflow — one design and one build.**
Design the erasure path: anonymise authorship labels in the version chain (replacing "Kimi,
your hand" with "Designer [pseudonym]"), delete thread content, and leave the version structure
intact. Build an export function that packages a designer's thread history, version attributions,
and any reports they authored into a structured, machine-readable format. Both must be tested
against the 30-day deadline before a request arrives.

**Incident response — one document and one process.**
Write a breach-response procedure: who is notified internally, how the controller (OEM) is
informed within the timeline they specify in the DPA (which must be ≤72 hours to allow the
controller to meet their own Art. 33 deadline), and what information the notification includes.
Implement basic breach-detection logging: anomalous access patterns on thread data, failed
authentication spikes, and bulk-export events.
