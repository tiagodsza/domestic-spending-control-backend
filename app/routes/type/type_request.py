from pydantic import BaseModel

from app.domains.type.models import Type


class CreateTypeRequest(BaseModel):
    name: str
    color: str = None

    def to_domain(self):
        return Type(
            name=self.name,
            color=self.color,
        )