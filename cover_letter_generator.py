# cover_letter_generator.py
import streamlit as st
import cohere
from typing import Dict, List, Optional
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CoverLetterGenerator:
    def __init__(self):
        try:
            self.co = cohere.Client(st.secrets["cohere"]["api_key"])
        except Exception as e:
            logger.error(f"Error initializing Cohere client: {str(e)}")
            self.co = None
    
    def generate_cover_letter_basic(self, name: str, role: str, company: str) -> str:
        """Generate a basic cover letter template"""
        return f"""
Dear Hiring Manager,

My name is {name}, and I am writing to express my interest in the {role} position at {company}. I have strong skills in this domain and am confident in my ability to contribute effectively to your team.

I would welcome the opportunity to bring my expertise to {company} and help achieve your goals.

Thank you for considering my application.

Sincerely,
{name}
"""
    
    def generate_cover_letter_advanced(self, name: str, role: str, company: str, 
                                     user_skills: List[str], experience: Optional[str] = None,
                                     company_info: Optional[str] = None) -> str:
        """Generate an advanced, personalized cover letter using AI"""
        if not self.co:
            return self.generate_cover_letter_basic(name, role, company)
        
        try:
            # Create a detailed prompt for the AI
            prompt = self.create_cover_letter_prompt(name, role, company, user_skills, experience, company_info)
            
            response = self.co.chat(
                model="command-r",
                message=prompt,
                temperature=0.7,
                max_tokens=800
            )
            
            generated_letter = response.text.strip()
            
            # Post-process the generated letter
            return self.post_process_cover_letter(generated_letter, name, role, company)
            
        except Exception as e:
            logger.error(f"Error generating AI cover letter: {str(e)}")
            return self.generate_cover_letter_basic(name, role, company)
    
    def create_cover_letter_prompt(self, name: str, role: str, company: str, 
                                 user_skills: List[str], experience: Optional[str] = None,
                                 company_info: Optional[str] = None) -> str:
        """Create a detailed prompt for AI cover letter generation"""
        
        skills_str = ", ".join(user_skills) if user_skills else "various technical skills"
        
        prompt = f"""
Write a professional cover letter for a job application with the following details:

Applicant Name: {name}
Job Role: {role}
Company: {company}
Skills: {skills_str}
"""
        
        if experience:
            prompt += f"\nRelevant Experience: {experience}"
        
        if company_info:
            prompt += f"\nCompany Information: {company_info}"
        
        prompt += f"""

Please write a compelling cover letter that:
1. Opens with a strong introduction that mentions the specific role and company
2. Highlights relevant skills and experience that match the {role} position
3. Shows enthusiasm for the company and role
4. Includes specific examples of achievements or projects when possible
5. Ends with a professional closing that encourages next steps
6. Maintains a professional yet personable tone
7. Is approximately 250-300 words

The cover letter should be tailored specifically for the {role} position and demonstrate knowledge of what the role entails.
"""
        
        return prompt
    
    def post_process_cover_letter(self, generated_letter: str, name: str, role: str, company: str) -> str:
        """Post-process the generated cover letter for quality"""
        # Remove any unwanted formatting
        letter = generated_letter.strip()
        
        # Ensure proper greeting
        if not letter.startswith("Dear"):
            letter = f"Dear Hiring Manager,\n\n{letter}"
        
        # Ensure proper closing
        if not any(closing in letter.lower() for closing in ["sincerely", "best regards", "thank you"]):
            letter += f"\n\nSincerely,\n{name}"
        
        # Replace any placeholder names/companies that might have been generated
        letter = re.sub(r'\[Your Name\]', name, letter, flags=re.IGNORECASE)
        letter = re.sub(r'\[Company Name\]', company, letter, flags=re.IGNORECASE)
        letter = re.sub(r'\[Position\]', role, letter, flags=re.IGNORECASE)
        
        return letter
    
    def get_cover_letter_tips(self, role: str) -> List[str]:
        """Get role-specific cover letter tips"""
        tips = {
            "Data Analyst": [
                "Mention specific data analysis tools and techniques you've used",
                "Include examples of insights you've derived from data",
                "Highlight your ability to communicate complex findings to stakeholders",
                "Show familiarity with data visualization tools"
            ],
            "Backend Developer": [
                "Mention specific programming languages and frameworks",
                "Highlight experience with API development and databases",
                "Include examples of scalable systems you've built",
                "Show understanding of software architecture principles"
            ],
            "ML Engineer": [
                "Highlight experience with machine learning frameworks",
                "Mention specific ML projects and their business impact",
                "Show understanding of ML lifecycle and deployment",
                "Include experience with data preprocessing and model evaluation"
            ],
            "Frontend Developer": [
                "Mention modern frontend frameworks and libraries",
                "Highlight responsive design and user experience skills",
                "Include examples of interactive web applications",
                "Show understanding of web performance optimization"
            ],
            "DevOps Engineer": [
                "Highlight experience with CI/CD pipelines",
                "Mention cloud platforms and infrastructure tools",
                "Include examples of automation achievements",
                "Show understanding of security and monitoring practices"
            ]
        }
        
        general_tips = [
            "Research the company and mention specific details about their mission or products",
            "Quantify your achievements with specific numbers and results",
            "Show enthusiasm for the role and company",
            "Keep it concise and focused on the most relevant qualifications",
            "Proofread carefully for grammar and spelling errors"
        ]
        
        return tips.get(role, []) + general_tips
    
    def analyze_cover_letter_quality(self, cover_letter: str) -> Dict:
        """Analyze the quality of a cover letter"""
        analysis = {
            'word_count': len(cover_letter.split()),
            'paragraph_count': len([p for p in cover_letter.split('\n\n') if p.strip()]),
            'has_greeting': cover_letter.strip().startswith('Dear'),
            'has_closing': any(closing in cover_letter.lower() for closing in ['sincerely', 'best regards', 'thank you']),
            'quality_score': 0,
            'suggestions': []
        }
        
        # Calculate quality score
        score = 0
        
        # Word count (ideal: 200-350 words)
        if 200 <= analysis['word_count'] <= 350:
            score += 25
        elif 150 <= analysis['word_count'] <= 400:
            score += 15
        else:
            analysis['suggestions'].append("Adjust length to 200-350 words for optimal impact")
        
        # Structure
        if analysis['has_greeting']:
            score += 20
        else:
            analysis['suggestions'].append("Add a proper greeting (Dear Hiring Manager,)")
        
        if analysis['has_closing']:
            score += 20
        else:
            analysis['suggestions'].append("Add a professional closing (Sincerely, Best regards)")
        
        # Paragraph structure (ideal: 3-4 paragraphs)
        if 3 <= analysis['paragraph_count'] <= 4:
            score += 15
        else:
            analysis['suggestions'].append("Organize into 3-4 clear paragraphs")
        
        # Content quality indicators
        if 'experience' in cover_letter.lower() or 'project' in cover_letter.lower():
            score += 10
        else:
            analysis['suggestions'].append("Include specific examples of your experience")
        
        if 'company' in cover_letter.lower() or 'organization' in cover_letter.lower():
            score += 10
        else:
            analysis['suggestions'].append("Show knowledge of the company")
        
        analysis['quality_score'] = score
        
        return analysis
    
    def get_template_suggestions(self, role: str) -> Dict[str, str]:
        """Get template suggestions for different roles"""
        templates = {
            "Data Analyst": {
                "opening": "I am excited to apply for the Data Analyst position at [Company]. With my strong background in data analysis and visualization, I am confident I can help [Company] turn data into actionable insights.",
                "body": "In my previous role, I successfully analyzed large datasets using Python and SQL, creating dashboards that improved decision-making by 30%. My experience with tools like Tableau and PowerBI has enabled me to communicate complex findings to stakeholders effectively.",
                "closing": "I would welcome the opportunity to discuss how my analytical skills and passion for data can contribute to [Company]'s continued success."
            },
            "Backend Developer": {
                "opening": "I am writing to express my interest in the Backend Developer position at [Company]. With my expertise in server-side development and API design, I am excited about the opportunity to contribute to your engineering team.",
                "body": "I have extensive experience building scalable web applications using Python/Django and have successfully implemented RESTful APIs that handle millions of requests daily. My background in database optimization and cloud deployment would be valuable for [Company]'s technical challenges.",
                "closing": "I look forward to the opportunity to discuss how my technical expertise can help [Company] build robust and efficient backend systems."
            },
            "ML Engineer": {
                "opening": "I am thrilled to apply for the ML Engineer position at [Company]. With my deep understanding of machine learning algorithms and production deployment, I am eager to help [Company] leverage AI for business growth.",
                "body": "I have successfully deployed machine learning models that improved business metrics by 25%, using TensorFlow and PyTorch. My experience with MLOps practices and cloud platforms enables me to build end-to-end ML solutions that scale effectively.",
                "closing": "I would love to discuss how my expertise in machine learning and software engineering can contribute to [Company]'s AI initiatives."
            }
        }
        
        return templates.get(role, {})

# Initialize cover letter generator
cover_letter_generator = CoverLetterGenerator()

# Backwards compatibility function
def generate_cover_letter(name: str, role: str, company: str) -> str:
    """Generate a basic cover letter"""
    return cover_letter_generator.generate_cover_letter_basic(name, role, company)

def generate_cover_letter_advanced(name: str, role: str, company: str, 
                                 user_skills: List[str], experience: Optional[str] = None,
                                 company_info: Optional[str] = None) -> str:
    """Generate an advanced cover letter"""
    return cover_letter_generator.generate_cover_letter_advanced(name, role, company, user_skills, experience, company_info)

def get_cover_letter_tips(role: str) -> List[str]:
    """Get cover letter tips for a specific role"""
    return cover_letter_generator.get_cover_letter_tips(role)

def analyze_cover_letter_quality(cover_letter: str) -> Dict:
    """Analyze cover letter quality"""
    return cover_letter_generator.analyze_cover_letter_quality(cover_letter)