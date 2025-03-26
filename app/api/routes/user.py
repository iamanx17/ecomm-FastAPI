from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.models import User, loginUser
from app.core.validate import validate_api_key
from app.core.db import get_session
from app.services.user import userServices
import jwt


user_router = APIRouter(tags=['User API'], prefix='/user')
user_services = userServices()


@user_router.get('/getUser')
def get_user(user_id: str = Depends(validate_api_key), session: Session = Depends(get_session)):
    response = user_services.get_user(user_id=user_id, session=session)
    return response

@user_router.post('/createUser')
def create_user(user_model: User, session: Session = Depends(get_session)):
    response = user_services.create_user(user_model, session)
    return response


@user_router.delete('/removeUser')
def remove_user(user_id: str = Depends(validate_api_key), session: Session = Depends(get_session)):
    response = user_services.delete_user(user_id=user_id, session=session)
    return response


@user_router.post('/updateUser')
def update_user(user_model: User, user_id: str = Depends(validate_api_key), session: Session = Depends(get_session)):
    response = user_services.update_user(user_id=user_id, user_model=user_model, session=session)
    return response

@user_router.post('/loginUser')
def login_user(user_model: loginUser, session:Session = Depends(get_session)):
    response = user_services.login_user(email=user_model.email, password=user_model.password, session=session)
    return response