from uuid import uuid4

from sqlalchemy import Column, String, DateTime

from app.utils.date_time import generate_datetime_now


class AbstractModel(object):
    id = Column(
        String(length=36),
        default=lambda: str(uuid4()),
        primary_key=True,
    )
    created_at = Column(DateTime, default=lambda: generate_datetime_now())
    updated_at = Column(
        DateTime,
        default=lambda: generate_datetime_now(),
        onupdate=lambda: generate_datetime_now(),
    )
    deleted_at = Column(
        DateTime,
        nullable=True,
    )
