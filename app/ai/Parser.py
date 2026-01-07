import pdfplumber
from .cleaner import clean_text
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# if __name__ == "__main__":
#     pdf_path = "data/Kartikey_ml.pdf"  # Replace with your PDF file path
#     extracted_text = extract_text_from_pdf(pdf_path)
#     cleaned_text = clean_text(extracted_text)
#     print(extracted_text)
#     print("this is cleaned text")
#     print(cleaned_text)