import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def extract_nouns_and_phrases(text):
    doc = nlp(text)
    keywords = set()

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:  # nouns and proper nouns
            if len(token.text) > 1:
                keywords.add(token.text.strip().lower())

    # Also include noun phrases (multi-word)
    for chunk in doc.noun_chunks:
        if len(chunk.text.split()) > 1:
            keywords.add(chunk.text.strip().lower())

    return sorted(keywords)
