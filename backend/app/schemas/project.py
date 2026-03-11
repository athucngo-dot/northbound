import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.enum import ProjectStatus


class ProjectCreate(BaseModel):
    organization_id: uuid.UUID
    name: str
    description: str | None = None
    status: ProjectStatus | None = None


class ProjectRead(BaseModel):
    id: uuid.UUID
    organization_id: uuid.UUID
    name: str
    description: str | None
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True