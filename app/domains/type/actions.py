from app.database.repository import get_repository
from app.routes.type.type_request import CreateTypeRequest
from app.routes.type.type_response import TypeResponse


def create_type(request: CreateTypeRequest):
    repository = get_repository()
    type = request.to_domain()
    repository.save(type)
    repository.close()
    return TypeResponse.from_domain(type)