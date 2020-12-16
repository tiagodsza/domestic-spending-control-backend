from fastapi import APIRouter

from app.domains.categorie.actions import create_categorie
from app.routes.categorie.categorie_request import CreateCategorieRequest

router = APIRouter()

@router.post('/')
async def post(request: CreateCategorieRequest):
    response = await create_categorie(
        request=request
    )
    return response
