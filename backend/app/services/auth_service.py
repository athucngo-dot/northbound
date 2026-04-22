from fastapi import HTTPException, Response
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.core.security import verify_password, create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def login(self, email: str, password: str) -> str:
        user = self.user_repo.get_by_email(email)

        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        token = create_access_token({"sub": str(user.id)})
        return token
    
    def set_auth_cookies(self, response: Response, token: str):
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,     # httpOnly to prevent JavaScript access
            secure=True,       # HTTPS only (False in local dev if needed)
            samesite="lax",    # CSRF protection - allows sending cookies on same-site requests
            max_age=60 * 60 * 24,  # 1 day expiration
        )