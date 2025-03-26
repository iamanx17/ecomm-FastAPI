from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.validate import validate_api_key
from app.core.db import get_session
from app.models  import orderCreate
from app.services.order import orderServices


order_router = APIRouter(tags=['Order API'], prefix='/order')
order_service = orderServices()


@order_router.get('/getAll')
def getAllOrders(user_id:int = Depends(validate_api_key), session:Session = Depends(get_session)):
    response = order_service.get_all_orders(user_id=user_id, session=session)
    return response


@order_router.post('/createOrder')
def createOrder(order_model: orderCreate, user_id: int = Depends(validate_api_key), session:Session = Depends(get_session)):
    response = order_service.create_order(order_model=order_model, user_id=user_id, session=session)
    return response


@order_router.post('/updateOrder/{order_id}')
def updateOrder(order_id:str, order_model: orderCreate, user_id: int = Depends(validate_api_key), session:Session=Depends(get_session)):
    response = order_service.update_order(order_id=order_id, order_model = order_model, user_id=user_id, session=session)
    return response
