from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from recommender.recommend import recommend

app = FastAPI()

# ⭐ ENABLE CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow all origins
    allow_credentials=True,
    allow_methods=["*"],      # allow POST, GET, OPTIONS etc.
    allow_headers=["*"],
)

class Query(BaseModel):
    query: str


@app.get("/")
def root():
    return {"message": "API Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/recommend")
def get_recommendations(data: Query):
    results = recommend(data.query)
    return {"recommended_assessments": results}