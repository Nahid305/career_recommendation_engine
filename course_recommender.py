# course_recommender.py
def suggest_courses(skill):
    # Static links or scrape from Udemy/Coursera
    courses = {
        'python': 'https://www.udemy.com/course/pythonforbeginners/',
        'sql': 'https://www.coursera.org/learn/sql-for-data-science',
        'aws': 'https://www.udemy.com/course/aws-certified-solutions-architect-associate/',
        'excel': 'https://www.coursera.org/learn/excel',
        'streamlit': 'https://learn.streamlit.io/',
        'data visualization': 'https://www.coursera.org/learn/datavisualization',
        'statistics': 'https://www.khanacademy.org/math/statistics-probability'
    }
    return courses.get(skill, 'No course found')
