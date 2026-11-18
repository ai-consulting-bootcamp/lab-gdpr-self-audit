# Data processing brief — Editorial research agent for independent bookshops

Ironhack Project 3 · public repo `jaimegmarquerie-ui/proyecto3-agente-editorial`, commit `3939562` · checked 17 Nov 2026 against the code and 20 saved runs · **[V]** verified · **[D]** declared · **[A]** assumption · **[NC]** not checked

**System.** A command-line Python/LangGraph agent. From a bookshop profile, a query and usually an author's name, it searches web and book databases, has an LLM describe and judge each book, and saves a Markdown dossier plus a JSON evidence file [V]. The only user is the founder of *La Insumisa* (not yet open). There is **no customer, sales or staff data** [V].

**Personal data: yes.** Public sources are still personal data.
- Authors' names, biographies, interviews and press profiles [V: the author's name appears in all 10 runs that set one].
- **Third persons** described in retrieved text, including the real subject of a non-fiction book, in a context of political militancy and torture. **Art. 9 data is inferable** [V: 7 of 20 files].
- Social-profile URLs [V: 3].
- The bookseller's unfiltered free-text query [V].
- LLM-written synopses and themes about authors' books [V].

**Sources:** Tavily search; Open Library; Google Books; publisher pages via Tavily; the bookseller's input [V]. Nothing comes from the authors directly.

**Purposes:**
- **F1** Research an author's works for stock decisions.
- **F2** Gemini describes and judges each book.
- **F3** Local audit trail.
- **F4** **Publication of runs on public GitHub** (portfolio).
- **F5** Planned pilot with other bookshops [D].

**Processors and recipients [V, `graph.py`]:**

| Recipient | Receives |
|---|---|
| **Tavily** | Query; title + author (+ publisher) |
| **Open Library** | Author, ISBN |
| **Google Books** | ISBN (+ API key in the URL) |
| **Google Gemini** | Title, author, publisher, ≤ 4,000 characters of publisher text, web snippets, the profile's values (not the shop name) |
| **GitHub** | Published evidence and dossiers |

**Location and storage:**
- Founder's laptop: `evidence/` (21 files) and `samples/` (11 files), **with no retention rule** [V].
- The same files are **public on GitHub** [V].
- Tavily is a US company [V]; Google and Internet Archive are US-based [A]. Server regions and transfer mechanisms: **not documented** [NC].
- Gemini **free tier** [V: README]. Google's terms let it use unpaid-service content to improve its products [V: terms, 23 Mar 2026].

**Decisions and human review.** The agent automatically chooses searches, works, edition and "useful / not useful", and whether to retry [V]. These are decisions about **books, not people**. It orders and publishes nothing. The bookseller is meant to decide, but no approval step or record of that decision exists [V].

**Unknown:** Tavily's role and retention period; applicable DPAs and transfer tools; current Gemini billing; clones or forks of the repo.
