from fastapi import APIRouter
from app.routes.expense import expense_routes
from app.routes.categorie import categorie_routes

api_router = APIRouter()

api_router.include_router(
    expense_routes.router,
    prefix='/expenses',
    tags=['expenses'],
)

api_router.include_router(
    categorie_routes.router,
    prefix='/categories',
    tags=['categories'],
)