from fastapi import FastAPI, Query
from pydantic import BaseModel
import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Load FAISS index and metadata
# model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")  # ~40MB model
index = faiss.read_index("embeddings/shl_index.faiss")
meta = pd.read_csv("embeddings/shl_meta.csv")

class QueryInput(BaseModel):
    query: str

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/recommend")
def recommend(input: QueryInput, top_k: int = Query(default=10, ge=1, le=10)):
    query_embedding = model.encode([input.query])
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for i in indices[0]:
        row = meta.iloc[i]
        results.append({
    "name": str(row["name"]),
    "url": str(row["url"]),
    "remote": str(row["remote"]),
    "adaptive": str(row["adaptive"]),
    "duration": int(row["duration"]),  # 🔥 FIXED
    "test_type": str(row["test_type"])
})


    return {"results": results}
