from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED

from app.routes.expense.expense_request import CreateExpenseRequest

router = APIRouter()

# @router.post('/', status_code=HTTP_201_CREATED)
# def post(
#     expense_request: CreateExpenseRequest
# ):
