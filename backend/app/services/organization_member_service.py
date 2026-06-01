from sqlalchemy.orm import Session

from app.repositories.organization_member_repository import OrganizationMemberRepository
from app.models.user import User

class OrganizationMemberService:
    def __init__(self, db: Session):
        self.repo = OrganizationMemberRepository(db)

    def create_org_member(self, org_member):
        return self.repo.create(org_member)
    
    def get_user_memberships(self, user: User):
         return self.repo.get_user_memberships(user)
    
    