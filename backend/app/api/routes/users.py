from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.api.deps import get_db


router = APIRouter()


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    service = UserService(db)

    return service.create_user(user)