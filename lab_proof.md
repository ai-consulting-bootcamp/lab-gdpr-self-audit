# GDPR audit of the VC Screening Agent

**Scope.** This bootcamp prototype helps an analyst at Puente Ventures, a fictional fund, check B2B startups before a first meeting. Sandra used Tavily and OpenAI for Kalipso and Lawra. The audit uses the [reviewed GitHub commit](https://github.com/Sobregonm/project3-vc-screening/tree/84afd71f9c2356ff038f84cbd59c9a83188a3161) and the attached report from the Kalipso run with a news search error.

## Run and evidence

- **Code:** [LangGraph entry point](code/main.py), [setup instructions](code/README.md), [investment rules](code/knowledge/investment_thesis.json), and [OpenAI evidence extraction](code/headquarters_extractor.py).
- **Input:** Kalipso and its official website, `https://kalipso.ai/`. The command below uses these inputs and the documented CLI. The original terminal log is unavailable.
- **Evidence produced:** The report includes an official product description and three source quotes that place Kalipso in Barcelona. It records funding stage as *Not verified* because some claims could not be matched to their source text and further checks were needed. The report includes the quotes and source links. The full API responses are unavailable.
- **Final output and observed failure:** [Kalipso screening report](evidence/kalipso-screening.md). GDELT returned HTTP 429. The workflow still wrote the report and marked recent news *Not verified*. This is the attached version that records the error.

```bash
cd code
python main.py "Kalipso" "https://kalipso.ai/"
```

## Phase 1 — Personal data inventory

| Data category | Source | Purpose | Retention period | Crosses the EEA border? |
|---|---|---|---|---|
| Names and job titles, if present | Tavily excerpts and URLs sent to OpenAI | Check the company's headquarters | In memory during the run. Provider retention unknown. | Unknown |
| Names and job titles, if present | Tavily excerpts and URLs sent to OpenAI | Check the company's funding stage | In memory during the run. Provider retention unknown. | Unknown |
| Names or other identifiers, if present | Public page text from Jina Reader and Tavily results | Describe the company and let the analyst check sources | Selected text, titles and URLs may stay in the Markdown report. No deletion period found in the code. | Unknown |
| Names or other identifiers, if present | GDELT headlines and URLs | Find recent news for the analyst | Headlines and links can stay in the report. Provider retention unknown. | Unknown |

The Kalipso report has no founder names. The full API inputs and responses are unavailable, so personal data in them is unconfirmed. **Possible change of purpose:** A person may be named in a public article to announce a funding round. The agent may then collect that name while screening the startup for investment. We could not confirm a specific example in the run.

## Phase 2 — Role map

| Entity | Proposed role | Activity | DPA status |
|---|---|---|---|
| Puente Ventures | Controller in a real deployment | Sets the purpose and screening criteria. Its analyst makes the decision. | Fictional client. In a real deployment, agreements would be needed with its processors. |
| Sandra / project team | Controller of the test if it sets the purpose and means. Processor in a deployment if it works under the fund's instructions. | Runs the agent and prepares the reports. | No agreement with the fictional fund. A real processor relationship would require one. |
| OpenAI API | Processor or subprocessor for data covered by its DPA | Extracts headquarters and funding evidence from Tavily excerpts. | [Published DPA](https://openai.com/policies/data-processing-addendum/). Coverage for the API account is unconfirmed. |
| Tavily | Possible processor or subprocessor for searches made on the customer's behalf | Searches by company name and domain and returns results. | [DPA available](https://help.tavily.com/articles/8202749643-gdpr-dpa-security-documentation). Agreement for the API account is unconfirmed. |
| Jina Reader | To confirm | Receives the company URL and returns page text. | Check the terms and whether a DPA is required. |
| GDELT DOC API | To confirm | Receives a company news query and returns article information. | Check the terms and whether a DPA is required. |
| GitHub | To confirm for report hosting if reports include personal data | Hosts the project files and published reports. | Check the terms and whether a DPA is required. |

Sandra used Gmail to sign in to OpenAI and Tavily. API account coverage remains unconfirmed. OpenAI's DPA provides for standard contractual clauses (SCCs) or an adequacy decision for covered transfers. Tavily reports mainly US infrastructure and the use of SCCs. Destinations, agreements and transfer safeguards for personal data in the actual tests remain unconfirmed. See [EDPB role guidance](https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en).

## Phase 3 — Lawful basis

| Purpose | Proposed lawful basis | Justification | Legal review? |
|---|---|---|---|
| Check headquarters | TBD — legal review | The city and country can be checked using company facts. The need for personal data is unproven. | Yes |
| Check funding stage | TBD — legal review | The funding round and date can often be checked using company facts. Sending names needs a separate reason. | Yes |
| Describe the company and document sources | Legitimate interests candidate. TBD — legal review. | References help analysts verify claims. Including a person's identity needs a separate justification. | Yes |
| Find recent news | Legitimate interests candidate. TBD — legal review. | News can help check recent company changes. The need to keep personal identifiers is unclear. | Yes |

1. **Interest.** The fund needs reliable company evidence to decide whether to invite a startup to a first meeting.
2. **Necessity.** Test whether company facts and shorter excerpts with personal details removed can support the same checks. The prototype review did not show that names or job titles are needed.
3. **Balancing.** People named in public news may expect readers to see their names. Sending those names to an API or publishing them in a report may create a different impact. We need the actual data and provider retention details to complete this step.

See [GDPR Article 6](https://eur-lex.europa.eu/eli/reg/2016/679/ojv) and [EDPB legitimate interests guidance](https://www.edpb.europa.eu/system/files/2026-11/edpb_guidelines_202401_legitimateinterest_v2_en.pdf).

## Phase 4 — Risks and rights

**Special category data.** We found no special category data or related inferences in the attached Kalipso report. The full inputs remain unverified, so we have not identified an Article 9 condition.

**Automated decisions.** The agent checks company facts and prepares a report. The design gives the analyst the final decision and the code does not automatically invite or reject a startup. The reviewed design does not show a solely automated decision with legal or similarly significant effects on a person.

**DPIA.** Innovative use is plausible because the agent uses a language model on excerpts that may contain personal data. Combining data about the same person is unconfirmed because the workflow gathers sources around company names. We found no evidence of scoring people, significant automated decisions, systematic monitoring, sensitive or highly personal data, large-scale processing, vulnerable people, or processing that blocks a right, service, or contract. The controller should record the criteria and decide whether a DPIA is required before a real deployment. See [EDPB criteria](https://www.edpb.europa.eu/system/files_en?file=decisions%2Fit_dpia_blacklist.pdf) and [AEPD guidance](https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/realizacion-de-evaluaciones-de).

**Data subject rights.** For access, the team can review saved reports, but it has not shown it can find all excerpts or provider records on time. For erasure, the team can edit local reports, but GitHub history and provider copies need a process. For objection, the prototype has no documented request channel or decision process if legitimate interests are used. A timely response within the general one-month period is unproven for all three rights. See [GDPR Articles 12, 15, 17 and 21](https://eur-lex.europa.eu/eli/reg/2016/679/ojv).

## Phase 5 — Other EU laws

- **AI Act:** The agent is likely outside the high-risk category because it screens companies for an investment meeting. In a real deployment, AI literacy measures would help staff use the tool and check its reports. [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689)
- **ePrivacy:** The reviewed code uses public websites and APIs, with no observed cookies, tracking pixels, device tracking, or private messages. We found no feature in the workflow that requires ePrivacy consent. [ePrivacy Directive](https://eur-lex.europa.eu/eli/dir/2002/58/oj)
- **Data Act:** The prototype does not use IoT data or involve a cloud switch. Check switching rules if a covered service is replaced later. [European Commission guidance](https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained)

## Phase 6 — Compliance memo

**To the Legal Counsel of Puente Ventures**  
**Subject — GDPR review of the VC Screening Agent prototype**

**Proceed with conditions.** The fund should move toward a controlled pilot because the agent can help analysts check company facts, provided the fund limits the personal data it uses and verifies its provider agreements before the pilot starts.

The prototype was tested with Kalipso and Lawra. It sends public search excerpts and links from Tavily to OpenAI to find evidence about a company’s headquarters and funding stage. These excerpts may include names or job titles. The Kalipso report we reviewed showed no founder names, but the full excerpts from both tests were unavailable. We could not confirm what personal data the providers received or where they processed it.

1. **Limit the data first.** Send only the sentences needed to check the company’s location and funding. Remove names and job titles that the analyst does not need. Review reports before sharing them and set a deletion date.

2. **Check provider agreements before the pilot.** Identify who holds each API account. Confirm which providers act as processors and whether the applicable data processing agreements cover the services used. Record where personal data is processed and which safeguard applies to any transfer outside the European Economic Area.

3. **Complete the legal and operational review.** If the pilot still needs personal data, document the proposed lawful basis and complete the legitimate interests assessment before relying on it. Record whether a data protection impact assessment is required. Assign someone to handle requests for access, deletion, and objection. Keep the analyst responsible for checking the evidence and deciding whether to invite a startup to a meeting.

**Residual risks.** A source link may still identify someone after names are removed from the text. Public sources may contain old or incorrect claims. Copies already shared may be difficult to remove, especially from public repositories.

**Scope.** This memo is a preliminary advisory note. A legal opinion, a formal impact assessment, and certification are outside its scope. The fund must consult legal counsel before relying on this assessment for compliance decisions.
