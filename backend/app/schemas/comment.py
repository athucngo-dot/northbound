import uuid
from datetime import datetime
from pydantic import BaseModel


class CommentCreate(BaseModel):
    issue_id: uuid.UUID
    user_id: uuid.UUID | None = None
    comment: str


class CommentRead(BaseModel):
    id: uuid.UUID
    issue_id: uuid.UUID
    user_id: uuid.UUID | None
    comment: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True