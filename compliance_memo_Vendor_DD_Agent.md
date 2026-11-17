# Compliance memo — Vendor Due-Diligence Agent

**To:** Data Protection Officer, [design-partner law firm]
**From:** Pieter Albrecht, Privacy & AI Advisory
**Re:** GDPR readiness of the vendor due-diligence agent before a pilot
**Date:** 17 November 2026

**Bottom line: Proceed with conditions.** The agent screens companies, but it processes data about people, including allegations of crimes. It can't run on real vendors until that data is minimised, legally covered and correctable.

**What we found**
The agent checks a vendor's identity, sanctions status and news coverage, then rates the risk. Sanctions screening sits on solid legal ground. The weak spot is adverse media: news results name executives, employees and suspects, and the agent stores their names and alleged offences in reports, in US-hosted debugging logs and possibly in a public code repository. Criminal-offence data needs a specific legal basis that hasn't been confirmed. Testing also showed the agent can describe a crime victim as the wrongdoer, and today there is no way to correct that.

**Top three actions, in this order**
1. **Before any real vendor is checked:** move the language model to your own account under a data processing agreement, switch the debugging trace off or to an EU instance, and remove any real reports from the public repository.
2. **Before the pilot:** have counsel confirm the legal basis for processing criminal-offence data about third parties, then complete a DPIA. It is required: the agent scores parties, combines several datasets, processes criminal-offence data and uses new AI technology.
3. **At pilot launch:** keep findings at company level, with no individuals' names unless essential and each person labelled as perpetrator, victim or mentioned. Add a reviewer sign-off before any recommendation is final, a correction route for named individuals, and a retention rule, e.g. delete after the vendor decision plus the legally required period.

**Risks that remain even if you do all this**
- **Misattribution.** Role labels reduce, but don't eliminate, the chance of the model linking a person to conduct they weren't responsible for. Human review remains the last safeguard.
- **Legal uncertainty.** Screening *suppliers* for criminal conduct sits outside the clear client due-diligence rules of anti-money-laundering law. Even a positive legal opinion leaves some regulatory exposure.
- **US transfers.** The language model, tracing and search providers are US-based. The EU-US framework is under appeal at the EU Court of Justice; keep standard contractual clauses ready.

**What this memo is not:** a legal opinion, a DPIA or a certification. Engage legal counsel before relying on this assessment for compliance decisions.

*Pieter Albrecht*
