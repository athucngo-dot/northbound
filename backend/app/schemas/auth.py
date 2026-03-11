from pydantic import BaseModel, EmailStr


# Schemas for authentication
# These are used for login and token management
class OAuth2PasswordRequestForm(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: str | None = None