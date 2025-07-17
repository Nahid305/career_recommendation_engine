def get_interview_questions(role):
    questions = {
        "Data Analyst": [
            "What is the difference between inner and outer join?",
            "How do you handle missing data in a dataset?",
            "Explain a time when you built a dashboard.",
            "What is data cleaning and why is it important?",
            "How do you identify outliers in a dataset?",
            "Explain the difference between correlation and causation.",
            "What tools do you use for data visualization?",
            "How do you ensure data quality in your analysis?"
        ],
        "Backend Developer": [
            "What is REST and how does it work?",
            "Explain how authentication and authorization work in web apps.",
            "How do you scale a backend service?",
            "What is the difference between SQL and NoSQL databases?",
            "Explain microservices architecture.",
            "How do you handle database migrations?",
            "What is API rate limiting and why is it important?",
            "Explain the concept of caching in backend systems."
        ],
        "ML Engineer": [
            "What's the difference between overfitting and underfitting?",
            "Explain a project where you applied machine learning.",
            "What are hyperparameters, and how do you tune them?",
            "How do you evaluate machine learning models?",
            "What is cross-validation and why is it important?",
            "Explain the bias-variance tradeoff.",
            "How do you handle imbalanced datasets?",
            "What is feature engineering and why is it important?"
        ]
    }
    return questions.get(role, [])


def get_interview_tips(role, question):
    """Get specific tips for answering interview questions"""
    tips_db = {
        "Data Analyst": {
            "What is the difference between inner and outer join?": [
                "Draw a Venn diagram to illustrate the concept visually",
                "Provide concrete examples with sample data",
                "Mention performance implications of different join types",
                "Explain when to use each type of join"
            ],
            "How do you handle missing data in a dataset?": [
                "Discuss different strategies: deletion, imputation, prediction",
                "Explain when to use each approach",
                "Mention tools like pandas for handling missing data",
                "Give examples of business impact of missing data"
            ],
            "default": [
                "Use specific examples from your experience",
                "Mention relevant tools and technologies",
                "Explain your thought process step-by-step",
                "Connect your answer to business impact"
            ]
        },
        "Backend Developer": {
            "What is REST and how does it work?": [
                "Explain the key principles: stateless, cacheable, uniform interface",
                "Describe HTTP methods (GET, POST, PUT, DELETE)",
                "Give examples of RESTful API design",
                "Mention status codes and their meanings"
            ],
            "How do you scale a backend service?": [
                "Discuss horizontal vs vertical scaling",
                "Mention load balancing and database sharding",
                "Explain caching strategies",
                "Talk about microservices architecture"
            ],
            "default": [
                "Provide code examples when appropriate",
                "Discuss trade-offs and design decisions",
                "Mention scalability and performance considerations",
                "Connect to real-world scenarios"
            ]
        },
        "ML Engineer": {
            "What's the difference between overfitting and underfitting?": [
                "Explain using bias-variance tradeoff",
                "Provide visual examples or graphs",
                "Discuss regularization techniques",
                "Mention cross-validation for detection"
            ],
            "What are hyperparameters, and how do you tune them?": [
                "Explain difference from model parameters",
                "Discuss grid search, random search, and Bayesian optimization",
                "Mention validation strategies",
                "Give specific examples for common algorithms"
            ],
            "default": [
                "Use mathematical concepts appropriately",
                "Mention specific algorithms and frameworks",
                "Discuss model evaluation metrics",
                "Explain real-world implementation challenges"
            ]
        }
    }
    
    role_tips = tips_db.get(role, {})
    return role_tips.get(question, role_tips.get("default", [
        "Structure your answer clearly",
        "Use specific examples",
        "Show your problem-solving approach",
        "Demonstrate technical knowledge"
    ]))


def get_preparation_links(role):
    return {
        "GeeksForGeeks Interview Prep": "https://www.geeksforgeeks.org/interview-corner/",
        "Glassdoor Experiences": "https://www.glassdoor.co.in/Interview/index.htm",
        "Leetcode Discussion": "https://leetcode.com/discuss/interview-question/",
        "AmbitionBox PYQs": "https://www.ambitionbox.com/interviews"
    }
