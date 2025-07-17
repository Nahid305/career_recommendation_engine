# course_recommender.py
import logging
from typing import Dict, List, Optional
import requests
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CourseRecommender:
    def __init__(self):
        self.courses_database = self.load_courses_database()
    
    def load_courses_database(self) -> Dict[str, List[Dict]]:
        """Load comprehensive courses database"""
        return {
            'python': [
                {
                    'title': 'Python for Everybody Specialization',
                    'provider': 'Coursera',
                    'url': 'https://www.coursera.org/specializations/python',
                    'duration': '8 months',
                    'level': 'beginner',
                    'rating': 4.8,
                    'price': 'Free'
                },
                {
                    'title': 'Complete Python Bootcamp',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/complete-python-bootcamp/',
                    'duration': '22 hours',
                    'level': 'beginner',
                    'rating': 4.6,
                    'price': '$84.99'
                },
                {
                    'title': 'Python Programming',
                    'provider': 'edX',
                    'url': 'https://www.edx.org/course/python-programming',
                    'duration': '5 weeks',
                    'level': 'beginner',
                    'rating': 4.5,
                    'price': 'Free'
                }
            ],
            'sql': [
                {
                    'title': 'SQL for Data Science',
                    'provider': 'Coursera',
                    'url': 'https://www.coursera.org/learn/sql-for-data-science',
                    'duration': '4 weeks',
                    'level': 'beginner',
                    'rating': 4.6,
                    'price': 'Free'
                },
                {
                    'title': 'The Complete SQL Bootcamp',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/the-complete-sql-bootcamp/',
                    'duration': '9 hours',
                    'level': 'beginner',
                    'rating': 4.7,
                    'price': '$84.99'
                },
                {
                    'title': 'Introduction to SQL',
                    'provider': 'Khan Academy',
                    'url': 'https://www.khanacademy.org/computing/computer-programming/sql',
                    'duration': 'Self-paced',
                    'level': 'beginner',
                    'rating': 4.4,
                    'price': 'Free'
                }
            ],
            'machine learning': [
                {
                    'title': 'Machine Learning Course',
                    'provider': 'Coursera',
                    'url': 'https://www.coursera.org/learn/machine-learning',
                    'duration': '11 weeks',
                    'level': 'intermediate',
                    'rating': 4.9,
                    'price': 'Free'
                },
                {
                    'title': 'Machine Learning A-Z',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/machinelearning/',
                    'duration': '44 hours',
                    'level': 'intermediate',
                    'rating': 4.5,
                    'price': '$84.99'
                },
                {
                    'title': 'Applied Machine Learning',
                    'provider': 'edX',
                    'url': 'https://www.edx.org/course/applied-machine-learning',
                    'duration': '7 weeks',
                    'level': 'intermediate',
                    'rating': 4.6,
                    'price': 'Free'
                }
            ],
            'aws': [
                {
                    'title': 'AWS Certified Solutions Architect',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/aws-certified-solutions-architect-associate/',
                    'duration': '23 hours',
                    'level': 'intermediate',
                    'rating': 4.6,
                    'price': '$84.99'
                },
                {
                    'title': 'AWS Fundamentals',
                    'provider': 'AWS Training',
                    'url': 'https://aws.amazon.com/training/digital/',
                    'duration': 'Self-paced',
                    'level': 'beginner',
                    'rating': 4.7,
                    'price': 'Free'
                },
                {
                    'title': 'AWS Cloud Practitioner',
                    'provider': 'Coursera',
                    'url': 'https://www.coursera.org/learn/aws-cloud-practitioner-essentials',
                    'duration': '6 weeks',
                    'level': 'beginner',
                    'rating': 4.5,
                    'price': 'Free'
                }
            ],
            'excel': [
                {
                    'title': 'Excel Skills for Data Analytics',
                    'provider': 'Coursera',
                    'url': 'https://www.coursera.org/learn/excel-data-analytics',
                    'duration': '4 weeks',
                    'level': 'beginner',
                    'rating': 4.6,
                    'price': 'Free'
                },
                {
                    'title': 'Microsoft Excel - Advanced',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/microsoft-excel-advanced/',
                    'duration': '7 hours',
                    'level': 'intermediate',
                    'rating': 4.5,
                    'price': '$84.99'
                },
                {
                    'title': 'Excel Fundamentals',
                    'provider': 'Microsoft Learn',
                    'url': 'https://learn.microsoft.com/en-us/training/paths/excel-fundamentals/',
                    'duration': 'Self-paced',
                    'level': 'beginner',
                    'rating': 4.4,
                    'price': 'Free'
                }
            ],
            'react': [
                {
                    'title': 'React - The Complete Guide',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/react-the-complete-guide-incl-redux/',
                    'duration': '48 hours',
                    'level': 'intermediate',
                    'rating': 4.6,
                    'price': '$84.99'
                },
                {
                    'title': 'React Basics',
                    'provider': 'Coursera',
                    'url': 'https://www.coursera.org/learn/react-basics',
                    'duration': '4 weeks',
                    'level': 'beginner',
                    'rating': 4.5,
                    'price': 'Free'
                },
                {
                    'title': 'React Tutorial',
                    'provider': 'freeCodeCamp',
                    'url': 'https://www.freecodecamp.org/learn/front-end-development-libraries/',
                    'duration': 'Self-paced',
                    'level': 'beginner',
                    'rating': 4.7,
                    'price': 'Free'
                }
            ],
            'javascript': [
                {
                    'title': 'JavaScript Algorithms and Data Structures',
                    'provider': 'freeCodeCamp',
                    'url': 'https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/',
                    'duration': 'Self-paced',
                    'level': 'beginner',
                    'rating': 4.8,
                    'price': 'Free'
                },
                {
                    'title': 'The Complete JavaScript Course',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/the-complete-javascript-course/',
                    'duration': '69 hours',
                    'level': 'beginner',
                    'rating': 4.7,
                    'price': '$84.99'
                },
                {
                    'title': 'JavaScript Programming',
                    'provider': 'edX',
                    'url': 'https://www.edx.org/course/javascript-programming',
                    'duration': '6 weeks',
                    'level': 'beginner',
                    'rating': 4.5,
                    'price': 'Free'
                }
            ],
            'docker': [
                {
                    'title': 'Docker Mastery',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/docker-mastery/',
                    'duration': '19 hours',
                    'level': 'intermediate',
                    'rating': 4.6,
                    'price': '$84.99'
                },
                {
                    'title': 'Docker Fundamentals',
                    'provider': 'Pluralsight',
                    'url': 'https://www.pluralsight.com/courses/docker-fundamentals',
                    'duration': '4 hours',
                    'level': 'beginner',
                    'rating': 4.5,
                    'price': 'Subscription'
                },
                {
                    'title': 'Docker Tutorial',
                    'provider': 'Docker',
                    'url': 'https://docs.docker.com/get-started/',
                    'duration': 'Self-paced',
                    'level': 'beginner',
                    'rating': 4.4,
                    'price': 'Free'
                }
            ],
            'tensorflow': [
                {
                    'title': 'TensorFlow Developer Certificate',
                    'provider': 'Coursera',
                    'url': 'https://www.coursera.org/professional-certificates/tensorflow-in-practice',
                    'duration': '4 months',
                    'level': 'intermediate',
                    'rating': 4.6,
                    'price': '$49/month'
                },
                {
                    'title': 'TensorFlow for Deep Learning',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/tensorflow-for-deep-learning/',
                    'duration': '15 hours',
                    'level': 'intermediate',
                    'rating': 4.5,
                    'price': '$84.99'
                },
                {
                    'title': 'TensorFlow Tutorials',
                    'provider': 'TensorFlow',
                    'url': 'https://www.tensorflow.org/tutorials',
                    'duration': 'Self-paced',
                    'level': 'intermediate',
                    'rating': 4.7,
                    'price': 'Free'
                }
            ],
            'kubernetes': [
                {
                    'title': 'Kubernetes for Absolute Beginners',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/kubernetes-for-absolute-beginners/',
                    'duration': '6 hours',
                    'level': 'beginner',
                    'rating': 4.6,
                    'price': '$84.99'
                },
                {
                    'title': 'Kubernetes Fundamentals',
                    'provider': 'Linux Foundation',
                    'url': 'https://training.linuxfoundation.org/training/kubernetes-fundamentals/',
                    'duration': 'Self-paced',
                    'level': 'intermediate',
                    'rating': 4.5,
                    'price': '$299'
                },
                {
                    'title': 'Kubernetes Tutorial',
                    'provider': 'Kubernetes',
                    'url': 'https://kubernetes.io/docs/tutorials/',
                    'duration': 'Self-paced',
                    'level': 'intermediate',
                    'rating': 4.4,
                    'price': 'Free'
                }
            ],
            'data visualization': [
                {
                    'title': 'Data Visualization with Python',
                    'provider': 'Coursera',
                    'url': 'https://www.coursera.org/learn/python-for-data-visualization',
                    'duration': '4 weeks',
                    'level': 'intermediate',
                    'rating': 4.6,
                    'price': 'Free'
                },
                {
                    'title': 'Tableau Fundamentals',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/tableau-fundamentals/',
                    'duration': '8 hours',
                    'level': 'beginner',
                    'rating': 4.5,
                    'price': '$84.99'
                },
                {
                    'title': 'Data Visualization Basics',
                    'provider': 'edX',
                    'url': 'https://www.edx.org/course/data-visualization-basics',
                    'duration': '6 weeks',
                    'level': 'beginner',
                    'rating': 4.4,
                    'price': 'Free'
                }
            ],
            'statistics': [
                {
                    'title': 'Statistics and Probability',
                    'provider': 'Khan Academy',
                    'url': 'https://www.khanacademy.org/math/statistics-probability',
                    'duration': 'Self-paced',
                    'level': 'beginner',
                    'rating': 4.7,
                    'price': 'Free'
                },
                {
                    'title': 'Statistics for Data Science',
                    'provider': 'Coursera',
                    'url': 'https://www.coursera.org/learn/statistics-for-data-science',
                    'duration': '4 weeks',
                    'level': 'intermediate',
                    'rating': 4.5,
                    'price': 'Free'
                },
                {
                    'title': 'Business Statistics',
                    'provider': 'Udemy',
                    'url': 'https://www.udemy.com/course/business-statistics/',
                    'duration': '12 hours',
                    'level': 'intermediate',
                    'rating': 4.4,
                    'price': '$84.99'
                }
            ]
        }
    
    def suggest_courses(self, skill: str) -> str:
        """Get a single course URL for a skill (backwards compatibility)"""
        courses = self.courses_database.get(skill.lower(), [])
        if courses:
            return courses[0]['url']
        return 'https://www.google.com/search?q=' + skill.replace(' ', '+') + '+course'
    
    def get_course_recommendations(self, skill: str, limit: int = 5) -> List[Dict]:
        """Get detailed course recommendations for a skill"""
        skill_lower = skill.lower()
        
        # Direct match
        if skill_lower in self.courses_database:
            return self.courses_database[skill_lower][:limit]
        
        # Partial match
        matches = []
        for db_skill, courses in self.courses_database.items():
            if skill_lower in db_skill or db_skill in skill_lower:
                matches.extend(courses)
        
        if matches:
            return matches[:limit]
        
        # Fallback - return general programming courses
        return self.courses_database.get('python', [])[:limit]
    
    def get_learning_path(self, skills: List[str]) -> List[Dict]:
        """Get a structured learning path for multiple skills"""
        learning_path = []
        
        # Define skill dependencies
        skill_dependencies = {
            'python': [],
            'sql': [],
            'machine learning': ['python', 'statistics'],
            'tensorflow': ['python', 'machine learning'],
            'pytorch': ['python', 'machine learning'],
            'data visualization': ['python'],
            'react': ['javascript', 'html', 'css'],
            'docker': ['linux basics'],
            'kubernetes': ['docker'],
            'aws': ['linux basics'],
            'django': ['python'],
            'flask': ['python']
        }
        
        for skill in skills:
            skill_lower = skill.lower()
            prerequisites = skill_dependencies.get(skill_lower, [])
            courses = self.get_course_recommendations(skill, 3)
            
            learning_path.append({
                'skill': skill,
                'prerequisites': prerequisites,
                'courses': courses,
                'estimated_time': self.estimate_learning_time(skill),
                'difficulty': self.estimate_difficulty(skill)
            })
        
        # Sort by dependencies (skills with fewer dependencies first)
        learning_path.sort(key=lambda x: len(x['prerequisites']))
        
        return learning_path
    
    def estimate_learning_time(self, skill: str) -> str:
        """Estimate learning time for a skill"""
        time_estimates = {
            'python': '2-3 months',
            'sql': '1-2 months',
            'machine learning': '4-6 months',
            'tensorflow': '2-3 months',
            'pytorch': '2-3 months',
            'docker': '1-2 months',
            'kubernetes': '2-3 months',
            'aws': '3-4 months',
            'react': '2-3 months',
            'javascript': '2-3 months',
            'data visualization': '1-2 months',
            'statistics': '2-4 months'
        }
        return time_estimates.get(skill.lower(), '2-3 months')
    
    def estimate_difficulty(self, skill: str) -> str:
        """Estimate difficulty level of a skill"""
        difficulty_levels = {
            'python': 'beginner',
            'sql': 'beginner',
            'html': 'beginner',
            'css': 'beginner',
            'excel': 'beginner',
            'javascript': 'intermediate',
            'react': 'intermediate',
            'aws': 'intermediate',
            'docker': 'intermediate',
            'machine learning': 'advanced',
            'tensorflow': 'advanced',
            'pytorch': 'advanced',
            'kubernetes': 'advanced',
            'statistics': 'intermediate'
        }
        return difficulty_levels.get(skill.lower(), 'intermediate')
    
    def get_skill_market_value(self, skill: str) -> Dict:
        """Get market value information for a skill"""
        market_data = {
            'python': {
                'demand': 'very high',
                'salary_boost': '+$15,000',
                'job_openings': '50,000+',
                'growth_rate': '+22%'
            },
            'machine learning': {
                'demand': 'extremely high',
                'salary_boost': '+$25,000',
                'job_openings': '30,000+',
                'growth_rate': '+35%'
            },
            'aws': {
                'demand': 'high',
                'salary_boost': '+$20,000',
                'job_openings': '40,000+',
                'growth_rate': '+28%'
            },
            'react': {
                'demand': 'high',
                'salary_boost': '+$12,000',
                'job_openings': '35,000+',
                'growth_rate': '+18%'
            },
            'sql': {
                'demand': 'high',
                'salary_boost': '+$8,000',
                'job_openings': '60,000+',
                'growth_rate': '+15%'
            }
        }
        
        return market_data.get(skill.lower(), {
            'demand': 'medium',
            'salary_boost': '+$5,000',
            'job_openings': '10,000+',
            'growth_rate': '+10%'
        })
    
    def get_free_courses(self, skill: str) -> List[Dict]:
        """Get only free courses for a skill"""
        all_courses = self.get_course_recommendations(skill)
        return [course for course in all_courses if course['price'].lower() == 'free']
    
    def get_premium_courses(self, skill: str) -> List[Dict]:
        """Get premium courses for a skill"""
        all_courses = self.get_course_recommendations(skill)
        return [course for course in all_courses if course['price'].lower() != 'free']
    
    def search_courses(self, query: str) -> List[Dict]:
        """Search for courses across all skills"""
        results = []
        query_lower = query.lower()
        
        for skill, courses in self.courses_database.items():
            if query_lower in skill:
                results.extend(courses)
            else:
                # Search in course titles
                for course in courses:
                    if query_lower in course['title'].lower():
                        results.append(course)
        
        # Remove duplicates and sort by rating
        unique_results = []
        seen_urls = set()
        
        for course in results:
            if course['url'] not in seen_urls:
                unique_results.append(course)
                seen_urls.add(course['url'])
        
        return sorted(unique_results, key=lambda x: x['rating'], reverse=True)

# Initialize course recommender
course_recommender = CourseRecommender()

# Backwards compatibility functions
def suggest_courses(skill: str) -> str:
    """Backwards compatibility function"""
    return course_recommender.suggest_courses(skill)

def get_course_recommendations(skill: str, limit: int = 5) -> List[Dict]:
    """Get detailed course recommendations"""
    return course_recommender.get_course_recommendations(skill, limit)

def get_learning_path(skills: List[str]) -> List[Dict]:
    """Get learning path for multiple skills"""
    return course_recommender.get_learning_path(skills)

def get_free_courses(skill: str) -> List[Dict]:
    """Get free courses for a skill"""
    return course_recommender.get_free_courses(skill)

def search_courses(query: str) -> List[Dict]:
    """Search for courses"""
    return course_recommender.search_courses(query)
