from ..dto.jwt import Jwt
from ..dto.payload import Payload
from jose import jwt
from datetime import datetime, timedelta
from ..exceptions.invalid_token import InvalidTokenException
from ...config import settings


class TokenService:
    __secret_key: str
    __algorithm: str
    __access_token_ttl: int
    __refresh_token_ttl: int

    def __init__(self):
        self.__secret_key = settings.jwt_secret
        self.__algorithm = 'HS256'
        self.__access_token_ttl = settings.jwt_access_token_ttl
        self.__refresh_token_ttl = settings.jwt_refresh_token_ttl

    def generate_access_token(self, user_id: str) -> str:
        expire = datetime.utcnow() + timedelta(minutes=self.__access_token_ttl)
        expire = int(round(expire.timestamp()))
        payload = Payload(id=user_id, is_refresh_token=False, exp=expire)

        return jwt.encode(payload.to_json(), self.__secret_key, algorithm=self.__algorithm)

    def generate_refresh_token(self, user_id: str) -> str:
        expire = datetime.utcnow() + timedelta(minutes=self.__refresh_token_ttl)
        expire = int(round(expire.timestamp()))
        payload = Payload(id=user_id, is_refresh_token=True, exp=expire)

        return jwt.encode(payload.to_json(), self.__secret_key, algorithm=self.__algorithm)

    def verify(self, token: str) -> Payload:
        """
        :raises InvalidTokenException
        """
        try:
            payload = jwt.decode(token, self.__secret_key)

            return Payload.from_json(payload)
        except Exception:
            raise InvalidTokenException()

    def generate_tokens(self, user_id: str) -> Jwt:
        access_token = self.generate_access_token(user_id)
        refresh_token = self.generate_refresh_token(user_id)

        return Jwt(access_token=access_token, refresh_token=refresh_token)

    def verify_access_token(self, token: str) -> Payload:
        """
        :raises InvalidTokenException
        """
        payload = self.verify(token)

        if payload.is_refresh_token:
            raise InvalidTokenException()

        return payload

    def verify_refresh_token(self, token: str) -> Payload:
        """
        :raises InvalidTokenException
        """
        payload = self.verify(token)

        if not payload.is_refresh_token:
            raise InvalidTokenException()

        return payload
