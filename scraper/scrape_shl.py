import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

os.makedirs("data", exist_ok=True)

base_url = "https://www.shl.com"
headers = {"User-Agent": "Mozilla/5.0"}

assessments = []

# Crawl multiple pages
for page in range(1, 15):   # increase if needed
    url = f"https://www.shl.com/solutions/products/product-catalog/?start={page*12}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.select("a[href*='/products/']"):
        name = a.get_text(strip=True)
        link = a["href"]

        if name:
            assessments.append({
                "name": name,
                "url": base_url + link
            })

    print("Scraped page", page)
    time.sleep(1)  # polite delay

df = pd.DataFrame(assessments).drop_duplicates()

df.to_csv("data/assessments.csv", index=False)

print("Saved", len(df), "assessments")