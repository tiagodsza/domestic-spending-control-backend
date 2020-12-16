from sqlalchemy import Column, String, Float, DateTime, ForeignKey

from app.database import DeclarativeBase
from app.database.models import AbstractModel
from app.exceptions.exceptions import InvalidValueException
from app.utils.utils import is_empty, is_valid_uuid


class Expense(AbstractModel, DeclarativeBase):
    __tablename__ = 'expenses'

    name = Column(String(64), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=True)
    place = Column(String(124), nullable=True)
    categorie_id = Column(String(36), ForeignKey('categories.id'), nullable=True)

    def __init__(self, **kwargs):
        super(Expense, self).__init__(**kwargs)
        self.__validate_name()
        self.__validate_amount()
        self.__validate_categorie_id()

    def update(self, request):
        self.name = request.name
        self.amount = request.amount
        self.date = request.date
        self.place = request.place
        self.categorie_id = request.categorie_id

    def __validate_name(self):
        if is_empty(self.name):
            raise InvalidValueException('name')

    def __validate_amount(self):
        if self.amount == 0 or type(self.amount) != float:
            raise InvalidValueException('amount. Must be floar and do not be zero.')

    def __validate_categorie_id(self):
        if self.categorie_id == None:
            return
        if not is_valid_uuid(self.categorie_id):
            raise InvalidValueException('categorie id')