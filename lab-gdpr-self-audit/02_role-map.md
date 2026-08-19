# Phase 2 — Role map

## Role table

| Entity | Role | Processing activity | DPA in place? |
|---|---|---|---|
| **OEM customer** (the design studio deploying the tool) | **Controller** | Determines *why* their designers use the tool — it is their professional context, their employees, their decision to adopt it. Controls access, configures sessions, receives reports. | N/A (they are the controller, not our processor) |
| **Onyx Dynamics / me** (system builder and operator) | **Processor** | Processes personal data on behalf of the OEM controller: stores threads, runs inference, assembles reports. We do not decide the purposes — the OEM does. We provide the means. | **No. No DPA exists.** This is a blocking gap. No personal data may lawfully flow to us as processor without one. |
| **OpenAI** (LLM API provider) | **Sub-processor** | Receives the designer's typed questions and session context as inference input. Processes it to return a completion. Retention and secondary use governed by their API data usage policy. | **No DPA between us and OpenAI specific to this deployment.** OpenAI publishes a standard DPA for API customers, but we have not executed it, and we have not verified that its terms are compatible with the OEM controller's requirements. |
| **Cloud hosting provider** | **Sub-processor** | Stores session state, thread history, geometry files, version logs. | **No deployment-specific DPA.** Standard cloud terms likely exist but have not been reviewed against this use case. |

## The chain that must exist before any personal data flows

```
OEM (controller)
  → DPA with Onyx (processor)
      → Sub-processor agreement with OpenAI
      → Sub-processor agreement with cloud host
```

None of these agreements exist today. The entire chain is missing. This is not a nuanced gap — it
is a binary legal prerequisite that has not been met.

## International transfers

The designer's typed questions are sent to OpenAI's API. OpenAI processes API data in the United
States. This is a transfer of personal data from the EEA to a third country.

**Transfer mechanism needed:** Standard Contractual Clauses (SCCs) or reliance on the
EU–US Data Privacy Framework, if OpenAI is certified under it. I have not verified OpenAI's
current certification status under the DPF. This must be confirmed before any deployment
involving EEA-based designers.

If the OEM is itself outside the EEA (e.g. Rimac in Croatia — which is in the EU — vs a
hypothetical partner in the UK post-Brexit), additional transfer analysis applies to the report
delivery step.

## A note on the controller/processor boundary

I have mapped Onyx as processor and the OEM as controller. This is the standard SaaS model and
the most likely correct answer. But it is not automatically correct, and two things could
complicate it:

1. If Onyx retains thread data for its own purposes (analytics, model improvement, product
   development), Onyx becomes a controller for those purposes — and the OEM's designers become
   data subjects of a company they did not contract with. This is why a no-secondary-use clause
   in the DPA is not a nice-to-have but a structural requirement.

2. If the OEM has enough control over the AI's behaviour (loading custom rule sets, adjusting
   confidence floors, choosing what enters the report), a regulator could argue joint
   controllership. This is a legal determination, not a technical one, and it should be settled
   in the DPA drafting rather than discovered later.

## Where a lawyer is needed

- Drafting the Onyx ↔ OEM DPA, including the sub-processor authorisation clause.
- Verifying OpenAI's DPF certification or executing SCCs.
- Settling the controller/processor boundary, especially around custom rule sets.
- Determining whether OpenAI's current API data-use terms are compatible with "no secondary use."
