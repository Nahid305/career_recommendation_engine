# utils.py - Enhanced skill extraction
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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

# Comprehensive skills database
SKILLS_DATABASE = {
    'programming_languages': [
        'python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin',
        'go', 'rust', 'scala', 'r', 'matlab', 'perl', 'shell', 'bash', 'powershell'
    ],
    'web_technologies': [
        'html', 'css', 'react', 'angular', 'vue', 'node.js', 'express', 'django',
        'flask', 'spring', 'asp.net', 'bootstrap', 'jquery', 'webpack', 'sass'
    ],
    'databases': [
        'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'cassandra', 'oracle',
        'sqlite', 'dynamodb', 'elasticsearch', 'neo4j', 'firebase'
    ],
    'data_science': [
        'machine learning', 'deep learning', 'data analysis', 'statistics', 'pandas',
        'numpy', 'scikit-learn', 'tensorflow', 'pytorch', 'keras', 'opencv',
        'matplotlib', 'seaborn', 'plotly', 'jupyter', 'r studio'
    ],
    'cloud_platforms': [
        'aws', 'azure', 'gcp', 'google cloud', 'docker', 'kubernetes', 'jenkins',
        'terraform', 'ansible', 'heroku', 'digitalocean', 'lambda'
    ],
    'tools_software': [
        'git', 'github', 'gitlab', 'jira', 'confluence', 'slack', 'trello',
        'postman', 'swagger', 'excel', 'powerbi', 'tableau', 'streamlit'
    ],
    'methodologies': [
        'agile', 'scrum', 'kanban', 'devops', 'ci/cd', 'tdd', 'bdd', 'microservices',
        'rest api', 'graphql', 'oauth', 'jwt', 'soap'
    ],
    'soft_skills': [
        'leadership', 'communication', 'teamwork', 'problem solving', 'critical thinking',
        'project management', 'time management', 'adaptability', 'creativity'
    ]
}

# Flatten all skills into a single list
ALL_SKILLS = []
for category, skills in SKILLS_DATABASE.items():
    ALL_SKILLS.extend(skills)

# Add aliases and variations
SKILL_ALIASES = {
    'js': 'javascript',
    'nodejs': 'node.js',
    'reactjs': 'react',
    'angularjs': 'angular',
    'vuejs': 'vue',
    'ml': 'machine learning',
    'dl': 'deep learning',
    'ai': 'artificial intelligence',
    'nlp': 'natural language processing',
    'cv': 'computer vision',
    'db': 'database',
    'api': 'rest api',
    'ci': 'ci/cd',
    'cd': 'ci/cd'
}

def normalize_skill(skill):
    """Normalize skill name using aliases"""
    skill_lower = skill.lower().strip()
    return SKILL_ALIASES.get(skill_lower, skill_lower)

def extract_skills(text):
    """Enhanced skill extraction with better matching"""
    if not text:
        return []
    
    download_nltk_data()
    
    # Convert to lowercase for matching
    text_lower = text.lower()
    
    # Remove special characters but keep spaces, dots, and hyphens
    cleaned_text = re.sub(r'[^\w\s\.\-]', ' ', text_lower)
    
    detected_skills = set()
    
    # Method 1: Direct substring matching
    for skill in ALL_SKILLS:
        if skill in cleaned_text:
            detected_skills.add(skill)
    
    # Method 2: Token-based matching (for compound skills)
    try:
        tokens = word_tokenize(cleaned_text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token not in stop_words and len(token) > 2]
        
        # Check for multi-word skills
        text_for_ngrams = ' '.join(filtered_tokens)
        for skill in ALL_SKILLS:
            if len(skill.split()) > 1 and skill in text_for_ngrams:
                detected_skills.add(skill)
    except:
        pass
    
    # Method 3: Check aliases
    for alias, actual_skill in SKILL_ALIASES.items():
        if alias in cleaned_text:
            detected_skills.add(actual_skill)
    
    # Method 4: Pattern matching for specific formats
    patterns = {
        r'\b(python|java|javascript|c\+\+|c#)\b': lambda m: m.group(1).lower(),
        r'\b(react|angular|vue)\.?js\b': lambda m: m.group(1).lower(),
        r'\b(node)\.?js\b': 'node.js',
        r'\b(tensorflow|pytorch|keras)\b': lambda m: m.group(1).lower(),
        r'\b(aws|azure|gcp)\b': lambda m: m.group(1).lower(),
    }
    
    for pattern, skill_func in patterns.items():
        matches = re.finditer(pattern, cleaned_text, re.IGNORECASE)
        for match in matches:
            if callable(skill_func):
                skill = skill_func(match)
            else:
                skill = skill_func
            if skill in ALL_SKILLS:
                detected_skills.add(skill)
    
    return list(detected_skills)

def get_skill_category(skill):
    """Get the category of a skill"""
    skill_lower = skill.lower()
    for category, skills in SKILLS_DATABASE.items():
        if skill_lower in skills:
            return category.replace('_', ' ').title()
    return 'Other'

def get_skills_by_category(skills):
    """Group skills by category"""
    categorized = {}
    for skill in skills:
        category = get_skill_category(skill)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(skill)
    return categorized

def calculate_skill_score(user_skills, required_skills):
    """Calculate a more sophisticated skill matching score"""
    if not required_skills:
        return 100
    
    user_skills_lower = [skill.lower() for skill in user_skills]
    required_skills_lower = [skill.lower() for skill in required_skills]
    
    # Direct matches
    direct_matches = len(set(user_skills_lower) & set(required_skills_lower))
    
    # Partial matches (for related skills)
    partial_matches = 0
    for req_skill in required_skills_lower:
        for user_skill in user_skills_lower:
            if user_skill != req_skill and (user_skill in req_skill or req_skill in user_skill):
                partial_matches += 0.5
                break
    
    total_matches = direct_matches + partial_matches
    score = min(100, int((total_matches / len(required_skills_lower)) * 100))
    
    return score

def suggest_missing_skills(user_skills, required_skills):
    """Suggest skills that are missing but important"""
    user_skills_lower = [skill.lower() for skill in user_skills]
    missing_skills = []
    
    for req_skill in required_skills:
        if req_skill.lower() not in user_skills_lower:
            missing_skills.append(req_skill)
    
    return missing_skills

def get_skill_recommendations(current_skills, target_role):
    """Get personalized skill recommendations based on current skills and target role"""
    recommendations = {
        'Data Analyst': {
            'core': ['python', 'sql', 'excel', 'statistics', 'data visualization'],
            'advanced': ['machine learning', 'r', 'tableau', 'powerbi', 'pandas', 'numpy'],
            'tools': ['jupyter', 'git', 'aws', 'google analytics']
        },
        'Backend Developer': {
            'core': ['python', 'java', 'sql', 'rest api', 'git'],
            'advanced': ['docker', 'kubernetes', 'microservices', 'ci/cd', 'mongodb'],
            'tools': ['postman', 'jenkins', 'aws', 'redis', 'nginx']
        },
        'ML Engineer': {
            'core': ['python', 'machine learning', 'statistics', 'pandas', 'numpy'],
            'advanced': ['tensorflow', 'pytorch', 'deep learning', 'scikit-learn', 'opencv'],
            'tools': ['jupyter', 'docker', 'aws', 'git', 'mlflow']
        }
    }
    
    role_skills = recommendations.get(target_role, {})
    current_skills_lower = [skill.lower() for skill in current_skills]
    
    suggestions = {
        'missing_core': [],
        'missing_advanced': [],
        'missing_tools': []
    }
    
    for category, skills in role_skills.items():
        missing_key = f'missing_{category}'
        if missing_key in suggestions:
            for skill in skills:
                if skill.lower() not in current_skills_lower:
                    suggestions[missing_key].append(skill)
    
    return suggestions
