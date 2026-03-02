from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import os
import uvicorn
import sys

# ⭐ FIX MODULE PATH FOR RENDER
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from recommender.recommend import recommend

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "API Running Successfully 🚀"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recommend")
def get_recommendations(data: Query):
    results = recommend(data.query)
    return {"recommended_assessments": results}

# ⭐ For local run only
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
