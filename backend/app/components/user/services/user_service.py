from sqlalchemy.orm import Session, sessionmaker, scoped_session
from ..exceptions.user_not_found import UserNotFoundException
from ...user.models.user import User


class UserService:
    __db: Session

    def __init__(self, db: Session):
        self.__db = db

    def get_user(self, user_id: str) -> User:
        """
        :raises UserNotFoundException
        """
        user: User | None = self.__db.query(User).where(User.id == user_id).first()

        if not isinstance(user, User):
            raise UserNotFoundException()

        return user

    def get_user_by_email(self, email: str) -> User:
        """
        :raises UserNotFoundException
        """
        user: User | None = self.__db.query(User).where(User.email == email).first()

        if not isinstance(user, User):
            raise UserNotFoundException()

        return user
