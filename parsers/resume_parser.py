import os
import pdfplumber
import docx
import re
from utils.nlp_utils import extract_nouns_and_phrases


def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text.strip()

def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX: {e}")
    return text.strip()

def extract_basic_info(text):
    info = {}

    # Email
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    info["email"] = email_match.group(0) if email_match else None

    # Phone (Indian and global pattern)
    phone_match = re.search(r"(\+91[\s-]?)?[0]?[6789]\d{9}", text)
    info["phone"] = phone_match.group(0) if phone_match else None

    # Name (naive guess = first non-empty line)
    lines = text.splitlines()
    for line in lines:
        if line.strip():
            info["name"] = line.strip()
            break

    # Experience section (grab text block between "experience" and "education")
    exp_match = re.search(r"(experience|professional experience)(.*?)(education|projects|skills|certification|$)", text, re.IGNORECASE | re.DOTALL)
    info["experience"] = exp_match.group(2).strip() if exp_match else None

    # Extract all noun keywords & phrases
    info["nouns_phrases"] = extract_nouns_and_phrases(text)

    # Skills will be identified later using GenAI from these phrases
    info["skills"] = []

    return info

def parse_resume(file_path):
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext in [".docx"]:
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Only PDF and DOCX are supported.")

    # Clean text and extract fields
    return extract_basic_info(text)
