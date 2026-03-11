# app/models/enums.py

import enum


class OrganizationUserRole(str, enum.Enum):
    owner = "owner"
    admin = "admin"
    member = "member"


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