from fastapi import APIRouter
from app.routes.expense import expense_routes
from app.routes.type import type_routes

api_router = APIRouter()

api_router.include_router(
    expense_routes.router,
    prefix='/expenses',
    tags=['expenses'],
)

api_router.include_router(
    type_routes.router,
    prefix='/types',
    tags=['types'],
)