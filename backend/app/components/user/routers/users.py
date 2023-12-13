from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.user_service import UserService
from ...auth.dependencies.jwt_auth import auth_jwt
from ....db.database import get_session
from ..dto.user import User

router = APIRouter(prefix='/api/v1/users')


@router.get("/me", response_model=User, tags=["user"])
async def me(db: Session = Depends(get_session), user_id=Depends(auth_jwt)) -> User:
    user_service = UserService(db)
    user = user_service.get_user(user_id)
    return User(email=user.email, name=user.name)
