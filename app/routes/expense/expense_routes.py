from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK

from app.database.repository import get_repository, Repository
from app.domains.expense.models import Expense
from app.domains.expense.actions import create_expense, update_expense, delete_expense
from app.routes.expense.expense_request import CreateExpenseRequest

router = APIRouter()


@router.post('/', status_code=HTTP_201_CREATED)
def post(
        request: CreateExpenseRequest,
):
    response = create_expense(
        request=request
    )
    return response


@router.get('/', status_code=HTTP_200_OK)
def get(
        repository: Repository = Depends(get_repository)
):
    response = repository.get(Expense)
    repository.close()
    return response.all()


@router.get('/{id}', status_code=HTTP_200_OK)
def get(
        id: str,
):
    repository = get_repository()
    response = repository.get_by_id(Expense, id)
    repository.close()
    return response


@router.put('/{id}', status_code=HTTP_200_OK)
def update(
        id,
        request: CreateExpenseRequest,
):
    response = update_expense(
        id=id,
        request=request
    )
    return response


@router.delete('/{id}', status_code=HTTP_204_NO_CONTENT)
def delete(id: str):
    delete_expense(id=id)
