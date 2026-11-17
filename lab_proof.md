# Lab proof — audit your own project under GDPR

**Project** CompanyScope, Sean Langsdorf's actual Ironhack Project 3.\
**Audited version** CompanyScope's [published 34-node n8n workflow](https://github.com/sean173-lang/CompanyScope/blob/542665b0a4c6c5c18a8ac59896b87d5bd0eb39f6/projects/ironhack_project3/workflow.json) at commit `542665b0a4c6c5c18a8ac59896b87d5bd0eb39f6`.\
**Decision** Proceed with conditions. Synthetic demo only until the firm establishes vendor, retention and human-review controls and the relevant legal basis.

## Reproduce one offline run

Run from this directory with Node.js 18 or later. No n8n server, network, package installation or credentials needed.

```bash
node replay-companyscope-data-flow.cjs synthetic-data-flow-input.json
```

- **Code / workflow:** [Replay harness](replay-companyscope-data-flow.cjs) runs five unmodified JavaScript code nodes and two body expressions from the [credential-free workflow excerpt](companyscope-workflow-evidence-excerpt.json). It reads synthetic upstream data instead of making live requests.
- **Input:** [Synthetic form, registry and search fixture](synthetic-data-flow-input.json) contains a fictional company, an address marker, a name/email in a relevant excerpt and an unrelated comparison excerpt.
- **Observed evidence:** [Captured run](companyscope-data-flow-run.json) shows that the registry address enters both Tavily and OpenAI request bodies and that the relevant name and email enter the OpenAI payload despite `store:false`. The unrelated excerpt and extra form field did not reach those payloads. The export saves all successful and failed execution payloads by configuration.
- **Failure and limitation:** The Tavily relevance filter accepted the correct company excerpt but did not scrub the personal identifiers within it. The replay demonstrates payload construction, not live vendor receipt, storage, deployed n8n pruning, region, or the actual legal status of a transfer. The run sent no external requests and used no real personal data.
- **Final output:** Read the [data processing brief](companyscope-data-processing-brief.md), [audit worksheet](companyscope-gdpr-audit.md), [DPO recommendation memo](companyscope-dpo-memo.md) and [accountability check and sources](companyscope-accountability-and-sources.md).

The unmodified Project 3 repository's offline suite passed 34 tests on the audited commit. Those are functional regressions, not a GDPR compliance test.
