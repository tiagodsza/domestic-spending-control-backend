from app.core.database.repository import Repository
from app.routes.expense.expense_request import CreateExpenseRequest
from app.routes.expense.expense_response import ExpenseResponse


class CreateExpenseUseCase:

    @classmethod
    async def execute(
            cls,
            repository: Repository,
            request: CreateExpenseRequest,
    ):
        expense = request.to_domain()
        repository.save(expense)
        return ExpenseResponse.from_domain(expense)
