from sqlmodel import select, Session
from app.models import Products, Images


class productService:
    def get_all_product(self, user_id, session):
        statement = select(Products).where(Products.user_id == user_id)
        result = session.exec(statement).all()
        
        all_products = []
        for pro in result:
            product_data = {
                "id": pro.id,
                "pname": pro.pname,
                "p_desc": pro.p_desc,
                "price": pro.price,
                "user_id": pro.user_id,
                "images": [img.image_url for img in pro.images],
                "total_orders": len(pro.orders)

            }
            all_products.append(product_data)

        return {
            'products': all_products
        }

    def remove_product(self, product_id, user_id, session):
        statement = select(Products).where((Products.id == product_id) & (Products.user_id == user_id))
        product = session.exec(statement).first()
        if not product:
            return {'message': 'product doesnt exists'}
        
        session.delete(product)
        session.commit()
        return {'message': 'Product has been deleted successfully'}


    def add_product(self, product_model, user_id, session):
        product = Products(pname=product_model.pname, p_desc=product_model.p_desc, price=product_model.price, user_id=user_id)
        session.add(product)
        session.commit()
        session.refresh(product)

        images_entity = []
        for img in product_model.images:
            image = Images(image_url=img, user_id=user_id,product_id=product.id)
            images_entity.append(image)
        
        session.add_all(images_entity)
        session.commit()

        return {
            'message': 'product has been created successfully',
        }
    
    def update_product(self, product_model,product_id, user_id, session):
        statement = select(Products).where((Products.id == product_id) & (Products.user_id == user_id))
        product = session.exec(statement).first()

        if not product:
            return {'message': 'Product doesnt exists'}
        
        product.pname = product_model.pname
        product.p_desc = product_model.p_desc

        statement = select(Images).where((Images.product_id == product_id) & (Images.user_id == user_id))
        images = session.exec(statement).all()
        for img in images:
            session.delete(img)
            session.commit()

        images_entity = []
        for img in product_model.images:
            image = Images(image_url=img, user_id=user_id, product_id=product.id)
            images_entity.append(image)
        
        session.add_all(images_entity)
        session.commit()
        return {
            'message': 'Product has been updated successfully'
        }
    
    def retrieve_product(self, product_id, user_id, session):
        statement = select(Products).where((Products.id == product_id) & (Products.user_id == user_id))
        product = session.exec(statement).first()
        if not product:
            return {'message': 'product deosnt exists'}
        
        product_data={
            'id': product.id,
            'images': [{'image_id': img.id, 'image_url':img.image_url} for img in product.images],
            'pname': product.pname,
            'p_desc': product.p_desc,
            'total_orders': len(product.orders)
        }
        print('orders are', product.orders)
        return {
            'product': product_data
        }
        
        
