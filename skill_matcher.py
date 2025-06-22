# skill_matcher.py
import json

def match_skills(user_skills, job_role):
    with open("assets/job_roles_data.json", "r") as f:
        job_data = json.load(f)

    required_skills = job_data[job_role]
    matched = list(set(user_skills).intersection(required_skills))
    missing = list(set(required_skills) - set(user_skills))

    match_percent = int((len(matched) / len(required_skills)) * 100)

    return matched, missing, match_percent
