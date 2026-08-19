# Audit your own project — GDPR lens

**Track:** Module 7 — GDPR · **When:** Week 7, Day 3 · **Status:** Required

This repository contains everything you need for this lab.

## Files

- [`instructions.md`](./instructions.md) — the lab instructions
- [`rubric.md`](./rubric.md) — how your submission is graded; this is what the AI reviewer checks your PR against

## How to complete this lab

1. **Fork** this repository.
2. Do the work described in `instructions.md`, committing to your fork.
3. Open a **pull request** back into this repository.
4. You'll receive **AI feedback** on your PR based on `rubric.md`. Address any blocking feedback and push updates to the same PR.

## Submission hygiene

- Keep this repository scoped to this lab only — no unrelated projects or personal files.
- Use clear, descriptive filenames.
- Remove secrets, API keys, and tokens before committing.

---

## Submission contents (Ugo Ahukannah)

**System audited:** [AI Pre-Scan](https://github.com/nyelugo/PROJECT-AI-Pre-Scan) — my Week 5
Project. Give it a company name, get an evidence-backed first draft of that company's AI-system
inventory, plus the questions public evidence cannot settle. This is the GDPR lens on the same
system I audited under the EU AI Act.

| File | Contents |
|---|---|
| [`gdpr-self-audit-ai-pre-scan.md`](./gdpr-self-audit-ai-pre-scan.md) | The audit: data processing brief, Recognize, Phase 1 personal data inventory, Phase 2 role map, Phase 3 lawful basis with a full three-part LIA, Phase 4 risk and rights, Phase 5 law stacking, and the accountability test |
| [`compliance-memo-dpo.md`](./compliance-memo-dpo.md) | Phase 6: 385-word memo to a DPO — bottom line, three sequenced actions, residual risks, and what the memo is not |
| [`reinforce-accountability-and-legal-review.md`](./reinforce-accountability-and-legal-review.md) | Reinforce: the accountability documentation checklist ticked against reality, and how to prepare the one flagged legal question |
| [`stretch-data-protection-by-design.md`](./stretch-data-protection-by-design.md) | Stretch: data protection by design checklist for the highest-risk processing activity, with the dependency order for fixing it |

**Headline finding.** The project's own proposal states that no personal data is collected and that
named individuals encountered in sources are not recorded. It processes personal data anyway: whole
public pages carrying names, titles and quotes are chunked, embedded and stored in a US vector
database, and `store.py` has no deletion path of any kind. The legal basis for *reading* public
sources holds; the LIA fails on necessity at the *storage* step, because the evidence gate only ever
needs the validated passage and its provenance. Verified in the other direction too: both sample
reports committed to the public repo are clean of person names — the exposure is at ingestion, not
in the published output.
