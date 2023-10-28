from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract

app = FastAPI()

@app.post("/recognize")
async def recognize_text(image: UploadFile):
    
    if not image.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        return JSONResponse(content={"error": "Only image files are supported"}, status_code=400)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = Image.open(image.file)
    text = pytesseract.image_to_string(img)

    return {"text": text}
