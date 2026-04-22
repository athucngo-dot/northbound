from sqlalchemy.orm import Session
import uuid
from app.models.attachment import Attachment
from app.schemas.attachment import AttachmentCreate

class AttachmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, attachment_id: uuid.UUID):
        return self.db.query(Attachment).filter(Attachment.id == attachment_id).first()

    def create(self, attachment: AttachmentCreate):
        db_attachment = Attachment(**attachment.model_dump())
        self.db.add(db_attachment)
        self.db.flush()  # Flush to assign an ID before commit
        self.db.refresh(db_attachment)
        return db_attachment

    def list_all(self):
        return self.db.query(Attachment).all()