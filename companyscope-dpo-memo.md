# CompanyScope — recommendation to the DPO

**To** Data Protection Officer / legal counsel of the prospective deploying firm\
**From** Sean Langsdorf · 17 November 2026

**Proceed with conditions.** Continue the synthetic demo, but keep the present configuration off live client matters until the firm limits what leaves n8n, establishes its vendor arrangements and can show where every copy goes.

1. **Minimize the outbound data before any live pilot.** Replace the Tavily query's full registry address and business-purpose text with the exact company name and, where needed to disambiguate, a city. Compare the results against a registry-only or manual baseline. Keep the register identifier local where possible, filter source fields before sending them to OpenAI, and exclude names, contact details, home addresses, sensitive details and offence allegations unless separately justified and approved. The offline replay showed that a relevant web snippet's synthetic name and email reached the model payload even though an unrelated result was rejected.

2. **Establish the legal basis and vendor terms.** Have Legal record the purpose-by-purpose legitimate interests assessment and decide how people named in indirect sources will be informed. Record any applicable exception instead of assuming public sources remove that obligation. Confirm the actual OpenRegister, Tavily and OpenAI recipients, access locations, retention and subprocessors. Finalize processor terms and any required transfer safeguards before allowing an outbound request with personal data. The model's `store:false` flag is not proof that the provider retains nothing.

3. **Make the pilot auditable before opening it.** Complete the DPIA, replace the export's full success and error capture with minimal operational logging, and set and test automatic expiry for reports, execution data, metadata sidecars and backups. Run an access and deletion drill across the remaining stores. Give reviewers a checkable sign-off step and require them to verify sources before relying on or sharing a report. Consult the supervisory authority if high residual risk remains despite mitigation.

Residual risks remain. Public records can be stale or misattribute an individual despite correct company matching. Redaction can miss indirect identifiers in prose, and even a minimal search can reveal a confidential matter target. Finally, a valid source ID does not prove that a source supports an inference. Keep the report as a starting point for a human researcher.

This is a first-pass assessment, not a legal opinion, DPIA or certification. Engage legal counsel before relying on it for compliance decisions.
