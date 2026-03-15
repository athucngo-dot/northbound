import uuid
from sqlalchemy import DateTime, ForeignKey, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from app.db.base import Base
from app.models.enum import OrganizationMemberRole, OrganizationMemberStatus


class OrganizationMember(Base):
    __tablename__ = "organization_members"
    __table_args__ = (UniqueConstraint("user_id", "organization_id"),)

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
    )

    organization_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("organizations.id", ondelete="CASCADE"),
    )

    role: Mapped[OrganizationMemberRole] = mapped_column(
        Enum(OrganizationMemberRole),
        default=OrganizationMemberRole.member,
        nullable=False,
    )

    status: Mapped[OrganizationMemberStatus] = mapped_column(
        Enum(OrganizationMemberStatus),
        default=OrganizationMemberStatus.invited,
        nullable=False,
    )

    invited_by: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    
    invited_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    joined_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    member = relationship("User", back_populates="organization_members")
    organization = relationship("Organization", back_populates="organization_members")