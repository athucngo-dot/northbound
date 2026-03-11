from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.auth import Token
from app.core.security import verify_password, create_access_token


router = APIRouter()


@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):

    repo = UserRepository(db)

    user = repo.get_by_email(email)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer",
    }