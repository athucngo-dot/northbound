import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.enum import EpicStatus


class EpicCreate(BaseModel):
    project_id: uuid.UUID
    title: str
    description: str | None = None
    status: EpicStatus | None = None


class EpicRead(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    title: str
    description: str | None
    status: EpicStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True