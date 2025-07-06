import os
from parsers.resume_parser import parse_resume
from parsers.jd_parser import parse_jd
from embeddings.embedder import calculate_similarity
from genai.skill_extractor import extract_skills_with_experience

# Load JD text
jd_text = parse_jd("data/jd.txt")

# Resume folder
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

        # Use GenAI to extract skills with experience
        skills = extract_skills_with_experience(nouns_phrases, resume_text_blob)
        resume["skills"] = skills

        # Join skill names only for similarity calculation
        skill_str = " ".join(s["skill"] for s in skills) if isinstance(skills, list) else ""

        # Combine into full resume text
        resume_text = f"{name} {email} {skill_str} {resume.get('experience', '')}"

        similarity = calculate_similarity(resume_text, jd_text)

        results.append({
            "name": name,
            "email": email,
            "skills": skills,
            "nouns_phrases": resume.get("nouns_phrases", []),
            "score": similarity
        })

# Sort by similarity score
ranked = sorted(results, key=lambda x: x["score"], reverse=True)

# Print output
print("\n📝 Ranked Resumes:")
for i, res in enumerate(ranked, 1):
    print(f"{i}. {res['name']} | Score: {res['score']}")
    print(f"   Email: {res['email']}")

    if res['skills']:
        for s in res['skills']:
            print(f"   - {s['skill']} ({s['experience']})")
    else:
        print("   Skills: Not detected")

    print(f"   Phrases: {', '.join(res['nouns_phrases'][:10])} ...\n")
