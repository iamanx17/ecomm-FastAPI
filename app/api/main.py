from fastapi import APIRouter
from app.api.routes.order import order_router
from app.api.routes.product import product_router
from app.api.routes.user import user_router





app_router = APIRouter()
app_router.include_router(order_router)
app_router.include_router(product_router)
app_router.include_router(user_router)

