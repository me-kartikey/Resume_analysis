Overview.......................
This project is an AI-based Resume Screening System that analyzes a candidate’s resume against a given job description and provides a similarity score along with skill-based insights.
It is designed to simulate how real-world Applicant Tracking Systems (ATS) perform initial resume screening.

Features...............................

Upload resume in PDF format

Enter job description text

Extract and clean resume content

Calculate similarity score using NLP (TF-IDF + Cosine Similarity)

Identify matched and missing skills

Provide human-readable recommendations

Exposed as a REST API using FastAPI

 How the System Works..................

Resume PDF is uploaded via API

Text is extracted from the PDF

Resume and job description text are cleaned

AI computes similarity score

Skills are extracted and compared

Final result is returned as JSON
NOTES*********************************
pdfplumber:used to extract and read pdf file 
re = replace / remove / regex

re.sub(pattern, replacement, text)
HERE SUB----------------->

pattern → kya dhoondhna hai

replacement → kis se replace karna hai

text → jisme change karna hai

r''   → raw string
\n    → newline
\s    → space/tab/newline
\d    → digit
+     → 1 or more
*     → 0 or more
[]    → set
^     → NOT (inside [])
{}    → exact count

split=== split make a new list of string 
text = "python fastapi sql"
print(text.split()
OUTPUT
['python', 'fastapi', 'sql']