from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

from app.core.database.repository import get_repository, Repository
from app.domains.expense.usecase import CreateExpenseUseCase
from app.routes.expense.expense_request import CreateExpenseRequest

router = APIRouter()


def get_create_expense_usecase():
    return CreateExpenseUseCase()


@router.post('/', status_code=HTTP_201_CREATED)
async def post(
        request: CreateExpenseRequest,
        usecase: CreateExpenseUseCase = Depends(get_create_expense_usecase),
        respository: Repository = Depends(get_repository)
):
    response = await usecase.execute(
        repository=respository,
        request=request
    )
    return response

@router.get('/message')
def get():
    return {'message':'Get works!'}
