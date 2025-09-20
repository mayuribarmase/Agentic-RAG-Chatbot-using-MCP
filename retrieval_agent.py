from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"  

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
