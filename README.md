# SHL Assessment Recommendation System

##  Overview

This project implements an AI-powered recommendation system that suggests relevant SHL assessments based on a job role or skill query.

It uses Natural Language Processing (NLP) and semantic similarity to match user input with assessments from SHL’s product catalogue.

---

##  Problem Statement

Selecting appropriate assessments for candidates based on job requirements is time-consuming. This system automates the process by recommending the most relevant SHL assessments for a given query.

---

##  Approach

1. Scraped assessment data from SHL product catalogue  
2. Generated semantic embeddings for assessment titles  
3. Used Sentence Transformers to understand query meaning  
4. Calculated similarity between query and assessments  
5. Returned top relevant recommendations  

---

##  Model Used

**Sentence Transformers — all-MiniLM-L6-v2**

Reasons for selection:

- Lightweight and fast  
- Strong semantic understanding  
- Suitable for real-time systems  
- Pretrained on large datasets  

Similarity Metric:

**Cosine Similarity**

---

##  Dataset

Assessment information was collected from SHL’s public catalogue.

Dataset contains ~400 assessments with:

- Name  
- URL  
- Duration  
- Test type  
- Remote support  

Stored in:

data/assessments.csv

---

##  System Architecture

User → Frontend → FastAPI → AI Model → Recommendations

---

##  Features

- AI-based semantic search  
- Fast recommendation engine  
- REST API using FastAPI  
- Interactive web interface  
- Evaluation output generation  

---

##  How to Run

### 1️ Install dependencies

pip install -r requirements.txt

### 2️ Run backend server

uvicorn api.main:app --reload

Open API docs:

http://127.0.0.1:8000/docs

### 3️ Run frontend

Open:

frontend/index.html

in your browser.

---

##  Evaluation Output

Generate submission file:

python evaluation/generate_submission.py

This creates:

submission.csv

---

##  Example Query

Input: Java developer  

Output: Relevant Java-related SHL assessments

---

##  Project Structure

SHL-Recommendation-System/
 ├── api/
 ├── recommender/
 ├── scraper/
 ├── data/
 ├── frontend/
 ├── evaluation/
 ├── submission.csv
 ├── requirements.txt
 └── README.md

---

##  Future Improvements

- Use assessment descriptions for better accuracy  
- Add filtering options  
- Deploy as public web application  
- Hybrid recommendation methods  

---

## Author

Lokesh  
B.Tech Computer Science Engineering  
AI / Software Engineering Enthusiast  

---

## License

Developed for educational and evaluation purposes.