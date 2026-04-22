from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import hash_password


class UserService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, user: UserCreate):

        existing = self.repo.get_by_email(user.email)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )

        hashed = hash_password(user.password)

        try:
            return self.repo.create(user, hashed)
        except IntegrityError:
            # race conditions can bypass the get_by_email check, so catch the unique constraint violation here as well
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists."
            )