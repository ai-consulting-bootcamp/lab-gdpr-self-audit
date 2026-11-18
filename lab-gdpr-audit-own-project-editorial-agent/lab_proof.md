# lab_proof — Audit your own project, GDPR lens (editorial research agent)

**Entry point for the reviewer.** Read in this order:
1. [`data_processing_brief_editorial_agent.md`](data_processing_brief_editorial_agent.md) — kick-off, one page
2. [`gdpr_self_audit_editorial_agent.md`](gdpr_self_audit_editorial_agent.md) — CFU 1, Phases 1–5, accountability test
3. [`compliance_memo_dpo_editorial_agent.md`](compliance_memo_dpo_editorial_agent.md) — Phase 6, 389 words

## 1. Code or workflow export (the system audited)

The audited system is Project 3. The full code lives in its own repository and is **not copied here**. This repository must contain only this lab's material.
- Repository: `https://github.com/jaimegmarquerie-ui/proyecto3-agente-editorial`, commit **`3939562`** (13 Nov 2026, 10:45 CET).
- Workflow: a LangGraph graph with 10 nodes, wired in [`editorial_agent/graph.py` l. 1855–1883](https://github.com/jaimegmarquerie-ui/proyecto3-agente-editorial/blob/3939562dec432c07f804a5412cf4a8c02dfdccd3/editorial_agent/graph.py#L1855-L1883):

```text
START → read_profile → search_tavily → fetch_books → fetch_google_books → fetch_publisher_pages
      → describe_books → judge_results ─(insufficient, ≤2 tries)→ reformulate_query → search_tavily
                                        └(sufficient)→ write_dossier → save_result → END
```

**Personal-data flows read in the code (17 Nov 2026):**

| Flow | Code location |
|---|---|
| Query → Tavily | `graph.py` l. 314–321 |
| Title + author → Tavily | l. 750–775 |
| Author/ISBN → Open Library | l. 364–530 |
| ISBN + key → Google Books | l. 582–586 |
| Publisher text (≤ 4,000 chars) → Gemini | l. 829 and 895–931 |
| Profile values, without the shop name → Gemini judge | l. 1103–1110 |
| Query, author, titles, URLs → Gemini reformulation | l. 1414–1427 |
| Everything → JSON evidence file | `save_result`, l. 1814–1846 |

## 2. Runs actually performed today (no paid calls, no external API calls)

| # | Input | Command | Evidence |
|---|---|---|---|
| A | Fresh clone of the public repo at `3939562`, in the tutor's (Claude's) sandbox | `git clone …` then `git log -1` → `3939562dec43… 2026-11-13 10:45:52 +0100` | console |
| B | The 20 saved run files in `evidence/` | `python -I proof/scan_personal_data.py <repo>` — read-only, prints **counts only**, copies no personal content | [`proof/lab2_scan.txt`](proof/lab2_scan.txt) |
| C | The project's test suite with the pinned `requirements.txt`, isolated virtual environment, all services mocked | `python -m pytest -q` | [`proof/lab2_pytest.txt`](proof/lab2_pytest.txt) → `49 passed` |
| D | Text search of the repository docs for GDPR or privacy documentation | `grep -rli "gdpr\|rgpd\|privacy\|privacidad\|retention\|conservaci\|dpa\|dpia" --include=*.md .` | **no results** → used in the accountability test |

Output of run B (excerpt; the full output is in `proof/lab2_scan.txt`):

```text
evidence_files 20
distinct_author_values 1 runs_with_author 10
runs_where_query_contains_author_surname 10
distinct_profile_names {'La Insumisa': 20}
tavily_results_total 100 books_total 70
social_profile_results {'linkedin.com': 2, 'x.com': 1}
top_domains [('casadellibro.com', 19), ('todostuslibros.com', 17), ('elpais.com', 15), ('anagrama-ed.es', 15), ...]
email_like_strings 0
```

A separate `grep` counted how many files mention the third person named in a non-fiction book: **7 files**. Her name is deliberately not reproduced here.

## 3. Final output (how the evidence changed the audit)

- **The provisional System Brief was wrong.** It said "the exact personal data … has not yet been verified". The code shows exactly which fields reach each provider (section 1). The brief also mentioned GDELT, which is **not** in the code. It is listed as postponed in `README.md` §5.
- **"Public sources" does not mean "no GDPR".** Run B shows author data in every run with an author, social-profile URLs, and 7 files containing a third person in a sensitive context. This led to the Art. 9 finding and the F4 purpose-limitation flag.
- **There is no email or customer data** (run B: 0 email-like strings; the profile status says no customers). This confirms there is no Art. 22 issue.
- **Run D** found no ROPA, notice, LIA, DPIA, DPA or retention document. This is the basis for the "no" verdict in the accountability test.
- **The memo's decision:** proceed with conditions.

## 4. Failure or limitation hit

1. **Provider facts I could not verify.**
   - I could not open the full Gemini terms page: it is not on the sandbox's allowed list. I relied on search excerpts of `ai.google.dev/terms` (effective 23 Mar 2026) and archived versions.
   - The "EEA → Paid Services only" restriction appears in the 20 Nov 2025 archived version. It must be re-read in the current version.
   - I did not check Tavily's DPA, hosting region or DPF certification [NC].
   - **Gemini status (17 Nov, 17:39):** Jaime reports that Gemini "still works" [D]. That confirms the key is active; it does **not** say whether the project is billed (Paid Services) or on the free tier. The README says free tier, so the finding stands until billing is checked in Google AI Studio.
2. **No runtime check of data actually sent.** I read the code and the saved outputs, but did not intercept a live request. That would have required real API calls with the student's keys, which were not used.
3. **Tests do not cover privacy.** The 49 tests mock every service, and none checks what personal data leaves the system.
4. **Missing official source.** `01_gdpr-fundamentals.md` was not available and has not been read.
5. **The student has not reviewed this yet.** These are tutor drafts. The student must read and defend them before any PR.
