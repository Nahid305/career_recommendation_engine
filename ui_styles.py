# ui_styles.py
import streamlit as st

def apply_custom_css():
    """Apply custom CSS for enhanced UI"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: #f8fafc;
        color: #1e293b;
    }
    
    /* Override Streamlit's default text colors */
    .stApp p, .stApp span, .stApp div, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: #1e293b !important;
    }
    
    .stApp .stMarkdown p, .stApp .stMarkdown span, .stApp .stMarkdown div {
        color: #1e293b !important;
        font-weight: 400;
    }
    
    .stApp .stMarkdown h1, .stApp .stMarkdown h2, .stApp .stMarkdown h3, .stApp .stMarkdown h4 {
        color: #1e293b !important;
        font-weight: 600;
    }
    
    /* Main container */
    .main .block-container {
        padding: 2rem 1rem;
        max-width: 1200px;
        background: white;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin: 1rem auto;
        border: 1px solid #e2e8f0;
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 25px rgba(79, 70, 229, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 200"><polygon fill="rgba(255,255,255,0.1)" points="0,200 1000,200 1000,0 0,100"/></svg>');
        background-size: cover;
    }
    
    .main-header h1 {
        font-size: 2.8rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        position: relative;
        z-index: 1;
    }
    
    .main-header p {
        font-size: 1.2rem;
        margin: 1rem 0 0 0;
        opacity: 0.95;
        position: relative;
        z-index: 1;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e293b 0%, #334155 100%) !important;
        color: white !important;
        border-right: 1px solid #475569 !important;
    }
    
    .css-1d391kg .stSelectbox label {
        color: white !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
    }
    
    .css-1d391kg .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    
    .css-1d391kg .stSelectbox > div > div > div {
        color: white !important;
    }
    
    .css-1d391kg .stSelectbox input {
        color: white !important;
        background: transparent !important;
    }
    
    .css-1d391kg .stMarkdown {
        color: white !important;
    }
    
    .css-1d391kg .stMarkdown h1, 
    .css-1d391kg .stMarkdown h2, 
    .css-1d391kg .stMarkdown h3, 
    .css-1d391kg .stMarkdown h4, 
    .css-1d391kg .stMarkdown h5, 
    .css-1d391kg .stMarkdown h6 {
        color: white !important;
    }
    
    .css-1d391kg .stMarkdown p {
        color: white !important;
    }
    
    .css-1d391kg .stAlert {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    
    .css-1d391kg .stAlert div {
        color: white !important;
    }
    
    /* Sidebar content override */
    .st-emotion-cache-ja5xo9 {
        color: white !important;
    }
    
    .st-emotion-cache-ja5xo9 .stMarkdown {
        color: white !important;
    }
    
    .st-emotion-cache-ja5xo9 .stMarkdown h1, 
    .st-emotion-cache-ja5xo9 .stMarkdown h2, 
    .st-emotion-cache-ja5xo9 .stMarkdown h3, 
    .st-emotion-cache-ja5xo9 .stMarkdown h4, 
    .st-emotion-cache-ja5xo9 .stMarkdown h5, 
    .st-emotion-cache-ja5xo9 .stMarkdown h6 {
        color: white !important;
    }
    
    .st-emotion-cache-ja5xo9 .stMarkdown p {
        color: white !important;
    }
    
    .st-emotion-cache-ja5xo9 .stAlert {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    .st-emotion-cache-ja5xo9 .stAlert div {
        color: white !important;
    }
    
    .st-emotion-cache-ja5xo9 .stSelectbox label {
        color: white !important;
    }
    
    .st-emotion-cache-ja5xo9 .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    
    .st-emotion-cache-ja5xo9 .stSelectbox > div > div > div {
        color: white !important;
    }
    
    .st-emotion-cache-ja5xo9 .stSelectbox input {
        color: white !important;
        background: transparent !important;
    }
    
    /* Card Styling */
    .custom-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.1);
        transition: all 0.3s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
    }
    
    /* Job Card Styling */
    .job-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        position: relative;
    }
    
    .job-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        border-color: #4f46e5;
    }
    
    .job-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
        line-height: 1.3;
    }
    
    .job-company {
        color: #4f46e5;
        font-weight: 500;
        font-size: 1.1rem;
        margin-bottom: 0.8rem;
    }
    
    .job-salary {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem 0;
        font-size: 1rem;
        box-shadow: 0 2px 4px rgba(16, 185, 129, 0.2);
    }
    
    .job-location {
        background: #f1f5f9;
        color: #475569;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        display: inline-block;
        margin-right: 0.5rem;
        font-weight: 500;
    }
    
    .job-experience {
        background: #fef3c7;
        color: #92400e;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        display: inline-block;
        margin-right: 0.5rem;
        font-weight: 500;
    }
    
    /* Skill Tags */
    .skill-tag {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
        margin: 0.2rem 0.3rem;
        box-shadow: 0 2px 4px rgba(79, 70, 229, 0.2);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.3);
        text-transform: none;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 12px rgba(79, 70, 229, 0.4);
        background: linear-gradient(135deg, #4338ca 0%, #6d28d9 100%);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: #f8fafc;
        border-radius: 8px;
        padding: 0.5rem;
        margin-bottom: 1rem;
        border: 1px solid #e2e8f0;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: #64748b;
        border-radius: 6px;
        font-weight: 500;
        padding: 0.5rem 1rem;
        margin: 0.2rem;
        transition: all 0.3s ease;
        border: 1px solid transparent;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: #e2e8f0;
        color: #1e293b;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: #4f46e5;
        color: white;
        border: 1px solid #4f46e5;
        box-shadow: 0 2px 4px rgba(79, 70, 229, 0.2);
    }
    
    /* Progress bars */
    .stProgress > div > div {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    /* Success/Error Messages */
    .success-message {
        background: #dcfce7;
        color: #166534;
        border: 1px solid #bbf7d0;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-weight: 500;
    }
    
    .error-message {
        background: #fef2f2;
        color: #991b1b;
        border: 1px solid #fecaca;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-weight: 500;
    }
    
    /* Streamlit success/error override */
    .stAlert > div {
        background: white;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        padding: 1rem;
    }
    
    .stAlert[data-baseweb="notification"] > div {
        color: #1e293b;
    }
    
    /* File uploader */
    .stFileUploader {
        background: rgba(102, 126, 234, 0.05);
        border: 2px dashed #667eea;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        background: rgba(102, 126, 234, 0.1);
        border-color: #764ba2;
    }
    
    /* Metrics */
    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        margin: 0.5rem;
        border-top: 4px solid #667eea;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #64748b;
        font-weight: 500;
    }
    
    /* Status indicators */
    .status-online {
        background: #10b981;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    .status-offline {
        background: #64748b;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.6s ease-out;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem 0.5rem;
            margin: 1rem auto;
        }
        
        .main-header h1 {
            font-size: 2rem;
        }
        
        .job-card {
            padding: 1rem;
        }
    }
    
    /* Loading spinner */
    .loading-spinner {
        border: 4px solid #f3f3f3;
        border-top: 4px solid #667eea;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin: 2rem auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Notification badges */
    .notification-badge {
        background: #ef4444;
        color: white;
        border-radius: 50%;
        padding: 0.2rem 0.5rem;
        font-size: 0.7rem;
        font-weight: 600;
        position: absolute;
        top: -5px;
        right: -5px;
    }
    
    /* Skills Section Enhancement */
    .skills-container {
        background: #f8fafc;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
    }
    
    .skill-category-card {
        background: white;
        border-radius: 10px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .skill-category-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        border-color: #4f46e5;
    }
    
    .skill-category-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.8rem;
        border-bottom: 2px solid #4f46e5;
        padding-bottom: 0.5rem;
    }
    
    .skill-item {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        display: inline-block;
        margin: 0.3rem 0.4rem;
        box-shadow: 0 2px 4px rgba(79, 70, 229, 0.2);
    }
    
    .skill-match-score {
        background: #10b981;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
        float: right;
        margin-top: -0.5rem;
    }
    
    .course-card {
        background: white;
        border-radius: 10px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        position: relative;
    }
    
    .course-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        border-color: #10b981;
    }
    
    .course-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .course-provider {
        color: #4f46e5;
        font-weight: 500;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    .course-description {
        color: #64748b;
        line-height: 1.5;
        margin-bottom: 1rem;
    }
    
    .course-duration {
        background: #fef3c7;
        color: #92400e;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
        display: inline-block;
        margin-right: 0.5rem;
    }
    
    .course-difficulty {
        background: #dbeafe;
        color: #1e40af;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
        display: inline-block;
    }
    
    .progress-bar {
        background: #f1f5f9;
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    .section-header {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(79, 70, 229, 0.2);
    }
    
    .info-card {
        background: #f0f9ff;
        border: 1px solid #0ea5e9;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        color: #0c4a6e;
    }
    
    .warning-card {
        background: #fefce8;
        border: 1px solid #eab308;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        color: #713f12;
    }
    
    .analysis-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #4f46e5;
    }
    
    .analysis-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.8rem;
    }
    
    .analysis-content {
        color: #475569;
        line-height: 1.6;
    }
    
    .feature-highlight:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        border-color: #4f46e5;
    }
    
    .feature-highlight h3 {
        color: #1e293b;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .feature-highlight p {
        color: #64748b;
        line-height: 1.6;
    }
    
    
    /* Additional text contrast improvements */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #0f172a !important;
        font-weight: 600 !important;
    }
    
    /* Metric value styling */
    .stMetric .metric-value {
        color: #0f172a !important;
        font-weight: 600 !important;
    }
    
    /* Success, warning, error message styling */
    .stSuccess {
        background-color: #f0fdf4 !important;
        border: 1px solid #22c55e !important;
        color: #166534 !important;
    }
    
    .stWarning {
        background-color: #fefce8 !important;
        border: 1px solid #eab308 !important;
        color: #713f12 !important;
    }
    
    .stInfo {
        background-color: #f0f9ff !important;
        border: 1px solid #0ea5e9 !important;
        color: #0c4a6e !important;
    }
    
    .stError {
        background-color: #fef2f2 !important;
        border: 1px solid #ef4444 !important;
        color: #991b1b !important;
    }
    
    /* Expander styling */
    .stExpander {
        background-color: #f8fafc !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
    }
    
    .stExpander .streamlit-expanderHeader {
        color: #1e293b !important;
        font-weight: 600 !important;
    }
    
    /* Selectbox and input styling */
    .stSelectbox > div > div > div, .stTextInput > div > div > input {
        background-color: white !important;
        border: 1px solid #d1d5db !important;
        color: #1e293b !important;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #4f46e5 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #4338ca !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3) !important;
    }
    
    /* Sidebar text color fix - comprehensive override */
    .css-1d391kg .stMarkdown, 
    .css-1d391kg .stMarkdown h1, 
    .css-1d391kg .stMarkdown h2, 
    .css-1d391kg .stMarkdown h3, 
    .css-1d391kg .stMarkdown h4, 
    .css-1d391kg .stMarkdown h5, 
    .css-1d391kg .stMarkdown h6,
    .css-1d391kg .stMarkdown p,
    .css-1d391kg .stMarkdown div,
    .css-1d391kg .stMarkdown span,
    .css-1d391kg .stAlert,
    .css-1d391kg .stAlert div,
    .css-1d391kg .stAlert p,
    .css-1d391kg .stSelectbox label,
    .st-emotion-cache-ja5xo9,
    .st-emotion-cache-ja5xo9 .stMarkdown,
    .st-emotion-cache-ja5xo9 .stMarkdown h1,
    .st-emotion-cache-ja5xo9 .stMarkdown h2,
    .st-emotion-cache-ja5xo9 .stMarkdown h3,
    .st-emotion-cache-ja5xo9 .stMarkdown h4,
    .st-emotion-cache-ja5xo9 .stMarkdown h5,
    .st-emotion-cache-ja5xo9 .stMarkdown h6,
    .st-emotion-cache-ja5xo9 .stMarkdown p,
    .st-emotion-cache-ja5xo9 .stMarkdown div,
    .st-emotion-cache-ja5xo9 .stMarkdown span,
    .st-emotion-cache-ja5xo9 .stAlert,
    .st-emotion-cache-ja5xo9 .stAlert div,
    .st-emotion-cache-ja5xo9 .stAlert p,
    .st-emotion-cache-ja5xo9 .stSelectbox label {
        color: white !important;
    }
    
    /* Fix for any remaining text visibility issues */
    .stApp > div > div > div > div {
        color: #1e293b !important;
    }
    
    /* Override for sidebar specifically */
    .st-emotion-cache-1lqf7hx * {
        color: white !important;
    }
    
    .st-emotion-cache-1lqf7hx .stMarkdown * {
        color: white !important;
    }
    
    .st-emotion-cache-1lqf7hx .stAlert * {
        color: white !important;
    }
    
    .st-emotion-cache-1lqf7hx .stSelectbox * {
        color: white !important;
    }
    
    /* Sidebar user content area */
    .st-emotion-cache-ja5xo9 * {
        color: white !important;
    }
    
    /* Sidebar selectbox dropdown */
    .st-emotion-cache-ja5xo9 .stSelectbox [data-baseweb="select"] > div {
        color: white !important;
        background: rgba(255, 255, 255, 0.1) !important;
    }
    
    .st-emotion-cache-ja5xo9 .stSelectbox [data-baseweb="select"] > div > div {
        color: white !important;
    }
    
    .st-emotion-cache-ja5xo9 .stSelectbox [data-baseweb="select"] input {
        color: white !important;
    }
    
    /* Table styling */
    .stDataFrame {
        background-color: white !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
    }
    
    .stDataFrame th {
        background-color: #f8fafc !important;
        color: #1e293b !important;
        font-weight: 600 !important;
    }
    
    .stDataFrame td {
        color: #475569 !important;
    }
    
    /* Comprehensive sidebar text fix - highest priority */
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stAlert * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4, 
    [data-testid="stSidebar"] h5, 
    [data-testid="stSidebar"] h6,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: white !important;
    }
    
    /* Sidebar user content specifically */
    [data-testid="stSidebarUserContent"] * {
        color: white !important;
    }
    
    /* Selectbox specific fixes */
    [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox input {
        color: white !important;
        background: transparent !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox [role="combobox"] {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] [class*="st-"] {
        color: white !important;
    }
    
    /* Ultimate sidebar fix - nuclear option */
    .stApp [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #334155 100%) !important;
    }
    
    .stApp [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stMarkdown * {
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stAlert * {
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox * {
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] h1, 
    .stApp [data-testid="stSidebar"] h2, 
    .stApp [data-testid="stSidebar"] h3, 
    .stApp [data-testid="stSidebar"] h4, 
    .stApp [data-testid="stSidebar"] h5, 
    .stApp [data-testid="stSidebar"] h6,
    .stApp [data-testid="stSidebar"] p,
    .stApp [data-testid="stSidebar"] div,
    .stApp [data-testid="stSidebar"] span,
    .stApp [data-testid="stSidebar"] label {
        color: white !important;
    }
    
    /* Force selectbox text to be white */
    .stApp [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] > div {
        color: white !important;
        background: rgba(255, 255, 255, 0.1) !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] > div > div {
        color: white !important;
        background: rgba(255, 255, 255, 0.1) !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] input {
        color: white !important;
        background: rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Fix for selectbox dropdown options - make them dark background with white text */
    .stApp [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] [role="listbox"] {
        background: #1e293b !important;
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] [role="option"] {
        background: #1e293b !important;
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] [role="option"]:hover {
        background: #334155 !important;
        color: white !important;
    }
    
    /* Fix for selectbox button/display area */
    .stApp [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] button {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] button:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    
    /* Fix all selectbox components */
    .stApp [data-testid="stSidebar"] .stSelectbox * {
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] * {
        color: white !important;
        background: rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Override white backgrounds in sidebar */
    .stApp [data-testid="stSidebar"] [style*="background-color: white"],
    .stApp [data-testid="stSidebar"] [style*="background-color: rgb(255, 255, 255)"],
    .stApp [data-testid="stSidebar"] [style*="background: white"],
    .stApp [data-testid="stSidebar"] [style*="background: rgb(255, 255, 255)"] {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
    
    /* Force dark background for any white elements in sidebar */
    .stApp [data-testid="stSidebar"] .stSelectbox [class*="st-"] {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
    
    /* Override any dark theme forcing */
    .stApp [data-testid="stSidebar"] [class*="st-emotion-cache"] {
        color: white !important;
    }
    
    /* Fix for warning alerts in sidebar */
    .stApp [data-testid="stSidebar"] .stAlert[data-baseweb="notification"] {
        background: rgba(255, 193, 7, 0.2) !important;
        border: 1px solid rgba(255, 193, 7, 0.5) !important;
    }
    
    .stApp [data-testid="stSidebar"] .stAlert[data-baseweb="notification"] * {
        color: white !important;
    }
    
    /* Force all sidebar elements to be white - most aggressive approach */
    .stApp > * [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Target all possible Streamlit CSS classes in sidebar */
    [data-testid="stSidebar"] [class*="st-"], 
    [data-testid="stSidebar"] [class*="emotion-cache"] {
        color: white !important;
    }
    
    /* Force white text for all text elements in sidebar */
    .stApp [data-testid="stSidebar"] .stMarkdown,
    .stApp [data-testid="stSidebar"] .stText,
    .stApp [data-testid="stSidebar"] .stHeading,
    .stApp [data-testid="stSidebar"] .stSelectbox,
    .stApp [data-testid="stSidebar"] .stAlert {
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stMarkdown *,
    .stApp [data-testid="stSidebar"] .stText *,
    .stApp [data-testid="stSidebar"] .stHeading *,
    .stApp [data-testid="stSidebar"] .stSelectbox *,
    .stApp [data-testid="stSidebar"] .stAlert * {
        color: white !important;
    }
    
    /* Ensure sidebar background is always dark */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #334155 100%) !important;
    }
    
    /* Override any inherited colors */
    .stApp [data-testid="stSidebar"] {
        color: white !important;
        background: linear-gradient(180deg, #1e293b 0%, #334155 100%) !important;
    }
    
    .stApp [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Global fix for any white backgrounds in sidebar */
    .stApp [data-testid="stSidebar"] * {
        background-color: transparent !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox,
    .stApp [data-testid="stSidebar"] .stSelectbox * {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stAlert {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
    
    /* Fix for any remaining white elements */
    .stApp [data-testid="stSidebar"] [style*="background"] {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
    
    /* Make sure dropdown options are visible */
    .stApp [data-testid="stSidebar"] .stSelectbox ul {
        background: #1e293b !important;
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox li {
        background: #1e293b !important;
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stSelectbox li:hover {
        background: #334155 !important;
        color: white !important;
    }
    
    </style>
    """, unsafe_allow_html=True)

def create_job_card(job):
    """Create enhanced job card with Indian salary format"""
    return f"""
    <div class="job-card fade-in">
        <div class="job-title">{job['title']}</div>
        <div class="job-company">🏢 {job['company']}</div>
        <div class="job-salary">💰 {job['salary']}</div>
        <div style="margin: 0.5rem 0;">
            <span class="job-location">📍 {job['location']}</span>
            <span class="job-experience">👨‍💼 {job['experience']}</span>
        </div>
        <div style="margin: 1rem 0;">
            <strong>Key Skills:</strong><br>
            {''.join([f'<span class="skill-tag">{skill}</span>' for skill in job['requirements']])}
        </div>
        <div style="margin: 1rem 0; color: #64748b;">
            <strong>Description:</strong> {job['description']}
        </div>
        <div style="margin: 1rem 0;">
            <strong>Benefits:</strong> {', '.join(job.get('benefits', ['Standard Benefits']))}
        </div>
    </div>
    """

def create_feature_highlight(title, description, icon="✨"):
    """Create feature highlight card"""
    return f"""
    <div class="feature-highlight">
        <div style="font-size: 1.5rem; margin-bottom: 0.5rem; color: #4f46e5;">{icon}</div>
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """

def create_status_indicator(status, text):
    """Create status indicator"""
    status_class = "status-online" if status else "status-offline"
    return f'<span class="{status_class}">{text}</span>'

def create_success_message(message):
    """Create success message"""
    return f'<div class="success-message">✅ {message}</div>'

def create_error_message(message):
    """Create error message"""
    return f'<div class="error-message">❌ {message}</div>'
