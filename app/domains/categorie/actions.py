from app.database.repository import get_repository
from app.domains.categorie.models import Categorie
from app.routes.categorie.categorie_request import CreateCategorieRequest
from app.routes.categorie.categorie_response import CategorieResponse


async def create_categorie(request: CreateCategorieRequest):
    repository = await get_repository()
    categorie = request.to_domain()
    repository.save(categorie)
    return CategorieResponse.from_domain(categorie)

async def get_categorie():
    repository = await get_repository()
    response = repository.get(Categorie)
    return response.all()
