import os
import docx
import re

def read_jd_docx(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading JD DOCX: {e}")
    return text.strip()

def read_jd_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error reading JD TXT: {e}")
        return ""

def parse_jd(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract keywords (basic filtering)
    text = text.lower()
    words = re.findall(r"\b[a-zA-Z][a-zA-Z0-9\+\#\.]{1,}\b", text)
    keywords = set(word for word in words if len(word) > 2)

    return {
        "raw": text,
        "skills": list(keywords)
    }
