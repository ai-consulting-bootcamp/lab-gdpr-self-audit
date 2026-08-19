# Compliance memo

**To:** Data Protection Officer, [OEM Client]
**From:** Kimia Sharifi Rad, Product Design — Onyx Dynamics
**Subject:** GDPR first-pass assessment — RegGuard-Mini
**Date:** August 2026

---

## Bottom line

**Proceed with conditions.** The system's personal-data footprint is small and its subject matter
is geometry, not people — but three structural prerequisites are missing, and no personal data
should flow through the system in production until they are in place.

## Top three actions

**(1) Execute a Data Processing Agreement before any pilot.** Onyx processes personal data on
your behalf: your designers' names, their typed questions, thread histories, and the names of
report recipients. No DPA exists. This is not a compliance improvement — it is a legal
prerequisite under Article 28. The DPA must cover Onyx as processor, and authorise OpenAI and our
cloud host as sub-processors, with transfer safeguards for data sent to OpenAI in the US.

**(2) Set retention periods and build an erasure path.** Thread history and version logs currently
persist indefinitely. No retention schedule exists. Storage limitation under Article 5(1)(e)
requires a defined period tied to the purpose — we recommend tying it to the vehicle programme
lifecycle, with automatic anonymisation of authorship labels after a set window. Separately,
erasure requests will break the version chain unless we design for them now: anonymising the
author label while preserving the version is the least disruptive approach, and it must be built
before the first request arrives, not improvised under a 30-day deadline.

**(3) Conduct a DPIA before production deployment.** The system uses innovative AI technology and
transfers personal data to the US for inference — two EDPB trigger criteria, with a third
(systematic workplace monitoring) arguable. A DPIA is the right instrument to document these
risks and the mitigations we have already designed (human oversight, no autonomous action,
confidence disclosure).

## Residual risks

Even with these actions taken, three risks remain. First, designers' free-text questions may
incidentally contain special-category data (health references, personal opinions); no input
filter exists and building one that works without degrading the tool is hard. Second, the
version timeline creates a behavioural record of each designer's work patterns that could be
repurposed for employee monitoring — contractual prohibition helps, but technical access controls
are stronger and do not yet exist. Third, the LLM vendor's data-use terms may change; ongoing
monitoring of those terms is a recurring obligation, not a one-time check.

## What this memo is not

This is a first-pass assessment by the system's designer, not a legal opinion, a DPIA, or a
certification. The controller should engage qualified legal counsel before relying on this
assessment for compliance decisions. The three actions above are sequenced — the DPA must come
first, and no personal data should flow until it is signed.
