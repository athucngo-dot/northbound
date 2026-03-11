import uuid
from datetime import datetime
from pydantic import BaseModel


class ActivityCreate(BaseModel):
    organization_id: uuid.UUID
    user_id: uuid.UUID | None = None
    project_id: uuid.UUID | None = None
    issue_id: uuid.UUID | None = None
    event_type: str
    activity_metadata: dict | None = None


class ActivityRead(BaseModel):
    id: uuid.UUID
    organization_id: uuid.UUID
    user_id: uuid.UUID | None
    project_id: uuid.UUID | None
    issue_id: uuid.UUID | None
    event_type: str
    activity_metadata: dict | None
    created_at: datetime

    class Config:
        from_attributes = True