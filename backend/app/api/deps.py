from fastapi import Depends, HTTPException, status, Cookie
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.models.user import User
from app.core.config import settings
from app.schemas.auth import TokenPayload
from app.core.security import decode_access_token


def get_current_user(
    access_token: str = Cookie(None),
    db: Session = Depends(get_db)
) -> User:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    if not access_token:
        raise credentials_exception

    try:
        payload = decode_access_token(access_token)

        token_data = TokenPayload(**payload)

        if not token_data.sub:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    try:
        user_id = UUID(token_data.sub)
    except ValueError:
        raise credentials_exception

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise credentials_exception

    return user