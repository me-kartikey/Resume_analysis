from .Parser import extract_text_from_pdf 
from .cleaner import clean_text
from .matcher import compute_similarity ,extract_skills 
def runPipeline(resume_pdf_path: str, jd_text: str) -> float:
    # Extract text from resume PDF
    extracted_text = extract_text_from_pdf(resume_pdf_path)
    # Clean the extracted text
    cleaned_resume_text = clean_text(extracted_text)
    # Compute similarity between cleaned resume text and job description text
    similarity_score = compute_similarity(cleaned_resume_text, jd_text)
    # return similarity_score
    resume_skills = extract_skills(cleaned_resume_text)
    jd_skills = extract_skills(jd_text)
    matched_skills = set(resume_skills).intersection(set(jd_skills))
    missing_skills = set(jd_skills) - set(resume_skills)
    if similarity_score >= 70:
        recommendation = "Strong match! Your resume aligns well with the job description."
    elif similarity_score >= 50:
        recommendation = "Moderate match. Consider improving your resume to better fit the job description."
    else:
        recommendation = "Weak match. Significant improvements are needed to align your resume with the job description."   
        return{
            "similarity_score": round(similarity_score, 2),
            "matched_skills": list(matched_skills),
            "missing_skills": list(missing_skills),
            "recommendation": recommendation
        }
# # if __name__ == "__main__":
#     # resume_pdf_path = "data/Kartikey_ml.pdf"  # Replace with your resume PDF file path
#     jd_text = """We are looking for a skilled Machine Learning Engineer to join our team. 
#     The ideal candidate will have experience with Python, TensorFlow, and data preprocessing. 
#     Responsibilities include developing ML models, collaborating with data scientists, 
#     and deploying solutions to production."""  # Sample job description text
#     score = runPipeline(resume_pdf_path, jd_text)
#     print(f"Similarity Score: {score:.2f}%")