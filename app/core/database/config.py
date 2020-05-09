import sqlalchemy
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.core import config

DeclarativeBase = declarative_base()

# def _build_engine(**kwargs) -> Engine:
#     return sqlalchemy.create_engine(config.DATABASE_URL, **kwargs)
#
# engine = _build_engine(pool_size=5, max_overflow=1)
#
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )

engine = create_engine(config.DATABASE_URL)
DeclarativeBase.metadata.create_all(engine)
