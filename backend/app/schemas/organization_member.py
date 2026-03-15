import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.enum import OrganizationMemberRole


class OrganizationMemberCreate(BaseModel):
    user_id: uuid.UUID
    organization_id: uuid.UUID
    role: OrganizationMemberRole | None = None


class OrganizationMemberRead(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    organization_id: uuid.UUID
    role: OrganizationMemberRole
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True