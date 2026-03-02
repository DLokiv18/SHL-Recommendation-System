from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from recommender.recommend import recommend

import os
import uvicorn

app = FastAPI()


# ✅ ENABLE CORS (Important for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ✅ Request model
class Query(BaseModel):
    query: str


# ✅ Root endpoint
@app.get("/")
def root():
    return {"message": "API Running Successfully 🚀"}


# ✅ Health check endpoint (Render uses this sometimes)
@app.get("/health")
def health():
    return {"status": "healthy"}


# ✅ Recommendation endpoint
@app.post("/recommend")
def get_recommendations(data: Query):
    results = recommend(data.query)
    return {"recommended_assessments": results}


# ⭐ IMPORTANT FOR RENDER DEPLOYMENT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)