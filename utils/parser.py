# EXTRACTING DATA FROM PDF
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    text = ""
    # READING PDF WITH HEP OF PDF READER FUNCTION
    pdf_reader = PdfReader(pdf_file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text
