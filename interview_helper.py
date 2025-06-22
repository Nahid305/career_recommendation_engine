def get_interview_questions(role):
    questions = {
        "Data Analyst": [
            "What is the difference between inner and outer join?",
            "How do you handle missing data in a dataset?",
            "Explain a time when you built a dashboard."
        ],
        "Backend Developer": [
            "What is REST and how does it work?",
            "Explain how authentication and authorization work in web apps.",
            "How do you scale a backend service?"
        ],
        "ML Engineer": [
            "What’s the difference between overfitting and underfitting?",
            "Explain a project where you applied machine learning.",
            "What are hyperparameters, and how do you tune them?"
        ]
    }
    return questions.get(role, [])


def get_preparation_links(role):
    return {
        "GeeksForGeeks Interview Prep": "https://www.geeksforgeeks.org/interview-corner/",
        "Glassdoor Experiences": "https://www.glassdoor.co.in/Interview/index.htm",
        "Leetcode Discussion": "https://leetcode.com/discuss/interview-question/",
        "AmbitionBox PYQs": "https://www.ambitionbox.com/interviews"
    }
