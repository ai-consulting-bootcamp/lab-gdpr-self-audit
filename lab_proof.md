# lab_proof.md – GDPR audit of my own Project 3 (Week 7)
**Author:** Murat Çömez · **System:** RCSA Evidence & Challenge Agent (Python, LangGraph, OpenAI API)

## File map
| File | What it contains |
|---|---|
| [`gdpr_data_brief_rcsa_evidence_challenge_agent.md`](gdpr_data_brief_rcsa_evidence_challenge_agent.md) / [`.pdf`](gdpr_data_brief_rcsa_evidence_challenge_agent.pdf) | Data processing brief (updated from yesterday's AI system brief to answer the personal-data questions; sent to my partner) |
| [`gdpr_self_audit_rcsa.md`](gdpr_self_audit_rcsa.md) | Phases 1–5: data inventory, controller/processor map, lawful basis with LIA, risks and rights, law tracking |

## 1. Workflow
Yesterday's brief described the AI system. I rewrote it around **personal data**: who is identified, which fields, where they go. Then inventory → roles → Art. 6 basis → Art. 9/10, DPIA, rights → other laws.

## 2. One run – input
Inventory row 6: free-text loss event narratives from the internal loss database, sent to OpenAI to check whether they contradict an owner's answer.

## 3. Evidence it produced
The narratives can contain health data (Art. 9) and internal-fraud data (Art. 10) about named employees, and they go to a US processor. This met several EDPB DPIA criteria, and the necessity test showed names are not needed for the challenge.

## 4. Final output
Basis: Art. 6(1)(f) with a documented LIA. **DPIA likely required.** Key control: pseudonymise and redact before any LLM call. Controller = bank; processor = OpenAI (and the tool provider if SaaS).

## 5. Failure or limitation
Yesterday's AI Act brief hid the data question: it said "the system assesses processes, not people", which is true for the AI Act but wrong for GDPR, because names, answers and loss narratives are still personal data. I also cannot verify OpenAI's current transfer mechanism and retention settings from here; these are marked "to verify".
