from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
SKILLS=["machine learning", "data science", "python", "tensorflow", "data preprocessing",
        "ml models", "data scientists", "production", "deep learning", "neural networks"]
def compute_similarity(resumeText: str, jdText: str) -> float:
    documents = [resumeText, jdText]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity_matrix[0][0]*100

def extract_skills(text: str):
    text = text.lower()
    foundSkills = []
    for skill in SKILLS:
        if skill in text.lower():
            foundSkills.append(skill)
    return list(set(foundSkills))