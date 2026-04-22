import uuid
from sqlalchemy import Boolean, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from app.db.base import Base


class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    projects = relationship("Project", back_populates="organization", cascade="all, delete")
    organization_members = relationship("OrganizationMember", back_populates="organization", cascade="all, delete")
    
    # Access users in the organization
    members = relationship(
        "User",
        secondary="organization_members",
        primaryjoin="Organization.id==OrganizationMember.organization_id",
        secondaryjoin="User.id==OrganizationMember.user_id",
        back_populates="organizations",
        viewonly=True # This relationship is read-only since the association table is managed through OrganizationMember
    )

    activities = relationship("Activity", back_populates="organization", cascade="all, delete")