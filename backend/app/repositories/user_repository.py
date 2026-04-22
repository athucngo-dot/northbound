from sqlalchemy.orm import Session
import uuid
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: uuid.UUID):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user: UserCreate, hashed_password: str):
        db_user = User(
            email=user.email,
            hashed_password=hashed_password,
            first_name=user.first_name,
            last_name=user.last_name
        )
        self.db.add(db_user)
        self.db.flush()  # Flush to assign an ID before commit
        self.db.refresh(db_user)
        return db_user

    def list_all(self):
        return self.db.query(User).all()