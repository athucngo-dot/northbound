import uuid
from datetime import datetime
from pydantic import BaseModel, field_validator


class OrganizationCreateRequest(BaseModel):
    name: str
    description: str | None = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()

        if not value or len(value.strip()) < 2:
            raise ValueError("Organization name must be at least 2 characters long.")
        
        if len(value) > 255:
            raise ValueError(
                "Organization name cannot exceed 255 characters."
            )
        
        return value.strip()

class OrganizationCreateInternal(BaseModel):
    name: str
    slug: str
    description: str | None = None
    is_active: bool = True


class OrganizationRead(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    description: str | None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True # SQLAlchemy → Pydantic


class OrganizationSummaryRead(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    is_active: bool

    class Config:
        from_attributes = True