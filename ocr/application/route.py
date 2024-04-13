from fastapi import APIRouter, UploadFile
from application.controllers import recognize_controller
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get('/')
async def root():
    return {'message':'Use /recognize'}


@router.post("/recognize")
async def recognize_text(image: UploadFile):
    return await recognize_controller.recognize_text(image)
