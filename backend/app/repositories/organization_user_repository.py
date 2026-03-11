from sqlalchemy.orm import Session
import uuid
from app.models.organization_user import OrganizationUser
from app.schemas.organization_user import OrganizationUserCreate

class OrganizationUserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, org_user_id: uuid.UUID):
        return self.db.query(OrganizationUser).filter(OrganizationUser.id == org_user_id).first()

    def create(self, org_user: OrganizationUserCreate):
        db_org_user = OrganizationUser(**org_user.model_dump())
        self.db.add(db_org_user)
        self.db.commit()
        self.db.refresh(db_org_user)
        return db_org_user

    def list_all(self):
        return self.db.query(OrganizationUser).all()