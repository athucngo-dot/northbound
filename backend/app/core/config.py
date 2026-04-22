from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    LOG_PATH: str = "logs/app.log"

    ALLOWED_ORIGINS: str = ""

    @property
    def allowed_origins(self) -> list[str]:
        parts = self.ALLOWED_ORIGINS.split(",")

        result = []
        for part in parts:
            cleaned = part.strip()
            if cleaned:
                result.append(cleaned)

        return result
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
