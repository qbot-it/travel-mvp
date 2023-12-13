from pydantic import BaseModel
from .jwt import Jwt
from ...user.dto.user import User


class LoggedIn(BaseModel):
    jwt: Jwt
    user: User
