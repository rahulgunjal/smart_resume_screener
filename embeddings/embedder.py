from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    return model.encode([text], convert_to_tensor=False)[0]

def calculate_similarity(resume_text: str, jd_text: str):
    resume_vec = get_embedding(resume_text)
    jd_vec = get_embedding(jd_text)
    
    similarity = cosine_similarity([resume_vec], [jd_vec])[0][0]
    return round(float(similarity), 4)
