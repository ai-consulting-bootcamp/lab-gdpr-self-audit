# Stretch

## Data Protection by Design Checklist

Since this system processes no personal data, there is no "highest-risk processing activity involving personal data" to audit in the traditional sense. This checklist is instead applied to the **closest analogous risk activity**: handling of business-identifying data (part descriptions and facility addresses tied to a specific client engagement), since this is the most sensitive data category the system does handle, even though it falls outside personal data.

| Design principle | Current state | Pass / Fail / Unknown |
|---|---|---|
| **Data minimisation** — only the minimum necessary data is collected | Inputs are limited to exactly what's needed for cost calculation (material, weight, features, addresses, quantity) — no extraneous fields are collected | **Pass** |
| **Purpose binding** — data is technically restricted to the stated purpose | All inputs flow directly into the cost/freight calculation pipeline with no secondary use (e.g., no marketing use, no analytics profiling of requests) | **Pass** |
| **Access controls** — access is limited to those who need it | Google Sheets and Notion access controls are asserted to follow standard Workspace/account permissions, but this was not independently verified as part of this audit | **Unknown** |
| **Retention enforcement** — automated deletion or anonymisation is in place | No retention or deletion policy is documented anywhere in the system for logged requests | **Fail** |
| **Subject rights workflow** — N/A given no personal data, but analogously: can a client request their own business data be deleted from the system? | No documented process exists for a client to request their historical reports/data be removed | **Fail (by analogy)** |
| **Incident response** — breach detection and 72-hour notification process is documented | No incident response process is documented for this system | **Fail** |

**What would need to change:** a written retention policy (even a simple one — "logs older than 90 days are purged"), a documented incident-response contact/process (even a one-line commitment for this consulting-scale MVP), and direct confirmation of Sheets/Notion access restrictions rather than an assumed default. None of these are GDPR-mandated given the no-personal-data conclusion, but all three are the kind of operational hygiene a real client engagement should have regardless — and each becomes non-negotiable immediately if the system's scope ever expands to include personal data.
