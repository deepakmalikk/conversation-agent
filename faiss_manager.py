 # FAISS management     
import faiss
import numpy as np
from models import QueryResponse

class FAISSManager:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.mapping = {}  # Maps index IDs to QueryResponse objects
        self.next_id = 0

    def add_record(self, query_response: QueryResponse):
        embedding = np.array([query_response.embedding], dtype=np.float32)
        self.index.add(embedding)
        self.mapping[self.next_id] = query_response
        self.next_id += 1

    def search(self, embedding: list[float], k: int = 5):
        embedding_np = np.array([embedding], dtype=np.float32)
        distances, indices = self.index.search(embedding_np, k)
        return distances[0], indices[0]

    def get_related_queries(self, embedding: list[float], threshold: float, k: int = 5):
        distances, indices = self.search(embedding, k)
        related = [
            self.mapping[idx] for idx, dist in zip(indices, distances) if dist < threshold
        ]
        return related