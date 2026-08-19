# Intellectus data processing brief

**Prepared for:** a Data Protection Officer unfamiliar with the project  
**System assessed:** [Intellectus — Social Impact Intelligence](https://github.com/paolahsp/Social-Impact-Consulting-Intelligence)  
**Assessment boundary:** demonstrated public-data MVP versus a prospective production pilot

## System and flow

Intellectus is a consultant-facing diagnostic tool for social-impact organisations. In the demonstrated MVP, a consultant enters an organisation name, website, country, current challenge and research window in a React web application. The browser sends JSON to an n8n webhook, which invokes a child workflow, performs bounded public-web research and local knowledge retrieval, structures evidence and findings, and returns a draft diagnostic for consultant review. The public repository contains controlled fixtures and retained public-source evidence; it contains no credentials or private client data.

The current interface includes `uploaded_document_refs`, but the evidenced browser flow does not upload document contents: selected files remain session-only until a secure server-side upload boundary exists. Processing internal client documents, using a hosted external AI model, and storing production case files are therefore **prospective**, not demonstrated current capabilities.

## Personal data

The MVP can process personal data even though its target is an organisation. A consultant may enter a person's name, role, business contact detail or narrative about a person in the free-text challenge field. Public research can retrieve names, professional roles, quotations, public contact details and statements written by or about employees, volunteers, leaders or other identifiable people. URLs, search results, run identifiers and timestamps may also become personal data when linked to a user or named individual. Controlled demo fixtures are fictional, but public-source runs can include real people.

A future private-document pilot could additionally expose employee and volunteer records, donor or beneficiary information, case narratives, performance comments and inferred attributes. Those documents may contain Article 9 data, including health, disability, political or religious beliefs, ethnicity or trade-union membership. Such data is excluded by default until a separate Article 6 basis, Article 9 condition and necessity assessment are approved.

## Sources and purposes

Data comes from: (1) the consultant or client representative completing intake; (2) public websites and search results; (3) system-generated workflow metadata; and, only in a future pilot, (4) client-provided internal documents. The purposes are kept separate: establish the organisational context; retrieve and cite bounded public evidence; generate a structured diagnostic draft; enable consultant quality review; and maintain limited security and troubleshooting records. Internal documents must not be reused for model training, general product improvement or another client without a new lawful-basis and purpose-compatibility assessment.

## Actors, storage and locations

The React application, n8n workflows, public web sources and local retrieval corpus participate in the demonstrated path. A client organisation would normally be controller for its internal data and diagnostic purpose; the Intellectus service operator would normally act as processor under documented instructions. The exact hosting, n8n deployment, log storage, subprocessors, retention periods and processing countries are not established in the public project evidence. No EEA-to-third-country transfer may be assumed lawful until the deployment map, vendor DPAs, hosting regions and transfer mechanisms are recorded. Any future external AI provider would be a processor or subprocessor and must be assessed before activation.

## Decisions and human review

Intellectus produces research-supported hypotheses and recommendations about an organisation. It does not currently make hiring, eligibility, service-access, credit or other decisions with legal or similarly significant effects on individuals. A consultant must review the evidence, unknowns, inferences and proposed actions before anything is used with a client. This human-review gate is mandatory; the system must be reassessed if future use introduces person-level scoring, ranking, flagging or consequential decisions.

## Current conclusion

GDPR applies because real public-source and free-text inputs can identify people. The demonstrated MVP is lower risk than the proposed private-document production scenario, but it still needs documented purpose limits, a legitimate-interests assessment, minimisation, retention and rights handling. Private client documents must remain disabled until the production governance and DPIA conditions in the audit are completed.
