import os
import re
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def extract_skills_with_experience(nouns_phrases, resume_text):
    prompt = f"""
You are a resume skill extractor. I will give you:

1. A list of words and phrases extracted from a candidate's resume.
2. The full text of the resume.

Your job:
- From the list, identify only technical skills, tools, or programming languages.
- For each skill, extract the number of years/months of experience the candidate has (if mentioned).
- If experience is not clearly mentioned, return experience as "unknown".

Return result in this JSON format:
[
  {{ "skill": "skill_name", "experience": "X years" or "unknown" }},
  ...
]

Only return valid JSON array, no explanation or extra text.

List of words/phrases:\n{nouns_phrases}
Resume:\n{resume_text[:3000]}
"""

    try:
        response = model.generate_content(prompt)

        match = re.search(r'\[\s*\{.*?\}\s*\]', response.text, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)
        else:
            print("No valid JSON array found in Gemini response.")
            print("Raw response:\n", response.text)
            return []

    except Exception as e:
        print("Error parsing Gemini response:", e)
        print("Raw response:\n", response.text)
        return []


def extract_skills_from_noun_phrases(nouns_phrases, jd_text=""):
    prompt = f"""
You are a job description skill extractor.

From the given list of words/phrases, identify only real technical skills, programming languages, or tools.

Exclude soft skills, generic phrases, or non-technical terms.

Return result in this format:
[
  "skill1",
  "skill2",
  ...
]

Noun phrases extracted:\n{nouns_phrases}
(Optional JD context):\n{jd_text[:500]}
"""

    try:
        response = model.generate_content(prompt)

        match = re.search(r'\[\s*".*?"\s*(?:,\s*".*?"\s*)*\]', response.text, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)
        else:
            print("No valid JSON array found in JD skill response.")
            print("Raw response:\n", response.text)
            return []

    except Exception as e:
        print("Error parsing JD skill response:", e)
        return []
