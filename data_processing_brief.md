# Data Processing Brief — Platform Risk Research Agent

Written for a Data Protection Officer who has not seen this project.

## What personal data does the system process?

Three categories:

1. **Account data.** Name and email, if a buyer signs up to use the tool.
2. **Buyer context data.** Company name, use case, and internal context the user types in to scope a vendor check. Can include names of internal teams or roles if the user includes them.
3. **Incidental data from public web research.** The research agent pulls public web content about the vendor under review. This can include named individuals mentioned in breach disclosures, news articles, or reviews. This is not intentional collection.

No special category data is intentionally collected. It could be inferred if a public source names an individual's health, criminal, or other sensitive status inside a breach disclosure.

## Where does that data come from?

- Account and buyer context data: submitted directly by the user.
- Vendor research data: pulled from public web sources by the research tools (web search, compliance search, firmographic search).
- No data comes from an existing company database or third-party data broker.

## What is the data used for?

- Account data: login and product access.
- Buyer context data: scoping the vendor risk report to the buyer's actual use case.
- Vendor research data: producing the risk report.

Each purpose is separate. No data collected for one purpose is reused for another purpose the user did not agree to.

## Who processes it?

- The Platform Risk Research Agent (FastAPI backend, LangGraph pipeline).
- DeepSeek, through Vercel AI Gateway, for reasoning calls.
- OpenAI, for embeddings (`text-embedding-3-small`).
- Pinecone, for vector storage of the RAG corpus.
- Railway, for hosting the backend service.

All four vendors above are US-based.

## Where is the data stored and processed?

- Report data and account data: stored on Railway, US region.
- Embeddings: stored in Pinecone, US region.
- No EU-based storage in place.

Personal data crosses the EU border on every use, when the buyer is in the EU.

## Does the system make or assist in any decision that affects people?

The system scores a vendor, not a person. It does not decide anything about an individual. The recommendation engine ranks alternative vendors when a verdict is negative. This is a business decision, not a decision with legal or similarly significant effect on a person. No automated decision under Article 22 is currently made.

## Confirmation

This system does process personal data: account data, buyer-submitted context, and incidental data pulled from public web research. It does not qualify for the "no personal data" exemption.
