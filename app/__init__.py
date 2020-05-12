from fastapi import FastAPI
from app.routes.expense.expense_routes import router

app = FastAPI()

app.include_router(router)