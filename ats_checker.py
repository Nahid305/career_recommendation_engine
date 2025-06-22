def get_ats_score_and_feedback(resume_text, role):
    keywords = {
        "Data Analyst": ["python", "sql", "excel", "visualization"],
        "Backend Developer": ["django", "rest api", "sql", "python"],
        "ML Engineer": ["machine learning", "tensorflow", "scikit-learn", "python"]
    }

    role_keywords = keywords.get(role, [])
    resume_text = resume_text.lower()
    matched = [kw for kw in role_keywords if kw in resume_text]

    score = int((len(matched) / len(role_keywords)) * 100) if role_keywords else 0
    feedback = []
    for kw in role_keywords:
        if kw not in resume_text:
            feedback.append(f"Add the keyword '{kw}' to improve your resume for {role}.")

    return score, feedback
