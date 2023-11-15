# app/services/recognize_service.py

from PIL import Image
import pytesseract

def extract_text(image) -> str:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = Image.open(image)
    return pytesseract.image_to_string(img)
