# utils.py
skills_list = ['python', 'sql', 'machine learning', 'data analysis', 'aws', 'excel', 'streamlit']

def extract_skills(text):
    text = text.lower()
    return [skill for skill in skills_list if skill in text]
