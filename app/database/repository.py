from sqlalchemy.orm import Session

from app.database import SessionLocal


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

    def get(self, model):
        return self._db.query(model)

    def get_by_id(self, model, id):
        return self._db.query(model).get(id)

    def close(self):
        self._db.close()

def get_repository():
    repository = Repository()
    repository.set_db(SessionLocal())
    return repository