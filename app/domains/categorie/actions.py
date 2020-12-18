from app.database.repository import get_repository
from app.domains.categorie.models import Categorie
from app.exceptions.exceptions import NotFoundException
from app.routes.categorie.categorie_request import CreateCategorieRequest
from app.routes.categorie.categorie_response import CategorieResponse
from app.utils.utils import verify_if_exists_and_is_not_deleted


async def get_categorie():
    repository = await get_repository()
    response = repository.get(Categorie)
    return response.all()

async def get_categorie_by_id(id: str):
    repository = await get_repository()
    categorie = repository.get_by_id(Categorie, id)
    if not verify_if_exists_and_is_not_deleted(categorie):
        raise NotFoundException()
    return categorie

async def create_categorie(request: CreateCategorieRequest):
    repository = await get_repository()
    categorie = request.to_domain()
    repository.save(categorie)
    return CategorieResponse.from_domain(categorie)


async def delete_categorie(id: str):
    repository = await get_repository()
    categorie = repository.get_by_id(Categorie, id)
    if not verify_if_exists_and_is_not_deleted(categorie):
        raise NotFoundException()
    categorie.delete()
    repository.save(categorie)


async def update_categorie(
        id: str,
        request: CreateCategorieRequest
):
    repository = await get_repository()
    categorie = repository.get_by_id(Categorie, id)
    if not verify_if_exists_and_is_not_deleted(categorie):
        raise NotFoundException()
    categorie.update(request)
    repository.save(categorie)
    response = CategorieResponse.from_domain(categorie)
    return response
