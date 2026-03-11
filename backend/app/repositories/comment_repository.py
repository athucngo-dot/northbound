from sqlalchemy.orm import Session
import uuid
from app.models.comment import Comment
from app.schemas.comment import CommentCreate

class CommentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, comment_id: uuid.UUID):
        return self.db.query(Comment).filter(Comment.id == comment_id).first()

    def create(self, comment: CommentCreate):
        db_comment = Comment(**comment.model_dump())
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return db_comment

    def list_all(self):
        return self.db.query(Comment).all()