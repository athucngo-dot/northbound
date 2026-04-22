from sqlalchemy.orm import Session
import uuid
from app.models.activity import Activity
from app.schemas.activity import ActivityCreate

class ActivityRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, activity_id: uuid.UUID):
        return self.db.query(Activity).filter(Activity.id == activity_id).first()

    def create(self, activity: ActivityCreate):
        db_activity = Activity(**activity.model_dump())
        self.db.add(db_activity)
        self.db.flush()  # Flush to assign an ID before commit
        self.db.refresh(db_activity)
        return db_activity

    def list_all(self):
        return self.db.query(Activity).all()