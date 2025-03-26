from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.validate import validate_api_key
from app.core.db import get_session
from app.models import addProductModel
from app.services.product import productService

product_router = APIRouter(tags=['Product API'], prefix='/product')
product_service = productService()



@product_router.get('/getAll', description='Fetch the list of products')
def fetch_all_Product(user_id:int = Depends(validate_api_key), session:Session = Depends(get_session)):
    print('userid fetched is', user_id)
    response = product_service.get_all_product(user_id=user_id, session=session)
    return response

@product_router.get('/retrieveProduct/{product_id}', description='Fetch product by product id')
def retrieve_product_by_id(product_id:str,user_id:int = Depends(validate_api_key), session:Session=Depends(get_session)):
    response = product_service.retrieve_product(product_id=product_id, user_id=user_id, session=session)
    return response

@product_router.post('/addProduct', description='Create product')
def addProduct(product_model: addProductModel, user_id:str = Depends(validate_api_key), session: Session = Depends(get_session)):
    response = product_service.add_product(product_model=product_model,user_id=user_id, session=session)
    return response

@product_router.delete('/removeProduct/{product_id}', description='Remove the product by productId')
def removeProduct(product_id: str, user_id:str = Depends(validate_api_key), session:Session = Depends(get_session)):
    response = product_service.remove_product(product_id=product_id, user_id=user_id, session=session)
    return response


@product_router.post('/updateProduct/{product_id}', description='Update the product details')
def updateProduct(product_model: addProductModel,product_id:str, user_id: str = Depends(validate_api_key), session:Session=Depends(get_session)):
    response = product_service.update_product(product_model=product_model, product_id=product_id, user_id=user_id, session=session)
    return response
    
