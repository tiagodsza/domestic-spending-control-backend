from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK

from app.domains.expense.actions import create_expense, update_expense, delete_expense, get_expense_by_id, get_expenses
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
def get():
    response = get_expenses()
    return response


@router.get('/{id}', status_code=HTTP_200_OK)
def get_by_id(
        id:str,
):
    response = get_expense_by_id(id)
    return response


@router.put('/{id}', status_code=HTTP_200_OK)
def update(
        id: str,
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
