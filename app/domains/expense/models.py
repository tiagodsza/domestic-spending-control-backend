from typing import Final

from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Integer, Enum
import enum
from app.database import DeclarativeBase
from app.database.models import AbstractModel

class Month(str, enum.Enum):
    January: Final[str] = 'January'
    February: Final[str] = 'February'
    March: Final[str] = 'March'
    April: Final[str] = 'April'
    May: Final[str] = 'May'
    June: Final[str] = 'June'
    July: Final[str] = 'July'
    August: Final[str] = 'August'
    September: Final[str] = 'September'
    October: Final[str] = 'October'
    November: Final[str] = 'November'
    December: Final[str] = 'December'

class Expense(AbstractModel, DeclarativeBase):
    __tablename__ = 'expenses'

    name = Column(String(64), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=True)
    place = Column(String(124), nullable=True)
    month = Column(Enum(Month, name='month'))
    categorie_id = Column(String(36), ForeignKey('categories.id'), nullable=True)


    def __init__(self, **kwargs):
        super(Expense, self).__init__(**kwargs)

    def update(self, request):
        self.name = request.name
        self.amount = request.amount
        self.date = request.date
        self.place = request.place
        self.month = request.month
        self.categorie_id = request.categorie_id

