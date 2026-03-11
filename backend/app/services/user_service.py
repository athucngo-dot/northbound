from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import hash_password


class UserService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, user: UserCreate):

        existing = self.repo.get_by_email(user.email)

        if existing:
            raise ValueError("User already exists")

        hashed = hash_password(user.password)

        return self.repo.create(user, hashed)