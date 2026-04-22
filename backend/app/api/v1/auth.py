from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(data: LoginRequest, response: Response, db: Session = Depends(get_db)):
    token = AuthService(db).login(data.email, data.password)
    AuthService(db).set_auth_cookies(response, token)

    return {"message": "login successful"}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "logout successful"}

