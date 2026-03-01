import sys
import os

# ⭐ ADD PROJECT ROOT TO PYTHON PATH (GUARANTEED FIX)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from recommender.recommend import recommend
import pandas as pd


queries = [
    "Java developer",
    "Python developer",
    "Software engineer",
    "Personality test",
    "Cognitive ability test"
]

rows = []

for q in queries:
    results = recommend(q)

    for r in results:
        rows.append({
            "Query": q,
            "Assessment_url": r["url"]
        })

df = pd.DataFrame(rows)
df.to_csv("submission.csv", index=False)

print("submission.csv created!")