from sqlalchemy.orm import Session
import uuid
from app.models.project import Project
from app.schemas.project import ProjectCreate

class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, project_id: uuid.UUID):
        return self.db.query(Project).filter(Project.id == project_id).first()

    def create(self, project: ProjectCreate):
        db_project = Project(**project.model_dump())
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project

    def list_all(self):
        return self.db.query(Project).all()