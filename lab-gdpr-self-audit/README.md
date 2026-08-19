# GDPR audit — RegGuard-Mini (Onyx Dynamics)

Module 7 lab submission. First-pass GDPR compliance assessment of a system I built:
**RegGuard-Mini**, an AI assistant that checks vehicle exterior geometry against regulatory and
internal design rules and answers a designer's follow-up questions.

## File map

| File | Contents | Lab phase |
|---|---|---|
| `00_data-processing-brief.md` | What personal data the system processes, where it flows, who touches it | Kick-off |
| `01_personal-data-inventory.md` | Per-category, per-purpose inventory with retention and border-crossing flags | Phase 1 |
| `02_role-map.md` | Controller / processor classification, DPA status, transfer mechanisms | Phase 2 |
| `03_lawful-basis-assessment.md` | Article 6 basis per purpose, with full LIA where legitimate interests is proposed | Phase 3 |
| `04_risk-and-rights-analysis.md` | Article 9, Article 22, DPIA triggers, data subject rights friction | Phase 4 |
| `05_law-stacking-check.md` | AI Act, ePrivacy, Data Act cross-references | Phase 5 |
| `06_compliance-memo.md` | 300–400 word memo to DPO with bottom line, actions, residual risks | Phase 6 |
| `07_reinforce-accountability-test.md` | Documentation checklist and TBD preparation | Reinforce |
| `08_stretch-dpbd-checklist.md` | Data protection by design checklist for the highest-risk processing activity | Stretch |

## Scope and caveats

- First-pass self-assessment by the system's designer. Not a legal opinion, DPIA, or certification.
- Where a legal interpretation is uncertain, the document says `TBD — legal review` rather than
  asserting a conclusion.
- No API keys, tokens, or customer geometry are contained in this repository.
