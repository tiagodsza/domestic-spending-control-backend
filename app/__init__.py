from fastapi import FastAPI
from app.routes import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(api_router)

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
