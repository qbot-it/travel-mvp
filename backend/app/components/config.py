from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    jwt_secret: str
    jwt_access_token_ttl: int
    jwt_refresh_token_ttl: int
    encryption_secret_key: str
    gpt_model: str
    amadeus_api_url: str
    amadeus_api_auth_url: str
    amadeus_api_key: str
    amadeus_api_secret: str


settings = Settings()
