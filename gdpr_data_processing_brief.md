# TenderAI Assistant — GDPR Data Processing Brief

**Project:** TenderAI — Enterprise RAG AI Assistant
**Audit:** GDPR Lens — Project 3
**Document:** Data Processing Brief
**Date:** 19 August 2026
**Status:** Pre-audit inventory

---

## 1. System Overview

TenderAI is an enterprise RAG (Retrieval-Augmented Generation) assistant designed to help organisations analyse tenders and prepare evidence-based tender responses.

The system ingests enterprise documents, extracts and chunks their content, creates vector embeddings, stores those embeddings in a vector database, retrieves relevant evidence in response to a tender requirement, and uses an LLM to generate an assessment or draft response based on the retrieved evidence.

The current MVP includes:

* PDF document ingestion
* PDF text extraction
* Document chunking
* OpenAI embeddings
* Pinecone vector storage
* Semantic retrieval
* Tender requirement analysis
* Evidence-based compliance assessment
* Draft tender-response generation
* Report generation
* A Streamlit user interface

The current test knowledge base uses synthetic company documents created for the project.

---

# 2. Does TenderAI Process Personal Data?

## Current MVP

The current TenderAI MVP has been tested using synthetic company documents such as:

* Company Profile
* ISO Compliance and Certifications
* Renewable Energy Project References
* Technical Capabilities
* Tender Response Guidelines

These documents were created for demonstration and testing purposes and are not intended to contain real individuals' personal data.

Therefore, based on the current test dataset, the MVP does not intentionally process meaningful real-world personal data.

## Production Scenario

The system is nevertheless designed to process documents supplied by an enterprise client.

Those documents could contain personal data about employees, consultants, clients, suppliers, project personnel, or other identifiable individuals.

Examples could include:

* Names
* Professional email addresses
* Business telephone numbers
* Job titles
* Professional biographies
* CV information
* Employment history
* Project responsibilities
* Contact details
* Text written by or about identifiable individuals

Therefore, the GDPR audit must assess the system's ability to process personal data in a real client deployment even though the current MVP uses synthetic data.

**Conclusion: GDPR is relevant to the intended production deployment because the system may process personal data contained in client-provided enterprise documents.**

---

# 3. Personal Data Processed

The categories of personal data that TenderAI could process include:

### Identification and contact information

* Name
* Professional email address
* Business telephone number
* Other contact information contained in documents

### Professional information

* Job title
* Employer/company affiliation
* Professional role
* Employment history
* Professional experience
* Qualifications
* Certifications
* Project responsibilities
* Professional biography

### Text content

TenderAI may process free-text content contained in uploaded documents.

This could include text written by an identifiable person or information describing an identifiable person.

### AI-generated or derived information

Depending on the document and query, the system may generate:

* Extracted text
* Document chunks
* Vector embeddings
* Retrieved passages
* Tender requirement assessments
* Evidence summaries
* Draft responses

These outputs must be assessed to determine whether they contain or remain linked to personal data.

---

# 4. Sources of the Data

The primary source of information is documentation supplied by the client or authorised users.

Potential sources include:

* Client-uploaded PDF documents
* Company profiles
* Project references
* Technical capability documents
* Tender documents
* Certifications
* Compliance documentation
* Tender-response guidelines
* Other enterprise documentation

The current MVP's documents are synthetic and were created specifically for testing.

The production system may therefore receive personal data directly from client users or indirectly through documents originally collected by the client from employees, consultants, clients, suppliers, or other third parties.

---

# 5. Purposes of Processing

TenderAI processes uploaded information for several distinct purposes.

## Purpose 1 — Document ingestion

Documents are uploaded and processed so that their content can be made available to the TenderAI knowledge base.

## Purpose 2 — Knowledge-base creation

Documents are extracted, split into chunks, embedded, and stored in a vector database so that relevant information can later be retrieved.

## Purpose 3 — Tender requirement analysis

Tender requirements are analysed against information retrieved from the client's knowledge base.

## Purpose 4 — Evidence retrieval

The system retrieves relevant passages from the knowledge base to support an assessment.

## Purpose 5 — AI-assisted response generation

The LLM uses retrieved evidence to generate draft tender responses and other requested outputs.

## Purpose 6 — Reporting

The system can produce structured assessments and reports that can be reviewed and used by the client's team.

### Purpose limitation consideration

Personal data contained in enterprise documents should only be processed for documented purposes compatible with the client's original purpose for collecting the data.

The system should not assume that information uploaded for one business purpose can automatically be reused for unrelated AI processing.

**Assessment: TBD — legal review for production deployments.**

---

# 6. Who Processes the Data?

The principal components/entities involved in the processing flow are:

### Client organisation

The client supplies the enterprise documents and determines the business purpose for using TenderAI.

The client's exact GDPR role must be confirmed for each deployment.

### TenderAI application

The TenderAI application performs:

* Document ingestion
* Text extraction
* Chunking
* Retrieval
* Tender analysis
* Response generation
* Report generation

### OpenAI

OpenAI services are used in the current architecture for:

* Text embeddings
* Large-language-model processing

Candidate or client documents may therefore be transmitted to the relevant OpenAI service when the application performs embedding or LLM processing.

The precise contractual role, applicable service terms, data-processing terms, retention settings, and processing locations must be verified for the production configuration.

**Assessment: TBD — legal review.**

### Pinecone

Pinecone is used as the vector database/retrieval infrastructure.

The application sends document embeddings and associated metadata to Pinecone for storage and retrieval.

The exact production configuration, region, retention settings, subprocessors, and contractual role must be verified.

**Assessment: TBD — legal review.**

---

# 7. Data Flow

The current architecture can be represented as:

**Client documents**

↓

**TenderAI document ingestion**

↓

**PDF text extraction**

↓

**Text chunking**

↓

**OpenAI embedding generation**

↓

**Pinecone vector database**

↓

**User submits tender requirement**

↓

**TenderAI semantic retrieval**

↓

**Retrieved evidence**

↓

**OpenAI LLM processing**

↓

**Tender assessment / draft response**

↓

**Human review by client team**

↓

**Optional report generation**

---

# 8. Storage and Processing Locations

TenderAI does not currently operate entirely on local infrastructure.

The architecture uses external cloud services for AI processing and vector storage.

The relevant external services are:

* OpenAI
* Pinecone

The exact geographic processing and storage locations used by the production configuration have not yet been documented in this project.

It is therefore not currently possible to conclude from the project files alone whether all personal-data processing remains within the EEA.

**Assessment: TBD — legal review.**

The following information must be confirmed before a production GDPR assessment can be finalised:

* OpenAI processing location
* Pinecone storage region
* Relevant subprocessors
* Applicable data-processing terms
* Whether data is transferred outside the EEA
* Applicable transfer mechanism
* Retention/deletion arrangements

---

# 9. International Transfers

The current project documentation does not establish whether personal data processed through OpenAI or Pinecone leaves the EEA.

Therefore:

**International transfer status: TBD — legal review.**

If personal data is transferred outside the EEA, the applicable GDPR Chapter V mechanism must be identified, such as:

* Adequacy decision
* Standard Contractual Clauses (SCCs)
* Another legally recognised transfer mechanism, where applicable

The transfer assessment must also consider the relevant provider, processing location, subprocessors, and contractual safeguards.

---

# 10. Does TenderAI Make Decisions About People?

## Current MVP

TenderAI does not currently make decisions about individuals such as:

* Hiring decisions
* Credit decisions
* Insurance decisions
* Eligibility decisions
* Employee performance decisions

The system's primary function is to analyse enterprise documentation and support tender/proposal work.

Its outputs concern tender requirements and company evidence.

Examples include:

* Supported
* Partially supported
* Insufficient
* Evidence supporting an assessment
* Missing information
* Relevant project references
* Draft tender responses

## Human Review

TenderAI outputs are intended to be reviewed by the client team before being used in a tender, proposal, or other business deliverable.

Therefore, the current project does not appear to make automated decisions with legal or similarly significant effects on individuals.

**Assessment: No current Article 22 use case identified in the MVP. TBD — reassess if the system is later extended to make decisions about identifiable individuals.**

---

# 11. Special-Category Data — Initial Assessment

The current synthetic MVP does not intentionally contain Article 9 special-category personal data.

However, production enterprise documents could potentially contain or reveal special-category information.

Examples could include information relating to:

* Health
* Disability
* Racial or ethnic origin
* Religious or philosophical beliefs
* Trade-union membership
* Political opinions
* Sexual orientation
* Biometric data used for identification

The RAG system could also reproduce or summarise such information if it exists in uploaded documents.

**Assessment: TBD — legal review for production data.**

The client should determine whether Article 9 data can enter the knowledge base and whether technical controls are required to prevent unnecessary processing.

---

# 12. Initial GDPR Risk Areas

The data-processing brief identifies the following areas for the subsequent GDPR audit:

1. Lawful basis for processing client-provided documents containing personal data.
2. Purpose limitation and compatibility of AI processing with the client's original purpose.
3. Data minimisation.
4. Controller/processor allocation.
5. Data Processing Agreements with external providers.
6. International transfers.
7. Retention and deletion.
8. Data-subject rights.
9. Security and access controls.
10. Potential Article 9 special-category data.
11. AI-generated or derived information containing personal data.
12. Accountability and documentation.

---

# 13. Initial Conclusion

The current TenderAI MVP has been developed and tested using synthetic enterprise documents and therefore presents limited immediate GDPR exposure in its current test configuration.

However, the intended production system is capable of processing personal data contained in client enterprise documents.

The GDPR assessment must therefore focus on the production data flow rather than treating the current synthetic test data as proof that GDPR is irrelevant.

The most important unresolved questions before production deployment concern:

* lawful basis,
* controller/processor roles,
* DPAs,
* international transfers,
* retention,
* data-subject rights,
* potential Article 9 data,
* and accountability documentation.

**Status: Kick-off data processing brief complete. Ready for Phase 1 — Personal Data Inventory.**
