# Oracle ACE Apprentice Contribution Document

# Contribution Title
**OracleGenAI-RAG: Enterprise Knowledge Assistant via OCI Generative AI & Autonomous DB**

# Project Overview
OracleGenAI-RAG is an enterprise AI assistant leveraging OCI Generative AI Service (Cohere Command R+ & Meta Llama 3 foundation models) via official Python OCI SDK, persisting chat conversations and metadata in Oracle Autonomous Database.

# Problem Statement
Enterprises require custom AI knowledge assistants that analyze proprietary documents without compromising data privacy or risking data leakage to public LLM training datasets.

# Solution
The platform connects directly to OCI Generative AI Service hosted inside isolated OCI tenancy clusters. Customer prompts and generated responses are stored safely in Oracle Autonomous Database for auditing.

# Oracle Technologies Used
1. **OCI Generative AI Service:** Fully managed LLM inference service running Cohere Command R+ and Llama 3 models via `oci.generative_ai_inference` SDK.
2. **Oracle Autonomous Database:** Relational database storing chat audit history and model execution latencies.
3. **OCI Object Storage:** Bucket storage for enterprise reference documents.

# GitHub Repository
`https://github.com/vignesh3003/Oracle_ace_apprenticeship/tree/main/Project-4`
