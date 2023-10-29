from fastapi import FastAPI
from app import route

app = FastAPI()

app.include_router(route.router)