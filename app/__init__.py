from fastapi import FastAPI
from app.routes.expense.expense_routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8081",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
