# job_scraper.py

def get_jobs_for_role(role):
    job_data = {
        "Data Analyst": [
            {"company": "TCS", "title": "Data Analyst", "location": "Mumbai", "link": "https://www.tcs.com/careers"},
            {"company": "Infosys", "title": "Business Analyst", "location": "Pune", "link": "https://www.infosys.com/careers"},
            {"company": "Wipro", "title": "Data Analyst", "location": "Hyderabad", "link": "https://careers.wipro.com"},
            {"company": "Fractal Analytics", "title": "Data Analyst - Python", "location": "Bangalore", "link": "https://fractal.ai/careers/"},
            {"company": "Mu Sigma", "title": "Business Data Analyst", "location": "Bangalore", "link": "https://www.mu-sigma.com/careers"},
            {"company": "Razorpay", "title": "Data Analyst Intern", "location": "Remote", "link": "https://razorpay.com/careers/"},
            {"company": "Paytm", "title": "Junior Data Analyst", "location": "Noida", "link": "https://paytm.com/careers"},
            {"company": "Zoho", "title": "Analytics Consultant", "location": "Chennai", "link": "https://careers.zohocorp.com"},
            {"company": "Cimpress", "title": "PowerBI Data Analyst", "location": "Ahmedabad", "link": "https://careers.cimpress.com/"},
            {"company": "L&T Infotech", "title": "Data Analyst Trainee", "location": "Kolkata", "link": "https://www.ltimindtree.com/careers"}
        ],
        "Backend Developer": [
            {"company": "Amazon", "title": "Backend Developer", "location": "Hyderabad", "link": "https://www.amazon.jobs"},
            {"company": "Flipkart", "title": "Java Developer", "location": "Bangalore", "link": "https://www.flipkartcareers.com"},
            {"company": "Zoho", "title": "Backend Software Engineer", "location": "Chennai", "link": "https://careers.zohocorp.com"},
            {"company": "Freshworks", "title": "Python Backend Developer", "location": "Chennai", "link": "https://www.freshworks.com/company/careers"},
            {"company": "Paytm", "title": "Backend Developer – Node.js", "location": "Noida", "link": "https://paytm.com/careers"},
            {"company": "CRED", "title": "Software Engineer – Backend", "location": "Remote", "link": "https://www.cred.club/careers"},
            {"company": "TCS", "title": "Backend Developer – Spring Boot", "location": "Mumbai", "link": "https://www.tcs.com/careers"},
            {"company": "Yellow.ai", "title": "Backend Intern – GoLang", "location": "Bangalore", "link": "https://yellow.ai/careers"},
            {"company": "Fyle", "title": "Django Developer", "location": "Remote", "link": "https://www.fylehq.com/careers"},
            {"company": "Coding Ninjas", "title": "Backend Web Engineer", "location": "Gurgaon", "link": "https://www.codingninjas.com/careers"}
        ],
        "ML Engineer": [
            {"company": "Google", "title": "Machine Learning Engineer", "location": "Bangalore", "link": "https://careers.google.com"},
            {"company": "OpenAI", "title": "AI Research Engineer", "location": "Remote", "link": "https://openai.com/careers"},
            {"company": "Fractal", "title": "ML Engineer – Python", "location": "Mumbai", "link": "https://fractal.ai/careers/"},
            {"company": "TCS", "title": "AI/ML Engineer", "location": "Chennai", "link": "https://www.tcs.com/careers"},
            {"company": "Yellow.ai", "title": "ML Intern", "location": "Bangalore", "link": "https://yellow.ai/careers"},
            {"company": "Amazon", "title": "Applied Scientist – ML", "location": "Hyderabad", "link": "https://www.amazon.jobs"},
            {"company": "Zoho", "title": "Machine Learning Developer", "location": "Chennai", "link": "https://careers.zohocorp.com"},
            {"company": "Razorpay", "title": "ML Intern", "location": "Remote", "link": "https://razorpay.com/careers"},
            {"company": "Wipro HOLMES", "title": "AI Developer", "location": "Pune", "link": "https://careers.wipro.com"},
            {"company": "LTIMindtree", "title": "Data Scientist – NLP", "location": "Mumbai", "link": "https://www.ltimindtree.com/careers"}
        ]
    }

    return job_data.get(role, [])