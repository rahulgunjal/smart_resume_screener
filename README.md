# 📄 Smart Resume Screener & Matching Agent (GenAI + RAG)

This project is a **smart AI-based resume screener** that uses **Generative AI (Gemini)** and **NLP** to automatically:

- 🔍 Parse and understand candidate resumes (PDF/DOCX)
- 🎯 Extract real technical skills using noun phrase filtering + Gemini
- 📄 Parse job descriptions and extract required skills
- 📊 Match candidates to JD using skill overlap
- 🏆 Rank resumes by score out of 100
- 📥 Present clean, recruiter-friendly output

> ✅ This project is a **portfolio showcase** to demonstrate skills in **GenAI, RAG, NLP, and multi-agent reasoning**.

---

## 🚀 Features

| Feature                               | Description |
|--------------------------------------|-------------|
| 🧠 GenAI Skill Extraction            | Uses Gemini to extract only real skills from resumes and JDs |
| 📑 Resume Parsing                    | Parses both `.pdf` and `.docx` files |
| 🧾 JD Understanding                  | Extracts technical skill keywords from job description |
| ⚖️ Resume Ranking                    | Scores each resume out of 100 based on skill overlap |
| 📈 Clean Output                      | Prints ranked candidate list with matched skills |
| 🛡️ Modular Code Structure            | Organized, extensible components for future enhancements |

---

## 🧠 How It Works (Workflow)

### Step-by-Step

```
          ┌─────────────┐
          │ Job Description (JD) - Text File
          └────┬────────┘
               │
     [Extract Noun Phrases using NLP]
               ↓
  [Gemini filters only technical skills]  ←─┐
               ↓                          │
     JD Skills Set (cleaned by LLM)       │
                                          │
      ┌───────────────────────────┐       │
      │ Resume Folder (.pdf/.docx)│       │
      └────────────┬──────────────┘       │
                   │                      │
       [Text extraction + noun phrases]   │
                   ↓                      │
     [Gemini extracts skills w/ exp]      │
                   ↓                      │
      Resume Skills → Compare to JD Skills
                   ↓
     Score = (Matched Skills / JD Skills) * 100
                   ↓
     Output: Ranked candidates with score
```

---

## 🧾 Sample Output

```
JD Skills Required:
java, selenium, postman, rest api, testng

📝 Ranked Candidates:

1. Rahul Gunjal
   Matched Skills: java, selenium, rest api
   Score: 60.0 / 100

2. Arti Pisal
   Matched Skills: java, testng
   Score: 40.0 / 100
```

---

## 📁 Project Structure

```
smart_resume_screener/
│
├── data/
│   ├── jd.txt                    # Job description
│   └── resumes/                  # Folder with resumes (.pdf, .docx)
│
├── genai/
│   └── skill_extractor.py       # Gemini-based skill extraction logic
│
├── parsers/
│   ├── resume_parser.py         # Resume reading + noun extraction
│
├── utils/
│   └── nlp_utils.py             # Noun phrase extraction (NLTK)
│
├── main.py                      # Entry point - ranking pipeline
├── requirements.txt             # Cleaned dependencies
└── .env                         # Contains GEMINI_API_KEY
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/smart_resume_screener.git
cd smart_resume_screener
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure `.env`

Create a `.env` file and add your Gemini API Key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

> You can get the key from https://makersuite.google.com/app/apikey

### 5. Run the Project

```bash
python main.py
```

---

## 📦 Dependencies Used

```
pdfplumber            → Parse PDF resumes  
docx2txt              → Parse DOCX resumes  
nltk                  → Extract noun phrases  
google-generativeai   → Gemini integration  
python-dotenv         → Load secrets from .env  
pandas (optional)
```

---

## 💡 Future Enhancements

- 🔮 Generate personalized interview questions using Gemini
- 📊 Streamlit or Flask Web UI for recruiters
- 📁 Export output to Excel or CSV
- 🔁 Add RAG/vector DB for more intelligent scoring
- ☁️ Deploy as REST API for integration

---

## 🧑‍💻 Author

**Rahul Gunjal**  
[GitHub](https://github.com/rahulgunjal)

---
