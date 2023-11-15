from fastapi import FastAPI
from application import route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [  
    "chrome-extension://kcmfgkjmdhbhlmfkkebomchhnlpedknk",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route.router)