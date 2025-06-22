# 🧠 Smart Career Recommendation Engine

An AI-powered Streamlit web app that analyzes resumes, extracts key skills, matches them with suitable job roles, identifies skill gaps, and recommends relevant online courses. It helps users explore the best career paths based on their current skills.

---

## 🚀 Features

- 📄 Resume parsing (PDF) using `pdfplumber`
- 🧠 Skill extraction and job role matching
- 📚 Course recommendations for missing skills
- 🔍 Upcoming: Job scraping (Naukri, LinkedIn)
- 🤖 Upcoming: AI-generated career path suggestions

---

## 🛠️ Tech Stack

- Python
- Streamlit
- pdfplumber
- Selenium (planned)
- BeautifulSoup (planned)
- Spacy

---

## 📁 Folder Structure

career_recommendation_engine/
│
├── app.py # Streamlit main file
├── resume_parser.py # Extracts resume text
├── skill_matcher.py # Skill matching logic
├── course_recommender.py # Suggests learning resources
├── job_scraper.py # (Coming soon)
├── utils.py # Helper functions
├── requirements.txt
├── assets/
│ └── job_roles_data.json # Predefined roles and required skills
└── resumes/
└── sample_resume.pdf


---

## ▶️ Run the App

```bash
streamlit run app.py
