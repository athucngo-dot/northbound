from sqlalchemy.orm import Session
import uuid
from backend.app.models.organization_member import OrganizationMember
from app.schemas.organization_member import OrganizationMemberCreate

class OrganizationMemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, org_member_id: uuid.UUID):
        return self.db.query(OrganizationMember).filter(OrganizationMember.id == org_member_id).first()

    def create(self, org_member: OrganizationMemberCreate):
        db_org_member = OrganizationMember(**org_member.model_dump())
        self.db.add(db_org_member)
        self.db.commit()
        self.db.refresh(db_org_member)
        return db_org_member

    def list_all(self):
        return self.db.query(OrganizationMember).all()