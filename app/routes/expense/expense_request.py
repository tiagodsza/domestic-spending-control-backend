from datetime import datetime
from pydantic import BaseModel
from app.domains.expense.models import Expense


class CreateExpenseRequest(BaseModel):
    name: str
    amount: float
    date: datetime = None
    place: str = None
    categorie_id: str = None
    month: str

    def to_domain(self):
        return Expense(
            name=self.name,
            amount=self.amount,
            date=self.date,
            place=self.place,
            categorie_id=self.categorie_id,
            month=self.month,
        )

