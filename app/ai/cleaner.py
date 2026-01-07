import re
def clean_text(text: str) -> str:
    # Remove extra whitespace
    text = re.sub(r'\n+', ' ', text)
    # Remove special characters (keeping basic punctuation)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Strip leading and trailing whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text
# if __name__ == "__main__":
    sample_text = """This is   a sample text!\nWith some   irregular spacing...\nAnd special #characters
    
    ksjsjj
    
    $."""
    cleaned = clean_text(sample_text)
    print(cleaned)