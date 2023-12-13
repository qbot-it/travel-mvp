from pydantic import BaseModel


class Refresh(BaseModel):
    token: str
