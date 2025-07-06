import os
import docx

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

def parse_jd(file_path):
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".docx":
        return read_jd_docx(file_path)
    elif ext == ".txt":
        return read_jd_txt(file_path)
    else:
        raise ValueError("Unsupported JD file type. Only DOCX and TXT are supported.")
