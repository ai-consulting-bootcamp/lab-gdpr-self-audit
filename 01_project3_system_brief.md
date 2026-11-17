# Phase 1: System Brief — Mobile Game Competitor Snapshot Agent

**System Name:** Mobile Game Competitor Snapshot Agent (`Mobile Game Competitor Snapshot mk.III`)  
**Author:** Jędrzej Czarnota

## What the System Does
The Mobile Game Competitor Snapshot Agent is an automated research and briefing tool built for product, marketing, and product-marketing teams at mobile game studios. When a user types in the name of a rival game studio, the system automatically collects public business information, recent news articles, and live Apple App Store performance metrics for that competitor. It then compares the competitor's games and recent moves against the user's own internal studio strategy and key performance indicator (KPI) benchmarks, and emails a formatted four-part competitive intelligence report within approximately 40 seconds.

## What Inputs It Takes
The system takes two categories of input:
1. **User-submitted form data:** Through a web form, the user provides the competitor studio's name (text), their own email address (personal data under the GDPR), and an optional PDF file containing their studio's internal strategy and KPI benchmarks (if no PDF is uploaded, the system uses a pre-loaded fictional studio playbook called *Northstar Nova Games Strategy & KPI Benchmarks*).
2. **External public web and storefront data:** The workflow automatically queries three external sources in parallel: the Tavily web search API (for studio background, estimated revenue, and downloads), the GNews API (for up to five recent English-language news articles), and the Apple iTunes Search API (for up to five US iOS games, star ratings, rating counts, release dates, and update dates). While these queries target company-level data, web and news snippets occasionally contain personal data, such as the names and job titles of studio founders, executives, or journalists.

## What It Outputs
The system outputs a styled HTML email report divided into four fixed sections:
* **1. Who They Are:** A three-paragraph summary of the competitor's headquarters, business model, and core game genres.
* **2. How They're Doing:** Bullet points of reported studio revenue and download estimates with source links, paired with an iOS Storefront Telemetry Table showing star ratings, rating velocity per year, days since last update, and a calculated LiveOps activity signal (`Active LiveOps`, `Moderate`, or `Maintenance / Slow`).
* **3. What's New:** Three summarized news headlines with clickable source links.
* **4. What It Means For Our Studio:** Three concrete strategic recommendations formatted as *Observation -> Implication for Our Studio -> Low-Risk Test -> Success Metric*.

## Who Is Affected by the Output
The primary people affected are internal mobile game studio staff—Product Managers, Marketing Managers, and Product Marketing Managers—who use the briefing to prioritize product experiments, LiveOps cadence, and marketing positioning. Indirectly, competitor game studios are evaluated in the reports, and individuals mentioned in public news or industry articles appear in the underlying research context.

## Human Review in Practice
There is **zero human review between form submission and email delivery**; once the user clicks "Research competitor," the system gathers data, drafts the text, and sends the email autonomously. However, the system cannot execute business decisions on its own. In practice, human review happens *after* delivery: the receiving Product or Marketing Manager reads the email briefing, checks the cited news and telemetry links, and decides whether to propose any suggested "Low-Risk Test" to their team.

## Who Built It and Who Uses It in Production
I (Jędrzej Czarnota) designed and built the workflow by configuring and integrating third-party services inside **n8n**, combining **OpenAI** (`gpt-4o-mini` for report writing and `text-embedding-3-small` for document embeddings), **Pinecone** (vector database for strategy retrieval), **Tavily**, **GNews**, **Apple iTunes Search**, and **Gmail**. In production, the system supports two operating modes: during Go-To-Market (GTM) validation sprints, I operate the hosted workflow and deliver reports to client PMs, MMs, and PMMs across studios in Berlin, Warsaw, and Helsinki (progressing to a €99/month subscription plan); alternatively, a client studio's Product Ops team can import the n8n workflow file to run it internally for their own staff.
