from sqlalchemy.orm import Session
import uuid
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate

class OrganizationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, org_id: uuid.UUID):
        return self.db.query(Organization).filter(Organization.id == org_id).first()

    def get_by_slug(self, slug: str):
        return self.db.query(Organization).filter(Organization.slug == slug).first()

    def create(self, organization: OrganizationCreate):
        db_org = Organization(**organization.model_dump())
        self.db.add(db_org)
        self.db.commit()
        self.db.refresh(db_org)
        return db_org

    def list_all(self):
        return self.db.query(Organization).all()