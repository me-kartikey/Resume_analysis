from fastapi import FastAPI,UploadFile,Form
import shutil 
import os
from app.ai.pipeline import runPipeline
app=FastAPI(title="Resume Analysis",description="An API to match resumes with job descriptions using AI",version="1.0.0")
@app.get("/")
def root():
    return {
        "message": "AI Resume Screening API is running. Visit /docs to try the API."
    }
@app.post("/analyze")
async def analyze_resume(file: UploadFile, jd_text: str = Form(...)):
    # Save uploaded file to a temporary location
    temp_file_path = f"temp_{file.filename}"
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        # Run the AI pipeline
        file.file.close()
        score = runPipeline(temp_file_path, jd_text)

    finally:
        if(os.path.exists(temp_file_path)):
            os.remove(temp_file_path)

    return score