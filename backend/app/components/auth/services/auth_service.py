from sqlalchemy.orm import Session
from .token_service import TokenService
from ..dto.jwt import Jwt
from ..dto.logged_in import LoggedIn
from passlib.hash import bcrypt
from ..exceptions.invalid_credentials import InvalidCredentialsException
from ...user.dto.user import User
from ...user.exceptions.user_not_found import UserNotFoundException
from ...user.services.user_service import UserService


class AuthService:
    __user_service: UserService
    __token_service: TokenService

    def __init__(self, db: Session):
        self.__user_service = UserService(db)
        self.__token_service = TokenService()

    def login(self, email: str, password: str) -> LoggedIn:
        """
        :raises InvalidCredentialsException
        """
        try:
            user = self.__user_service.get_user_by_email(email)
        except UserNotFoundException:
            raise InvalidCredentialsException()

        if not bcrypt.verify(password, user.password):
            raise InvalidCredentialsException()

        jwt = self.__token_service.generate_tokens(str(user.id))

        return LoggedIn(user=User(email=user.email, name=user.name), jwt=jwt)

    def refresh(self, refresh_token: str) -> Jwt:
        """
        :raises UserNotFoundException
        :raises InvalidTokenException
        """
        payload = self.__token_service.verify_refresh_token(refresh_token)
        user = self.__user_service.get_user(payload.id)

        return self.__token_service.generate_tokens(str(user.id))
