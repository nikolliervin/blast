from PIL import Image
import pytesseract

def extract_text(image) -> str:
    img = Image.open(image)
    return pytesseract.pytesseract.image_to_string(img)
