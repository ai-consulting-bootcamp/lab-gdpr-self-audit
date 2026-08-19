# Phase 5 — Law stacking check

## AI Act cross-check

**Risk tier:** Limited risk — transparency obligations under Article 50. Classified in the
companion AI Act audit of this system.

**Does the AI Act impose anything GDPR does not already require?** Yes, in two places:

1. **Article 50(1) — AI disclosure.** GDPR requires transparency about data processing; the AI
   Act separately requires that the user be told they are interacting with an AI system. These
   are different obligations with different triggers. A GDPR privacy notice does not satisfy the
   AI Act disclosure, and an AI Act "this is an AI" label does not satisfy GDPR's Article 13/14
   information requirements. Both are needed.

2. **Article 50(2) — machine-readable marking of generated content.** GDPR has no equivalent.
   The handoff report contains AI-generated text that leaves the system — the AI Act may require
   provenance marking. Whether this obligation legally applies to an internal engineering
   document is uncertain and flagged for legal review in the AI Act audit.

3. **Article 4 — AI literacy.** GDPR's transparency principle is about informing data subjects;
   the AI Act's literacy duty is about ensuring *staff* understand the AI they operate. Overlapping
   but distinct.

## ePrivacy check

The system does not use cookies, tracking pixels, or device-level data collection. It is a
web-based professional tool; session state is maintained server-side. No content of electronic
communications (email, messaging) is accessed or processed.

**ePrivacy consent requirement: does not apply** in the current design.

One edge case to watch: if the handoff report is sent via email integration (rather than
downloaded and forwarded manually), the content of the email — including the recipient's address
and any covering note — would be electronic communication content. This would bring ePrivacy
into scope for that specific flow. The current wireframes show a "Send report" button without
specifying the delivery mechanism. If it becomes email, revisit this.

## Data Act check

The system does not involve connected-product data, IoT data streams, or cloud-service switching
in the Data Act's sense. Vehicle geometry files are uploaded manually by the designer; they are
not streamed from a connected vehicle or an IoT sensor.

**Data Act: not applicable.**

One long-term note: if Onyx Dynamics later integrates with a connected-vehicle platform or
receives telemetry data alongside geometry (e.g. wind-tunnel sensor data paired with design
versions), the Data Act's data-sharing obligations and cloud-switching provisions could engage.
This is not the current system.
