# Phase 4: Risk and Rights Analysis

**System:** Fix My Process (Ironhack Project 3) · **Input:** [00_data_processing_brief.md](00_data_processing_brief.md) · **Lens:** GDPR only · **Date:** 17 Nov 2026

**Special category data (Art. 9).** Not asked for, but free text can reveal it, for example a colleague's sick leave (health) or a works council matter (trade union membership), and the reports can repeat it. It is not inferable from the flags or ratings. No Art. 9(2) condition fits this purpose, so the design must filter it before the LLM call and delete it when found.

**Automated decision-making (Art. 22).** No. The outputs concern processes and tools, the employee decides what to do, and no output has a legal or similarly significant effect on a person; the red-case Board decision concerns the use case. This changes if flags, feedback or department summaries feed into performance judgments: then human review, a right to contest and an explanation of the logic are needed. A simple way to contest a red flag should be added now.

**DPIA trigger (EDPB criteria).** Two criteria clearly apply: employees are vulnerable data subjects because of the power imbalance, and an LLM agent with retrieval is innovative technology. Combining employee input with web, news and internal documents partly meets the matching criterion, and evaluation and systematic monitoring would apply once department summaries are built. A DPIA is therefore required before the pilot.

**Data subject rights friction.** Access is hard because there is no user ID: a case sits in Airtable, Notion, Slack, n8n history and vendor logs, linked only by the reference code, so a timely answer depends on the employee having kept that code. Erasure cannot be handled in time today, as there is no retention period, no deletion procedure across five stores, and vendor-side logs are outside direct control. Employees can object only by not using the tool, and named colleagues or customers cannot exercise any of these rights in practice.

## Sources

- Article 29 WP / EDPB WP248 rev.01, DPIA guidelines (nine criteria)
