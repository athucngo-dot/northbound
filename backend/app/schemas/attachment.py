import uuid
from datetime import datetime
from pydantic import BaseModel


class AttachmentCreate(BaseModel):
    issue_id: uuid.UUID | None = None
    comment_id: uuid.UUID | None = None
    filename: str
    filepath: str
    uploaded_by: uuid.UUID | None = None


class AttachmentRead(BaseModel):
    id: uuid.UUID
    issue_id: uuid.UUID | None
    comment_id: uuid.UUID | None
    filename: str
    filepath: str
    uploaded_by: uuid.UUID | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True