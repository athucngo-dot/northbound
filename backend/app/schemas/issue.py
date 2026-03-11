import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.enum import IssueStatus, IssuePriority


class IssueCreate(BaseModel):
    project_id: uuid.UUID
    sprint_id: uuid.UUID | None = None
    epic_id: uuid.UUID | None = None

    title: str
    description: str | None = None

    status: IssueStatus | None = None
    priority: IssuePriority | None = None

    assignee_id: uuid.UUID | None = None
    reporter_id: uuid.UUID | None = None

    story_points: int | None = None


class IssueRead(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    sprint_id: uuid.UUID | None
    epic_id: uuid.UUID | None

    title: str
    description: str | None

    status: IssueStatus
    priority: IssuePriority

    assignee_id: uuid.UUID | None
    reporter_id: uuid.UUID | None

    story_points: int | None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True