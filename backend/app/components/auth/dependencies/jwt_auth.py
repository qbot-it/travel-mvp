from fastapi import HTTPException, Depends
from ..exceptions.invalid_token import InvalidTokenException
from ..services.token_service import TokenService
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import re

auth_scheme = HTTPBearer()


async def auth_jwt(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    try:
        token = re.sub("^bearer\\s+", '', token.credentials, flags=re.IGNORECASE).strip()
        token_service = TokenService()
        payload = token_service.verify_access_token(token)
        return payload.id
    except InvalidTokenException as e:
        raise HTTPException(401, detail=e.message)
