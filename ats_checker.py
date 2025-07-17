# ats_checker.py - Enhanced ATS scoring and feedback
import re
import nltk
from textstat import flesch_reading_ease, flesch_kincaid_grade
from collections import Counter
import streamlit as st

# Download required NLTK data
@st.cache_data
def download_nltk_data():
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
    except:
        pass

def get_ats_score_and_feedback(resume_text, role):
    """
    Enhanced ATS scoring with comprehensive feedback
    """
    if not resume_text:
        return 0, ["No resume text provided"]
    
    download_nltk_data()
    
    # Role-specific keywords and weights
    role_keywords = {
        "Data Analyst": {
            'core': ['python', 'sql', 'excel', 'data analysis', 'statistics'],
            'tools': ['pandas', 'numpy', 'matplotlib', 'tableau', 'powerbi'],
            'skills': ['data visualization', 'reporting', 'dashboard', 'etl'],
            'soft': ['analytical', 'problem solving', 'communication']
        },
        "Backend Developer": {
            'core': ['python', 'java', 'api', 'database', 'server'],
            'tools': ['django', 'flask', 'spring', 'docker', 'kubernetes'],
            'skills': ['rest api', 'microservices', 'authentication', 'security'],
            'soft': ['debugging', 'optimization', 'scalability']
        },
        "ML Engineer": {
            'core': ['machine learning', 'python', 'statistics', 'algorithms'],
            'tools': ['tensorflow', 'pytorch', 'scikit-learn', 'jupyter', 'git'],
            'skills': ['deep learning', 'neural networks', 'model deployment', 'mlops'],
            'soft': ['research', 'experimentation', 'analytical thinking']
        }
    }
    
    keywords = role_keywords.get(role, role_keywords["Data Analyst"])
    
    # Calculate different scoring components
    scores = {}
    feedback = []
    
    # 1. Keyword Matching (40% weight)
    keyword_score, keyword_feedback = analyze_keywords(resume_text, keywords)
    scores['keywords'] = keyword_score * 0.4
    feedback.extend(keyword_feedback)
    
    # 2. Format and Structure (25% weight)
    format_score, format_feedback = analyze_format(resume_text)
    scores['format'] = format_score * 0.25
    feedback.extend(format_feedback)
    
    # 3. Content Quality (20% weight)
    content_score, content_feedback = analyze_content_quality(resume_text)
    scores['content'] = content_score * 0.20
    feedback.extend(content_feedback)
    
    # 4. ATS Compatibility (15% weight)
    ats_score, ats_feedback = analyze_ats_compatibility(resume_text)
    scores['ats'] = ats_score * 0.15
    feedback.extend(ats_feedback)
    
    # Calculate total score
    total_score = sum(scores.values())
    
    # Add overall feedback
    if total_score >= 80:
        feedback.insert(0, "✅ Excellent! Your resume is well-optimized for ATS systems.")
    elif total_score >= 60:
        feedback.insert(0, "⚠️ Good resume, but there's room for improvement.")
    else:
        feedback.insert(0, "❌ Your resume needs significant improvements for ATS optimization.")
    
    return min(100, int(total_score)), feedback

def analyze_keywords(text, keywords):
    """Analyze keyword presence and density"""
    text_lower = text.lower()
    score = 0
    feedback = []
    total_possible = 0
    found_keywords = []
    
    for category, words in keywords.items():
        category_found = 0
        category_missing = []
        
        for keyword in words:
            total_possible += 1
            if keyword.lower() in text_lower:
                category_found += 1
                found_keywords.append(keyword)
            else:
                category_missing.append(keyword)
        
        if category_found == 0:
            feedback.append(f"❌ No {category} keywords found. Consider adding: {', '.join(category_missing[:3])}")
        elif category_found < len(words) * 0.5:
            feedback.append(f"⚠️ Few {category} keywords found. Consider adding: {', '.join(category_missing[:2])}")
        else:
            feedback.append(f"✅ Good {category} keyword coverage!")
    
    # Calculate keyword density
    if total_possible > 0:
        score = (len(found_keywords) / total_possible) * 100
    
    # Check for keyword stuffing
    word_count = len(text.split())
    keyword_density = len(found_keywords) / word_count * 100
    
    if keyword_density > 3:
        feedback.append("⚠️ Keyword density is too high. Avoid keyword stuffing.")
        score *= 0.9
    elif keyword_density < 0.5:
        feedback.append("❌ Keyword density is too low. Include more relevant keywords naturally.")
    
    return score, feedback

def analyze_format(text):
    """Analyze resume format and structure"""
    score = 100
    feedback = []
    
    # Check for common sections
    sections = {
        'contact': r'(email|phone|linkedin|github)',
        'summary': r'(summary|objective|profile|about)',
        'experience': r'(experience|employment|work|career)',
        'education': r'(education|degree|university|college)',
        'skills': r'(skills|competencies|technical)'
    }
    
    missing_sections = []
    for section, pattern in sections.items():
        if not re.search(pattern, text, re.IGNORECASE):
            missing_sections.append(section)
            score -= 15
    
    if missing_sections:
        feedback.append(f"❌ Missing sections: {', '.join(missing_sections)}")
    
    # Check length
    word_count = len(text.split())
    if word_count < 300:
        feedback.append("❌ Resume is too short. Aim for 300-800 words.")
        score -= 20
    elif word_count > 1000:
        feedback.append("⚠️ Resume is quite long. Consider condensing to 600-800 words.")
        score -= 10
    else:
        feedback.append("✅ Good resume length!")
    
    # Check for bullet points
    if text.count('•') + text.count('-') + text.count('*') < 5:
        feedback.append("⚠️ Use more bullet points to improve readability.")
        score -= 10
    
    # Check for numbers and metrics
    numbers = re.findall(r'\d+', text)
    if len(numbers) < 3:
        feedback.append("❌ Add more quantifiable achievements (numbers, percentages, etc.).")
        score -= 15
    
    return max(0, score), feedback

def analyze_content_quality(text):
    """Analyze content quality and readability"""
    score = 100
    feedback = []
    
    # Check readability
    try:
        reading_ease = flesch_reading_ease(text)
        if reading_ease < 30:
            feedback.append("❌ Text is too complex. Simplify language for better readability.")
            score -= 20
        elif reading_ease > 80:
            feedback.append("⚠️ Text might be too simple. Add more professional terminology.")
            score -= 10
        else:
            feedback.append("✅ Good readability level!")
    except:
        pass
    
    # Check for action verbs
    action_verbs = [
        'achieved', 'developed', 'managed', 'led', 'created', 'implemented',
        'designed', 'optimized', 'analyzed', 'built', 'improved', 'increased'
    ]
    
    found_verbs = 0
    for verb in action_verbs:
        if verb in text.lower():
            found_verbs += 1
    
    if found_verbs < 3:
        feedback.append("❌ Use more action verbs to describe your achievements.")
        score -= 15
    
    # Check for passive voice (basic check)
    passive_indicators = ['was', 'were', 'been', 'being']
    passive_count = sum(text.lower().count(indicator) for indicator in passive_indicators)
    total_words = len(text.split())
    
    if passive_count / total_words > 0.1:
        feedback.append("⚠️ Reduce passive voice. Use more active voice statements.")
        score -= 10
    
    # Check for repetitive words
    words = text.lower().split()
    word_counts = Counter(words)
    repetitive_words = [word for word, count in word_counts.items() if count > 5 and len(word) > 4]
    
    if repetitive_words:
        feedback.append(f"⚠️ Words used too frequently: {', '.join(repetitive_words[:3])}")
        score -= 10
    
    return max(0, score), feedback

def analyze_ats_compatibility(text):
    """Analyze ATS compatibility"""
    score = 100
    feedback = []
    
    # Check for problematic characters
    problematic_chars = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}']
    char_count = sum(text.count(char) for char in problematic_chars)
    
    if char_count > 10:
        feedback.append("⚠️ Reduce special characters that might confuse ATS systems.")
        score -= 15
    
    # Check for tables/columns (basic check)
    if '\t' in text or '|' in text:
        feedback.append("⚠️ Avoid tables and columns. Use simple formatting.")
        score -= 20
    
    # Check for standard section headers
    standard_headers = ['experience', 'education', 'skills', 'summary']
    non_standard_headers = ['expertise', 'qualifications', 'competencies']
    
    has_standard = any(header in text.lower() for header in standard_headers)
    has_non_standard = any(header in text.lower() for header in non_standard_headers)
    
    if not has_standard and has_non_standard:
        feedback.append("⚠️ Use standard section headers (Experience, Education, Skills, etc.).")
        score -= 10
    
    # Check for contact information format
    if '@' not in text:
        feedback.append("❌ Include email address in standard format.")
        score -= 20
    
    # Check for date formats
    date_patterns = [
        r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',  # MM/DD/YYYY or MM-DD-YYYY
        r'\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b',    # YYYY/MM/DD or YYYY-MM-DD
        r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}\b'  # Month YYYY
    ]
    
    date_found = any(re.search(pattern, text) for pattern in date_patterns)
    if not date_found:
        feedback.append("⚠️ Include dates in standard format (Jan 2020, 01/2020, etc.).")
        score -= 10
    
    return max(0, score), feedback

def get_keyword_suggestions(role, current_keywords):
    """Get personalized keyword suggestions"""
    role_suggestions = {
        "Data Analyst": [
            "data mining", "statistical analysis", "data modeling", "business intelligence",
            "kpi", "metrics", "dashboard", "reporting", "sql queries", "data cleaning"
        ],
        "Backend Developer": [
            "api development", "database design", "server architecture", "cloud computing",
            "devops", "testing", "debugging", "version control", "code review", "deployment"
        ],
        "ML Engineer": [
            "feature engineering", "model training", "cross-validation", "hyperparameter tuning",
            "model deployment", "a/b testing", "data pipeline", "mlops", "computer vision", "nlp"
        ]
    }
    
    suggestions = role_suggestions.get(role, [])
    current_lower = [kw.lower() for kw in current_keywords]
    
    return [suggestion for suggestion in suggestions if suggestion.lower() not in current_lower]

def generate_improvement_report(resume_text, role):
    """Generate a comprehensive improvement report"""
    score, feedback = get_ats_score_and_feedback(resume_text, role)
    
    report = {
        'overall_score': score,
        'feedback': feedback,
        'priority_actions': [],
        'keyword_suggestions': get_keyword_suggestions(role, []),
        'next_steps': []
    }
    
    # Prioritize actions based on score
    if score < 60:
        report['priority_actions'] = [
            "Add more relevant keywords naturally throughout the resume",
            "Include quantifiable achievements with numbers and percentages",
            "Ensure all standard sections are present and clearly labeled",
            "Use action verbs to describe your accomplishments"
        ]
    elif score < 80:
        report['priority_actions'] = [
            "Optimize keyword density without stuffing",
            "Add more technical skills relevant to the role",
            "Include metrics and numbers to quantify achievements",
            "Improve readability and formatting"
        ]
    else:
        report['priority_actions'] = [
            "Fine-tune keyword placement",
            "Add more specific technical details",
            "Consider adding relevant certifications or projects"
        ]
    
    # Next steps based on role
    role_next_steps = {
        "Data Analyst": [
            "Highlight specific tools and technologies used",
            "Include examples of data projects and their business impact",
            "Add relevant certifications (Google Analytics, Tableau, etc.)"
        ],
        "Backend Developer": [
            "Showcase API development experience",
            "Include information about system architecture and scalability",
            "Mention specific frameworks and databases used"
        ],
        "ML Engineer": [
            "Detail machine learning projects and their outcomes",
            "Include information about model performance and metrics",
            "Mention experience with MLOps and model deployment"
        ]
    }
    
    report['next_steps'] = role_next_steps.get(role, [])
    
    return report
