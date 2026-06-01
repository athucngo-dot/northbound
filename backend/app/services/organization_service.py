from psycopg2 import IntegrityError
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from fastapi import HTTPException, status

from app.repositories.organization_repository import OrganizationRepository
from app.repositories.organization_member_repository import OrganizationMemberRepository
from app.schemas.organization import OrganizationCreateInternal, OrganizationCreateRequest
from app.utils.slug import generate_slug
from app.services.slug_service import make_unique_slug
from app.models.user import User
from app.schemas.organization_member import OrganizationMemberCreateInternal
from app.models.enum import OrganizationMemberRole, OrganizationMemberStatus


class OrganizationService:

    def __init__(self, db: Session):
        self.repo = OrganizationRepository(db)
        self.organization_member_repo = OrganizationMemberRepository(db)
    
    def create_my_organization(self, current_user: User, org_data: OrganizationCreateRequest):

        org_data.name = org_data.name.strip()
        slug = generate_slug(org_data.name)
        unique_slug = make_unique_slug(slug, self.repo.slug_exists)

        create_org_data = OrganizationCreateInternal(
            name = org_data.name,
            slug = unique_slug,
            description = org_data.description,
            is_active = True
        )
        
        try:
            new_org = self.repo.create(create_org_data)
            
        except IntegrityError:
            # catch the unique constraint violation when two orgs with the same slug at the same time
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organization with this slug already exists."
            )
        
        # Create organization membership for the creator        
        org_member_data = OrganizationMemberCreateInternal(
            user_id = current_user.id,
            organization_id = new_org.id,
            role = OrganizationMemberRole.owner,
            status = OrganizationMemberStatus.active,
            invited_at = datetime.now(timezone.utc),
            joined_at = datetime.now(timezone.utc)
        )
        
        try:
            self.organization_member_repo.create(org_member_data)
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create organization membership."
            )
        
        return new_org
        