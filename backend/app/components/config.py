from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    jwt_secret: str
    jwt_access_token_ttl: int
    jwt_refresh_token_ttl: int
    encryption_secret_key: str
    gpt_model: str


settings = Settings()
