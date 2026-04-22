def normalize_email(email: str) -> str:
    # Normalize email by stripping whitespace and converting to lowercase
    return email.strip().lower()