# Audit your own project — GDPR lens

**Track:** Module 7 — GDPR · **When:** Week 7, Day 3 · **Status:** Required

This repository contains everything you need for this lab.

## Files

- [`instructions.md`](./instructions.md) — the lab instructions
- [`rubric.md`](./rubric.md) — how your submission is graded; this is what the AI reviewer checks your PR against

### My submission

- [`data-processing-brief.md`](./data-processing-brief.md) — kick-off data processing brief. Recognises the data (CFU 1), maps every category across two data streams, and lists purposes, processors and storage locations.
- [`gdpr-audit-stups.md`](./gdpr-audit-stups.md) — the audit worksheet. Phases 1 to 6 (data inventory, roles, lawful basis with full LIAs, risk and rights, law stacking, and a compliance memo), plus the CFU 4 accountability test.

The system audited is my IronHack Project 3, "Stups", a personal evening suggestion agent built in n8n. The audit is a self assessment, not a legal opinion.

**Note on scope.** This lab asks me to audit my own project, so the two files above are the deliverables. `instructions.md` and `rubric.md` are the lab's own files and are left unmodified.

**Privacy note.** The Telegram chat ID is redacted as `[TELEGRAM_CHAT_ID]` throughout. The workflow JSON is deliberately not committed, because it carries that identifier and credential names.

## How to complete this lab

1. **Fork** this repository.
2. Do the work described in `instructions.md`, committing to your fork.
3. Open a **pull request** back into this repository.
4. You'll receive **AI feedback** on your PR based on `rubric.md`. Address any blocking feedback and push updates to the same PR.

## Submission hygiene

- Keep this repository scoped to this lab only — no unrelated projects or personal files.
- Use clear, descriptive filenames.
- Remove secrets, API keys, and tokens before committing.
