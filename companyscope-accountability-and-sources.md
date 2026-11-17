# CompanyScope — accountability and design safeguards

## Accountability test

**Could the operator demonstrate GDPR compliance with the current documentation alone? No.** The published project can show how the nodes route data and what its prototype checks do. It does not demonstrate that a defined live deployment lawfully processes, transfers and deletes personal data or handles rights requests.

| Evidence a regulator could ask for | Status from reviewed materials | What the controller needs |
| --- | --- | --- |
| Processing flow, fields, versions and software checks | Partial. Pinned repository, export, architecture and runnable replay. | Compare with deployed graph, regions and live execution/prune settings. Preserve configuration evidence without copying raw payloads. |
| Art. 30 records of processing | Not evidenced. | Record purposes, subjects, categories, recipients, transfers, retention and safeguards. Assess any Art. 30(5) exception, do not assume it. |
| Art. 6 assessment and signed LIA | Not evidenced. | Purpose-specific tests and legal sign-off. The worksheet contains a first-pass screen only. |
| Privacy information and request workflow | Not evidenced. | Notice for direct data if applicable, Art. 14 plan for registry and web subjects, request owner, vendor coordination and tested responses. |
| DPAs, role analysis and transfer evidence | Not evidenced for the actual accounts. Public vendor terms are not deployment records. | Contracts, importer/region inventory, subprocessors, applicable adequacy or SCCs and assessment evidence. |
| DPIA screening / DPIA / consultation | No approved assessment evidenced. | Complete before deployment if likely high risk, document residual risks and consult if required. |
| Retention schedule and deletion evidence | Not evidenced. Export enables full success/error capture. | Per-store TTL, pruning and backup tests. Include helper copies and deletion exceptions. |
| Technical and organizational measures | Partial. Form/workflow auth, webhook token and source checks are documented. | Access and export permissions, encryption and backup controls, incident playbook, reviewer training and evidence of end-to-end tests. |

**Brief for counsel on P2/P3.** Bring a redacted side-by-side of the current and minimized query/prompt, a list of fields and why each is needed, source types, test results on quality and false exclusions, and proposed alternatives. Add the expected matter volume and subject types, who decides the research purpose, actual API recipient and region, retention and access including support, Art. 14 notice plan, and concrete deletion and objection steps. Ask counsel to assess whether the remaining disclosure is necessary under Art. 6(1)(f), whether any local confidentiality obligations preclude sending the target at all, and what should happen if Art. 9 or 10 data appears.

## Privacy-by-design checklist

**Highest-risk activity** Sending unredacted public-web and registry excerpts to the model and retaining copies in executions.

| Principle | Status | Current evidence and next change |
| --- | --- | --- |
| Minimize | Fail | Relevance filtering passes identifiers. Allowlist registry fields, remove unnecessary personal details from excerpts and test before HTTP calls. |
| Bind purpose | Unknown | Company-focused prompt is not a technical data-use rule. Enforce permitted inputs, vendor no-reuse settings and restrictions on exports and secondary use. |
| Access control | Unknown | Entry authentication is visible. Verify least-privilege access to history, reports, service accounts and support. |
| Retention | Fail | Export stores full success and error data. Verify instance pruning and implement explicit TTLs for execution payloads, file copies and backups. |
| Rights | Unknown | No end-to-end test shown. Run access, correction and erasure drills across raw sources, analysis, files and vendors within one month unless an extension applies. |
| Incident response | Unknown | No tested playbook shown. Assign owners and exercise processor escalation and supervisory notification within 72 hours of awareness when required. |

## Sources

- [CompanyScope, audited commit](https://github.com/sean173-lang/CompanyScope/tree/542665b0a4c6c5c18a8ac59896b87d5bd0eb39f6) · [original workflow export](https://github.com/sean173-lang/CompanyScope/blob/542665b0a4c6c5c18a8ac59896b87d5bd0eb39f6/projects/ironhack_project3/workflow.json) · [tool notes](https://github.com/sean173-lang/CompanyScope/blob/542665b0a4c6c5c18a8ac59896b87d5bd0eb39f6/docs/tools.md).
- [GDPR official text](https://eur-lex.europa.eu/eli/reg/2016/679) · [EDPB-endorsed WP248 and WP251](https://www.edpb.europa.eu/endorsed-wp29-guidelines_en) · [EDPB small-business DPIA criteria](https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en).
- [EDPB Chapter V transfer guidance](https://www.edpb.europa.eu/system/files/documents/2023-02/edpb_guidelines_05-2021_interplay_between_the_application_of_art3-chapter_v_of_the_gdpr_v2_en_0.pdf) · [EU–US adequacy decision](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj) · [EU transfer SCCs](https://eur-lex.europa.eu/eli/dec_impl/2021/914/oj).
- [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data) · [OpenAI DPA](https://openai.com/policies/data-processing-addendum/) · [Tavily privacy policy](https://www.tavily.com/privacy) · [Tavily DPA availability](https://help.tavily.com/articles/8202749643-gdpr-dpa-security-documentation).
- [Consolidated EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng) · [ePrivacy amending directive](https://eur-lex.europa.eu/eli/dir/2009/136/oj) · [§ 25 TDDDG](https://www.gesetze-im-internet.de/tdddg/__25.html) · [EU Data Act, Chapter VI](https://eur-lex.europa.eu/eli/reg/2023/2854/oj).
