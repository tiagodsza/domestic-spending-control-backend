from datetime import datetime
from pydantic import BaseModel

class ExpenseResponse(BaseModel):
    id:str
    created_at: datetime
    updated_at: datetime = None
    deleted_at: datetime = None
    name: str
    amount: float
    date: datetime = None
    place: str = None

    def __init__(self, **kwargs):
        super(ExpenseResponse, self).__init__(**kwargs)

    @classmethod
    def from_domain(csl, data):
        return ExpenseResponse(
            id=data.id,
            created_at=data.created_at,
            updated_at=data.updated_at,
            deleted_at= data.deleted_at,
            name=data.name,
            amount=data.amount,
            date=data.date,
            place=data.place,
        )


