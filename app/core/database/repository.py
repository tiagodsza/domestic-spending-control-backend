from sqlalchemy.orm import Session

from app.core.database import SessionLocal


class Repository:
    def __init__(self):
        self._db: Session

    def set_db(self, session):
        self._db = session

    def save(
            self,
            model,
    ):
        self._db.add(model)
        self._db.commit()
        self._db.refresh(model)
        self._db.close()


def get_repository():
    repository = Repository()
    repository.set_db(SessionLocal())
    return repository