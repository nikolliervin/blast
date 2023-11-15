from fastapi import UploadFile
from fastapi.responses import JSONResponse
from application.services import recognize_service
async def recognize_text(image: UploadFile):
    if not image.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        return JSONResponse(content={"error": "Only image files are supported"}, status_code=400)
    
    text = recognize_service.extract_text(image.file)
    return {"text": text}
