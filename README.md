# Agentic RAG Chatbot (MCP)

A modular Retrieval-Augmented Generation chatbot that answers user questions from multiple document formats (PDF, DOCX, PPTX, CSV, TXT, MD).  
Built using an agent-based architecture with Model Context Protocol (MCP) for message passing.

***

## Features

- **Multi-format document QA:** PDF, DOCX, PPTX, TXT, CSV, MD
- **Agentic pipeline:**
  - **IngestionAgent:** Parses and preprocesses the uploaded file.
  - **RetrievalAgent:** Splits and indexes the document, retrieves top chunks for a question.
  - **LLMResponseAgent:** Calls LLM API (Google Gemini preferred) to answer from context.
- **Model Context Protocol (MCP):**  
  All agent messages structured with sender, receiver, type, trace_id, and payload.
- **Interactive UI:** Built with Streamlit for uploading, asking, and getting answers with context.

***

## Architecture

```mermaid
flowchart LR
    subgraph Agents
    IngestionAgent --> RetrievalAgent --> LLMResponseAgent
    end
    User -. Upload .-> IngestionAgent
    User <-. Answer .- LLMResponseAgent
```

- Each arrow represents an MCP message.  
  Example MCP message:
  ```json
  {
    "sender": "RetrievalAgent",
    "receiver": "LLMResponseAgent",
    "type": "CONTEXT_RESPONSE",
    "trace_id": "abc-123",
    "payload": { "top_chunks": ["..."], "query": "..." }
  }
  ```

***

## Tech Stack

- **UI:** Streamlit
- **Language:** Python 3.12+
- **LLM:** Google Gemini (`google-generativeai`), (Hugging Face/OpenAI optional)
- **Parsing:** PyMuPDF, python-docx, markdown, csv, etc.

***

## Quick Start

1. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Add your Google Gemini API key** in `llm_response_agent.py`.
3. **Run:**
   ```bash
   streamlit run app.py
   ```
4. **Use:** Upload a doc, ask questions, see answers and context.

***

## UI Preview

- Upload document, ask questions.
- Answers are LLM-backed and always grounded in document content.
- Click “See relevant source chunks” for transparency.

***

## Challenges

- Switching LLM APIs (Hugging Face failures, switched to Gemini).
- Parsing various document formats reliably.
- Ensuring temp file cleanup.
- Harmonizing agent communication via MCP.

***

## Future Scope

- Add conversational memory and chat history.
- Use real vector database for semantic retrieval.
- Add support for more LLM providers.

***

**MIT License**  
**Author:** Mayuri Lukman Barmase

***