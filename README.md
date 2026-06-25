# AI Resume Screening System

# 🤖 AI Resume Screening System  
### 🧠 Intelligent Resume Analysis & Candidate Ranking Using Artificial Intelligence


<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/NLP-Natural%20Language%20Processing-green?style=for-the-badge">

<img src="https://img.shields.io/badge/Machine%20Learning-Classification-orange?style=for-the-badge">

<img src="https://img.shields.io/badge/AI-Resume%20Analyzer-purple?style=for-the-badge">

</p>


<p align="center">
An AI-powered system that automatically analyzes resumes, extracts skills, and ranks candidates based on job requirements.
</p>


---

# 🚀 Project Overview


Recruiters often receive hundreds of resumes for a single job opening, making manual screening slow and inefficient.

This project uses **Artificial Intelligence and Natural Language Processing (NLP)** to automate resume screening.


The system can:

✅ Extract important information from resumes  
✅ Identify candidate skills  
✅ Compare resumes with job descriptions  
✅ Calculate candidate matching score  
✅ Rank candidates based on suitability  


---

# 🎯 Business Problem


### Traditional Hiring Challenges:


❌ Manual resume screening takes time  
❌ Important candidates may be missed  
❌ Large applications are difficult to analyze  
❌ Recruitment process becomes inefficient  


### AI-Based Solution:


An intelligent screening system that helps recruiters quickly identify the most suitable candidates.


---

# 💡 How It Works


```
                Resume Files

                     ↓

          Resume Text Extraction

                     ↓

              Text Cleaning

                     ↓

        NLP Feature Extraction

                     ↓

      Resume & Job Description Matching

                     ↓

          Candidate Ranking Score

                     ↓

           Shortlisted Candidates

```


---

# 🧠 AI Approach


This project uses **Natural Language Processing (NLP)** techniques.


## Main Techniques:


### 📄 Text Extraction

Extracts text from resume documents.


### 🧹 Text Preprocessing

Includes:

- Lowercasing
- Removing unnecessary characters
- Tokenization
- Stopword removal


### 🔢 Feature Extraction


Converts text into numerical vectors using:


- TF-IDF Vectorization
- Word Embeddings


### 📐 Similarity Matching


Uses similarity algorithms to compare:


```
Resume Skills

        VS

Job Description Requirements

```


---

# 🛠️ Tech Stack


## 👨‍💻 Programming Language

🐍 Python


## 📚 Libraries


| Purpose | Libraries |
|---|---|
| Data Processing | Pandas, NumPy |
| NLP | NLTK, spaCy |
| Machine Learning | Scikit-learn |
| File Processing | PyPDF2 |
| Visualization | Matplotlib |


---

# 📂 Project Structure


```
AI-Resume-Screening-System

│
├── 📄 resume_screening.py
│
├── 📁 resumes
│     ├── resume1.pdf
│     ├── resume2.pdf
│
├── 📄 job_description.txt
│
├── 📄 requirements.txt
│
├── 📘 README.md
│
└── 📸 output.png

```


---

# 📊 Input Data


## Resume


Example:


```
Name:
John Smith


Skills:

Python
Machine Learning
SQL
Deep Learning

Experience:

2 Years Data Science Experience

```



## Job Description


Example:


```
Required Skills:

Python
SQL
Machine Learning
NLP

Experience:

Data Scientist

```


---

# ⚙️ Project Workflow


## 1️⃣ Resume Upload


Users upload candidate resumes in PDF format.


---

## 2️⃣ Text Extraction


The system extracts text from resumes automatically.


Example:


```
PDF Resume

      ↓

Extracted Text

      ↓

NLP Processing

```


---

## 3️⃣ Skill Extraction


The model identifies important skills:


Example:


```
Python
SQL
Machine Learning
AWS
NLP

```


---

## 4️⃣ Resume Matching


The system compares:


```
Candidate Resume

        +

Job Description


        ↓


Matching Score

```


---

# 📈 Sample Output


### Job Role:

```
Data Scientist

```


### Candidate Ranking:


| Candidate | Match Score |
|---|---|
| Candidate A | 92% |
| Candidate B | 84% |
| Candidate C | 71% |



Prediction:


```
🏆 Candidate A Recommended For Interview

```


---

# 📸 Output Screenshot


Add your actual output screenshot:


```markdown
![Output](output.png)

```


---

# 🏆 Skills Demonstrated


```
🐍 Python Programming

🧠 Natural Language Processing

📄 Text Processing

🔍 Feature Extraction

🤖 Machine Learning

📊 Data Analysis

⚙️ AI Automation

```


---

# 🚀 Future Enhancements


🔹 Use Large Language Models (LLMs)  
🔹 Add AI interview question generation  
🔹 Build resume improvement suggestions  
🔹 Add skill gap analysis  
🔹 Create recruiter dashboard  
🔹 Deploy using Streamlit/FastAPI  
🔹 Integrate with job portals  


---

# 🌍 Real-World Applications


This system can be used in:


💼 Recruitment Platforms

🏢 HR Departments

🎓 Campus Placement Systems

🔎 Job Search Applications

👥 Talent Management Systems


---

# 👨‍💻 Author


**Your Name**


GitHub:

```
https://github.com/yourusername

```


---

# ⭐ Support


If you found this project useful, consider giving it a ⭐ on GitHub!
