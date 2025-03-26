from sqlmodel import select
from app.models import User
from passlib.context import CryptContext
from datetime import datetime, timedelta
from app import constants
import jwt

pwd_context = CryptContext(schemes=['bcrypt'])


class userServices:

    def hash_password(self, password):
        return pwd_context.hash(password)

    def verify_password(self, password, hashed_password):
        return pwd_context.verify(password, hashed_password)

    def create_user(self, user, session):
        user.password = self.hash_password(user.password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return {
            'message': 'User created successfully!!',
            'user': user
        }

    def get_user(self, user_id, session):
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()

        data = {
            'user_id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'timestamp': user.timestamp,
            'api_key': user.api_key,
            'images': user.images,
            'orders': user.orders,
            'products': user.products
        }
        return {'message': 'User not found'} if not user else data
    
    def get_user_by_api_key(self, api_key, session):
        statement = select(User).where(User.api_key == api_key)
        user = session.exec(statement).first()
        return user if user else None

    def delete_user(self, user_id, session):
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()
        print('user is', user)
        if not user:
            return {'message':f"User doesn't exist with the user_id: {user_id}"}

        session.delete(user)
        session.commit()
        return {'message':'User deleted successfully'}

    def update_user(self, user_id, user_model, session):
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()
        if not user:
            return {'message': f'User doesnt exist with the user id: {user_id}'}
        
        user.first_name = user_model.first_name
        user.last_name = user_model.last_name
        user.email = user_model.email

        session.add(user)
        session.commit()
        session.refresh(user)

        return {'message': 'user updated successfully', 'user': user}
    
    def login_user(self, email, password, session):
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()

        if not user:
            return {"message": f"User doesn't exist with the user email: {email}"}

        if not self.verify_password(password, user.password):
            return {"message": f"Password not matched"}
        
        to_encode= {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=constants.ACCESS_TOKEN_EXPIRE_TIME_MINUTES)
        }

        bearer_token = jwt.encode(to_encode, constants.SECRET_KEY, algorithm=constants.ALOGRITHM)


        return {
            'user_id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'bearer_token': f"Bearer {bearer_token}",
            'timestamp': user.timestamp
        }
