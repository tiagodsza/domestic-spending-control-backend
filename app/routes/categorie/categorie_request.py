from pydantic import BaseModel

from app.domains.categorie.models import Categorie


class CreateCategorieRequest(BaseModel):
    name: str
    color: str = None

    def to_domain(self):
        return Categorie(
            name=self.name,
            color=self.color,
        )
