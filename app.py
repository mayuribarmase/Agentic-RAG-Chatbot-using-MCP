# app.py

import streamlit as st
from ingestion_agent import ingest_document
from retrieval_agent import RetrievalAgent
from llm_response_agent import LLMResponseAgent

@st.cache_data(show_spinner=False)
def process_file(uploaded_file):
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())
    text = ingest_document(temp_path)
    return text, temp_path

def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

st.title("Agentic RAG Chatbot")

hf_token = "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"

uploaded_file = st.file_uploader("Upload your document (PDF/DOCX/PPTX/CSV/TXT/MD)", type=['pdf', 'docx', 'pptx', 'csv', 'txt', 'md'])

if uploaded_file and hf_token:
    with st.spinner("Processing document..."):
        full_text, temp_path = process_file(uploaded_file)
        text_chunks = chunk_text(full_text)
        retriever = RetrievalAgent()
        retriever.build_knowledge_base(text_chunks)
        llm_agent = LLMResponseAgent()
        st.success("Document indexed. Ask your question below.")

    user_question = st.text_input("Ask your question about the document:")
    if user_question:
        top_chunks = retriever.retrieve(user_question, top_k=3)
        with st.spinner("Generating answer..."):
            answer = llm_agent.generate_answer(user_question, top_chunks)
        st.markdown("**Answer:**")
        st.write(answer)
        with st.expander("See relevant source chunks"):
            for i, chunk in enumerate(top_chunks):
                st.write(f"**Chunk {i+1}:** {chunk}")


    import os
    if 'temp_path' in locals():
        try:
            os.remove(temp_path)
        except FileNotFoundError:
            pass

elif not hf_token:
    st.info("Please enter your Hugging Face token to use the LLM for answering.")

