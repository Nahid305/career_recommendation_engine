# resume_parser.py - Enhanced resume parsing with error handling
import pdfplumber
import streamlit as st
import logging
import traceback
from io import BytesIO
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_pdf(uploaded_file):
    """
    Enhanced PDF text extraction with error handling and cleaning
    """
    if uploaded_file is None:
        return ""
    
    text = ""
    try:
        # Read the file content
        if hasattr(uploaded_file, 'read'):
            file_content = uploaded_file.read()
            uploaded_file.seek(0)  # Reset file pointer
        else:
            file_content = uploaded_file
        
        # Create BytesIO object for pdfplumber
        pdf_file = BytesIO(file_content)
        
        with pdfplumber.open(pdf_file) as pdf:
            # Check if PDF has pages
            if len(pdf.pages) == 0:
                st.error("❌ The PDF file appears to be empty or corrupted.")
                return ""
            
            # Extract text from each page
            for page_num, page in enumerate(pdf.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                    else:
                        logger.warning(f"No text found on page {page_num + 1}")
                except Exception as e:
                    logger.error(f"Error extracting text from page {page_num + 1}: {str(e)}")
                    continue
    
    except Exception as e:
        error_msg = f"Error reading PDF file: {str(e)}"
        logger.error(error_msg)
        st.error(f"❌ {error_msg}")
        return ""
    
    # Clean and process the extracted text
    cleaned_text = clean_extracted_text(text)
    
    if not cleaned_text.strip():
        st.warning("⚠️ No readable text found in the PDF. Please ensure the PDF contains text (not just images).")
        return ""
    
    return cleaned_text

def clean_extracted_text(text):
    """
    Clean and normalize extracted text
    """
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove common PDF artifacts
    text = re.sub(r'[•\uf0b7\uf0a7\uf0d8\uf0e0]', '• ', text)  # Bullet points
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Non-ASCII characters
    
    # Fix common OCR errors
    text = text.replace('|', 'I')  # Common OCR mistake
    text = text.replace('0', 'O')  # In context where O is expected
    
    # Remove page numbers and headers/footers (basic patterns)
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        # Skip likely page numbers
        if re.match(r'^\d+$', line):
            continue
        # Skip lines that are just special characters
        if re.match(r'^[^\w\s]+$', line):
            continue
        if len(line) > 3:  # Keep lines with substantial content
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def extract_contact_info(text):
    """
    Extract contact information from resume text
    """
    contact_info = {}
    
    # Email pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    if emails:
        contact_info['email'] = emails[0]
    
    # Phone pattern (various formats)
    phone_patterns = [
        r'(\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
        r'(\+\d{1,3}[-.\s]?)?\d{10}',
        r'(\+\d{1,3}[-.\s]?)?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}'
    ]
    
    for pattern in phone_patterns:
        phones = re.findall(pattern, text)
        if phones:
            contact_info['phone'] = phones[0]
            break
    
    # LinkedIn URL
    linkedin_pattern = r'linkedin\.com/in/[a-zA-Z0-9-]+'
    linkedin_matches = re.findall(linkedin_pattern, text)
    if linkedin_matches:
        contact_info['linkedin'] = 'https://' + linkedin_matches[0]
    
    # GitHub URL
    github_pattern = r'github\.com/[a-zA-Z0-9-]+'
    github_matches = re.findall(github_pattern, text)
    if github_matches:
        contact_info['github'] = 'https://' + github_matches[0]
    
    return contact_info

def extract_sections(text):
    """
    Extract different sections from resume
    """
    sections = {}
    
    # Common section headers
    section_patterns = {
        'education': r'(education|academic|qualification|degree)',
        'experience': r'(experience|employment|work|career|professional)',
        'skills': r'(skills|competencies|technical|technologies)',
        'projects': r'(projects|portfolio|work samples)',
        'certifications': r'(certifications?|certificates?|licenses?)',
        'summary': r'(summary|objective|profile|about)'
    }
    
    text_lower = text.lower()
    lines = text.split('\n')
    
    for section_name, pattern in section_patterns.items():
        for i, line in enumerate(lines):
            if re.search(pattern, line.lower()) and len(line.strip()) < 50:
                # Found a section header, extract content until next section
                section_content = []
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    if not next_line:
                        continue
                    
                    # Check if this might be another section header
                    is_next_section = False
                    for other_pattern in section_patterns.values():
                        if re.search(other_pattern, next_line.lower()) and len(next_line) < 50:
                            is_next_section = True
                            break
                    
                    if is_next_section:
                        break
                    
                    section_content.append(next_line)
                
                if section_content:
                    sections[section_name] = '\n'.join(section_content[:10])  # Limit length
                break
    
    return sections

def validate_resume_quality(text):
    """
    Assess the quality and completeness of the resume
    """
    issues = []
    suggestions = []
    
    if len(text.strip()) < 500:
        issues.append("Resume seems too short")
        suggestions.append("Add more details about your experience and skills")
    
    # Check for contact information
    contact_info = extract_contact_info(text)
    if 'email' not in contact_info:
        issues.append("No email address found")
        suggestions.append("Include a professional email address")
    
    if 'phone' not in contact_info:
        issues.append("No phone number found")
        suggestions.append("Include a contact phone number")
    
    # Check for common sections
    sections = extract_sections(text)
    required_sections = ['experience', 'skills', 'education']
    
    for section in required_sections:
        if section not in sections:
            issues.append(f"Missing {section} section")
            suggestions.append(f"Add a clear {section} section")
    
    # Check for keywords density
    if text.lower().count('experience') < 2:
        suggestions.append("Include more details about your work experience")
    
    if text.lower().count('skill') < 3:
        suggestions.append("Highlight more of your technical and soft skills")
    
    return {
        'issues': issues,
        'suggestions': suggestions,
        'quality_score': max(0, 100 - len(issues) * 15)
    }

def get_resume_statistics(text):
    """
    Get basic statistics about the resume
    """
    if not text:
        return {}
    
    words = text.split()
    sentences = re.split(r'[.!?]+', text)
    
    return {
        'word_count': len(words),
        'sentence_count': len([s for s in sentences if s.strip()]),
        'character_count': len(text),
        'paragraph_count': len([p for p in text.split('\n\n') if p.strip()])
    }
