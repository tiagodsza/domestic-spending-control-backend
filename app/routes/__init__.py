from fastapi import APIRouter
from app.routes.expense import expense_routes

api_router = APIRouter()

api_router.include_router(
    expense_routes.router,
    prefix='/expenses',
    tags=['expenses']
)