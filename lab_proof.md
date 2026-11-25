# Audit Your Own Project — GDPR Lens: Retune

**Audit date:** 25 November 2026  
**System:** Retune, the bilingual routine and wellbeing app in Lovable project “Activities Hub”  
**Source version reviewed:** `a912852896a89dc367dfe967ae3a1c8efaa0331d`  
**Scope:** The current MVP and the pilot use confirmed by the project owner. Real pilot users entered personal data and used group sharing. The number of users and exact fields entered are unknown. Future AI features are outside this review.

## Data-processing brief for the project operator

Retune is a web app for people to plan and track activities and personal routines. Users sign in with Google. They can enter activity names and schedules, personal goals, progress logs, free-text notes, sleep hours and quality, energy, mood, and short reflections. The app uses this information to show personal histories, counts, milestones, and simple rule-based patterns. It does not provide medical diagnosis or treatment. No AI model or AI API integration was found in the reviewed source.

The app also has a “Together” group feature. The project owner confirmed that pilot users used it. Users can join groups and choose activity check-ins to share. A shared record contains the activity name, completion status, and date. The system also stores group memberships, display names, optional avatar URLs, invitation codes, and supportive reactions. The code does not show sleep, mood, or private notes being included in shared check-ins. Separate usability or research surveys may exist outside the app; none were identified in the reviewed source, so their data and storage must be checked separately.

The app writes account and app records to a Supabase/PostgreSQL backend. The source contains a Supabase project reference, but direct access through the project owner’s Supabase dashboard was denied. The backend may be managed through Lovable Cloud; confirm this in the project’s Cloud settings. The database region, service agreements, transfer arrangements, and provider retention are unknown. No automatic expiry or full account-deletion flow was found in the reviewed app code. Users can delete some individual records. The app also uses browser storage for onboarding state, temporary answers before sign-in, and authentication.

**Personal-data conclusion:** Retune processes personal data. Account email and user IDs identify people; activity, mood, sleep, energy, and reflection entries relate to identifiable users. Some entries may reveal health information. Whether the pilot processed special-category health data under Article 9 depends on the actual entries and context and requires legal review. The in-app privacy text is short and says data is used “only inside this app,” although Google and the backend also take part in processing; the wording should be reviewed.

## Evidence labels

- **Code-confirmed:** visible in the source code or database migrations at the reviewed commit.
- **Owner-confirmed:** stated by the project owner: real pilot users entered data and used group sharing.
- **Unknown:** not proven by the reviewed code or owner confirmation; verify before relying on it.

## Phase 1 — Personal-data inventory

Rows are separated by purpose where the same data supports more than one activity.

| Data category | Source | Purpose | Retention period | Crosses EEA border? |
|---|---|---|---|---|
| Account email and account ID | Google sign-in / authenticated account | Authenticate the user and provide access to the saved account | Provider and account-deletion periods unknown | Unknown; Google and backend locations/transfer terms need confirmation |
| Activity names, categories, schedules, goals and notes | Directly entered by the user | Let the user plan and organize personal routines | No automatic expiry found; some activity records can be deleted | Unknown backend region |
| Activity names, categories, schedules and progress history | Directly entered by the user | Show personal counts, milestones, charts and rule-based patterns | No automatic expiry found; individual logs can be deleted | Unknown backend region |
| Date, completion status, duration, completion type, energy level and log note | Directly entered by the user | Save a daily activity record | No automatic expiry found; individual logs can be deleted | Unknown backend region |
| Sleep hours/quality, mood and daily energy | Directly entered by the user | Show the user’s own wellbeing history | No automatic expiry found | Unknown backend region; possible health-data implications need review |
| Sleep, mood, energy and activity records | Directly entered by the user | Compare the user’s own wellbeing and activity patterns | No automatic expiry found | Unknown backend region; possible health-data implications need review |
| Reflection: feeling, next step, what helped, linked activity and timestamp | Directly entered by the user | Support personal reflection and journey summaries | No period or deletion rule verified; code uses a `reflections` table, but no matching migration was found in the reviewed repository | Unknown backend region |
| Display name, optional avatar, group membership and invitation code | Entered or generated when users create/join groups | Identify group members and manage group access | No schedule found; some profiles/groups can be deleted | Unknown backend region and provider processing |
| Selected shared activity name, status, date and reactions | Chosen or entered by pilot users; the owner confirmed the feature was used | Share selected check-ins with group members and provide support | No schedule found; users can delete some check-ins and reactions | Unknown backend region and provider processing |
| Onboarding state, temporary answers and authentication state | Stored in the user’s browser | Remember onboarding progress and maintain the session | Remains in browser storage until removed or cleared; exact session period unknown | Browser storage stays on the device; authentication provider locations unknown |
| Font request and possible runtime error details | Browser/app runtime | Load fonts and diagnose errors, mainly in Lovable preview | Provider log retention unknown | Unknown; check external service locations and terms |

The code proves that these fields can be processed, not that pilot users filled in every field. The number of pilot users and exact categories they entered are unknown. If separate survey results were collected for the pilot, add them as their own data categories, purposes, storage locations, and retention periods.

## Phase 2 — Role map

| Entity | Likely GDPR role | Processing activity | DPA in place? / transfer status |
|---|---|---|---|
| Retune project operator | Likely controller because the operator chooses the app’s purposes and means. Confirm whether the university or another organisation jointly decided the pilot’s purposes or essential means. | Defines and runs the app, collects pilot information, decides which check-ins can be shared | Formal controller identity and any university role are unverified |
| Lovable Cloud / Supabase backend | Likely processor for app storage and authentication if Lovable Cloud manages the backend | Stores account and app records and serves database requests | Unknown. Confirm backend type, DPA, sub-processors, region and transfer terms in Lovable Cloud settings |
| Google | Authentication provider; role depends on the purpose and provider terms | Google OAuth sign-in and related authentication requests | Role, agreement and transfer mechanism not checked |
| Google Fonts | External service requested by the app shell | Serves font files to the user’s browser and may receive connection metadata | Role, disclosure and transfer details not checked |
| Pilot users and group members | Data subjects; group members can receive check-ins deliberately shared with them | Enter their own information and view selected check-ins from other members | Notice shown to pilot users and records of their choices need verification |

No LLM or AI API provider was identified in the reviewed application source.

## Phase 3 — Lawful-basis assessment

The source has a short privacy explanation but no complete privacy notice, terms, or recorded lawful-basis assessment. The bases below are reasoned candidates, not final legal conclusions. A lawful basis is needed for each purpose. If data reveals health information, an Article 9 condition is also needed.

| Purpose | Proposed basis / status | One-line justification | Legal review? |
|---|---|---|---|
| Account sign-in and saved account features | Article 6(1)(b), contract, is a candidate | Sign-in and saving data appear necessary to provide the account service requested by the user, but no service terms explaining this were found. | **TBD — legal review** |
| Personal activity planning and logs | Article 6(1)(b), contract, is a candidate; optional fields may need a separate basis | Users enter these details to receive the app’s core tracking service; the necessity and user-facing terms are not documented. | **TBD — legal review** |
| Wellbeing entries and personal pattern summaries | Article 6(1)(b) or consent may be candidates; Article 9 condition may also be needed | Users provide the data for personal wellbeing tracking, but the app does not explain the legal basis or health-data condition. | **TBD — legal review** |
| Optional group sharing | Article 6(1)(a), consent, is a candidate | Users select which check-ins to share; verify clear information, a genuine choice, and a way to withdraw without losing core features. Review Article 9 separately if shared content reveals health data. | **TBD — legal review** |
| Security and error diagnostics | Article 6(1)(f), legitimate interests, is a candidate only if this processing occurs | Protecting the service may be a legitimate interest, but the actual events, necessity, less intrusive alternatives, and user impact must be assessed. Complete a three-part LIA before relying on it. | **TBD — legal review** |

**Three-part LIA screen for possible diagnostics:** (1) **Purpose:** protecting the app and investigating errors is a legitimate interest if diagnostics are actually collected. (2) **Necessity:** collect only the minimum technical details needed to fix a problem; confirm whether the same goal can be met without a user ID, full text, or full activity history. (3) **Balancing:** users may not expect their route or error details to leave the app, and wellbeing entries can be sensitive; explain the collection, restrict access, and set a short retention period. All three parts remain **TBD** until the actual production telemetry and provider settings are confirmed.

## Phase 4 — Risk and rights analysis

**Special-category data (Article 9):** The app accepts mood, energy, sleep, therapy-related activity names, and free-text reflections. These fields are not automatically Article 9 data in every context, but they may reveal a person’s health when linked to an account. Review actual pilot fields and context. If the entries reveal health information, identify a valid Article 9 condition; none is documented in the material reviewed.

**Automated decision-making (Article 22):** The app calculates counts, milestones, and simple rule-based insights from user entries. No decision with legal or similarly significant effects on a person was found. The reviewed build does not appear to make consequential decisions without human review.

**DPIA criteria screen:**

| EDPB criterion | Finding for Retune |
|---|---|
| Evaluation or scoring | **Possible.** The app evaluates personal routines and calculates patterns, but does not rank users. |
| Automated decisions with significant effects | **No evidence found.** |
| Systematic monitoring | **Possible.** The app records routine and wellbeing data over time. |
| Sensitive or highly personal data | **Possible.** Mood, sleep, energy, reflections and activity names may reveal health information. |
| Large-scale processing | **Unknown.** Pilot size is not known; no evidence of large-scale use was found. |
| Matching or combining datasets | **No evidence found** beyond combining a user’s own app entries to show personal patterns. |
| Vulnerable people | **Unknown.** User ages and any age restrictions were not verified. |
| Innovative technology | **No AI or novel technology identified** in this build. |
| Processing prevents a right or service | **No evidence found.** |

Two or more criteria may apply. Document the screening and complete a DPIA before expanding the pilot if the processing is likely to create high risk. The EDPB says that, in most cases, processing meeting two criteria should be assessed through a DPIA.

**Data-subject rights:** Users can view some records and delete individual logs or shared check-ins. The app settings show sign-out, but no full account-deletion or data-export flow was found. No documented process was found for access, correction, objection, withdrawal of sharing, or tracking the one-month response deadline. Define a manual process and test it with synthetic accounts.

## Phase 5 — Law-stacking check

- **EU AI Act:** No AI system, model API, or AI feature was identified in the reviewed build. Treat the AI Act as not applicable to this version; reassess if AI is added.
- **ePrivacy:** The app stores onboarding and authentication state in browser storage and requests Google Fonts. No analytics SDK, tracking pixel, or cookie banner was found. Assess whether each storage item is strictly necessary and give clear information; assess the font request separately.
- **Data Act:** No connected-product or IoT data was identified, so those provisions appear not applicable. Check cloud portability and switching terms with the backend provider.

## Phase 6 — Recommendation memo

**To: Project operator / legal counsel**

**Bottom line: Retune should proceed only with conditions before collecting more pilot data, because the lawful basis, possible Article 9 condition, backend region, provider terms, and retention/deletion policy are unconfirmed.** The current build processes identifiable account data, activity histories, free-text reflections, sleep, mood, energy, and group check-ins. The project owner confirmed that real pilot users entered data and used group sharing. The source shows that users can choose to share an activity name, completion status, and date with their group.

First, identify the controller for the pilot and document each processing purpose, lawful basis, and any Article 9 condition. Confirm whether the university or another organisation helped decide the pilot’s purposes or essential means. Review the privacy information shown to participants. The current in-app text is brief and says data is used only inside the app, although Google and a backend provider also take part in processing.

Second, confirm in the Lovable project’s Cloud settings whether the backend is managed by Lovable or connected to a separate Supabase account. Record the database region, processor and sub-processor terms, international-transfer arrangements, and provider log retention. The project reference in source code does not prove that the database belongs to the operator’s Supabase account.

Third, set a clear retention schedule and a complete process for access, correction, export, sharing withdrawal, and deletion requests. The reviewed code has no automatic expiry or full account-deletion flow. Complete and document a DPIA screening for wellbeing data and longitudinal tracking; if likely high risk, complete a DPIA before any wider pilot.

Residual risks include health information inferred from activity names or free text, disclosure within groups if users misunderstand what a check-in reveals, and uncertainty about the backend region and backup retention. This memo is a first-pass assessment, not a legal opinion, DPIA, or certification. Obtain legal advice before relying on it for compliance decisions.

## Reinforce — Accountability evidence

| Document or control | Status from reviewed material | Next step |
|---|---|---|
| Records of processing activities | Not found | Create one, or document whether an exemption applies |
| Privacy notice | Short in-app explanation exists; full notice and proof it was shown to pilot users are unknown | Update with purposes, bases, recipients, location, retention, and rights |
| Processor agreement / DPA | Unknown | Confirm for Lovable Cloud or connected Supabase and sub-processors |
| Legitimate Interests Assessment | Not found | Complete only if Article 6(1)(f) is selected |
| DPIA | Not found | Finish the screening and record the decision; complete a DPIA if required |
| Retention schedule | Not found | Set periods for app data and separately record provider backup/log retention |
| Rights-request workflow | Not found | Assign an owner and track access, correction, export, objection, withdrawal, and erasure requests |
| Breach-response process | Not found | Document detection, escalation, and the 72-hour notification assessment |
| Transfer mechanism | Unknown | Confirm location, recipients, and applicable transfer safeguards |

## Stretch — Data protection by design

| Design principle | Current state | Change needed |
|---|---|---|
| Data minimisation | **Unknown.** Detailed wellbeing and free-text fields are supported. | Confirm each field is needed; make optional entries clearly optional and avoid requesting clinical details. |
| Purpose binding | **Partial.** Privacy text says most information is private; sharing is user-selected. | Connect each field to a stated purpose and technically share only the selected check-ins. |
| Access controls | **Partial.** Migrations enable row-level security and own-data/group policies. | Verify policies on the live backend, including the reflections table; test with synthetic users in separate groups. |
| Retention enforcement | **Fail / unknown.** No expiry or full account-deletion flow found in reviewed code. | Set periods and design complete deletion for accounts, app records, shared records, and provider backups where possible. |
| Data-subject rights | **Fail / unknown.** Some item-level deletion exists; no complete export or account-erasure workflow found. | Provide and test a documented process for access, correction, export, sharing withdrawal, and erasure. |
| Incident response | **Unknown.** No 72-hour assessment and notification process found. | Document who detects, escalates, preserves evidence, and assesses notification duties. |

## Lab proof — code, query, evidence, output, limitation

**Input:** Read-only review of the Lovable project source at commit `a912852896a89dc367dfe967ae3a1c8efaa0331d`. Files reviewed include `src/lib/data.ts`, `src/lib/daily.ts`, `src/lib/journey.ts`, `src/lib/social.ts`, `src/lib/prefs.ts`, `src/components/Onboarding.tsx`, `src/routes/auth.tsx`, `src/routes/_authenticated/settings.tsx`, Supabase client configuration, and the database migrations.

**Code/workflow evidence export:** The code writes daily wellbeing fields to the `daily_entries` table and selected group check-ins to `shared_checkins`. The following excerpt shows the data fields, with no user values:

```ts
// src/lib/daily.ts
await supabase.from("daily_entries").upsert({
  user_id: uid,
  entry_date: date,
  sleep_hours: patch.sleep_hours ?? current?.sleep_hours ?? null,
  sleep_quality: patch.sleep_quality ?? current?.sleep_quality ?? null,
  energy: patch.energy ?? current?.energy ?? null,
  mood: patch.mood ?? current?.mood ?? null,
});

// src/lib/social.ts
await supabase.from("shared_checkins").upsert(
  items.map((item) => ({
    user_id: uid, group_id: groupId,
    activity_name: item.activity_name,
    status: item.status,
    checkin_date: date,
  })),
);
```

**Read-only source query:** Search the listed source files for `supabase.from(...)`, `supabase.rpc(...)`, `localStorage`, and database migration `CREATE TABLE` statements.

**Evidence produced:** The code uses Google OAuth; app tables include activities, activity logs, daily entries, preferences, social profiles, groups, group members, invitations, sharing preferences, shared check-ins, reactions, badges, return events, and reflections. Onboarding answers may be held in browser storage before sign-in. Group sharing stores activity name, status, and date. The project owner separately confirmed real pilot use and use of group sharing.

**Final output:** This inventory, role map, lawful-basis assessment, risk analysis, recommendation memo, accountability checklist, and data-protection-by-design checklist.

**Failure / limitation:** Direct Supabase Dashboard access was denied, so the live backend type, region, user counts, provider retention, backups, and full account-deletion configuration could not be verified. The code uses a `reflections` table, but a matching migration was not found in the reviewed repository. No live user records were queried. These points remain **TBD** rather than being presented as confirmed safeguards.

## References

1. GDPR, Regulation (EU) 2016/679, Articles 2, 4–6, 9, 12–22, 25, 28, 30, 32, 35 and 44: <https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng>
2. European Data Protection Board, “Be compliant” and DPIA criteria: <https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en>
3. European Data Protection Board, “Data controller or data processor”: <https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en>
4. ePrivacy Directive, Article 5(3): <https://eur-lex.europa.eu/eli/dir/2002/58/art_5/par_3/oj/eng>
5. Data Act, Regulation (EU) 2023/2854: <https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng>
6. Supabase guidance on projects managed through Lovable Cloud: <https://supabase.com/kb/troubleshooting/cant-access-supabase-project-lovable-cloud>
