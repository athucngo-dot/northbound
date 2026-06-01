import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.enum import OrganizationMemberRole, OrganizationMemberStatus
from app.schemas.organization import OrganizationSummaryRead


class OrganizationMemberCreateInternal(BaseModel):
    user_id: uuid.UUID
    organization_id: uuid.UUID
    role: OrganizationMemberRole = OrganizationMemberRole.member
    status: OrganizationMemberStatus = OrganizationMemberStatus.invited
    invited_by_id: uuid.UUID | None = None
    invited_at: datetime | None = None
    joined_at: datetime | None = None


class OrganizationMemberRead(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    organization_id: uuid.UUID
    role: OrganizationMemberRole
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class MyOrganizationRead(BaseModel):
    organization: OrganizationSummaryRead
    role: OrganizationMemberRole

    class Config:
        from_attributes = True