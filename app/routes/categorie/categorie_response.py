from datetime import datetime

from pydantic import BaseModel


class CategorieResponse(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime = None
    deleted_at: datetime = None
    name: str
    color: str = None

    def __init__(self, **kwargs):
        super(CategorieResponse, self).__init__(**kwargs)

    @classmethod
    def from_domain(csl, data):
        return CategorieResponse(
            id = data.id ,
            created_at = data.created_at ,
            updated_at = data.updated_at ,
            deleted_at = data.deleted_at ,
            name = data.name ,
            color = data.color ,
        )