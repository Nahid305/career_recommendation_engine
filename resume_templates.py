def get_resume_template(role):
    templates = {
        "Data Analyst": "https://www.overleaf.com/latex/templates/data-analyst-resume-template/qhzqvkwvnkkp",
        "Backend Developer": "https://www.overleaf.com/latex/templates/backend-developer-resume/mqtrdnfdwbkb",
        "ML Engineer": "https://www.overleaf.com/latex/templates/machine-learning-engineer-resume/qbhfpbxfjbng"
    }
    return templates.get(role, "https://www.overleaf.com/gallery")

