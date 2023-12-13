from pydantic import BaseModel


class Jwt(BaseModel):
    access_token: str
    refresh_token: str
