# ui_styles.py
import streamlit as st

def apply_custom_css():
    """Apply custom CSS styles for enhanced UI"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Inter', 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .main .block-container {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 24px;
        padding: 2.5rem;
        margin: 1rem;
        box-shadow: 0 25px 50px rgba(0,0,0,0.15);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.3);
        max-width: 1200px;
    }
    
    /* Header Styles */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        color: white;
        padding: 4rem 2rem;
        border-radius: 24px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 30% 20%, rgba(255,255,255,0.2) 0%, transparent 50%),
                    radial-gradient(circle at 70% 80%, rgba(255,255,255,0.15) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .main-header h1 {
        font-size: 4rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #ffffff, #f0f8ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
    }
    
    .main-header p {
        font-size: 1.4rem;
        margin: 1.5rem 0;
        opacity: 0.95;
        font-weight: 400;
        letter-spacing: 0.01em;
    }
    
    /* Enhanced Section Headers */
    .section-header {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 16px;
        text-align: center;
        margin: 2rem 0;
        font-size: 1.8rem;
        font-weight: 700;
        box-shadow: 0 10px 30px rgba(79, 70, 229, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .section-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
        transform: translateX(-100%);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    /* Feature Highlight Cards */
    .feature-highlight {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .feature-highlight::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, #4f46e5, #7c3aed, #ec4899, #f59e0b);
        background-size: 300% 100%;
        animation: gradient 3s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .feature-highlight:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .feature-highlight h3 {
        color: #1e293b;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
    }
    
    .feature-highlight p {
        color: #64748b;
        font-size: 1.1rem;
        line-height: 1.7;
        margin: 0;
        font-weight: 400;
    }
    
    /* Enhanced Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e293b 0%, #334155 100%);
        border-radius: 0 20px 20px 0;
    }
    
    .css-1d391kg .css-1v3fvcr {
        color: #f1f5f9;
        font-weight: 500;
    }
    
    .css-1d391kg .stSelectbox label {
        color: #f1f5f9 !important;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .css-1d391kg .stButton button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        border: none;
        color: white;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
    }
    
    .css-1d391kg .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.5);
    }
    
    /* Enhanced Card Styles */
    .metric-container {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        text-align: center;
    }
    
    .metric-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
    }
    
    .metric-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: translateY(-5px) scale(1); }
        50% { transform: translateY(-5px) scale(1.05); }
        100% { transform: translateY(-5px) scale(1); }
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .metric-label {
        font-size: 1rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
    }
    
    /* Enhanced Status Boxes */
    .success-box {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        border: 1px solid #86efac;
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        color: #166534;
        box-shadow: 0 8px 25px rgba(34, 197, 94, 0.15);
        font-weight: 500;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        border: 1px solid #fcd34d;
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        color: #92400e;
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.15);
        font-weight: 500;
    }
    
    .info-card {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border: 1px solid #93c5fd;
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        color: #1e40af;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.15);
        font-weight: 500;
    }
    
    /* Enhanced Skill Tags */
    .skill-tag {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        margin: 0.4rem;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
        transition: all 0.3s ease;
        letter-spacing: 0.01em;
    }
    
    .skill-tag:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.4);
    }
    
    /* Enhanced Skills Container */
    .skills-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .skill-category-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .skill-category-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    }
    
    .skill-category-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    .skill-item {
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
        color: #475569;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        margin: 0.3rem;
        display: inline-block;
        font-size: 0.85rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .skill-item:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        transform: translateY(-2px);
    }
    
    /* Enhanced Job Cards */
    .job-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .job-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #4f46e5, #7c3aed, #ec4899);
        background-size: 300% 100%;
        animation: gradient 4s ease infinite;
    }
    
    .job-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0,0,0,0.15);
    }
    
    .job-title {
        color: #1e293b;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        letter-spacing: -0.01em;
    }
    
    .job-company {
        color: #4f46e5;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    
    .job-details {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 1.2rem;
        line-height: 1.6;
    }
    
    .job-salary {
        color: #059669;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    
    /* Enhanced Course Cards */
    .course-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .course-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #f59e0b, #ef4444, #ec4899);
    }
    
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.12);
    }
    
    .course-title {
        color: #1e293b;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .course-provider {
        color: #6b7280;
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .course-description {
        color: #64748b;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    .course-duration, .course-difficulty {
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
        color: #475569;
        padding: 0.4rem 0.8rem;
        border-radius: 15px;
        font-size: 0.9rem;
        font-weight: 500;
        display: inline-block;
    }
    
    .progress-bar {
        background: #e2e8f0;
        height: 8px;
        border-radius: 10px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }
    
    /* Enhanced Analysis Cards */
    .analysis-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .analysis-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.12);
    }
    
    .analysis-title {
        color: #1e293b;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    .analysis-content {
        color: #64748b;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Enhanced Buttons */
    .stButton button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        border: none;
        color: white;
        border-radius: 16px;
        padding: 1rem 2rem;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.3);
        letter-spacing: 0.01em;
        width: 100%;
        text-transform: none;
    }
    
    .stButton button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 12px 35px rgba(79, 70, 229, 0.4);
        background: linear-gradient(135deg, #4338ca 0%, #6d28d9 100%);
    }
    
    .stButton button:active {
        transform: translateY(-2px) scale(0.98);
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.5);
    }
    
    /* Success Message */
    .success-message {
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        color: #166534;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(34, 197, 94, 0.2);
        border: 1px solid #86efac;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2.5rem;
        }
        
        .main-header p {
            font-size: 1.1rem;
        }
        
        .feature-highlight {
            padding: 1.5rem;
        }
        
        .job-card {
            padding: 1.5rem;
        }
        
        .skills-container {
            grid-template-columns: 1fr;
        }
    }
    
    </style>
    """, unsafe_allow_html=True)

def create_job_card(job):
    """Create an enhanced job card HTML"""
    return f"""
    <div class="job-card">
        <div class="job-title">{job.get('title', 'N/A')}</div>
        <div class="job-company">{job.get('company', 'N/A')}</div>
        <div class="job-details">
            📍 {job.get('location', 'N/A')} • 
            📅 {job.get('experience', 'Any')} • 
            🏢 {job.get('company_size', 'Medium')} • 
            🔄 {job.get('job_type', 'Full-time')}
        </div>
        <div class="job-salary">💰 {job.get('salary', 'Not specified')}</div>
        <div class="job-description">
            {job.get('description', 'No description available')[:200]}...
        </div>
    </div>
    """

def create_feature_highlight(title, description, icon="🎯"):
    """Create a feature highlight card"""
    return f"""
    <div class="feature-highlight">
        <h3>{icon} {title}</h3>
        <p>{description}</p>
    </div>
    """

def create_status_indicator(status, message):
    """Create a status indicator"""
    if status == "success":
        return f'<div class="success-box">✅ {message}</div>'
    elif status == "warning":
        return f'<div class="warning-box">⚠️ {message}</div>'
    elif status == "info":
        return f'<div class="info-card">ℹ️ {message}</div>'
    else:
        return f'<div class="metric-card">{message}</div>'
