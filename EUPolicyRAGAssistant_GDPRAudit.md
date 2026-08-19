# Data Processing Brief — EU Policy RAG Assistant

**Purpose:** This document describes the data flows associated with the proposed EU Policy RAG Assistant and is intended to support review by the Data Protection Officer (DPO).

## 1. System overview

The EU Policy RAG Assistant is an internal employee-facing AI system that enables staff to ask questions about EU legislation, policy guidance, and internal compliance documents through a conversational interface. The system retrieves relevant information from a controlled document repository and generates responses based only on approved source material.

The system is intended to reduce routine requests to the policy department and provide employees with faster access to existing information. It is not intended to make decisions on behalf of the organization.

---

## 2. What personal data does the system process?

The system is designed primarily to process organizational policy documents rather than personal data. However, the following personal data may be processed as part of normal operation:

### Employee interaction data

* Employee name or user ID (through Slack or organizational authentication)
* Employee email address or account identifier
* Department/team information where available
* Chat messages and questions submitted by employees

### Text content

* Questions entered by employees
* Conversation history, if retained
* References to named individuals contained in policy documents
* Contact details included in policy documents

### Technical and operational data

* User account information
* Timestamps
* Workflow logs
* Error logs
* API usage logs

### Inferred data

The system does not intentionally create profiles, scores, rankings, or inferred attributes about employees. However, logs may indirectly reveal employee interests, policy concerns, or areas of work based on submitted questions.

No special-category personal data (GDPR Article 9) is intentionally processed as part of the system's intended purpose.

---

## 3. Where does the data come from?

The system receives data from the following sources:

### Employees

Employees submit questions directly through the chat interface.

### Organizational document repositories

Approved policy documents are stored in a designated Google Drive folder and are used as the knowledge base.

### Enterprise systems

User identity information may be obtained through Slack, Google Workspace, or organizational authentication systems.

### System-generated data

Operational logs, retrieval metadata, and usage statistics are generated automatically by the workflow.

The system is not intended to collect personal data from public internet sources or external third-party databases.

---

## 4. What is the data used for?

The system processes data for the following purposes:

1. **Answer employee questions** using approved policy and legislative documents.
2. **Retrieve relevant documents** from the knowledge base.
3. **Generate grounded AI responses** based on retrieved content.
4. **Provide escalation to policy staff** where information is insufficient.
5. **Authenticate users and manage access controls.**
6. **Operate, secure, and troubleshoot the system.**
7. **Monitor system performance and improve retrieval quality.**

The system is not intended to evaluate employees, monitor performance, rank individuals, or make decisions affecting employment.

---

## 5. Who processes the data?

The following parties may process data:

| Entity                          | Role                                  |
| ------------------------------- | ------------------------------------- |
| Client organization             | Controller / system owner             |
| Employees                       | End users                             |
| Policy department               | Human reviewers and content owners    |
| n8n                             | Workflow orchestration                |
| OpenAI                          | Language model provider (if API used) |
| Pinecone                        | Vector database provider              |
| Google Drive / Google Workspace | Document storage                      |
| Slack                           | User interface and messaging platform |
| IT administrators               | System support and maintenance        |

If OpenAI API services are used, employee questions and retrieved document content may be sent to OpenAI for response generation. If local models are deployed in future, this data flow may change.

---

## 6. Where is the data stored and processed?

Data may be stored and processed in several locations depending on the final architecture:

* **Google Drive:** Policy documents
* **Pinecone:** Vectorized document chunks and metadata
* **n8n:** Workflow execution and logs
* **Slack:** User messages
* **OpenAI:** Model processing (if API architecture is used)

Processing may occur in the EU or outside the EU depending on vendor hosting arrangements. International transfers and transfer mechanisms should be reviewed before production deployment.

---

## 7. Does the system make or assist decisions affecting people?

The system does **not make automated decisions about individuals**.

The system assists employees by retrieving information and generating answers to policy questions. Responses are intended as informational support only.

Where the system cannot provide sufficient information, users are directed to the policy department for human support.

Policy specialists review system quality during implementation and remain responsible for authoritative interpretation of legislation and organizational policy.

---

## 8. Summary

The EU Policy RAG Assistant is an internal knowledge-retrieval system that processes employee questions and organizational policy documents to provide faster access to information.

The principal data protection considerations are:

* Processing of employee chat content
* Potential personal data contained in policy documents
* Use of third-party AI and cloud services
* International data transfers
* Logging and retention
* Access controls

The system is not intended to profile employees or make decisions affecting their rights, employment, or access to services.
