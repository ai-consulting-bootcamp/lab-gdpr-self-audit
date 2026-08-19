# Phase 6: Compliance Memo — Platform Risk Research Agent

**To:** Data Protection Officer / Legal Counsel
**From:** AI Systems Review
**Re:** First-pass GDPR compliance assessment

## Bottom line

Proceed with conditions. The core design is sound, but three gaps must close before this tool handles real client data at scale.

## Top three actions

1. **Sign a DPA with every processor before more personal data flows through them.** DeepSeek, OpenAI, Pinecone, and Railway all process data with no Data Processing Agreement in place today. None of this should run without a signed DPA and a transfer mechanism, most likely Standard Contractual Clauses, since all four are US-based.

2. **Write a retention policy before collecting more account data or storing more reports.** There is no defined period for how long account data, reports, or logs are kept. This needs a number, not a placeholder, and it needs to be enforced technically, not just written down.

3. **Add a filter or review step for named individuals in research output.** Public web research can incidentally pull in named individuals, including from breach disclosures. Right now there is no way to find or remove that data on request. This closes both a GDPR gap and a fairness concern.

## Residual risks

Even after these three actions, some risk stays open. First, the research tools pull from public web sources, and there is a small chance a report could surface special-category data about a named individual, such as health or criminal information tied to a breach disclosure. This cannot be fully engineered away, only monitored. Second, the legitimate interests basis used for vendor research has not yet been documented as a formal LIA, so if challenged, the justification is thinner than it should be. Third, cross-border transfer risk is legally live wherever US vendors are involved, and no contractual clause fully removes government access concerns in the US, only reduces exposure.

## What this memo is not

This memo is a first-pass reading. It is not a legal opinion, not a DPIA, and not a certification. The client must engage legal counsel before relying on this assessment for compliance decisions.
