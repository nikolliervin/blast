from fastapi import APIRouter, UploadFile
from app.controllers import recognize_controller
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/recognize")
async def recognize_text(image: UploadFile):
    return await recognize_controller.recognize_text(image)
