from fastapi import APIRouter

from app.domains.type.actions import create_type
from app.routes.type.type_request import CreateTypeRequest

router = APIRouter()

@router.post('/')
def post(request: CreateTypeRequest):
    response = create_type(
        request=request
    )
    return response
