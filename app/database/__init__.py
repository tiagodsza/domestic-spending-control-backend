import sqlalchemy
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

DeclarativeBase = declarative_base()

DATABASE_URL = f'postgresql://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@localhost:5432/postgres'

def _build_engine(**kwargs) -> Engine:
    return sqlalchemy.create_engine(DATABASE_URL, **kwargs)

engine = _build_engine(pool_size=5)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)