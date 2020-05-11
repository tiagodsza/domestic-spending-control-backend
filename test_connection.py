from sqlalchemy import create_engine

from app.core.config import DATABASE_URL
from app.core.database.config import DeclarativeBase

engine = create_engine(DATABASE_URL)

DeclarativeBase.metadata.create_all(engine)
print("Created")