import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.enum import OrganizationUserRole


class OrganizationUserCreate(BaseModel):
    user_id: uuid.UUID
    organization_id: uuid.UUID
    role: OrganizationUserRole | None = None


class OrganizationUserRead(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    organization_id: uuid.UUID
    role: OrganizationUserRole
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True