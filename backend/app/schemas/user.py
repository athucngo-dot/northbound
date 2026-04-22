import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator
from app.core.normalizers import normalize_email, normalize_name
from app.core.validators import validate_password_strength


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str

    @field_validator("email")
    @classmethod
    def normalize_email_field(cls, value: str) -> str:
        return normalize_email(value)

    @field_validator("first_name")
    @classmethod
    def normalize_first_name(cls, value: str) -> str:
        return normalize_name(value)

    @field_validator("last_name")
    @classmethod
    def normalize_last_name(cls, value: str) -> str:
        return normalize_name(value)

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        return validate_password_strength(value)


class UserRead(BaseModel):
    id: uuid.UUID
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True