from app.database.repository import get_repository
from app.routes.categorie.categorie_request import CreateCategorieRequest
from app.routes.categorie.categorie_response import CategorieResponse


async def create_categorie(request: CreateCategorieRequest):
    repository = await get_repository()
    type = request.to_domain()
    repository.save(type)
    repository.close()
    return CategorieResponse.from_domain(type)