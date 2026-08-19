# Phase 3 — Lawful basis assessment

## Basis table

| # | Purpose | Proposed lawful basis | One-line justification | Flag for legal review? |
|---|---|---|---|---|
| 1 | Providing the service — processing questions, returning analysis | Art. 6(1)(b) — contract | Processing is necessary to perform the service the designer's employer contracted for; the designer is the user under that contract. | **Yes.** Art. 6(1)(b) applies to a contract with the data subject. The contract is between Onyx and the OEM, not Onyx and the individual designer. If the designer is not a party, legitimate interests (below) is the fallback. |
| 2 | Version management — tracking who created each version | Art. 6(1)(f) — legitimate interests | Necessary for the core product function of comparing and reverting design versions; the designer expects this as part of the tool. | No |
| 3 | Handoff — sending a report to a named colleague | Art. 6(1)(f) — legitimate interests | The designer initiates the send and selects the content; the recipient's name is necessary to address the report. | **Yes.** The recipient is a data subject who did not interact with the system. Their name is processed on the designer's instruction, not their own. Legitimate interests is the most plausible basis, but the balancing test must account for the recipient's reasonable expectations. |
| 4 | Session continuity — retaining threads for return visits | Art. 6(1)(f) — legitimate interests | The designer expects to return to their work; indefinite retention without a defined period is the problem, not the purpose itself. | **Yes.** The purpose is legitimate but the *duration* is not proportionate without a retention limit. |

## Legitimate interests assessments

### LIA for Purpose 2 — Version management

**1. Is the interest legitimate?**
Yes. Version tracking with authorship attribution is a core product function. Designers need to
know which version they created by hand and which the agent proposed, to make informed decisions
about what to keep. The OEM needs version provenance for its own design-review processes.

**2. Is the processing necessary?**
Yes. A version history without authorship is functionally incomplete — the designer cannot
distinguish their own work from agent suggestions, which defeats the human-oversight design.
There is no less intrusive way to provide this: anonymous version tracking removes the
information the user needs.

**3. Does the individual's interest override?**
No. The data subject is the designer using the tool in a professional context; they expect their
name on their own work. The privacy impact is low — this is equivalent to a "last modified by"
field in any collaborative tool.

**However:** the version timeline also exposes iteration count, override frequency, and
time-per-version, which are behavioural data. The legitimate interest covers *authorship
attribution*, not *performance profiling*. If the deployer uses version history for employee
monitoring, the balancing test flips. This must be addressed through a contractual use
restriction in the DPA, not through the LIA alone.

**Conclusion: Legitimate interests holds for the stated purpose, with a contractual safeguard
against repurposing for employee monitoring.**

---

### LIA for Purpose 3 — Handoff (recipient's name)

**1. Is the interest legitimate?**
Yes. Sending an engineering report to a named colleague is the final step in the product's
workflow. The report must be addressed to be actionable.

**2. Is the processing necessary?**
Yes. An unaddressed report cannot be delivered. The recipient's name is the minimum data needed —
no email address, job title, or other identifier is collected.

**3. Does the individual's interest override?**
Unlikely but not certain. The recipient is a colleague in the same organisation, in a
professional context, receiving a work document. Their reasonable expectation is that colleagues
can send them reports. But they did not interact with the system, were not informed their name
was processed by an AI tool, and have no visibility into how long it is retained or what else
it is used for.

**Conclusion: Legitimate interests is defensible but requires that the recipient can be informed
— either through the OEM's internal privacy notice covering workplace tools, or through a
notice on the report itself. `TBD — legal review` on whether the OEM's existing employee
privacy notice covers this, or whether a supplement is needed.**

---

### LIA for Purpose 4 — Session continuity

**1. Is the interest legitimate?**
Yes. Designers work on vehicle programmes over weeks or months. Losing thread history on each
session close would make the tool impractical.

**2. Is the processing necessary?**
Retaining threads: yes. Retaining them *indefinitely*: no. The necessity test requires the least
intrusive means. A retention period tied to the programme lifecycle (e.g. 12 months after the
last interaction, or until the programme milestone closes) would serve the same purpose.

**3. Does the individual's interest override?**
Not for time-limited retention. For indefinite retention, the balance shifts: an unbounded
archive of an employee's questions, reasoning, and working patterns across years of use is
disproportionate to "session continuity."

**Conclusion: Legitimate interests holds only with a defined retention period. Without one, the
proportionality leg fails. Set retention, and the basis is sound.**

---

## Summary of flags

Three items flagged for legal review:

1. Whether Art. 6(1)(b) or 6(1)(f) is the correct basis for the primary service purpose — turns
   on whether the individual designer is a party to the contract.
2. Whether the OEM's existing employee privacy notice covers the handoff recipient, or whether
   supplementary notice is needed.
3. Whether OpenAI's API data-use terms are compatible with the "no secondary use" position our
   legitimate-interests assessment depends on.
