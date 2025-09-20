# retrieval_agent.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Choose the best open model as of 2025
EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"  # Or "intfloat/e5-base-v2", "nomic-ai/nomic-embed-text-v1"

class RetrievalAgent:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.index = None
        self.documents = []
        self.embeddings = []

    def build_knowledge_base(self, doc_chunks):
        self.documents = doc_chunks
        self.embeddings = self.model.encode(doc_chunks, convert_to_numpy=True)
        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)

    def retrieve(self, query, top_k=3):
        query_emb = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_emb, top_k)
        result = [self.documents[i] for i in indices[0]]
        return result

# Example usage:
# agent = RetrievalAgent()
# agent.build_knowledge_base(["some text", "other doc"])
# print(agent.retrieve("some query"))
