from datetime import datetime

from pydantic import BaseModel


class TypeResponse(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime = None
    deleted_at: datetime = None
    name: str
    color: str = None

    def __init__(self, **kwargs):
        super(TypeResponse, self).__init__(**kwargs)

    @classmethod
    def from_domain(csl, data):
        return TypeResponse(
            id = data.id ,
            created_at = data.created_at ,
            updated_at = data.updated_at ,
            deleted_at = data.deleted_at ,
            name = data.name ,
            color = data.color ,
        )