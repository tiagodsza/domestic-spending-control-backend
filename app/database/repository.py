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
        response = self._db.query(model)
        self.close()
        return response

    def get_by_id(self, model, id):
        response = self._db.query(model).get(id)
        self.close()
        return response

    def close(self):
        self._db.close()

def create_repository():
    try:
        repository = Repository()
        repository.set_db(SessionLocal())
        yield repository
    finally:
        repository.close()

def get_repository():
    return next(create_repository())
