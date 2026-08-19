# Phase 4 — Risk and rights analysis

## Special category data (Article 9)

No special-category data is collected or processed by design. The system's subject matter is
vehicle geometry, and its outputs are measurements, rule flags, and engineering explanations.
None of the eight Article 9 categories (health, biometric, political opinion, religious belief,
sexual orientation, ethnic origin, trade union membership, genetic data) are present in the
structured data.

However, the designer's typed questions are free text with no input filtering. A designer could
type "I'm back from sick leave, catching up on zone 2" or "the team lead's feedback was
biased." These would be stored in the thread, sent to the LLM, and potentially included in a
handoff report. The system does not seek or process this data intentionally, but it does not
prevent it from entering, and it retains everything. This is incidental processing, not
systematic — but it means we cannot categorically state that no special-category data is ever
present. The practical mitigation is data minimisation: do not retain free-text thread history
longer than necessary, and do not include raw question text in handoff reports unless the
designer explicitly selects it.

## Automated decision-making (Article 22)

Article 22 applies to decisions based solely on automated processing that produce legal effects
or similarly significant effects on people. RegGuard-Mini does not meet this threshold on any
count.

The system's outputs are about vehicle geometry, not about people — no person is scored, ranked,
hired, denied a service, or evaluated. The designer reviews every output before acting on it;
the system cannot write geometry or send reports autonomously. And even within the geometry
domain, outputs are advisory: "this area may conflict with rule X" is a suggestion, not a
determination.

The one area worth noting: if an employer were to repurpose the version-history and
work-pattern data to evaluate a designer's productivity or competence, *that* use could trigger
Article 22. It is not a use we enable or intend, but it is technically possible with the data we
create. The control is contractual (prohibit this use in the DPA) and technical (do not expose
aggregated work-pattern dashboards or exports).

## DPIA trigger analysis

Applying the EDPB's nine criteria:

| # | Criterion | Applies? | Reasoning |
|---|---|---|---|
| 1 | Evaluation or scoring of people | No | The system evaluates geometry, not people. |
| 2 | Automated decision-making with significant effects | No | No decisions about people; advisory outputs only. |
| 3 | Systematic monitoring | **Arguable** | The system does not monitor people by design. But the version timeline with timestamps and authorship labels creates a continuous, granular record of one employee's work behaviour over weeks or months. If a regulator views this as systematic monitoring of employees in a workplace, this criterion fires. |
| 4 | Special category data at scale | No | Not processed by design; incidental presence in free text is not "at scale." |
| 5 | Large-scale data processing | No | Per-user, per-session processing; not population-scale. |
| 6 | Matching or combining datasets | No | No dataset combination. |
| 7 | Data concerning vulnerable people | No | Users are professional designers in a workplace context; not a vulnerable category. |
| 8 | Innovative technology | **Yes** | An AI assistant using LLM inference on proprietary industrial data is novel technology in this domain. The EDPB guidance flags innovative use of AI as a trigger. |
| 9 | Cross-border transfer preventing rights exercise | **Arguable** | Data is transferred to the US for LLM inference. Whether this "prevents data subjects from exercising a right or using a service or contract" is a stretch — the designer can still use the tool — but the transfer happens silently, and the designer has no way to know, object, or avoid it while still using the system. |

**Count: 1 clear yes, 2 arguable.** If either arguable criterion is counted, the total reaches
2 and a DPIA is generally required under EDPB guidance.

**My assessment: a DPIA should be conducted before production deployment.** Even at only one
clear trigger, the combination of innovative AI technology, silent international transfers, and
the foreseeable misuse risk of work-pattern data makes this a case where the spirit of the
requirement — identify and mitigate risks before they materialise — clearly applies. Waiting
for a regulator to tell us we needed one is worse than doing one we technically did not.

## Data subject rights friction

| Right | Friction level | Current design support |
|---|---|---|
| **Right of access (Art. 15)** | Medium | A designer could ask "what data do you hold about me?" Thread history and version logs are stored and could be exported, but no export function exists. Building one is straightforward; we just have not built it. |
| **Right to erasure (Art. 17)** | **High** | Deleting a designer's threads and version attributions from a shared version history is not trivial. Other users' versions reference theirs (e.g. "v9 branched from v5"). Erasure could break the version chain or orphan downstream versions. A technical approach is needed: anonymise the authorship label rather than deleting the version, and purge thread content. This must be designed, not improvised at request time. |
| **Right to object (Art. 21)** | Medium | If the lawful basis is legitimate interests, the data subject can object. For the primary service purpose, this effectively means "stop using the tool," which is operationally simple. For the work-pattern data (purpose unspecified), the right to object is the main safeguard — and it currently has no mechanism. |
| **Right to data portability (Art. 20)** | Low | Only applies where the basis is consent or contract. If we use legitimate interests, portability does not apply. If the basis turns out to be contract (Purpose 1), an export of thread history in a structured format would be needed — but this is the same export function needed for access. |
| **Right to rectification (Art. 16)** | Low | The designer can edit their own name and session details. Correcting thread content (a mistyped question) is not currently supported but is low-risk. |

**The hardest right to honour is erasure.** It requires a design decision about version-chain
integrity versus personal-data removal, and that decision should be made now, not when the first
request arrives.
