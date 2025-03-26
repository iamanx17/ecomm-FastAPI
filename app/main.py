from fastapi import FastAPI
from app.core.db import init_db
from app.api.main import app_router


init_db()
app = FastAPI(title='Welcome to Ecommerce App', description='create product, place order', summary='Developed by @iamanx17')
app.include_router(app_router)
print('server started successfully')