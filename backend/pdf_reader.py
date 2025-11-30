# backend/pdf_reader.py
import PyPDF2

def extract_text_from_pdf(file_path):
    """
    Extracts and returns text content from a given PDF file.
    Works for both single and multi-page PDFs.
    """
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"[ERROR] Failed to read PDF: {e}")
        text = ""
    return text
