# app.py
import streamlit as st
from resume_parser import extract_text_from_pdf
from utils import extract_skills
from skill_matcher import match_skills
from course_recommender import suggest_courses

st.title("🧠 Smart Career Recommendation Engine")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    user_skills = extract_skills(text)
    st.success(f"✅ Skills Extracted: {', '.join(user_skills)}")

    role = st.selectbox("Choose Target Role", ["Data Analyst", "Backend Developer", "ML Engineer"])

    matched, missing, match_percent = match_skills(user_skills, role)
    st.info(f"🎯 Skill Match for {role}: {match_percent}%")
    st.write("✅ Matched Skills:", matched)
    st.write("❌ Missing Skills:", missing)

    st.subheader("📚 Recommended Courses for Missing Skills")
    for skill in missing:
        st.markdown(f"- **{skill}**: [Click here]({suggest_courses(skill)})")

