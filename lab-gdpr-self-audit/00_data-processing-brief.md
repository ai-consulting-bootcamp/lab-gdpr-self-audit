# Data processing brief

## Does this system process personal data?

Yes. The primary subject matter is vehicle geometry, not people — but the system processes
personal data about the people who *use* it and the people they *communicate with* through it.
Dismissing this because "the data is about cars" was the shortcut I took during development. It
is wrong, and this brief explains why.

## What personal data the system processes

**1. Designer identity and behaviour.** The designer's name (displayed in the session and
attached to saved versions), their typed questions and instructions across every thread in a
session, timestamps of every interaction, and the sequence of geometry versions they created or
accepted. Over weeks of use, the thread history becomes a detailed record of one person's
design reasoning, decisions, and working patterns.

**2. Recipient identity.** When the designer sends a handoff report, they enter the name of the
receiving engineer (visible on screen as "To: A. Matwejew"). This is personal data about a
person who never interacted with the system.

**3. Content that may mention people.** The designer's typed questions are free text. Nothing
prevents them from typing a colleague's name, a manager's feedback, or internal team context.
The system stores and forwards this without filtering.

**4. Inferred work patterns.** Thread history, version timelines, and the "your hand" vs "agent"
labels on versions create a traceable record of when the designer worked, how many iterations
they needed, how often they overrode the assistant, and how long they spent. This is behavioural
data about an identifiable employee.

## Where the data comes from

All personal data is entered directly by the designer during use — names typed, questions
written, versions saved. No data is pulled from existing company databases or third-party
sources. The designer is the sole source.

## What the data is used for

- **Purpose 1 — providing the service:** processing the designer's questions and returning
  analysis results in the same session.
- **Purpose 2 — version management:** maintaining a history of geometry versions, who created
  each, and how (hand edit vs agent suggestion), so the designer can compare and revert.
- **Purpose 3 — handoff:** assembling and sending a report to a named colleague, including
  selected thread excerpts and geometry.
- **Purpose 4 — session continuity:** retaining thread history so the designer can return to a
  session and continue where they left off.

There is no stated purpose for analytics, model improvement, or any secondary use. But no
technical or contractual control currently prevents it, which is the gap.

## Who processes it

- **The RegGuard-Mini application** (our code): stores sessions, threads, versions, and
  assembles reports.
- **The LLM API provider** (OpenAI in the built version): receives the designer's typed
  questions and session context as part of inference calls. Their data processing terms govern
  what they may do with it; I have not verified whether those terms align with our stated purposes.
- **The hosting infrastructure** (cloud provider): stores session state, geometry files, and
  thread logs.

## Where the data is stored and processed

The built version runs on cloud infrastructure. The interface claims "Runs on: OEM network" —
this is inaccurate for the current build. The LLM API calls cross the network boundary
regardless. Whether the data crosses an EU border depends on the specific cloud region and the
API provider's processing location. For OpenAI's API: **data is processed in the US**, meaning
every inference call is an international transfer outside the EEA.

## Decisions affecting people

The system does not make decisions about people. It makes assessments about vehicle geometry.
No person is scored, ranked, evaluated, hired, denied, or flagged.

However: the inferred work-pattern data (how many iterations, how often the designer overrode
suggestions, time spent per version) could be repurposed by a manager for performance
monitoring. The system does not do this, but it creates the raw material for it, and no
technical control prevents an employer from extracting it. This is a foreseeable misuse that
matters under GDPR's purpose limitation principle.
