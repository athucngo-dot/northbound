# app/models/enums.py

import enum


class OrganizationMemberRole(str, enum.Enum):
    owner = "owner"
    admin = "admin"
    member = "member"

class OrganizationMemberStatus(str, enum.Enum):
    invited = "invited"
    active = "active"
    removed = "removed"


class ProjectStatus(str, enum.Enum):
    active = "active"
    archived = "archived"


class EpicStatus(str, enum.Enum):
    active = "active"
    completed = "completed"


class SprintStatus(str, enum.Enum):
    planned = "planned"
    active = "active"
    completed = "completed"


class IssueStatus(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class IssuePriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"