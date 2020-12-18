from fastapi import APIRouter

from app.domains.categorie.actions import create_categorie, get_categorie, delete_categorie
from app.routes.categorie.categorie_request import CreateCategorieRequest

router = APIRouter()

@router.post('/')
async def post(request: CreateCategorieRequest):
    response = await create_categorie(
        request=request
    )
    return response

@router.get('/')
async def get():
    response = await get_categorie()
    return response

@router.delete('/{id}', status_code=204)
async def delete(id: str):
    await delete_categorie(id)