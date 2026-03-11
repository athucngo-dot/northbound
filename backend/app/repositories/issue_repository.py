from sqlalchemy.orm import Session
import uuid
from app.models.issue import Issue
from app.schemas.issue import IssueCreate

class IssueRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, issue_id: uuid.UUID):
        return self.db.query(Issue).filter(Issue.id == issue_id).first()

    def create(self, issue: IssueCreate):
        db_issue = Issue(**issue.model_dump())
        self.db.add(db_issue)
        self.db.commit()
        self.db.refresh(db_issue)
        return db_issue

    def list_all(self):
        return self.db.query(Issue).all()