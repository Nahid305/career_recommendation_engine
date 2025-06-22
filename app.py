# app.py
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import time
from resume_parser import extract_text_from_pdf
from utils import extract_skills
from skill_matcher import match_skills
from course_recommender import suggest_courses
from job_scraper import get_jobs_for_role
from ats_checker import get_ats_score_and_feedback
from resume_templates import get_resume_template
from cover_letter_generator import generate_cover_letter
from interview_helper import get_interview_questions, get_preparation_links
from career_chatbot import ask_career_bot

try:
    from streamlit_lottie import st_lottie
    LOTTIE_ENABLED = True
except ImportError:
    st.warning("streamlit_lottie not installed")
    LOTTIE_ENABLED = False

# App Config
st.set_page_config(page_title="CareerCraft AI", layout="wide", page_icon="🚀")

@st.cache_data(show_spinner=False)
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Resume Templates
RESUME_TEMPLATES = {
    "Modern": {
        "image": "https://images.ctfassets.net/pdf29us7flmy/6J0QOogqkXhQ0QJXUJ7h6x/5c7f1a5e5e5e5e5e5e5e5e5e5e5e5e/modern-resume-template.png",
        "download": "https://example.com/modern-template.pdf"
    },
    "Professional": {
        "image": "https://images.ctfassets.net/pdf29us7flmy/6J0QOogqkXhQ0QJXUJ7h6x/5c7f1a5e5e5e5e5e5e5e5e5e5e5e5e/professional-resume-template.png",
        "download": "https://example.com/professional-template.pdf"
    },
    "Creative": {
        "image": "https://images.ctfassets.net/pdf29us7flmy/6J0QOogqkXhQ0QJXUJ7h6x/5c7f1a5e5e5e5e5e5e5e5e5e5e5e5e/creative-resume-template.png",
        "download": "https://example.com/creative-template.pdf"
    }
}

# Header
if LOTTIE_ENABLED:
    lottie = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
    if lottie:
        st_lottie(lottie, height=180, key="career-header")

st.markdown("""
<div style='text-align:center'>
  <h1 style='color:#4A90E2;'>🚀 CareerCraft AI</h1>
  <p style='font-size:1.2em;'>Smart Career Recommendation Engine Powered by AI</p>
</div>
""", unsafe_allow_html=True)

# Input
st.markdown("---")
st.subheader("📄 Upload Resume or Paste LinkedIn Summary")
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
with col2:
    linked_text = st.text_area("Or paste your LinkedIn 'About' section")

# Processing
if uploaded_file or linked_text:
    text = extract_text_from_pdf(uploaded_file) if uploaded_file else linked_text
    user_skills = extract_skills(text)

    if not user_skills:
        st.warning("⚠️ No skills detected.")
    else:
        st.markdown("### ✅ Extracted Skills")
        for skill in user_skills:
            st.markdown(
                f"<span style='background:#4A90E2;color:white;padding:6px 12px;border-radius:25px;display:inline-block;margin:4px;'>{skill}</span>",
                unsafe_allow_html=True
            )

        st.markdown("---")
        st.subheader("📊 Multi-Role Skill Comparison")

        roles = ["Data Analyst", "Backend Developer", "ML Engineer"]
        best_role = ""
        best_score = 0
        scores = {}

        for role in roles:
            matched, missing, score = match_skills(user_skills, role)
            scores[role] = score
            if score > best_score:
                best_score = score
                best_role = role

        for role in roles:
            st.write(f"🎯 **{role}** - {scores[role]}%")
            st.progress(scores[role] / 100)

        st.info(f"🧠 Best Fit Role: **{best_role}**")

        # Resume Audit
        st.markdown("---")
        st.subheader("📋 Resume Audit Summary")
        ats_score, feedback = get_ats_score_and_feedback(text, best_role)
        st.metric("⭐ ATS Score", f"{ats_score}/5")
        for f in feedback:
            st.markdown(f"- ❗ {f}")

        # Course Recommender
        st.subheader("📚 Recommended Courses")
        _, missing, _ = match_skills(user_skills, best_role)
        if missing:
            for skill in missing:
                st.markdown(f"- **{skill}** → [Course]({suggest_courses(skill)})")
        else:
            st.success("🎉 You have all required skills!")

        # Job Listings
        st.subheader("💼 Job Listings")
        location = st.text_input("📍 Filter by location (optional)")
        jobs = get_jobs_for_role(best_role)
        if location:
            jobs = [j for j in jobs if location.lower() in j.get("location", "").lower()]
        df = pd.DataFrame(jobs)
        if not df.empty:
            st.dataframe(df[["title", "company", "location", "link"]])
            csv = df.to_csv(index=False).encode()
            st.download_button("📥 Download Job List (CSV)", csv, "job_list.csv")
        else:
            st.warning("No jobs found.")

        # Resume Templates (Fixed)
        st.markdown("---")
        st.subheader("🖼️ Resume Templates")
        cols = st.columns(len(RESUME_TEMPLATES))
        items = list(RESUME_TEMPLATES.items())
        for i in range(len(items)):
            label, template = items[i]
            with cols[i]:
                st.image(template["image"], caption=label, use_container_width=True)
                st.markdown(
                    f"<div style='text-align:center; margin-top:-10px;'>"
                    f"<a href='{template['download']}' target='_blank'>"
                    f"<button style='background:#4A90E2; color:white; padding:8px 16px; border:none; border-radius:6px;'>📥 Download</button>"
                    f"</a></div>",
                    unsafe_allow_html=True
                )

        # Cover Letter
        st.markdown("---")
        if st.checkbox("✉️ Need a Cover Letter?"):
            name = st.text_input("Your Name")
            company = st.text_input("Company Name")
            if name and company:
                letter = generate_cover_letter(name, best_role, company)
                st.text_area("Suggested Cover Letter", letter, height=250)

        # Career Path Generator
        if st.button("🧠 Generate Career Plan"):
            prompt = f"Generate a 6-month and 3-year career roadmap for someone with skills {', '.join(user_skills)} targeting {best_role}."
            with st.spinner("Thinking..."):
                path = ask_career_bot(prompt)
                st.markdown("### 📈 Your Career Roadmap")
                st.markdown(path)

        # Interview Prep
        st.markdown("---")
        st.subheader("🎤 Interview Prep")
        questions = get_interview_questions(best_role)
        st.markdown("**Common Questions:**")
        for q in questions:
            st.markdown(f"- {q}")
        st.markdown("🔗 Useful Links:")
        for label, url in get_preparation_links(best_role).items():
            st.markdown(f"- [{label}]({url})")

        # CareerBot Chat
        st.markdown("---")
        st.subheader("🤖 CareerBot Q&A")
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_question = st.text_input("Ask CareerBot anything...")
        if user_question:
            with st.spinner("CareerBot is typing..."):
                response = ask_career_bot(user_question)
                st.session_state.chat_history.append(("You", user_question))
                st.session_state.chat_history.append(("CareerBot", response))

        for role, msg in st.session_state.chat_history:
            st.markdown(f"**{role}:** {msg}")

        if st.session_state.chat_history:
            chat_text = "\n".join([f"{r}: {m}" for r, m in st.session_state.chat_history])
            st.download_button("🧾 Download Chat", chat_text.encode(), "chat_history.txt")

else:
    st.info("📂 Please upload a resume or paste your LinkedIn summary to begin.")
