import pdfplumber
import pytesseract
from collections import Counter
from PIL import Image

# Configure Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def extract_text_with_dynamic_header_removal(pdf_path):
    """
    Extracts text from a PDF while dynamically removing headers that are common across pages.
    If the text extraction fails (empty text), it uses OCR to extract text from images.
    """
    header_candidates = Counter()
    page_texts = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                if len(lines) > 3:
                    header_candidates.update(lines[:3])  # Consider first three lines as header candidates
                page_texts.append(lines)

    common_headers = set(
        line for line, count in header_candidates.items() if count > len(page_texts) * 0.5
    )

    cleaned_texts = []
    for lines in page_texts:
        cleaned_lines = [line for line in lines if line not in common_headers]
        cleaned_texts.append("\n".join(cleaned_lines))

    for idx, text in enumerate(cleaned_texts):
        if not text.strip():  # If empty, use OCR
            print(f"Performing OCR on page {idx + 1}...")
            with pdfplumber.open(pdf_path) as pdf:
                image = pdf.pages[idx].to_image().original
                ocr_text = pytesseract.image_to_string(image, lang="eng")
                cleaned_texts[idx] = ocr_text

    return "\n".join(cleaned_texts)
