from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK

from app.domains.expense.actions import create_expense, update_expense, delete_expense, get_expense_by_id, get_expenses
from app.routes.expense.expense_request import CreateExpenseRequest

router = APIRouter()


@router.post('/', status_code=HTTP_201_CREATED)
async def post(
        request: CreateExpenseRequest,
):
    response = await create_expense(
        request=request
    )
    return response


@router.get('/', status_code=HTTP_200_OK)
async def get():
    response = await get_expenses()
    return response


@router.get('/{id}', status_code=HTTP_200_OK)
async def get_by_id(
        id:str,
):
    response = await get_expense_by_id(id)
    return response


@router.put('/{id}', status_code=HTTP_200_OK)
async def update(
        id: str,
        request: CreateExpenseRequest,
):
    response = await update_expense(
        id=id,
        request=request
    )
    return response


@router.delete('/{id}', status_code=HTTP_204_NO_CONTENT)
async def delete(id: str):
    await delete_expense(id=id)
