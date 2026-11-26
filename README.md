# Audit your own project — GDPR lens

**Track:** Module 7 — GDPR · **When:** Week 7, Day 3 · **Status:** Required

This repository contains everything you need for this lab.

## Files

- [`instructions.md`](./instructions.md) — the lab instructions
- [`rubric.md`](./rubric.md) — how your submission is graded; this is what the AI reviewer checks your PR against

## Submission map (Ben Mayer)

**System audited:** *Menohelp*, my bootcamp build project: a LangGraph agent that turns cycle data, blood tests and symptoms into a plain-language report. The lab calls it the "Week 5 Project"; in my course folders it is Project 3, under `week-6/`. Same fictional client as my [EU AI Act self-audit](https://github.com/benmayer/lab-eu-ai-act-self-audit): Wechselweise Coaching GmbH.

| File | Lab step |
|---|---|
| [`01-data-processing-brief-menohelp.md`](./01-data-processing-brief-menohelp.md) | Kick-off: data processing brief + CFU 1 Recognize |
| [`02-gdpr-audit-worksheet-menohelp.md`](./02-gdpr-audit-worksheet-menohelp.md) | CFU 2 Apply: Phase 1 inventory (per purpose, 5 purpose-limitation flags), Phase 2 role map + transfers, Phase 3 lawful basis + LIA, Phase 4 risk and rights (Art 9, Art 22, DPIA screen, rights friction), Phase 5 law stacking |
| [`03-compliance-memo-dpo-wechselweise.md`](./03-compliance-memo-dpo-wechselweise.md) | CFU 3 Integrate / Phase 6: memo to the DPO (392 words) |
| [`04-accountability-check-and-dpbd-checklist.md`](./04-accountability-check-and-dpbd-checklist.md) | CFU 4 Verify, Reinforce (documentation list, one TBD prepared for counsel), Stretch (data protection by design checklist) |

**Result:**
- **Bottom line:** proceed with conditions.
- **Art 9:** health and sex-life data at the core; explicit consent needed and missing.
- **Art 22:** doesn't apply (no decision), but it profiles health without human review.
- **DPIA:** required (4 of 9 EDPB criteria).
- **Biggest finding I hadn't noticed while building:** a showcase report built on a real person's health data sits in the public project repo.

**Legal baseline:** GDPR as in force (proposed Digital Omnibus GDPR changes not relied on). Not legal advice. Items marked ⚖️ need confirmation by counsel.

## How to complete this lab

1. **Fork** this repository.
2. Do the work described in `instructions.md`, committing to your fork.
3. Open a **pull request** back into this repository.
4. You'll receive **AI feedback** on your PR based on `rubric.md`. Address any blocking feedback and push updates to the same PR.

## Submission hygiene

- Keep this repository scoped to this lab only — no unrelated projects or personal files.
- Use clear, descriptive filenames.
- Remove secrets, API keys, and tokens before committing.
