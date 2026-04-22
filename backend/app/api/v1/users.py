from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.api.deps import get_current_user, get_db
from app.core.security import create_access_token

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, response: Response, db: Session = Depends(get_db)):
    service = UserService(db)    
    new_user = service.create_user(user)

    token = create_access_token({"sub": str(new_user.id)})
    AuthService(db).set_auth_cookies(response, token)

    return new_user


@router.get("/me", response_model=UserRead)
def read_current_user(current_user = Depends(get_current_user)):
    return current_user

