import sqlalchemy
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

DeclarativeBase = declarative_base()



def _build_engine(**kwargs) -> Engine:
    return sqlalchemy.create_engine(config.URL_DB, **kwargs)

engine = _build_engine(pool_size=5)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)