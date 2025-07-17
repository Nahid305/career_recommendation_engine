# skill_matcher.py - Enhanced skill matching
import json
import os
from utils import calculate_skill_score, get_skills_by_category

def match_skills(user_skills, job_role):
    """
    Enhanced skill matching with detailed analysis
    """
    try:
        # Load job roles data
        data_path = os.path.join("assets", "job_roles_data.json")
        with open(data_path, "r") as f:
            job_data = json.load(f)
        
        if job_role not in job_data:
            return [], user_skills, 0
        
        role_data = job_data[job_role]
        
        # Extract all required skills from different categories
        required_skills = []
        if isinstance(role_data, dict):
            # New enhanced format
            required_skills.extend(role_data.get('core_skills', []))
            required_skills.extend(role_data.get('tools', []))
            required_skills.extend(role_data.get('advanced_skills', []))
        else:
            # Old format (list of skills)
            required_skills = role_data
        
        # Find matches and missing skills
        user_skills_lower = [skill.lower() for skill in user_skills]
        required_skills_lower = [skill.lower() for skill in required_skills]
        
        matched = []
        for skill in required_skills:
            if skill.lower() in user_skills_lower:
                matched.append(skill)
        
        missing = []
        for skill in required_skills:
            if skill.lower() not in user_skills_lower:
                missing.append(skill)
        
        # Calculate match percentage using enhanced scoring
        match_percent = calculate_skill_score(user_skills, required_skills)
        
        return matched, missing, match_percent
        
    except Exception as e:
        print(f"Error in match_skills: {str(e)}")
        return [], user_skills, 0

def get_detailed_skill_analysis(user_skills, job_role):
    """
    Get detailed analysis of skill matching
    """
    try:
        data_path = os.path.join("assets", "job_roles_data.json")
        with open(data_path, "r") as f:
            job_data = json.load(f)
        
        if job_role not in job_data:
            return {}
        
        role_data = job_data[job_role]
        
        if not isinstance(role_data, dict):
            # Handle old format
            matched, missing, score = match_skills(user_skills, job_role)
            return {
                'overall_score': score,
                'matched_skills': matched,
                'missing_skills': missing,
                'category_breakdown': {}
            }
        
        # Detailed analysis for new format
        analysis = {
            'overall_score': 0,
            'matched_skills': [],
            'missing_skills': [],
            'category_breakdown': {},
            'recommendations': []
        }
        
        skill_categories = ['core_skills', 'tools', 'advanced_skills']
        user_skills_lower = [skill.lower() for skill in user_skills]
        
        total_score = 0
        total_weight = 0
        
        for category in skill_categories:
            if category not in role_data:
                continue
                
            category_skills = role_data[category]
            category_matched = []
            category_missing = []
            
            for skill in category_skills:
                if skill.lower() in user_skills_lower:
                    category_matched.append(skill)
                    analysis['matched_skills'].append(skill)
                else:
                    category_missing.append(skill)
                    analysis['missing_skills'].append(skill)
            
            # Calculate category score
            if category_skills:
                category_score = (len(category_matched) / len(category_skills)) * 100
            else:
                category_score = 100
            
            # Weight categories differently
            weights = {
                'core_skills': 0.5,
                'tools': 0.3,
                'advanced_skills': 0.2
            }
            
            weight = weights.get(category, 0.33)
            total_score += category_score * weight
            total_weight += weight
            
            analysis['category_breakdown'][category] = {
                'score': category_score,
                'matched': category_matched,
                'missing': category_missing,
                'total_skills': len(category_skills)
            }
        
        analysis['overall_score'] = int(total_score / total_weight) if total_weight > 0 else 0
        
        # Generate recommendations
        analysis['recommendations'] = generate_skill_recommendations(analysis, role_data)
        
        return analysis
        
    except Exception as e:
        print(f"Error in get_detailed_skill_analysis: {str(e)}")
        return {}

def generate_skill_recommendations(analysis, role_data):
    """
    Generate personalized skill recommendations
    """
    recommendations = []
    
    # Priority recommendations based on missing core skills
    core_missing = analysis['category_breakdown'].get('core_skills', {}).get('missing', [])
    if core_missing:
        recommendations.append({
            'priority': 'High',
            'category': 'Core Skills',
            'skills': core_missing[:3],  # Top 3
            'reason': 'Essential skills for this role'
        })
    
    # Tool recommendations
    tools_missing = analysis['category_breakdown'].get('tools', {}).get('missing', [])
    if tools_missing:
        recommendations.append({
            'priority': 'Medium',
            'category': 'Tools & Technologies',
            'skills': tools_missing[:3],
            'reason': 'Important tools that increase productivity'
        })
    
    # Advanced skill recommendations
    advanced_missing = analysis['category_breakdown'].get('advanced_skills', {}).get('missing', [])
    if advanced_missing:
        recommendations.append({
            'priority': 'Low',
            'category': 'Advanced Skills',
            'skills': advanced_missing[:2],
            'reason': 'Skills that help you stand out'
        })
    
    return recommendations

def get_role_comparison(user_skills, roles_to_compare=None):
    """
    Compare user skills against multiple roles
    """
    if roles_to_compare is None:
        roles_to_compare = ["Data Analyst", "Backend Developer", "ML Engineer", "Frontend Developer", "DevOps Engineer"]
    
    comparison_results = {}
    
    for role in roles_to_compare:
        analysis = get_detailed_skill_analysis(user_skills, role)
        if analysis:
            comparison_results[role] = {
                'score': analysis['overall_score'],
                'matched_count': len(analysis['matched_skills']),
                'missing_count': len(analysis['missing_skills']),
                'top_matches': analysis['matched_skills'][:5],
                'key_missing': analysis['missing_skills'][:3]
            }
    
    # Sort by score
    sorted_roles = sorted(comparison_results.items(), key=lambda x: x[1]['score'], reverse=True)
    
    return dict(sorted_roles)

def get_skill_gap_analysis(user_skills, target_role):
    """
    Detailed skill gap analysis for a target role
    """
    analysis = get_detailed_skill_analysis(user_skills, target_role)
    
    if not analysis:
        return {}
    
    gap_analysis = {
        'current_strength': analysis['overall_score'],
        'strength_level': get_strength_level(analysis['overall_score']),
        'gaps': [],
        'learning_path': [],
        'time_estimate': estimate_learning_time(analysis['missing_skills'])
    }
    
    # Identify gaps by priority
    for category, data in analysis['category_breakdown'].items():
        if data['missing']:
            gap_analysis['gaps'].append({
                'category': category.replace('_', ' ').title(),
                'missing_skills': data['missing'],
                'completion_rate': f"{len(data['matched'])}/{data['total_skills']}",
                'priority': get_category_priority(category)
            })
    
    # Generate learning path
    gap_analysis['learning_path'] = generate_learning_path(analysis['missing_skills'])
    
    return gap_analysis

def get_strength_level(score):
    """
    Convert numerical score to strength level
    """
    if score >= 80:
        return "Expert"
    elif score >= 60:
        return "Intermediate"
    elif score >= 40:
        return "Beginner"
    else:
        return "Novice"

def get_category_priority(category):
    """
    Get priority level for different skill categories
    """
    priority_map = {
        'core_skills': 'High',
        'tools': 'Medium',
        'advanced_skills': 'Low'
    }
    return priority_map.get(category, 'Medium')

def estimate_learning_time(missing_skills):
    """
    Estimate time needed to learn missing skills
    """
    if not missing_skills:
        return "0 months"
    
    # Basic estimation: 1-2 months per skill depending on complexity
    skill_complexity = {
        'python': 3,
        'machine learning': 6,
        'deep learning': 8,
        'sql': 2,
        'excel': 1,
        'tableau': 2,
        'powerbi': 2,
        'docker': 3,
        'kubernetes': 4,
        'aws': 4,
        'django': 3,
        'flask': 2,
        'react': 3,
        'angular': 4,
        'vue': 2
    }
    
    total_months = 0
    for skill in missing_skills:
        skill_months = skill_complexity.get(skill.lower(), 2)  # Default 2 months
        total_months += skill_months
    
    # Assuming parallel learning, reduce total time
    estimated_months = min(total_months, total_months * 0.6)
    
    if estimated_months <= 3:
        return "1-3 months"
    elif estimated_months <= 6:
        return "3-6 months"
    elif estimated_months <= 12:
        return "6-12 months"
    else:
        return "12+ months"

def generate_learning_path(missing_skills):
    """
    Generate a structured learning path
    """
    if not missing_skills:
        return []
    
    # Skill dependencies and learning order
    learning_order = {
        'beginner': ['python', 'sql', 'excel', 'html', 'css'],
        'intermediate': ['javascript', 'pandas', 'numpy', 'git', 'django', 'flask'],
        'advanced': ['machine learning', 'deep learning', 'docker', 'kubernetes', 'aws', 'react', 'angular']
    }
    
    path = []
    missing_lower = [skill.lower() for skill in missing_skills]
    
    for level, skills in learning_order.items():
        level_skills = [skill for skill in skills if skill in missing_lower]
        if level_skills:
            path.append({
                'level': level.title(),
                'skills': level_skills,
                'duration': f"{len(level_skills) * 2} weeks" if level == 'beginner' else f"{len(level_skills) * 4} weeks"
            })
    
    return path
