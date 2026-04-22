from sqlalchemy.orm import Session
import uuid
from app.models.epic import Epic
from app.schemas.epic import EpicCreate

class EpicRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, epic_id: uuid.UUID):
        return self.db.query(Epic).filter(Epic.id == epic_id).first()

    def create(self, epic: EpicCreate):
        db_epic = Epic(**epic.model_dump())
        self.db.add(db_epic)
        self.db.flush()  # Flush to assign an ID before commit
        self.db.refresh(db_epic)
        return db_epic

    def list_all(self):
        return self.db.query(Epic).all()