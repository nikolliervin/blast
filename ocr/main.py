from fastapi import FastAPI
from application import route

app = FastAPI()

app.include_router(route.router)