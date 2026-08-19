# Reinforce

## Accountability Principle — Documentation Inventory

| Documentation | Exists? |
|---|---|
| DPA with vendors (OpenAI, Pinecone, etc.) | Not established — not currently required, since no personal data is processed, but would need to exist immediately if scope changes |
| LIA (Legitimate Interests Assessment) | N/A — no lawful basis analysis was needed, since no personal data is processed |
| DPIA | N/A — not triggered |
| Privacy notice | **Missing entirely.** No privacy notice exists for this system, likely because it was never flagged as necessary given the no-personal-data conclusion — but a short public statement confirming what data is (and isn't) collected would be good practice for a client-facing tool regardless |
| Retention schedule | **Missing.** Flagged already in Phase 1 — no documented retention period for any logged data, even non-personal data |
| Records of Processing Activities (ROPA) | **Missing.** GDPR's Article 30 ROPA requirement applies to controllers processing personal data — not triggered here, but maintaining a lightweight internal record of what data the system touches (even confirming "none of it is personal") is good practice and this audit itself effectively serves as a first version of that record |

**What's entirely missing from the project:** a privacy notice and a retention schedule — both good practice even for a system that doesn't process personal data, since a client or regulator reviewing this system cold would want to see that its data-minimal design was a deliberate, documented choice, not an accident of scope that was never examined.

## Revisiting a TBD — What Would a Lawyer Need to Know?

The closest thing to a "TBD — legal review" item in this audit is the logging-retention gap (Phase 1). If this were escalated to a lawyer, they'd need to know: (1) does any vendor in the stack (OpenAI, Pinecone, n8n) retain request-level logs by default, and for how long, under their own data processing terms; (2) if so, could any part description or business address, even though not personal data, still carry any confidentiality concern for the client's own business (e.g., revealing a client's supplier negotiation strategy)?

What could be prepared in advance to make that conversation efficient: pulling each vendor's own data retention policy from their terms of service (OpenAI, Pinecone, Google, Notion all publish this) before the call, so the lawyer is reacting to concrete vendor commitments rather than starting from zero.
