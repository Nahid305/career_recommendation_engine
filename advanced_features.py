# advanced_features.py - Next-level features for CareerCraft AI
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta
import json
import random
from typing import Dict, List

def create_skills_radar_chart(user_skills, target_role):
    """Create a radar chart showing skill proficiency"""
    # Define role-specific skills and their importance
    role_skills = {
        "Data Analyst": {
            "Python": 90, "SQL": 95, "Excel": 85, "Statistics": 90, "Visualization": 85,
            "Machine Learning": 70, "Business Intelligence": 80, "Data Cleaning": 90
        },
        "Backend Developer": {
            "Python": 90, "Java": 85, "Database": 90, "API Development": 95, "Testing": 80,
            "Cloud Computing": 75, "System Design": 85, "Security": 80
        },
        "ML Engineer": {
            "Python": 95, "Machine Learning": 95, "Deep Learning": 90, "Statistics": 85,
            "Data Processing": 90, "MLOps": 80, "Mathematics": 85, "Cloud Computing": 75
        },
        "Frontend Developer": {
            "JavaScript": 95, "React": 90, "HTML/CSS": 90, "TypeScript": 80, "Testing": 75,
            "UI/UX": 70, "Performance": 80, "Mobile Development": 65
        },
        "DevOps Engineer": {
            "Docker": 90, "Kubernetes": 85, "CI/CD": 95, "Cloud Computing": 90, "Monitoring": 85,
            "Security": 80, "Automation": 90, "Infrastructure": 95
        }
    }
    
    target_skills = role_skills.get(target_role, role_skills["Data Analyst"])
    
    # Calculate current skill levels (simulate based on user skills)
    current_levels = {}
    for skill, target_level in target_skills.items():
        if any(skill.lower() in user_skill.lower() or user_skill.lower() in skill.lower() 
               for user_skill in user_skills):
            # User has this skill - simulate current level
            current_levels[skill] = min(target_level, random.randint(60, 90))
        else:
            # User doesn't have this skill
            current_levels[skill] = random.randint(10, 40)
    
    # Create radar chart
    fig = go.Figure()
    
    skills = list(target_skills.keys())
    current_values = [current_levels[skill] for skill in skills]
    target_values = [target_skills[skill] for skill in skills]
    
    # Add current skills
    fig.add_trace(go.Scatterpolar(
        r=current_values,
        theta=skills,
        fill='toself',
        name='Current Level',
        line_color='rgba(79, 70, 229, 0.8)',
        fillcolor='rgba(79, 70, 229, 0.3)'
    ))
    
    # Add target skills
    fig.add_trace(go.Scatterpolar(
        r=target_values,
        theta=skills,
        fill='toself',
        name='Target Level',
        line_color='rgba(239, 68, 68, 0.8)',
        fillcolor='rgba(239, 68, 68, 0.1)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title=f"Skills Proficiency Radar - {target_role}",
        height=500
    )
    
    return fig
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Skills Proficiency Analysis"
    )
    
    return fig

def create_career_progression_timeline(current_role, target_role):
    """Create a timeline showing career progression"""
    
    progression_data = {
        "Data Analyst": {
            "Junior Data Analyst": {"duration": "0-2 years", "skills": ["Excel", "SQL", "Python basics"]},
            "Data Analyst": {"duration": "2-4 years", "skills": ["Advanced SQL", "Python", "Tableau"]},
            "Senior Data Analyst": {"duration": "4-6 years", "skills": ["Machine Learning", "Advanced Analytics", "Leadership"]},
            "Data Science Manager": {"duration": "6+ years", "skills": ["Team Management", "Strategy", "Business Intelligence"]}
        },
        "Backend Developer": {
            "Junior Backend Developer": {"duration": "0-2 years", "skills": ["Python/Java", "SQL", "Git"]},
            "Backend Developer": {"duration": "2-4 years", "skills": ["APIs", "Databases", "Cloud Basics"]},
            "Senior Backend Developer": {"duration": "4-6 years", "skills": ["System Design", "Microservices", "DevOps"]},
            "Tech Lead": {"duration": "6+ years", "skills": ["Architecture", "Team Leadership", "Technical Strategy"]}
        },
        "ML Engineer": {
            "Junior ML Engineer": {"duration": "0-2 years", "skills": ["Python", "Statistics", "Basic ML"]},
            "ML Engineer": {"duration": "2-4 years", "skills": ["Deep Learning", "MLOps", "Model Deployment"]},
            "Senior ML Engineer": {"duration": "4-6 years", "skills": ["Advanced ML", "Research", "System Design"]},
            "ML Research Lead": {"duration": "6+ years", "skills": ["Research Leadership", "Innovation", "Strategy"]}
        }
    }
    
    timeline = progression_data.get(target_role, {})
    
    # Create timeline visualization
    positions = list(timeline.keys())
    durations = [timeline[pos]["duration"] for pos in positions]
    
    fig = go.Figure()
    
    for i, (position, data) in enumerate(timeline.items()):
        fig.add_trace(go.Scatter(
            x=[i],
            y=[position],
            mode='markers+text',
            marker=dict(size=20, color=f'rgba(74, 144, 226, {0.8 - i*0.2})'),
            text=data['duration'],
            textposition="bottom center",
            name=position,
            hovertext=f"Skills: {', '.join(data['skills'])}"
        ))
    
    fig.update_layout(
        title="Career Progression Timeline",
        xaxis_title="Career Stage",
        yaxis_title="Position",
        showlegend=False,
        height=400
    )
    
    return fig

def create_salary_projection_chart(role, experience_years):
    """Create salary projection chart"""
    
    salary_data = {
        "Data Analyst": {
            "0-1": [45000, 55000],
            "1-3": [55000, 70000],
            "3-5": [70000, 90000],
            "5-7": [90000, 120000],
            "7+": [120000, 150000]
        },
        "Backend Developer": {
            "0-1": [50000, 65000],
            "1-3": [65000, 85000],
            "3-5": [85000, 110000],
            "5-7": [110000, 140000],
            "7+": [140000, 180000]
        },
        "ML Engineer": {
            "0-1": [60000, 80000],
            "1-3": [80000, 110000],
            "3-5": [110000, 140000],
            "5-7": [140000, 180000],
            "7+": [180000, 220000]
        }
    }
    
    if role not in salary_data:
        return None
    
    experience_ranges = list(salary_data[role].keys())
    min_salaries = [salary_data[role][exp][0] for exp in experience_ranges]
    max_salaries = [salary_data[role][exp][1] for exp in experience_ranges]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=experience_ranges,
        y=max_salaries,
        fill=None,
        mode='lines',
        line_color='rgba(74, 144, 226, 0.8)',
        name='Max Salary'
    ))
    
    fig.add_trace(go.Scatter(
        x=experience_ranges,
        y=min_salaries,
        fill='tonexty',
        mode='lines',
        line_color='rgba(74, 144, 226, 0.8)',
        name='Min Salary',
        fillcolor='rgba(74, 144, 226, 0.2)'
    ))
    
    fig.update_layout(
        title=f"Salary Projection for {role}",
        xaxis_title="Experience",
        yaxis_title="Salary (USD)",
        showlegend=True
    )
    
    return fig

def generate_learning_plan(user_skills, target_role, timeline_months=6):
    """Generate a detailed learning plan"""
    
    from skill_matcher import get_detailed_skill_analysis
    
    analysis = get_detailed_skill_analysis(user_skills, target_role)
    
    if not analysis:
        return None
    
    missing_skills = analysis.get('missing_skills', [])
    
    if not missing_skills:
        return {"message": "You already have all the required skills!", "plan": []}
    
    # Categorize skills by priority and difficulty
    skill_priorities = {
        'python': {'priority': 'high', 'weeks': 8, 'difficulty': 'medium'},
        'sql': {'priority': 'high', 'weeks': 6, 'difficulty': 'medium'},
        'machine learning': {'priority': 'high', 'weeks': 12, 'difficulty': 'hard'},
        'javascript': {'priority': 'high', 'weeks': 6, 'difficulty': 'medium'},
        'react': {'priority': 'medium', 'weeks': 8, 'difficulty': 'medium'},
        'docker': {'priority': 'medium', 'weeks': 4, 'difficulty': 'easy'},
        'aws': {'priority': 'medium', 'weeks': 6, 'difficulty': 'medium'},
        'kubernetes': {'priority': 'low', 'weeks': 8, 'difficulty': 'hard'},
        'deep learning': {'priority': 'low', 'weeks': 16, 'difficulty': 'hard'},
    }
    
    # Create learning plan
    plan = []
    total_weeks = 0
    
    for skill in missing_skills:
        skill_info = skill_priorities.get(skill.lower(), {'priority': 'medium', 'weeks': 4, 'difficulty': 'medium'})
        
        if total_weeks + skill_info['weeks'] <= timeline_months * 4:  # 4 weeks per month
            plan.append({
                'skill': skill,
                'priority': skill_info['priority'],
                'duration_weeks': skill_info['weeks'],
                'difficulty': skill_info['difficulty'],
                'start_week': total_weeks + 1,
                'end_week': total_weeks + skill_info['weeks']
            })
            total_weeks += skill_info['weeks']
    
    return {
        'total_duration_weeks': total_weeks,
        'plan': plan,
        'completion_rate': f"{len(plan)}/{len(missing_skills)} skills"
    }

def create_learning_gantt_chart(learning_plan):
    """Create a Gantt chart for learning plan"""
    
    if not learning_plan or not learning_plan.get('plan'):
        return None
    
    df = pd.DataFrame(learning_plan['plan'])
    
    fig = px.timeline(
        df,
        x_start='start_week',
        x_end='end_week',
        y='skill',
        color='priority',
        title="Learning Plan Timeline",
        color_discrete_map={
            'high': '#FF6B6B',
            'medium': '#4ECDC4',
            'low': '#45B7D1'
        }
    )
    
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(
        xaxis_title="Week",
        yaxis_title="Skills",
        showlegend=True
    )
    
    return fig

def show_skill_assessment_quiz():
    """Show interactive skill assessment quiz"""
    
    st.markdown("### 🧠 Skill Assessment Quiz")
    
    # Sample questions for different skills
    questions = {
        "Python": [
            {
                "question": "What is the output of: print(type([]))?",
                "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
                "correct": 0,
                "difficulty": "easy"
            },
            {
                "question": "Which of the following is used for list comprehension?",
                "options": ["[]", "()", "{}", "||"],
                "correct": 0,
                "difficulty": "medium"
            }
        ],
        "SQL": [
            {
                "question": "Which SQL clause is used to filter records?",
                "options": ["WHERE", "FILTER", "SELECT", "HAVING"],
                "correct": 0,
                "difficulty": "easy"
            },
            {
                "question": "What does INNER JOIN return?",
                "options": ["All records from both tables", "Only matching records", "Left table records only", "Right table records only"],
                "correct": 1,
                "difficulty": "medium"
            }
        ]
    }
    
    selected_skill = st.selectbox("Select skill to assess:", list(questions.keys()), key="skill_assessment_selectbox")
    
    if selected_skill:
        skill_questions = questions[selected_skill]
        score = 0
        
        for i, q in enumerate(skill_questions):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            
            user_answer = st.radio(
                f"Select your answer:",
                q['options'],
                key=f"q_{selected_skill}_{i}"
            )
            
            if st.button(f"Submit Answer {i+1}", key=f"submit_{selected_skill}_{i}"):
                if q['options'].index(user_answer) == q['correct']:
                    st.success("✅ Correct!")
                    score += 1
                else:
                    st.error(f"❌ Incorrect. The correct answer is: {q['options'][q['correct']]}")
        
        if st.button("📊 Show Final Score"):
            percentage = (score / len(skill_questions)) * 100
            st.metric(f"{selected_skill} Assessment Score", f"{percentage:.1f}%")
            
            if percentage >= 80:
                st.success("🎉 Excellent! You have strong knowledge in this skill.")
            elif percentage >= 60:
                st.info("👍 Good! You have decent knowledge with room for improvement.")
            else:
                st.warning("📚 You might want to focus more on learning this skill.")

def show_networking_recommendations():
    """Show networking and community recommendations"""
    
    st.markdown("### 🤝 Networking & Community Recommendations")
    
    communities = {
        "Data Science": {
            "Reddit": "r/datascience, r/MachineLearning",
            "Discord": "Data Science Community, ML Collective",
            "LinkedIn": "Data Science Central, KDnuggets",
            "GitHub": "awesome-data-science, data-science-projects",
            "Events": "Data Science Meetups, Kaggle Competitions"
        },
        "Backend Development": {
            "Reddit": "r/webdev, r/programming",
            "Discord": "The Programmer's Hangout, Backend Developers",
            "LinkedIn": "Backend Developers United, API Design",
            "GitHub": "awesome-backend, system-design-primer",
            "Events": "API World, Backend Meetups"
        },
        "Machine Learning": {
            "Reddit": "r/MachineLearning, r/artificial",
            "Discord": "ML Collective, AI Research",
            "LinkedIn": "Machine Learning Engineers, AI Professionals",
            "GitHub": "awesome-machine-learning, ml-projects",
            "Events": "NeurIPS, ICML Conferences"
        }
    }
    
    for domain, platforms in communities.items():
        with st.expander(f"🌐 {domain} Communities"):
            for platform, links in platforms.items():
                st.markdown(f"**{platform}:** {links}")

def show_portfolio_builder():
    """Show portfolio building recommendations"""
    
    st.markdown("### 🎨 Portfolio Building Guide")
    
    portfolio_templates = {
        "Data Analyst": {
            "projects": [
                "Sales Dashboard with Tableau/Power BI",
                "Customer Segmentation Analysis",
                "A/B Testing Case Study",
                "Predictive Analytics Project",
                "Data Cleaning & Visualization Project"
            ],
            "tools": ["Tableau", "Power BI", "Python", "SQL", "Excel"],
            "github_structure": "data-analysis-portfolio/\n├── project1-sales-dashboard/\n├── project2-customer-segmentation/\n├── project3-ab-testing/\n└── README.md"
        },
        "Backend Developer": {
            "projects": [
                "RESTful API with Authentication",
                "Microservices Architecture",
                "Database Design & Optimization",
                "Real-time Chat Application",
                "E-commerce Backend System"
            ],
            "tools": ["Python/Java", "Docker", "PostgreSQL", "Redis", "AWS"],
            "github_structure": "backend-portfolio/\n├── api-project/\n├── microservices-demo/\n├── database-project/\n└── README.md"
        },
        "ML Engineer": {
            "projects": [
                "End-to-End ML Pipeline",
                "Deep Learning Model Deployment",
                "Computer Vision Application",
                "NLP Project with Transformers",
                "MLOps Pipeline with Docker"
            ],
            "tools": ["Python", "TensorFlow", "Docker", "MLflow", "Kubernetes"],
            "github_structure": "ml-portfolio/\n├── ml-pipeline/\n├── deep-learning-project/\n├── computer-vision/\n└── README.md"
        }
    }
    
    selected_role = st.selectbox("Select your target role:", list(portfolio_templates.keys()), key="portfolio_role_selectbox")
    
    if selected_role:
        template = portfolio_templates[selected_role]
        
        st.markdown("#### 📋 Recommended Projects")
        for project in template['projects']:
            st.markdown(f"• {project}")
        
        st.markdown("#### 🛠️ Key Tools to Showcase")
        tools_html = "".join([f'<span style="background: #4A90E2; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; margin: 0.2rem; display: inline-block;">{tool}</span>' for tool in template['tools']])
        st.markdown(tools_html, unsafe_allow_html=True)
        
        st.markdown("#### 📁 Suggested GitHub Structure")
        st.code(template['github_structure'], language='text')
        
        st.markdown("#### 💡 Portfolio Tips")
        st.info("• Include detailed README files with project descriptions")
        st.info("• Add live demos or screenshots")
        st.info("• Document your thought process and challenges faced")
        st.info("• Include performance metrics and results")
        st.info("• Keep code clean and well-commented")

def show_interview_simulator():
    """Show interactive interview simulator"""
    
    st.markdown("### 🎯 Interview Simulator")
    
    # Initialize session state for interview
    if 'interview_active' not in st.session_state:
        st.session_state.interview_active = False
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []
    
    # Interview questions by role
    interview_questions = {
        "Data Analyst": [
            "Tell me about a challenging data analysis project you worked on.",
            "How do you handle missing data in a dataset?",
            "Explain the difference between correlation and causation.",
            "Walk me through your process for creating a dashboard.",
            "How do you ensure data quality in your analysis?"
        ],
        "Backend Developer": [
            "Explain the difference between REST and GraphQL APIs.",
            "How do you handle authentication in a web application?",
            "Describe your approach to database optimization.",
            "How do you ensure your code is scalable?",
            "Walk me through designing a microservices architecture."
        ],
        "ML Engineer": [
            "Explain the bias-variance tradeoff in machine learning.",
            "How do you handle overfitting in your models?",
            "Describe your approach to feature engineering.",
            "How do you deploy machine learning models to production?",
            "Explain cross-validation and why it's important."
        ]
    }
    
    role = st.selectbox("Select role for interview:", list(interview_questions.keys()), key="interview_role_selectbox")
    
    if not st.session_state.interview_active:
        if st.button("🚀 Start Interview Simulation"):
            st.session_state.interview_active = True
            st.session_state.current_question = 0
            st.session_state.user_answers = []
            st.rerun()
    
    if st.session_state.interview_active:
        questions = interview_questions[role]
        
        if st.session_state.current_question < len(questions):
            question = questions[st.session_state.current_question]
            
            st.markdown(f"**Question {st.session_state.current_question + 1} of {len(questions)}:**")
            st.markdown(f"*{question}*")
            
            # Timer simulation
            col1, col2 = st.columns([3, 1])
            with col2:
                st.metric("Time", "2:00")  # Simulated timer
            
            with col1:
                answer = st.text_area("Your answer:", height=150, key=f"answer_{st.session_state.current_question}")
                
                if st.button("Next Question"):
                    st.session_state.user_answers.append(answer)
                    st.session_state.current_question += 1
                    st.rerun()
        
        else:
            # Interview completed
            st.success("🎉 Interview completed!")
            st.markdown("### 📊 Interview Summary")
            
            for i, answer in enumerate(st.session_state.user_answers):
                with st.expander(f"Question {i+1}: {questions[i]}"):
                    st.write(f"**Your answer:** {answer}")
                    
                    # Simulated feedback
                    feedback_options = [
                        "Good structure and clear explanation",
                        "Consider adding more technical details",
                        "Great use of examples",
                        "Could benefit from more specific metrics"
                    ]
                    st.info(f"💡 **Feedback:** {random.choice(feedback_options)}")
            
            if st.button("🔄 Start New Interview"):
                st.session_state.interview_active = False
                st.session_state.current_question = 0
                st.session_state.user_answers = []
                st.rerun()

def show_certification_roadmap():
    """Show certification roadmap"""
    
    st.markdown("### 🏆 Certification Roadmap")
    
    certifications = {
        "Data Analyst": {
            "Beginner": [
                {"name": "Google Data Analytics Certificate", "provider": "Google", "duration": "3-6 months", "cost": "$39/month"},
                {"name": "Microsoft Excel Expert", "provider": "Microsoft", "duration": "1-2 months", "cost": "$165"}
            ],
            "Intermediate": [
                {"name": "Tableau Desktop Specialist", "provider": "Tableau", "duration": "2-3 months", "cost": "$100"},
                {"name": "AWS Certified Cloud Practitioner", "provider": "AWS", "duration": "1-2 months", "cost": "$100"}
            ],
            "Advanced": [
                {"name": "SAS Certified Data Scientist", "provider": "SAS", "duration": "4-6 months", "cost": "$180"},
                {"name": "Certified Analytics Professional", "provider": "INFORMS", "duration": "6-12 months", "cost": "$695"}
            ]
        },
        "Backend Developer": {
            "Beginner": [
                {"name": "Python Institute PCAP", "provider": "Python Institute", "duration": "2-3 months", "cost": "$295"},
                {"name": "Oracle Database SQL", "provider": "Oracle", "duration": "1-2 months", "cost": "$245"}
            ],
            "Intermediate": [
                {"name": "AWS Certified Developer", "provider": "AWS", "duration": "3-4 months", "cost": "$150"},
                {"name": "Docker Certified Associate", "provider": "Docker", "duration": "2-3 months", "cost": "$195"}
            ],
            "Advanced": [
                {"name": "AWS Solutions Architect", "provider": "AWS", "duration": "4-6 months", "cost": "$150"},
                {"name": "Kubernetes Administrator", "provider": "CNCF", "duration": "3-4 months", "cost": "$375"}
            ]
        },
        "ML Engineer": {
            "Beginner": [
                {"name": "Google ML Crash Course", "provider": "Google", "duration": "2-3 months", "cost": "Free"},
                {"name": "IBM Data Science Certificate", "provider": "IBM", "duration": "3-6 months", "cost": "$39/month"}
            ],
            "Intermediate": [
                {"name": "TensorFlow Developer Certificate", "provider": "TensorFlow", "duration": "3-4 months", "cost": "$100"},
                {"name": "AWS ML Specialty", "provider": "AWS", "duration": "4-6 months", "cost": "$300"}
            ],
            "Advanced": [
                {"name": "Google ML Engineer", "provider": "Google Cloud", "duration": "6-8 months", "cost": "$200"},
                {"name": "Azure AI Engineer", "provider": "Microsoft", "duration": "4-6 months", "cost": "$165"}
            ]
        }
    }
    
    role = st.selectbox("Select your target role:", list(certifications.keys()), key="certifications_role_selectbox")
    
    if role:
        role_certs = certifications[role]
        
        for level, certs in role_certs.items():
            st.markdown(f"#### {level} Level")
            
            for cert in certs:
                with st.expander(f"🏅 {cert['name']}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**Provider:** {cert['provider']}")
                        st.markdown(f"**Duration:** {cert['duration']}")
                    
                    with col2:
                        st.markdown(f"**Cost:** {cert['cost']}")
                        st.markdown(f"**Level:** {level}")
                    
                    # Add progress tracking
                    progress = st.slider(f"Progress for {cert['name']}", 0, 100, 0, key=f"progress_{cert['name']}")
                    
                    if progress == 100:
                        st.success("🎉 Completed!")
                    elif progress > 0:
                        st.info(f"📚 In progress: {progress}%")
