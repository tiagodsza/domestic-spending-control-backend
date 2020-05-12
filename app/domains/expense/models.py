from sqlalchemy import Column, String, Float, DateTime

from app.core.database import DeclarativeBase
from app.core.database.models import AbstractModel



class Expense(AbstractModel, DeclarativeBase):
    __tablename__='expense'

    name = Column(String(64), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=True)
    place = Column(String(124), nullable=True)

    def __init__(self, **kwargs):
        super(Expense, self).__init__(**kwargs)
