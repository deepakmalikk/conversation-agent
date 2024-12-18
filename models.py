# Pydantic models   
from pydantic import BaseModel

class QueryResponse(BaseModel):
    query: str
    response: str
    embedding: list[float]