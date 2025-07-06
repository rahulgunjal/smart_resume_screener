# 💼 Smart Resume Screener & Matching Agent (GenAI + RAG + Multi-Agent Reasoning)

This is an intelligent resume screening system designed to **match resumes to job descriptions** using modern NLP, embeddings, and GenAI (Google Gemini). It demonstrates real-world AI automation skills by building an agent that can:

✅ Parse resumes from PDF/DOCX  
✅ Understand and extract real technical skills (using GenAI)  
✅ Estimate years of experience in each skill  
✅ Match resumes to a job description (using vector similarity)  
✅ Rank candidates with reasoning  
✅ Ready for next step: auto-interview question generation

---

## 📌 Problem It Solves

Recruiters and hiring managers often struggle with:
- Reading 100s of resumes for one job
- Missing qualified candidates due to keyword mismatch
- Lack of insight on actual experience behind buzzwords

This system solves that using AI-powered resume understanding.

---

## 🧠 How It Works – Workflow

### Step-by-step pipeline:

1. **Resume Parsing**  
   - Reads PDF/DOCX files using `pdfplumber` and `docx2txt`  
   - Extracts basic info: name, email, phone, experience section

2. **Noun Phrase Extraction**  
   - Uses `spaCy` to extract important **nouns and phrases** (potential skills)

3. **Skill Extraction via GenAI**  
   - Sends phrases + resume to **Gemini Pro** (LLM)  
   - Gemini responds with structured JSON:
     ```json
     [
       { "skill": "selenium", "experience": "4 years" },
       { "skill": "rest api", "experience": "unknown" }
     ]
     ```

4. **Similarity Scoring**  
   - Loads the job description
   - Embeds both resume and JD using `TF-IDF + Cosine Similarity`
   - Scores each resume based on skill match and context

5. **Ranking & Output**  
   - All resumes are ranked based on relevance to the JD  
   - Also prints skills with experience and explanation-ready phrases

---

## 🧱 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Main development language |
| pdfplumber, docx2txt | Resume parsing |
| spaCy | NLP: noun phrase extraction |
| Gemini (via `google-generativeai`) | GenAI for skill & experience extraction |
| scikit-learn | TF-IDF + Cosine similarity |
| dotenv | Environment variable management |
| VS Code | IDE used |

---

## 📁 Project Structure

```bash
smart_resume_screener/
│
├── data/                   # Input resumes & job description
│   ├── resumes/            # PDF or DOCX resumes
│   └── jd.txt              # Job description text
│
├── parsers/                # Resume & JD parsers
│   ├── resume_parser.py
│   └── jd_parser.py
│
├── embeddings/             # TF-IDF similarity logic
│   └── embedder.py
│
├── genai/                  # Gemini skill + experience extractor
│   └── skill_extractor.py
│
├── utils/                  # NLP helper (noun phrase extractor)
│   └── nlp_utils.py
│
├── .env                    # Contains your GEMINI_API_KEY (excluded via .gitignore)
├── main.py                 # Main driver script
├── requirements.txt        # Python dependencies
└── README.md               # You're reading this!
