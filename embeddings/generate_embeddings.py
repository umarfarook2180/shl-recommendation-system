import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load metadata
df = pd.read_csv("embeddings/shl_meta.csv")

# Use only the assessment name for embeddings
texts = df["name"].astype(str).tolist()

# Load sentence transformer
print("🔍 Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
print("🔧 Generating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

# Save vector index
np.save("embeddings/shl_vectors.npy", embeddings)
faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
faiss_index.add(embeddings)
faiss.write_index(faiss_index, "embeddings/shl_index.faiss")

# Confirm
print(f"✅ Saved FAISS index and vectors for {len(texts)} assessments.")
