# app.py - Enhanced but compatible version
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import time
import json
import os
from datetime import datetime

# Import enhanced modules
from resume_parser import extract_text_from_pdf
from utils import extract_skills, get_skills_by_category
from skill_matcher import match_skills, get_detailed_skill_analysis
from course_recommender import suggest_courses
from job_scraper import get_jobs_for_role, search_jobs_with_filters, search_jobs_by_skills, get_trending_jobs, get_job_market_stats
from ats_checker import get_ats_score_and_feedback
from resume_templates import get_resume_template
from cover_letter_generator import generate_cover_letter
from interview_helper import get_interview_questions, get_preparation_links, get_interview_tips
from career_chatbot import ask_career_bot
from ui_styles import apply_custom_css, create_job_card, create_feature_highlight, create_status_indicator

try:
    from streamlit_lottie import st_lottie
    LOTTIE_ENABLED = True
except ImportError:
    st.warning("streamlit_lottie not installed. Install with: pip install streamlit-lottie")
    LOTTIE_ENABLED = False

# App Config
st.set_page_config(
    page_title="🚀 CareerCraft AI - Smart Career Recommendation Engine",
    layout="wide",
    page_icon="🚀",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #4A90E2, #7B68EE);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    .skill-tag {
        background: #4A90E2;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.8rem;
    }
    .warning-box {
        background: #FFF3CD;
        border: 1px solid #FFEAA7;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .success-box {
        background: #D4EDDA;
        border: 1px solid #C3E6CB;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def load_lottie_url(url):
    """Load Lottie animation from URL"""
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def main():
    """Main application function"""
    # Apply custom CSS
    apply_custom_css()
    
    # Header with animation
    if LOTTIE_ENABLED:
        lottie_career = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
        if lottie_career:
            st_lottie(lottie_career, height=150, key="career-header")
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Navigation")
        page = st.selectbox(
            "Choose a section:",
            ["🏠 Home", "📄 Resume Analysis", "💼 Job Matching", "📚 Skills & Courses", "📈 Career Planning", "🚀 Advanced Features", "🤖 AI Assistant"],
            key="navigation_selectbox"
        )
        
        st.markdown("---")
        st.markdown("### 📊 Status")
        
        # Check if skills are loaded
        if 'user_skills' in st.session_state:
            st.success(f"✅ Skills loaded: {len(st.session_state.user_skills)} skills")
            if 'best_role' in st.session_state:
                st.info(f"🎯 Best match: {st.session_state.best_role}")
        else:
            st.warning("⚠️ Upload your resume to get started!")
            
        st.markdown("---")
        st.markdown("### � Actions")
        
        if 'user_skills' in st.session_state:
            if st.button("🗑️ Clear Resume Data"):
                # Clear session state
                if 'user_skills' in st.session_state:
                    del st.session_state.user_skills
                if 'resume_text' in st.session_state:
                    del st.session_state.resume_text
                if 'best_role' in st.session_state:
                    del st.session_state.best_role
                st.success("✅ Resume data cleared!")
                st.rerun()
        
        st.markdown("---")
        st.markdown("### �💡 Tips")
        st.markdown("• Upload a clear PDF resume")
        st.markdown("• Include technical skills")
        st.markdown("• Use standard section headers")
    
    # Main content based on page selection
    if page == "🏠 Home":
        show_home_page()
    elif page == "📄 Resume Analysis":
        show_resume_analysis()
    elif page == "💼 Job Matching":
        show_job_matching()
    elif page == "📚 Skills & Courses":
        show_skills_courses()
    elif page == "📈 Career Planning":
        show_career_planning()
    elif page == "🚀 Advanced Features":
        show_advanced_features()
    elif page == "🤖 AI Assistant":
        show_ai_assistant()

def show_home_page():
    """Display enhanced home page with features overview"""
    
    # Hero section with realistic content
    st.markdown("""
    <div class="main-header">
        <h1>🚀 CareerCraft AI</h1>
        <p>Your Intelligent Career Companion for the Indian Job Market</p>
        <div style="margin-top: 1.5rem;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 25px; margin: 0.5rem;">🎯 AI-Powered Matching</span>
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 25px; margin: 0.5rem;">💰 Salary Insights in LPA</span>
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 25px; margin: 0.5rem;">📊 Career Analytics</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Features overview with realistic descriptions
    st.markdown("### 🎯 How CareerCraft AI Helps You")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-highlight">
            <h3>📄 Smart Resume Analysis</h3>
            <p>Upload your resume and get AI-powered insights. Our system extracts skills, analyzes ATS compatibility, and provides actionable improvement suggestions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-highlight">
            <h3>💼 Personalized Job Matching</h3>
            <p>Discover job opportunities that match your skills and experience. Get salary information in LPA format and apply to positions from top Indian companies.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-highlight">
            <h3>🎯 Skill Development</h3>
            <p>Get personalized skill assessments and learning recommendations. Track your progress and build a roadmap for career advancement.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # How it works section
    st.markdown("### 🔄 How It Works")
    step_col1, step_col2, step_col3, step_col4 = st.columns(4)
    
    with step_col1:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="background: #4f46e5; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;">1</div>
            <h4 style="margin: 0.5rem 0; color: #1e293b;">Upload Resume</h4>
            <p style="color: #64748b; font-size: 0.9rem;">Upload your resume and let our AI analyze your skills and experience</p>
        </div>
        """, unsafe_allow_html=True)
    
    with step_col2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="background: #10b981; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;">2</div>
            <h4 style="margin: 0.5rem 0; color: #1e293b;">AI Analysis</h4>
            <p style="color: #64748b; font-size: 0.9rem;">Get detailed insights on your strengths and areas for improvement</p>
        </div>
        """, unsafe_allow_html=True)
    
    with step_col3:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="background: #f59e0b; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;">3</div>
            <h4 style="margin: 0.5rem 0; color: #1e293b;">Match Jobs</h4>
            <p style="color: #64748b; font-size: 0.9rem;">Discover relevant job opportunities with competitive salaries</p>
        </div>
        """, unsafe_allow_html=True)
    
    with step_col4:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="background: #7c3aed; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;">4</div>
            <h4 style="margin: 0.5rem 0; color: #1e293b;">Grow Career</h4>
            <p style="color: #64748b; font-size: 0.9rem;">Plan your career path with personalized recommendations</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Getting started section
    st.markdown("### 🚀 Get Started")
    start_col1, start_col2 = st.columns([2, 1])
    
    with start_col1:
        st.markdown("""
        <div style="background: #f8fafc; padding: 1.5rem; border-radius: 12px; border: 1px solid #e2e8f0;">
            <h4 style="color: #1e293b; margin-bottom: 1rem;">Ready to Transform Your Career?</h4>
            <p style="color: #64748b; margin-bottom: 1rem;">Start by uploading your resume and discover your potential in the Indian job market!</p>
            <div style="margin-top: 1rem;">
                <span style="background: #dcfce7; color: #166534; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.9rem; margin-right: 0.5rem;">✓ Free to use</span>
                <span style="background: #dbeafe; color: #1e40af; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.9rem; margin-right: 0.5rem;">✓ AI-powered</span>
                <span style="background: #fef3c7; color: #92400e; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.9rem;">✓ Indian market focus</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with start_col2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🎯</div>
            <p style="color: #4f46e5; font-weight: 600;">Start Your Journey</p>
            <p style="color: #64748b; font-size: 0.9rem;">Navigate to Resume Analysis to begin</p>
        </div>
        """, unsafe_allow_html=True)

def show_resume_analysis():
    """Display resume analysis page"""
    
    st.markdown("## 📄 Resume Analysis")
    
    # Input section
    st.markdown("### 📤 Upload Your Resume")
    col1, col2 = st.columns(2)
    
    with col1:
        uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
    
    with col2:
        linkedin_text = st.text_area("Or paste LinkedIn 'About' section", height=100)
    
    if uploaded_file or linkedin_text:
        # Process input
        with st.spinner("🔍 Analyzing your resume..."):
            if uploaded_file:
                text = extract_text_from_pdf(uploaded_file)
            else:
                text = linkedin_text
            
            if not text:
                st.error("❌ No text could be extracted. Please check your file.")
                return
            
            # Extract skills
            user_skills = extract_skills(text)
            
            if not user_skills:
                st.warning("⚠️ No skills detected. Please ensure your resume contains relevant technical skills.")
                return
            
            # Store skills in session state for use in other pages
            st.session_state.user_skills = user_skills
            st.session_state.resume_text = text
            
            # Display results
            show_skills_analysis(user_skills, text)

def show_skills_analysis(user_skills, resume_text):
    """Display skills analysis results"""
    
    st.markdown("### ✅ Extracted Skills")
    
    # Categorize skills
    categorized_skills = get_skills_by_category(user_skills)
    
    for category, skills in categorized_skills.items():
        st.markdown(f"**{category}:**")
        skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
        st.markdown(skills_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ATS Analysis
    st.markdown("### 📊 ATS Compatibility Analysis")
    
    # Get best matching role first
    roles = ["Data Analyst", "Backend Developer", "ML Engineer", "Frontend Developer", "DevOps Engineer"]
    best_role = None
    best_score = 0
    
    for role in roles:
        matched, missing, score = match_skills(user_skills, role)
        if score > best_score:
            best_score = score
            best_role = role
    
    if best_role:
        # Store best role in session state
        st.session_state.best_role = best_role
        
        ats_score, feedback = get_ats_score_and_feedback(resume_text, best_role)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("ATS Score", f"{ats_score}/100")
        with col2:
            st.metric("Best Matching Role", best_role)
        
        # Feedback
        st.markdown("### 💡 Improvement Suggestions")
        for item in feedback:
            if item.startswith("✅"):
                st.success(item)
            elif item.startswith("⚠️"):
                st.warning(item)
            else:
                st.info(item)

def show_job_matching():
    """Display job matching page with enhanced features"""
    
    st.markdown("## 💼 Job Matching & Recommendations")
    
    # Check if user has uploaded resume
    if 'user_skills' not in st.session_state:
        st.info("📄 Please upload your resume in the Resume Analysis section first.")
        return
    
    user_skills = st.session_state.user_skills
    
    # Enhanced UI with tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Role Analysis", "💼 Job Listings", "🔍 Advanced Search", "📊 Market Insights"])
    
    with tab1:
        show_role_analysis(user_skills)
    
    with tab2:
        show_job_listings(user_skills)
    
    with tab3:
        show_advanced_job_search(user_skills)
    
    with tab4:
        show_market_insights()

def show_role_analysis(user_skills):
    """Show role compatibility analysis"""
    st.markdown("### 📊 Role Compatibility Analysis")
    
    roles = ["Data Analyst", "Backend Developer", "ML Engineer", "Frontend Developer", "DevOps Engineer"]
    role_scores = {}
    
    for role in roles:
        matched, missing, score = match_skills(user_skills, role)
        role_scores[role] = {
            'score': score,
            'matched': len(matched),
            'missing': len(missing),
            'matched_skills': matched,
            'missing_skills': missing
        }
    
    # Display comparison with enhanced visuals
    for role, data in sorted(role_scores.items(), key=lambda x: x[1]['score'], reverse=True):
        with st.expander(f"🎯 {role} - {data['score']}% Match", expanded=(data['score'] == max(role_scores.values(), key=lambda x: x['score'])['score'])):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.progress(data['score'] / 100)
                
            with col2:
                st.metric("Score", f"{data['score']}%")
                
            with col3:
                st.metric("Skills Match", f"{data['matched']}/{data['matched'] + data['missing']}")
            
            # Show detailed skill breakdown
            if data['matched_skills']:
                st.success(f"✅ **You have:** {', '.join(data['matched_skills'][:8])}")
            
            if data['missing_skills']:
                st.warning(f"⚠️ **Need to learn:** {', '.join(data['missing_skills'][:8])}")
            
            # Show job recommendations for this role
            jobs = get_jobs_for_role(role)
            if jobs:
                st.info(f"📋 **Available jobs:** {len(jobs)} positions found")

def show_job_listings(user_skills):
    """Show actual job listings"""
    st.markdown("### 💼 Job Listings")
    
    # Get best matching role
    roles = ["Data Analyst", "Backend Developer", "ML Engineer", "Frontend Developer", "DevOps Engineer"]
    best_role = None
    best_score = 0
    
    for role in roles:
        matched, missing, score = match_skills(user_skills, role)
        if score > best_score:
            best_score = score
            best_role = role
    
    # Role selector
    col1, col2 = st.columns([2, 1])
    with col1:
        selected_role = st.selectbox(
            "Select job role:",
            roles,
            index=roles.index(best_role) if best_role else 0,
            key="job_role_selector"
        )
    
    with col2:
        location_filter = st.selectbox(
            "Location:",
            ["All Locations", "Remote", "Mumbai", "Bangalore", "Delhi", "Hyderabad", "Pune", "Chennai"],
            key="location_filter_selectbox"
        )
    
    # Get and display jobs
    jobs = get_jobs_for_role(selected_role)
    
    if location_filter != "All Locations":
        jobs = [job for job in jobs if location_filter.lower() in job.get('location', '').lower()]
    
    if jobs:
        st.markdown(f"""
        <div class="success-message">
            🎉 Found {len(jobs)} job opportunities for {selected_role} in Indian market!
        </div>
        """, unsafe_allow_html=True)
        
        # Display jobs using enhanced cards
        for i, job in enumerate(jobs[:10]):  # Show top 10 jobs
            st.markdown(create_job_card(job), unsafe_allow_html=True)
            
            # Add apply button
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button(f"🔗 Apply Now", key=f"apply_{i}"):
                    st.markdown(f"[Apply at {job.get('company', 'Company')}]({job.get('link', '#')})")
            with col2:
                if st.button(f"💾 Save Job", key=f"save_{i}"):
                    st.success("Job saved to your profile!")
            with col3:
                if st.button(f"� View Details", key=f"details_{i}"):
                    with st.expander("� Job Details", expanded=True):
                        st.markdown(f"**Company:** {job.get('company', 'N/A')}")
                        st.markdown(f"**Job Type:** {job.get('job_type', 'Full-time')}")
                        st.markdown(f"**Company Size:** {job.get('company_size', 'Medium')}")
                        st.markdown(f"**Remote Option:** {job.get('remote_option', 'Office-based')}")
                        st.markdown(f"**Posted:** {job.get('posted_date', 'Recently')}")
        
        # Download job list
        df = pd.DataFrame(jobs)
        if not df.empty:
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download Job List (CSV)",
                data=csv,
                file_name=f"{selected_role}_jobs.csv",
                mime="text/csv"
            )
    else:
        st.warning("No jobs found for the selected criteria. Try different filters.")

def show_advanced_job_search(user_skills):
    """Show advanced job search with filters"""
    st.markdown("### 🔍 Advanced Job Search")
    
    # Import additional functions
    from job_scraper import search_jobs_with_filters, search_jobs_by_skills
    
    # Search options
    search_type = st.radio(
        "Search by:",
        ["Role & Filters", "Your Skills", "Trending Jobs"],
        horizontal=True
    )
    
    if search_type == "Role & Filters":
        col1, col2, col3 = st.columns(3)
        
        with col1:
            role = st.selectbox(
                "Role:",
                ["All Roles", "Data Analyst", "Backend Developer", "ML Engineer", "Frontend Developer", "DevOps Engineer"],
                key="advanced_role_selectbox"
            )
            
        with col2:
            location = st.selectbox(
                "Location:",
                ["All", "Remote", "Mumbai", "Bangalore", "Delhi", "Hyderabad", "Pune", "Chennai"],
                key="advanced_location_selectbox"
            )
            
        with col3:
            experience = st.selectbox(
                "Experience:",
                ["All", "0-1 years", "1-3 years", "3-5 years", "5+ years"],
                key="advanced_experience_selectbox"
            )
        
        col4, col5 = st.columns(2)
        with col4:
            company_size = st.selectbox(
                "Company Size:",
                ["All", "Startup", "Small", "Medium", "Large"],
                key="advanced_company_size_selectbox"
            )
            
        with col5:
            job_type = st.selectbox(
                "Job Type:",
                ["All", "Full-time", "Part-time", "Contract", "Internship"],
                key="advanced_job_type_selectbox"
            )
        
        if st.button("🔍 Search Jobs"):
            with st.spinner("Searching for jobs..."):
                jobs = search_jobs_with_filters(
                    role=role if role != "All Roles" else None,
                    location=location if location != "All" else None,
                    experience=experience if experience != "All" else None,
                    company_size=company_size if company_size != "All" else None,
                    job_type=job_type if job_type != "All" else None
                )
                
                if jobs:
                    st.success(f"Found {len(jobs)} jobs matching your criteria")
                    display_job_cards(jobs)
                else:
                    st.warning("No jobs found matching your criteria")
    
    elif search_type == "Your Skills":
        st.info(f"Searching jobs based on your skills: {', '.join(user_skills[:10])}")
        
        if st.button("🔍 Find Jobs Matching My Skills"):
            with st.spinner("Finding jobs that match your skills..."):
                jobs = search_jobs_by_skills(user_skills)
                
                if jobs:
                    st.success(f"Found {len(jobs)} jobs matching your skills")
                    display_job_cards(jobs)
                else:
                    st.warning("No jobs found matching your specific skills")
    
    elif search_type == "Trending Jobs":
        from job_scraper import get_trending_jobs
        
        if st.button("🔥 Show Trending Jobs"):
            with st.spinner("Loading trending jobs..."):
                jobs = get_trending_jobs()
                
                if jobs:
                    st.success(f"Found {len(jobs)} trending job opportunities")
                    display_job_cards(jobs)
                else:
                    st.warning("No trending jobs available")

def display_job_cards(jobs):
    """Display job cards in a consistent format"""
    for job in jobs:
        st.markdown(f"""
        <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; margin: 1rem 0; background: white;">
            <h4 style="margin: 0; color: #2E86AB;">{job.get('title', 'N/A')}</h4>
            <p style="margin: 0.5rem 0; color: #666;"><strong>{job.get('company', 'N/A')}</strong> • {job.get('location', 'N/A')}</p>
            <p style="margin: 0.5rem 0; color: #666;">💰 {job.get('salary', 'Not specified')} • 📅 {job.get('experience', 'Any')}</p>
            <p style="margin: 0.5rem 0; color: #333;">{job.get('description', 'No description available')}</p>
            <div style="margin-top: 1rem;">
                <a href="{job.get('link', '#')}" target="_blank" style="background: #4A90E2; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 4px; display: inline-block;">Apply Now</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_market_insights():
    """Show job market insights and statistics"""
    st.markdown("### 📊 Job Market Insights")
    
    from job_scraper import get_job_market_stats
    
    # Get market statistics
    stats = get_job_market_stats()
    
    # Display key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Jobs", stats.get('total_jobs', 0))
    
    with col2:
        st.metric("Remote Jobs", stats.get('remote_jobs', 0))
    
    with col3:
        st.metric("Top Location", stats.get('top_location', 'N/A'))
    
    with col4:
        st.metric("Avg Salary", stats.get('avg_salary', 'N/A'))
    
    # Role distribution chart
    st.markdown("#### 📈 Job Distribution by Role")
    role_distribution = stats.get('role_distribution', {})
    
    if role_distribution:
        import plotly.express as px
        
        df_roles = pd.DataFrame(list(role_distribution.items()), columns=['Role', 'Count'])
        fig = px.bar(df_roles, x='Role', y='Count', title='Job Openings by Role')
        st.plotly_chart(fig, use_container_width=True)
    
    # Salary insights
    st.markdown("#### 💰 Salary Insights by Role")
    salary_data = stats.get('salary_by_role', {})
    
    if salary_data:
        df_salary = pd.DataFrame(list(salary_data.items()), columns=['Role', 'Avg Salary'])
        fig = px.bar(df_salary, x='Role', y='Avg Salary', title='Average Salary by Role')
        st.plotly_chart(fig, use_container_width=True)
    
    # Top skills in demand
    st.markdown("#### 🔥 Top Skills in Demand")
    top_skills = stats.get('top_skills', [])
    
    if top_skills:
        for i, skill in enumerate(top_skills[:10], 1):
            st.markdown(f"{i}. **{skill}**")
    
    # Industry trends
    st.markdown("#### 📊 Industry Trends")
    st.info("🚀 **AI/ML roles** are seeing 40% growth")
    st.info("🌐 **Remote work** is now available in 60% of tech jobs")
    st.info("☁️ **Cloud skills** are in high demand across all roles")
    st.info("🔒 **Cybersecurity** positions increased by 25% this year")

def show_skills_courses():
    """Display skills and courses page"""
    
    st.markdown('<div class="section-header">📚 Skills Development & Course Recommendations</div>', unsafe_allow_html=True)
    
    # Check if skills are loaded from resume
    if 'user_skills' not in st.session_state:
        st.markdown('<div class="info-card">💡 You can manually enter your skills or upload a resume in the Resume Analysis section.</div>', unsafe_allow_html=True)
        
        manual_skills = st.text_input("Enter your skills (comma-separated):")
        if manual_skills:
            user_skills = [skill.strip() for skill in manual_skills.split(',')]
            st.session_state.user_skills = user_skills
        else:
            return
    else:
        user_skills = st.session_state.user_skills
        st.success(f"✅ Using {len(user_skills)} skills from your resume")
        
        # Show current skills with enhanced styling
        with st.expander("🔍 View Your Current Skills"):
            categorized_skills = get_skills_by_category(user_skills)
            
            st.markdown('<div class="skills-container">', unsafe_allow_html=True)
            for category, skills in categorized_skills.items():
                st.markdown(f'<div class="skill-category-card">', unsafe_allow_html=True)
                st.markdown(f'<div class="skill-category-title">{category}</div>', unsafe_allow_html=True)
                
                skills_html = ''.join([f'<span class="skill-item">{skill}</span>' for skill in skills])
                st.markdown(skills_html, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Target role selection
    target_role = st.selectbox(
        "Select your target role:",
        ["Data Analyst", "Backend Developer", "ML Engineer", "Frontend Developer", "DevOps Engineer"],
        key="skills_target_role_selectbox"
    )
    
    # Skill gap analysis
    matched, missing, score = match_skills(user_skills, target_role)
    
    st.markdown(f'<div class="section-header">📊 Skill Gap Analysis for {target_role}</div>', unsafe_allow_html=True)
    
    # Skills match score display
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.metric("Skills Match", f"{len(matched)}/{len(matched) + len(missing)}")
    with col2:
        st.metric("Match Score", f"{score:.0%}")
    with col3:
        st.metric("Skills to Learn", f"{len(missing)}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
        st.markdown('<div class="analysis-title">✅ Skills You Have</div>', unsafe_allow_html=True)
        st.markdown('<div class="analysis-content">', unsafe_allow_html=True)
        if matched:
            skills_html = ''.join([f'<span class="skill-item">{skill}</span>' for skill in matched])
            st.markdown(skills_html, unsafe_allow_html=True)
        else:
            st.markdown("No matching skills found for this role.")
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
        st.markdown('<div class="analysis-title">❌ Skills to Develop</div>', unsafe_allow_html=True)
        st.markdown('<div class="analysis-content">', unsafe_allow_html=True)
        if missing:
            for skill in missing:
                st.markdown(f'<div style="margin: 0.5rem 0;">• {skill}</div>', unsafe_allow_html=True)
        else:
            st.markdown("Great! You have all the required skills.")
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Course recommendations section
    if missing:
        st.markdown('<div class="section-header">📚 Recommended Courses</div>', unsafe_allow_html=True)
        
        for skill in missing[:6]:  # Show top 6 missing skills
            course_link = suggest_courses(skill)
            
            st.markdown('<div class="course-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="course-title">🎯 {skill} Mastery Course</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="course-provider">CareerCraft Academy</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="course-description">Comprehensive course covering all aspects of {skill} with hands-on projects and real-world applications.</div>', unsafe_allow_html=True)
            
            # Course details
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<span class="course-duration">4-6 weeks</span>', unsafe_allow_html=True)
            with col2:
                st.markdown('<span class="course-difficulty">Intermediate</span>', unsafe_allow_html=True)
            
            # Progress bar (simulated)
            progress_value = min(90, 20 + len(skill) * 5)
            st.markdown(f'''
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress_value}%"></div>
            </div>
            ''', unsafe_allow_html=True)
            
            if course_link != "No course found":
                st.markdown(f'<a href="{course_link}" target="_blank" style="color: #4f46e5; text-decoration: none; font-weight: 500;">🔗 Start Learning {skill}</a>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

def show_career_planning():
    """Display career planning page"""
    
    st.markdown("## 📈 AI-Powered Career Planning")
    
    # Check if user has skills
    if 'user_skills' not in st.session_state:
        st.info("📄 Please upload your resume or enter your skills in the Resume Analysis section first.")
        return
    
    user_skills = st.session_state.user_skills
    st.success(f"✅ Planning career path based on your {len(user_skills)} skills")
    
    # Show current skills summary
    with st.expander("🔍 Your Current Skills Summary"):
        categorized_skills = get_skills_by_category(user_skills)
        for category, skills in categorized_skills.items():
            st.markdown(f"**{category}:** {', '.join(skills)}")
    
    # Career path generation
    st.markdown("### 🛤️ Personalized Career Roadmap")
    
    # Use best role from session state if available
    default_role = st.session_state.get('best_role', "Data Analyst")
    role_options = ["Data Analyst", "Backend Developer", "ML Engineer", "Frontend Developer", "DevOps Engineer"]
    
    # Set default index
    try:
        default_index = role_options.index(default_role)
    except ValueError:
        default_index = 0
    
    target_role = st.selectbox(
        "Select your target role:",
        role_options,
        index=default_index,
        key="career_target"
    )
    
    if st.button("🚀 Generate Career Roadmap"):
        with st.spinner("🤖 AI is creating your personalized career plan..."):
            prompt = f"""
            Create a detailed career roadmap for someone with these skills: {', '.join(user_skills)}
            who wants to become a {target_role}.
            
            Include:
            1. 6-month plan with specific milestones
            2. 3-year career progression
            3. Key skills to develop
            4. Recommended certifications
            5. Industry trends to watch
            
            Make it actionable and specific.
            """
            
            roadmap = ask_career_bot(prompt)
            
            st.markdown("### 🗺️ Your Personalized Career Roadmap")
            st.markdown(roadmap)
            
            # Download option
            st.download_button(
                "📥 Download Career Roadmap",
                roadmap,
                file_name=f"career_roadmap_{target_role.replace(' ', '_')}.txt",
                mime="text/plain"
            )

def show_advanced_features():
    """Display advanced features page"""
    
    st.markdown("## 🚀 Advanced Features")
    
    if 'user_skills' not in st.session_state:
        st.info("📄 Please upload your resume in the Resume Analysis section first to access advanced features.")
        return
    
    user_skills = st.session_state.user_skills
    best_role = st.session_state.get('best_role', 'Data Analyst')
    
    # Advanced features tabs
    feature_tabs = st.tabs([
        "📊 Skills Radar", 
        "📈 Career Timeline", 
        "💰 Salary Insights",
        "📚 Learning Plan",
        "🧠 Skill Assessment",
        "🎯 Interview Simulator",
        "🏆 Certifications",
        "🤝 Networking",
        "🎨 Portfolio Builder"
    ])
    
    with feature_tabs[0]:
        show_skills_radar(user_skills, best_role)
    
    with feature_tabs[1]:
        show_career_timeline(best_role)
    
    with feature_tabs[2]:
        show_salary_insights(best_role)
    
    with feature_tabs[3]:
        show_learning_plan_tab(user_skills, best_role)
    
    with feature_tabs[4]:
        show_skill_assessment_tab()
    
    with feature_tabs[5]:
        show_interview_simulator_tab()
    
    with feature_tabs[6]:
        show_certifications_tab()
    
    with feature_tabs[7]:
        show_networking_tab()
    
    with feature_tabs[8]:
        show_portfolio_tab()

def show_skills_radar(user_skills, target_role):
    """Show skills radar chart"""
    from advanced_features import create_skills_radar_chart
    
    st.markdown("### 📊 Skills Proficiency Radar")
    
    fig = create_skills_radar_chart(user_skills, target_role)
    
    if fig:
        st.plotly_chart(fig, use_container_width=True)
        st.info("💡 The blue area shows your current skills, while the red line shows the target level.")
    else:
        st.warning("Unable to generate radar chart. Please ensure you have skills data.")

def show_career_timeline(target_role):
    """Show career progression timeline"""
    from advanced_features import create_career_progression_timeline
    
    st.markdown("### 📈 Career Progression Timeline")
    
    fig = create_career_progression_timeline("Junior", target_role)
    
    if fig:
        st.plotly_chart(fig, use_container_width=True)
        st.info("💡 This timeline shows typical career progression in your target role.")
    else:
        st.warning("Unable to generate timeline chart.")

def show_salary_insights(target_role):
    """Show salary projection insights"""
    from advanced_features import create_salary_projection_chart
    
    st.markdown("### 💰 Salary Projection")
    
    fig = create_salary_projection_chart(target_role, 5)
    
    if fig:
        st.plotly_chart(fig, use_container_width=True)
        st.info("💡 Salary ranges are based on industry averages and may vary by location and company.")
    else:
        st.warning("Salary data not available for this role.")

def show_learning_plan_tab(user_skills, target_role):
    """Show learning plan tab"""
    from advanced_features import generate_learning_plan, create_learning_gantt_chart
    
    st.markdown("### 📚 Personalized Learning Plan")
    
    timeline_months = st.slider("Learning timeline (months):", 3, 24, 6)
    
    if st.button("🎯 Generate Learning Plan"):
        plan = generate_learning_plan(user_skills, target_role, timeline_months)
        
        if plan:
            if 'message' in plan:
                st.success(plan['message'])
            else:
                st.success(f"Learning plan generated! You can learn {plan['completion_rate']} in {plan['total_duration_weeks']} weeks.")
                
                # Show Gantt chart
                gantt_fig = create_learning_gantt_chart(plan)
                if gantt_fig:
                    st.plotly_chart(gantt_fig, use_container_width=True)
                
                # Show detailed plan
                st.markdown("#### 📋 Detailed Learning Schedule")
                for item in plan['plan']:
                    priority_color = {"high": "🔴", "medium": "🟡", "low": "🟢"}
                    st.markdown(f"{priority_color[item['priority']]} **{item['skill']}** - Week {item['start_week']}-{item['end_week']} ({item['duration_weeks']} weeks)")
        else:
            st.error("Unable to generate learning plan.")

def show_skill_assessment_tab():
    """Show skill assessment tab"""
    from advanced_features import show_skill_assessment_quiz
    show_skill_assessment_quiz()

def show_interview_simulator_tab():
    """Show interview simulator tab"""
    from advanced_features import show_interview_simulator
    show_interview_simulator()

def show_certifications_tab():
    """Show certifications tab"""
    from advanced_features import show_certification_roadmap
    show_certification_roadmap()

def show_networking_tab():
    """Show networking tab"""
    from advanced_features import show_networking_recommendations
    show_networking_recommendations()

def show_portfolio_tab():
    """Show portfolio building tab"""
    from advanced_features import show_portfolio_builder
    show_portfolio_builder()

def show_ai_assistant():
    """Display AI assistant page"""
    
    st.markdown("## 🤖 CareerBot - Your AI Career Assistant")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for role, message in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**👤 You:** {message}")
        else:
            st.markdown(f"**🤖 CareerBot:** {message}")
    
    # Chat input
    user_question = st.text_input("💬 Ask CareerBot anything about your career:")
    
    if user_question:
        with st.spinner("🤖 CareerBot is thinking..."):
            response = ask_career_bot(user_question)
            
            # Add to history
            st.session_state.chat_history.append(("You", user_question))
            st.session_state.chat_history.append(("CareerBot", response))
            
            # Rerun to update display
            st.rerun()
    
    # Download chat history
    if st.session_state.chat_history:
        chat_text = "\n".join([f"{role}: {msg}" for role, msg in st.session_state.chat_history])
        st.download_button(
            "📥 Download Chat History",
            chat_text,
            file_name="careerbot_chat_history.txt",
            mime="text/plain"
        )
    
    # Quick questions
    st.markdown("### 💡 Quick Questions")
    quick_questions = [
        "How do I improve my resume for ATS systems?",
        "What are the highest paying tech roles in 2024?",
        "How do I transition from my current role to tech?",
        "What certifications should I get for my target role?",
        "How do I prepare for technical interviews?"
    ]
    
    for question in quick_questions:
        if st.button(question):
            with st.spinner("🤖 Getting answer..."):
                response = ask_career_bot(question)
                st.session_state.chat_history.append(("You", question))
                st.session_state.chat_history.append(("CareerBot", response))
                st.rerun()

# Store user skills in session state when resume is analyzed
def store_user_skills(skills):
    """Store user skills in session state"""
    st.session_state.user_skills = skills

if __name__ == "__main__":
    main()
