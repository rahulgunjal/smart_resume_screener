import os
from utils.nlp_utils import extract_nouns_and_phrases
from parsers.resume_parser import parse_resume
from genai.skill_extractor import (
    extract_skills_with_experience,
    extract_skills_from_noun_phrases
)

def calculate_normalized_score(resume_skills, jd_skills):
    jd_skill_set = set(s.lower() for s in jd_skills)
    resume_skill_set = set(s["skill"].lower() for s in resume_skills)

    matched_skills = jd_skill_set.intersection(resume_skill_set)

    if not jd_skill_set:
        return 0.0, set()

    score = (len(matched_skills) / len(jd_skill_set)) * 100
    return round(score, 2), matched_skills

# --- Load JD and extract skills ---
with open("data/jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

jd_noun_phrases = extract_nouns_and_phrases(jd_text)
jd_skills = extract_skills_from_noun_phrases(jd_noun_phrases, jd_text)
jd_skill_set = set(s.lower() for s in jd_skills)

# --- Process Resumes ---
resume_folder = "data/resumes"
results = []

for filename in os.listdir(resume_folder):
    if filename.lower().endswith((".pdf", ".docx")):
        file_path = os.path.join(resume_folder, filename)
        resume = parse_resume(file_path)

        name = resume.get("name", filename)
        email = resume.get("email", "N/A")
        nouns_phrases = resume.get("nouns_phrases", [])
        resume_text_blob = f"{resume.get('name', '')} {resume.get('email', '')} {resume.get('experience', '')}"

        skills = extract_skills_with_experience(nouns_phrases, resume_text_blob)
        resume["skills"] = skills

        score, matched_skills = calculate_normalized_score(skills, jd_skills)

        results.append({
            "name": name,
            "email": email,
            "skills": skills,
            "matched_skills": matched_skills,
            "score": score
        })

# --- Print Output ---
ranked = sorted(results, key=lambda x: x["score"], reverse=True)

print("JD Skills Required:")
print(", ".join(sorted(jd_skill_set)))
print("\n📝 Ranked Candidates:\n")

for i, res in enumerate(ranked, 1):
    print(f"{i}. {res['name']}")
    print(f"   Matched Skills: {', '.join(sorted(res['matched_skills'])) or 'None'}")
    print(f"   Score: {res['score']} / 100\n")
