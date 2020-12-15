from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.database import DeclarativeBase
from app.database.models import AbstractModel


class Type(AbstractModel, DeclarativeBase):
    __tablename__ = 'types'

    name = Column(String(64), nullable=False, unique=True)
    color = Column(String(64), nullable=True, unique=True)

    def __init__(self, **kwargs):
        super(Type, self).__init__(**kwargs)

    def update(self, request):
        self.name = request.name
        self.color = request.type