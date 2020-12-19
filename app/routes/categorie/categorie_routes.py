from fastapi import APIRouter

from app.domains.categorie.actions import create_categorie, get_categorie, delete_categorie, update_categorie, \
    get_categorie_by_id
from app.routes.categorie.categorie_request import CreateCategorieRequest

router = APIRouter()


@router.get('/', status_code=200)
async def get():
    response = await get_categorie()
    return response

@router.get('/{id}', status_code=200)
async def get(id: str):
    response = await get_categorie_by_id(id)
    return response


@router.post('/', status_code=201)
async def post(request: CreateCategorieRequest):
    response = await create_categorie(
        request=request
    )
    return response


@router.delete('/{id}', status_code=204)
async def delete(id: str):
    await delete_categorie(id)


@router.put('/{id}', status_code=200)
async def put(id: str, request: CreateCategorieRequest):
    response = await update_categorie(id, request)
    return response
