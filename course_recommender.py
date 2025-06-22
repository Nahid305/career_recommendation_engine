# course_recommender.py
def suggest_courses(skill):
    # Static links or scrape from Udemy/Coursera
    courses = {
        'python': 'https://www.udemy.com/course/pythonforbeginners/',
        'sql': 'https://www.coursera.org/learn/sql-for-data-science',
        'aws': 'https://www.udemy.com/course/aws-certified-solutions-architect-associate/',
    }
    return courses.get(skill, 'No course found')
