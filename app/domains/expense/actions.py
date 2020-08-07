from app.database.repository import get_repository
from app.domains.expense.models import Expense
from app.routes.expense.expense_request import CreateExpenseRequest
from app.routes.expense.expense_response import ExpenseResponse


def create_expense(
        request: CreateExpenseRequest,
):
    repository = get_repository()
    expense = request.to_domain()
    repository.save(expense)
    repository.close()
    return ExpenseResponse.from_domain(expense)


def update_expense(
        id: str,
        request: CreateExpenseRequest,
):
    repository = get_repository()
    expense = repository.get_by_id(Expense, id)
    expense.update(request)
    repository.save(expense)
    repository.close()
    return ExpenseResponse.from_domain(expense)


def delete_expense(id: str):
    repository = get_repository()
    expense = repository.get_by_id(Expense, id)
    expense.delete()
    repository.save(expense)
    repository.close()
