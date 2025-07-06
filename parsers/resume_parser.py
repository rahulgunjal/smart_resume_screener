import os
import pdfplumber
import docx2txt
import re
from utils.nlp_utils import extract_nouns_and_phrases

def extract_text_from_file(filepath):
    if filepath.lower().endswith(".pdf"):
        with pdfplumber.open(filepath) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif filepath.lower().endswith(".docx"):
        return docx2txt.process(filepath)
    else:
        return ""

def parse_resume(filepath):
    text = extract_text_from_file(filepath)
    nouns_phrases = extract_nouns_and_phrases(text)

    # Simple name/email extract fallback
    name = os.path.basename(filepath).split(".")[0]
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    email = email_match.group(0) if email_match else "N/A"

    return {
        "name": name,
        "email": email,
        "text": text,
        "nouns_phrases": nouns_phrases
    }
