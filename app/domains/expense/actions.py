from fastapi import HTTPException

from app.database.repository import get_repository
from app.domains.expense.models import Expense
from app.routes.expense.expense_request import CreateExpenseRequest
from app.routes.expense.expense_response import ExpenseResponse
from app.utils.utils import verify_if_exists_and_is_not_deleted


def create_expense(
        request: CreateExpenseRequest,
):
    repository = get_repository()
    expense = request.to_domain()
    repository.save(expense)
    return ExpenseResponse.from_domain(expense)


def update_expense(
        id: str,
        request: CreateExpenseRequest,
):
    repository = get_repository()
    expense = repository.get_by_id(Expense, id)
    expense.update(request)
    repository.save(expense)
    return ExpenseResponse.from_domain(expense)


def delete_expense(id: str):
    repository = get_repository()
    expense = repository.get_by_id(Expense, id)
    if not verify_if_exists_and_is_not_deleted(expense):
        raise HTTPException(status_code=404)
    expense.delete()
    repository.save(expense)

def get_expense_by_id(id: str):
    repository = get_repository()
    response = repository.get_by_id(Expense, id)
    if not verify_if_exists_and_is_not_deleted(response):
        raise HTTPException(status_code=404)
    return response

def get_expenses():
    repository = get_repository()
    response = repository.get(Expense)
    expenses = []
    for expense in response.all():
        if verify_if_exists_and_is_not_deleted(expense):
           expenses.append(expense)
    return expenses
