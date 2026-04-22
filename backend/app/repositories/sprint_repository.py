from sqlalchemy.orm import Session
import uuid
from app.models.sprint import Sprint
from app.schemas.sprint import SprintCreate

class SprintRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, sprint_id: uuid.UUID):
        return self.db.query(Sprint).filter(Sprint.id == sprint_id).first()

    def create(self, sprint: SprintCreate):
        db_sprint = Sprint(**sprint.model_dump())
        self.db.add(db_sprint)
        self.db.flush()  # Flush to assign an ID before commit
        self.db.refresh(db_sprint)
        return db_sprint

    def list_all(self):
        return self.db.query(Sprint).all()