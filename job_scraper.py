# job_scraper.py
import requests
import logging
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class JobScraper:
    def __init__(self):
        self.job_database = self.load_job_database()
        self.location_mapping = {
            'remote': ['Remote', 'Work from Home', 'Anywhere'],
            'mumbai': ['Mumbai', 'Navi Mumbai', 'Thane'],
            'bangalore': ['Bangalore', 'Bengaluru', 'Whitefield'],
            'delhi': ['Delhi', 'New Delhi', 'Gurgaon', 'Noida'],
            'hyderabad': ['Hyderabad', 'Secunderabad', 'Cyberabad'],
            'pune': ['Pune', 'Pimpri-Chinchwad'],
            'chennai': ['Chennai', 'Tambaram'],
            'kolkata': ['Kolkata', 'Howrah']
        }
    
    def load_job_database(self) -> Dict[str, List[Dict]]:
        """Load comprehensive job database"""
        return {
            "Data Analyst": [
                {
                    "company": "TCS",
                    "title": "Data Analyst",
                    "location": "Mumbai",
                    "link": "https://www.tcs.com/careers",
                    "salary": "₹6.5 - 9.5 LPA",
                    "experience": "1-3 years",
                    "posted_date": "2024-01-15",
                    "description": "Analyze large datasets to provide business insights and drive data-driven decisions",
                    "requirements": ["Python", "SQL", "Excel", "Tableau"],
                    "company_size": "Large",
                    "job_type": "Full-time",
                    "remote_option": "Hybrid",
                    "benefits": ["Health Insurance", "Flexible Hours", "Learning Budget"]
                },
                {
                    "company": "Infosys",
                    "title": "Business Data Analyst",
                    "location": "Pune",
                    "link": "https://www.infosys.com/careers",
                    "salary": "₹7.2 - 11.8 LPA",
                    "experience": "2-4 years",
                    "posted_date": "2024-01-14",
                    "description": "Transform business requirements into analytical solutions using advanced analytics",
                    "requirements": ["SQL", "Python", "PowerBI", "Statistics"],
                    "company_size": "Large",
                    "job_type": "Full-time",
                    "remote_option": "Hybrid",
                    "benefits": ["Health Insurance", "Provident Fund", "Flexible Hours", "Training Budget"]
                },
                {
                    "company": "Wipro",
                    "title": "Senior Data Analyst",
                    "location": "Hyderabad",
                    "link": "https://careers.wipro.com",
                    "salary": "₹6.0 - 8.0 LPA",
                    "experience": "3-5 years",
                    "posted_date": "2024-01-13",
                    "description": "Lead data analysis projects and mentor junior analysts in global delivery model",
                    "requirements": ["Python", "SQL", "R", "Machine Learning"],
                    "company_size": "Large",
                    "job_type": "Full-time",
                    "remote_option": "Hybrid",
                    "benefits": ["Health Insurance", "Life Insurance", "Gratuity", "Performance Bonus"]
                },
                {
                    "company": "Fractal Analytics",
                    "title": "Data Analyst - Python",
                    "location": "Bangalore",
                    "link": "https://fractal.ai/careers/",
                    "salary": "₹6.5 - 8.5 LPA",
                    "experience": "1-3 years",
                    "posted_date": "2024-01-12",
                    "description": "Build predictive models and analyze customer behavior for Fortune 500 clients",
                    "requirements": ["Python", "SQL", "Pandas", "Numpy"],
                    "company_size": "Medium",
                    "job_type": "Full-time",
                    "remote_option": "Office-based",
                    "benefits": ["Health Insurance", "Stock Options", "Learning Budget", "Flexible Hours"]
                },
                {
                    "company": "Razorpay",
                    "title": "Data Analyst Intern",
                    "location": "Remote",
                    "link": "https://razorpay.com/careers/",
                    "salary": "₹3.5 - 4.5 LPA",
                    "experience": "0-1 years",
                    "posted_date": "2024-01-11",
                    "description": "Support data-driven decision making across fintech teams",
                    "requirements": ["SQL", "Excel", "Python", "Tableau"],
                    "company_size": "Medium",
                    "job_type": "Internship",
                    "remote_option": "Remote",
                    "benefits": ["Health Insurance", "Meal Allowance", "Learning Budget", "Flexible Hours"]
                },
                {
                    "company": "Paytm",
                    "title": "Junior Data Analyst",
                    "location": "Noida",
                    "link": "https://paytm.com/careers",
                    "salary": "₹4.5 - 6.0 LPA",
                    "experience": "1-2 years",
                    "posted_date": "2024-01-10",
                    "description": "Analyze payment patterns and user behavior in digital payments ecosystem",
                    "requirements": ["SQL", "Python", "Excel", "Statistics"],
                    "company_size": "Large",
                    "job_type": "Full-time",
                    "remote_option": "Hybrid",
                    "benefits": ["Health Insurance", "Life Insurance", "ESOP", "Wellness Programs"]
                },
                {
                    "company": "Swiggy",
                    "title": "Data Analyst - Growth",
                    "location": "Bangalore",
                    "link": "https://careers.swiggy.com",
                    "salary": "₹7.0 - 9.0 LPA",
                    "experience": "2-4 years",
                    "posted_date": "2024-01-09",
                    "description": "Drive growth initiatives through data analysis in food delivery ecosystem",
                    "requirements": ["Python", "SQL", "A/B Testing", "Statistics"],
                    "company_size": "Large",
                    "job_type": "Full-time",
                    "remote_option": "Hybrid",
                    "benefits": ["Health Insurance", "Food Allowance", "Stock Options", "Flexible Hours"]
                },
                {
                    "company": "Zomato",
                    "title": "Data Analyst",
                    "location": "Gurgaon",
                    "link": "https://www.zomato.com/careers",
                    "salary": "₹5.5 - 7.5 LPA",
                    "experience": "1-3 years",
                    "posted_date": "2024-01-08",
                    "description": "Analyze restaurant and delivery data for insights in food-tech industry",
                    "requirements": ["SQL", "Python", "Tableau", "Excel"],
                    "company_size": "Large",
                    "job_type": "Full-time",
                    "remote_option": "Office-based",
                    "benefits": ["Health Insurance", "Meal Vouchers", "Performance Bonus", "Learning Budget"]
                }
            ],
            "Backend Developer": [
                {
                    "company": "Amazon",
                    "title": "Backend Developer",
                    "location": "Hyderabad",
                    "link": "https://www.amazon.jobs",
                    "salary": "₹8.0 - 12.0 LPA",
                    "experience": "2-5 years",
                    "posted_date": "2024-01-15",
                    "description": "Build scalable backend systems for e-commerce platform serving millions of customers",
                    "requirements": ["Java", "Spring", "AWS", "Microservices"],
                    "company_size": "Large",
                    "job_type": "Full-time",
                    "remote_option": "Hybrid",
                    "benefits": ["Health Insurance", "Stock Options", "Relocation Assistance", "Learning Budget"]
                },
                {
                    "company": "Flipkart",
                    "title": "Java Backend Developer",
                    "location": "Bangalore",
                    "link": "https://www.flipkartcareers.com",
                    "salary": "$75,000 - $110,000",
                    "experience": "3-6 years",
                    "posted_date": "2024-01-14",
                    "description": "Develop high-performance backend services",
                    "requirements": ["Java", "Spring Boot", "MySQL", "Redis"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Google",
                    "title": "Senior Backend Engineer",
                    "location": "Bangalore",
                    "link": "https://careers.google.com",
                    "salary": "$100,000 - $150,000",
                    "experience": "4-8 years",
                    "posted_date": "2024-01-13",
                    "description": "Design and implement backend infrastructure",
                    "requirements": ["Go", "Python", "Kubernetes", "GCP"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Microsoft",
                    "title": "Backend Software Engineer",
                    "location": "Hyderabad",
                    "link": "https://careers.microsoft.com",
                    "salary": "$90,000 - $130,000",
                    "experience": "2-5 years",
                    "posted_date": "2024-01-12",
                    "description": "Build cloud-native applications and services",
                    "requirements": ["C#", ".NET", "Azure", "SQL Server"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Zomato",
                    "title": "Python Backend Developer",
                    "location": "Gurgaon",
                    "link": "https://www.zomato.com/careers",
                    "salary": "$70,000 - $95,000",
                    "experience": "2-4 years",
                    "posted_date": "2024-01-11",
                    "description": "Develop APIs for food delivery platform",
                    "requirements": ["Python", "Django", "PostgreSQL", "Redis"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Paytm",
                    "title": "Backend Developer – Node.js",
                    "location": "Noida",
                    "link": "https://paytm.com/careers",
                    "salary": "$65,000 - $85,000",
                    "experience": "1-3 years",
                    "posted_date": "2024-01-10",
                    "description": "Build payment processing systems",
                    "requirements": ["Node.js", "Express", "MongoDB", "AWS"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Razorpay",
                    "title": "Backend Engineer - Go",
                    "location": "Remote",
                    "link": "https://razorpay.com/careers/",
                    "salary": "$85,000 - $110,000",
                    "experience": "3-5 years",
                    "posted_date": "2024-01-09",
                    "description": "Build high-performance payment infrastructure",
                    "requirements": ["Go", "PostgreSQL", "Redis", "Kubernetes"],
                    "company_size": "Medium",
                    "job_type": "Full-time"
                }
            ],
            "ML Engineer": [
                {
                    "company": "Google",
                    "title": "Machine Learning Engineer",
                    "location": "Bangalore",
                    "link": "https://careers.google.com",
                    "salary": "$120,000 - $180,000",
                    "experience": "3-6 years",
                    "posted_date": "2024-01-15",
                    "description": "Build and deploy ML models at scale",
                    "requirements": ["Python", "TensorFlow", "Kubernetes", "GCP"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "OpenAI",
                    "title": "AI Research Engineer",
                    "location": "Remote",
                    "link": "https://openai.com/careers",
                    "salary": "$150,000 - $250,000",
                    "experience": "4-8 years",
                    "posted_date": "2024-01-14",
                    "description": "Research and develop cutting-edge AI models",
                    "requirements": ["Python", "PyTorch", "Research", "Deep Learning"],
                    "company_size": "Medium",
                    "job_type": "Full-time"
                },
                {
                    "company": "Microsoft",
                    "title": "Applied ML Engineer",
                    "location": "Hyderabad",
                    "link": "https://careers.microsoft.com",
                    "salary": "$110,000 - $160,000",
                    "experience": "2-5 years",
                    "posted_date": "2024-01-13",
                    "description": "Apply ML to solve real-world problems",
                    "requirements": ["Python", "Azure ML", "MLOps", "TensorFlow"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Flipkart",
                    "title": "ML Engineer - Recommendations",
                    "location": "Bangalore",
                    "link": "https://www.flipkartcareers.com",
                    "salary": "$90,000 - $130,000",
                    "experience": "2-4 years",
                    "posted_date": "2024-01-12",
                    "description": "Build recommendation systems for e-commerce",
                    "requirements": ["Python", "Spark", "Kafka", "TensorFlow"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Swiggy",
                    "title": "ML Engineer - Delivery",
                    "location": "Bangalore",
                    "link": "https://careers.swiggy.com",
                    "salary": "$95,000 - $125,000",
                    "experience": "2-4 years",
                    "posted_date": "2024-01-11",
                    "description": "Optimize delivery routes using ML",
                    "requirements": ["Python", "Scikit-learn", "AWS", "Docker"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Ola",
                    "title": "ML Engineer - Pricing",
                    "location": "Bangalore",
                    "link": "https://www.olacabs.com/careers",
                    "salary": "$85,000 - $115,000",
                    "experience": "1-3 years",
                    "posted_date": "2024-01-10",
                    "description": "Build dynamic pricing models",
                    "requirements": ["Python", "PyTorch", "Kubernetes", "AWS"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                }
            ],
            "Frontend Developer": [
                {
                    "company": "Meta",
                    "title": "Frontend Engineer",
                    "location": "Remote",
                    "link": "https://careers.meta.com",
                    "salary": "$90,000 - $140,000",
                    "experience": "2-5 years",
                    "posted_date": "2024-01-15",
                    "description": "Build user interfaces for social media platforms",
                    "requirements": ["React", "JavaScript", "TypeScript", "GraphQL"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Netflix",
                    "title": "Senior Frontend Developer",
                    "location": "Remote",
                    "link": "https://jobs.netflix.com",
                    "salary": "$100,000 - $150,000",
                    "experience": "4-7 years",
                    "posted_date": "2024-01-14",
                    "description": "Create streaming platform user experiences",
                    "requirements": ["React", "TypeScript", "Node.js", "Testing"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Airbnb",
                    "title": "Frontend Engineer - React",
                    "location": "Remote",
                    "link": "https://careers.airbnb.com",
                    "salary": "$85,000 - $125,000",
                    "experience": "2-4 years",
                    "posted_date": "2024-01-13",
                    "description": "Build booking and host management interfaces",
                    "requirements": ["React", "Redux", "CSS", "Jest"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Zomato",
                    "title": "Frontend Developer",
                    "location": "Gurgaon",
                    "link": "https://www.zomato.com/careers",
                    "salary": "$60,000 - $85,000",
                    "experience": "1-3 years",
                    "posted_date": "2024-01-12",
                    "description": "Build responsive web applications",
                    "requirements": ["React", "JavaScript", "SASS", "Webpack"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Freshworks",
                    "title": "React Developer",
                    "location": "Chennai",
                    "link": "https://www.freshworks.com/company/careers",
                    "salary": "$55,000 - $80,000",
                    "experience": "1-3 years",
                    "posted_date": "2024-01-11",
                    "description": "Develop CRM and customer service interfaces",
                    "requirements": ["React", "JavaScript", "HTML", "CSS"],
                    "company_size": "Medium",
                    "job_type": "Full-time"
                }
            ],
            "DevOps Engineer": [
                {
                    "company": "Amazon",
                    "title": "DevOps Engineer",
                    "location": "Mumbai",
                    "link": "https://www.amazon.jobs",
                    "salary": "$95,000 - $140,000",
                    "experience": "3-6 years",
                    "posted_date": "2024-01-15",
                    "description": "Manage cloud infrastructure and CI/CD pipelines",
                    "requirements": ["AWS", "Kubernetes", "Docker", "Terraform"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Google",
                    "title": "Site Reliability Engineer",
                    "location": "Bangalore",
                    "link": "https://careers.google.com",
                    "salary": "$110,000 - $160,000",
                    "experience": "4-8 years",
                    "posted_date": "2024-01-14",
                    "description": "Ensure system reliability and performance",
                    "requirements": ["GCP", "Kubernetes", "Python", "Monitoring"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Microsoft",
                    "title": "Azure DevOps Engineer",
                    "location": "Hyderabad",
                    "link": "https://careers.microsoft.com",
                    "salary": "$90,000 - $130,000",
                    "experience": "2-5 years",
                    "posted_date": "2024-01-13",
                    "description": "Build and maintain Azure infrastructure",
                    "requirements": ["Azure", "PowerShell", "ARM Templates", "CI/CD"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Uber",
                    "title": "DevOps Engineer - Platform",
                    "location": "Bangalore",
                    "link": "https://www.uber.com/careers",
                    "salary": "$85,000 - $120,000",
                    "experience": "2-4 years",
                    "posted_date": "2024-01-12",
                    "description": "Scale platform infrastructure globally",
                    "requirements": ["Docker", "Kubernetes", "AWS", "Python"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                }
            ],
            "Data Scientist": [
                {
                    "company": "Netflix",
                    "title": "Data Scientist",
                    "location": "Remote",
                    "link": "https://jobs.netflix.com",
                    "salary": "$120,000 - $180,000",
                    "experience": "3-6 years",
                    "posted_date": "2024-01-15",
                    "description": "Analyze viewer behavior and content performance",
                    "requirements": ["Python", "R", "Statistics", "Machine Learning"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Spotify",
                    "title": "Senior Data Scientist",
                    "location": "Remote",
                    "link": "https://www.lifeatspotify.com/jobs",
                    "salary": "$130,000 - $200,000",
                    "experience": "4-7 years",
                    "posted_date": "2024-01-14",
                    "description": "Build music recommendation algorithms",
                    "requirements": ["Python", "Scala", "Spark", "Deep Learning"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "LinkedIn",
                    "title": "Data Scientist - Growth",
                    "location": "Remote",
                    "link": "https://careers.linkedin.com",
                    "salary": "$110,000 - $160,000",
                    "experience": "2-5 years",
                    "posted_date": "2024-01-13",
                    "description": "Drive user growth through data insights",
                    "requirements": ["Python", "SQL", "A/B Testing", "Statistics"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                },
                {
                    "company": "Flipkart",
                    "title": "Data Scientist - Pricing",
                    "location": "Bangalore",
                    "link": "https://www.flipkartcareers.com",
                    "salary": "$85,000 - $125,000",
                    "experience": "2-4 years",
                    "posted_date": "2024-01-12",
                    "description": "Optimize pricing strategies using data",
                    "requirements": ["Python", "SQL", "Machine Learning", "Economics"],
                    "company_size": "Large",
                    "job_type": "Full-time"
                }
            ]
        }
    
    def get_jobs_for_role(self, role: str, limit: int = 10) -> List[Dict]:
        """Get jobs for a specific role"""
        jobs = self.job_database.get(role, [])
        return jobs[:limit]
    
    def search_jobs_with_filters(self, role: str = None, location: str = None, 
                               experience: str = None, salary_min: int = None,
                               company_size: str = None, job_type: str = None) -> List[Dict]:
        """Advanced job search with filters"""
        all_jobs = []
        
        # Get jobs from specific role or all roles
        if role:
            all_jobs = self.job_database.get(role, [])
        else:
            for role_jobs in self.job_database.values():
                all_jobs.extend(role_jobs)
        
        # Apply filters
        filtered_jobs = []
        
        for job in all_jobs:
            # Location filter
            if location:
                job_location = job.get('location', '').lower()
                location_lower = location.lower()
                
                # Check if location matches directly or through mapping
                location_match = False
                if location_lower in job_location:
                    location_match = True
                else:
                    # Check location mapping
                    for key, locations in self.location_mapping.items():
                        if location_lower in key:
                            if any(loc.lower() in job_location for loc in locations):
                                location_match = True
                                break
                
                if not location_match:
                    continue
            
            # Experience filter (simplified)
            if experience:
                job_experience = job.get('experience', '').lower()
                if experience.lower() not in job_experience:
                    continue
            
            # Salary filter (simplified)
            if salary_min:
                job_salary = job.get('salary', '')
                # Extract minimum salary from range (simplified)
                try:
                    salary_parts = job_salary.split(' - ')
                    if len(salary_parts) > 0:
                        min_salary_str = salary_parts[0].replace('$', '').replace(',', '')
                        min_salary = int(min_salary_str)
                        if min_salary < salary_min:
                            continue
                except:
                    continue
            
            # Company size filter
            if company_size:
                job_company_size = job.get('company_size', '').lower()
                if company_size.lower() not in job_company_size:
                    continue
            
            # Job type filter
            if job_type:
                job_job_type = job.get('job_type', '').lower()
                if job_type.lower() not in job_job_type:
                    continue
            
            filtered_jobs.append(job)
        
        return filtered_jobs
    
    def get_trending_jobs(self, limit: int = 10) -> List[Dict]:
        """Get trending jobs across all roles"""
        all_jobs = []
        for role_jobs in self.job_database.values():
            all_jobs.extend(role_jobs)
        
        # Sort by posting date (most recent first)
        all_jobs.sort(key=lambda x: x.get('posted_date', ''), reverse=True)
        
        return all_jobs[:limit]
    
    def get_remote_jobs(self, limit: int = 10) -> List[Dict]:
        """Get remote job opportunities"""
        return self.search_jobs_with_filters(location='remote')[:limit]
    
    def get_high_paying_jobs(self, min_salary: int = 100000, limit: int = 10) -> List[Dict]:
        """Get high-paying jobs"""
        return self.search_jobs_with_filters(salary_min=min_salary)[:limit]
    
    def get_entry_level_jobs(self, limit: int = 10) -> List[Dict]:
        """Get entry-level jobs"""
        entry_keywords = ['0-1', '1-2', 'entry', 'junior', 'intern']
        all_jobs = []
        for role_jobs in self.job_database.values():
            all_jobs.extend(role_jobs)
        
        entry_jobs = []
        for job in all_jobs:
            experience = job.get('experience', '').lower()
            if any(keyword in experience for keyword in entry_keywords):
                entry_jobs.append(job)
        
        return entry_jobs[:limit]
    
    def get_company_jobs(self, company_name: str) -> List[Dict]:
        """Get jobs from a specific company"""
        company_jobs = []
        for role_jobs in self.job_database.values():
            for job in role_jobs:
                if company_name.lower() in job.get('company', '').lower():
                    company_jobs.append(job)
        
        return company_jobs
    
    def get_job_market_stats(self) -> Dict:
        """Get job market statistics"""
        all_jobs = []
        for role_jobs in self.job_database.values():
            all_jobs.extend(role_jobs)
        
        # Count by location
        location_counts = {}
        for job in all_jobs:
            location = job.get('location', 'Unknown')
            location_counts[location] = location_counts.get(location, 0) + 1
        
        # Count by company size
        company_size_counts = {}
        for job in all_jobs:
            size = job.get('company_size', 'Unknown')
            company_size_counts[size] = company_size_counts.get(size, 0) + 1
        
        # Average salary calculation (simplified)
        salaries = []
        for job in all_jobs:
            salary_str = job.get('salary', '')
            if salary_str and '$' in salary_str:
                try:
                    # Extract average from range
                    salary_parts = salary_str.split(' - ')
                    if len(salary_parts) == 2:
                        min_sal = int(salary_parts[0].replace('$', '').replace(',', ''))
                        max_sal = int(salary_parts[1].replace('$', '').replace(',', ''))
                        avg_sal = (min_sal + max_sal) / 2
                        salaries.append(avg_sal)
                except:
                    continue
        
        avg_salary = sum(salaries) / len(salaries) if salaries else 0
        
        return {
            'total_jobs': len(all_jobs),
            'location_distribution': location_counts,
            'company_size_distribution': company_size_counts,
            'average_salary': avg_salary,
            'roles_count': len(self.job_database),
            'remote_jobs': len(self.get_remote_jobs(1000)),
            'entry_level_jobs': len(self.get_entry_level_jobs(1000))
        }
    
    def search_jobs_by_skills(self, skills: List[str], limit: int = 10) -> List[Dict]:
        """Search jobs based on user skills"""
        all_jobs = []
        for role_jobs in self.job_database.values():
            all_jobs.extend(role_jobs)
        
        job_scores = []
        user_skills_lower = [skill.lower() for skill in skills]
        
        for job in all_jobs:
            requirements = job.get('requirements', [])
            requirements_lower = [req.lower() for req in requirements]
            
            # Calculate match score
            matched_skills = set(user_skills_lower).intersection(set(requirements_lower))
            match_score = len(matched_skills) / len(requirements_lower) if requirements_lower else 0
            
            if match_score > 0:
                job_scores.append((job, match_score))
        
        # Sort by match score
        job_scores.sort(key=lambda x: x[1], reverse=True)
        
        return [job for job, score in job_scores[:limit]]

# Initialize job scraper
job_scraper = JobScraper()

# Backwards compatibility function
def get_jobs_for_role(role: str) -> List[Dict]:
    """Backwards compatibility function"""
    return job_scraper.get_jobs_for_role(role)

def search_jobs_with_filters(role: str = None, location: str = None, 
                           experience: str = None, salary_min: int = None,
                           company_size: str = None, job_type: str = None) -> List[Dict]:
    """Advanced job search with filters"""
    return job_scraper.search_jobs_with_filters(role, location, experience, salary_min, company_size, job_type)

def get_trending_jobs(limit: int = 10) -> List[Dict]:
    """Get trending jobs"""
    return job_scraper.get_trending_jobs(limit)

def get_remote_jobs(limit: int = 10) -> List[Dict]:
    """Get remote jobs"""
    return job_scraper.get_remote_jobs(limit)

def search_jobs_by_skills(skills: List[str], limit: int = 10) -> List[Dict]:
    """Search jobs by skills"""
    return job_scraper.search_jobs_by_skills(skills, limit)

def get_job_market_stats() -> Dict:
    """Get job market statistics"""
    return job_scraper.get_job_market_stats()