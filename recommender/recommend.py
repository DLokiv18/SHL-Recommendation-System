import pandas as pd
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = "data/assessments.csv"
EMB_PATH = "data/embeddings.npy"

df = pd.read_csv(DATA_PATH)

model = SentenceTransformer("all-MiniLM-L6-v2")

if not os.path.exists(EMB_PATH):
    embeddings = model.encode(df["name"].tolist())
    np.save(EMB_PATH, embeddings)
else:
    embeddings = np.load(EMB_PATH)


def recommend(query, top_k=5):
    query_emb = model.encode([query])
    scores = cosine_similarity(query_emb, embeddings)[0]

    top_idx = scores.argsort()[-top_k:][::-1]
    results = df.iloc[top_idx]

    return [
        {
            "name": row["name"],
            "url": row["url"],
            "adaptive_support": "Unknown",
            "description": "SHL assessment",
            "duration": 60,
            "remote_support": "Yes",
            "test_type": ["Knowledge & Skills"]
        }
        for _, row in results.iterrows()
    ]