from app.database.repository import get_repository
from app.routes.categorie.categorie_request import CreateCategorieRequest
from app.routes.categorie.categorie_response import CategorieResponse


def create_categorie(request: CreateCategorieRequest):
    repository = get_repository()
    type = request.to_domain()
    repository.save(type)
    repository.close()
    return CategorieResponse.from_domain(type)