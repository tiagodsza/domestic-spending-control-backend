from datetime import datetime

from pydantic import BaseModel

from app.domains.expense.models import Expense


class CreateExpenseRequest(BaseModel):
    name: str
    amount: float
    date: datetime = None
    place: str = None

    def to_domain(self):
        return Expense(
            name=self.name,
            amount=self.amount,
            date=self.date,
            place=self.place
        )

