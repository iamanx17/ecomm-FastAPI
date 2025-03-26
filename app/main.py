from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.db import init_db
from app.api.main import app_router
from app import constants


init_db()
app = FastAPI(title='Welcome to Ecommerce App', description='create product, place order', summary='Developed by @iamanx17')
app.add_middleware(CORSMiddleware, allow_origins=constants.ALLOWED_HOSTS, allow_credentials = ['*'], allow_methods=['*'], allow_headers=['*'] )
app.include_router(app_router)
print('server started successfully')