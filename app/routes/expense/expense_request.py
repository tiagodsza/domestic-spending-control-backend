from datetime import datetime

from pydantic import BaseModel


class CreateExpenseRequest(BaseModel):
    name: str
    amount: float
    date: datetime
    place: str