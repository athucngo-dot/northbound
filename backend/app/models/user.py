import uuid
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    organization_members = relationship("OrganizationMember", back_populates="member", cascade="all, delete")
        
    # Relationships to access organizations directly through the association table
    organizations = relationship("Organization", secondary="organization_members", back_populates="members")

    assigned_issues = relationship("Issue", back_populates="assignee")
    reported_issues = relationship("Issue", back_populates="reporter")

    comments = relationship("Comment", back_populates="user")
    activities = relationship("Activity", back_populates="user")
    attachments = relationship("Attachment", back_populates="uploader")