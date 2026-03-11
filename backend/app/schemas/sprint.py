import uuid
from datetime import datetime, date
from pydantic import BaseModel
from app.models.enum import SprintStatus


class SprintCreate(BaseModel):
    project_id: uuid.UUID
    name: str
    goal: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    status: SprintStatus | None = None


class SprintRead(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    goal: str | None
    start_date: date | None
    end_date: date | None
    status: SprintStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True