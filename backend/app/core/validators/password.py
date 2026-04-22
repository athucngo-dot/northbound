import re

from pydantic_core import PydanticCustomError

# Validators: passord regex at least 8 characters, one uppercase, one lowercase, and one number
PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"


def validate_password_strength(password: str) -> str:
    if not re.match(PASSWORD_REGEX, password):
        raise PydanticCustomError(
            "password_strong",
            "Password must be at least 8 characters and include uppercase, lowercase, and a number."
        )
    return password