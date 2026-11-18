"""Read-only scan of Project 3 evidence JSON files for personal-data indicators.
Usage: python -I scan_personal_data.py <repo_path>
Does not call any API. Prints counts only (no personal content copied)."""
import json, sys, pathlib, re, collections
repo = pathlib.Path(sys.argv[1])
ev = sorted((repo / "evidence").glob("editorial_*.json"))
authors = collections.Counter(); profile_names = collections.Counter()
social = collections.Counter(); domains = collections.Counter()
n_results = 0; n_books = 0; keys_seen = set(); queries_with_author = 0
for p in ev:
    d = json.loads(p.read_text(encoding="utf-8"))
    keys_seen |= set(d.keys())
    if d.get("author"): authors[d["author"]] += 1
    if d.get("profile_name"): profile_names[d["profile_name"]] += 1
    q = d.get("query") or ""
    if d.get("author") and d["author"].split()[-1].lower() in q.lower(): queries_with_author += 1
    for r in d.get("results", []) or []:
        n_results += 1
        url = r.get("url", "") if isinstance(r, dict) else ""
        host = re.sub(r"^https?://(www\.)?", "", url).split("/")[0]
        if host: domains[host] += 1
        if any(s in host for s in ("x.com", "twitter.com", "instagram.com", "facebook.com", "linkedin.com")):
            social[host] += 1
    n_books += len(d.get("books", []) or [])
print("evidence_files", len(ev))
print("top_level_keys", sorted(keys_seen))
print("distinct_author_values", len(authors), "runs_with_author", sum(authors.values()))
print("runs_where_query_contains_author_surname", queries_with_author)
print("distinct_profile_names", dict(profile_names))
print("tavily_results_total", n_results, "books_total", n_books)
print("social_profile_results", dict(social))
print("top_domains", domains.most_common(8))
txt = " ".join(p.read_text(encoding="utf-8") for p in ev)
print("email_like_strings", len(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", txt))))
