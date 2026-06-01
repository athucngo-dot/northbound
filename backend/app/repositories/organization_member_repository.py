from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
import uuid
from app.models.organization_member import OrganizationMember
from app.schemas.organization_member import OrganizationMemberCreateInternal
from app.models.enum import OrganizationMemberStatus
from app.models.organization import Organization
from app.models.user import User

class OrganizationMemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, org_member_id: uuid.UUID):
        return self.db.query(OrganizationMember).filter(OrganizationMember.id == org_member_id).first()

    def create(self, org_member: OrganizationMemberCreateInternal):
        db_org_member = OrganizationMember(**org_member.model_dump())
        self.db.add(db_org_member)
        self.db.flush()  # Flush to assign an ID before commit
        self.db.refresh(db_org_member)
        return db_org_member

    def list_all(self):
        return self.db.query(OrganizationMember).all()
    
    def get_user_memberships(self, user: User): 

        query = (
            select(OrganizationMember)
            .where(
                OrganizationMember.user_id == user.id,
                OrganizationMember.status == OrganizationMemberStatus.active,
                OrganizationMember.organization.has(
                    Organization.is_active.is_(True)
                )
            )
            .options(
                selectinload(OrganizationMember.organization)
            )
            .order_by(OrganizationMember.joined_at.desc())
        )

        memberships = self.db.scalars(query).all()

        return [
            {
                "organization": membership.organization,
                "role": membership.role,
            }
            for membership in memberships
        ]