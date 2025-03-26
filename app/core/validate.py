from fastapi import Depends, Header, HTTPException, status
from sqlmodel import Session
from app.core.db import get_session
from app import constants
from app.services.user import userServices
import jwt


user_services = userServices()


def validate_api_key(session: Session = Depends(get_session), Authorization: str = Header()):
    if 'bearer' in Authorization.lower():
        try:
            token = Authorization.split()
            payload = jwt.decode(token[1], constants.SECRET_KEY, algorithms=[constants.ALOGRITHM])
            return payload.get('user_id') if payload.get('user_id') else None

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token Expired')

        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')

    user = user_services.get_user_by_api_key(api_key=Authorization, session=session)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid API Key')
    return user.id
