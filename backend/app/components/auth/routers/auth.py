from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dto.refresh import Refresh
from ..exceptions.invalid_credentials import InvalidCredentialsException
from ..exceptions.invalid_token import InvalidTokenException
from ..services.auth_service import AuthService
from ...user.exceptions.user_not_found import UserNotFoundException
from ....db.database import get_session
from ..dto.jwt import Jwt
from ..dto.logged_in import LoggedIn
from ..dto.login import Login

router = APIRouter(prefix='/api/v1/auth')


@router.post("/login", response_model=LoggedIn, tags=["auth"])
async def login(dto: Login, db: Session = Depends(get_session)):
    try:
        auth_service = AuthService(db)

        return auth_service.login(dto.email, dto.password)
    except InvalidCredentialsException as e:
        raise HTTPException(401, detail=str(e.message))


@router.post("/refresh", response_model=Jwt, tags=["auth"])
async def refresh(refresh_token: Refresh, db: Session = Depends(get_session)):
    try:
        auth_service = AuthService(db)

        return auth_service.refresh(refresh_token.token)
    except InvalidTokenException as e:
        raise HTTPException(422, detail=str(e.message))
    except UserNotFoundException as e:
        raise HTTPException(404, detail=str(e.message))

