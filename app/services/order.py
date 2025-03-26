from sqlmodel import select
from app.models import Orders, Products, OrderProductLink


class orderServices:
    def get_all_orders(self, user_id, session):
        statement = select(Orders).where(Orders.user_id == user_id)
        orders = session.exec(statement).all()
        
        order_entities = []
        for order in orders:
            order_entities.append({
                "user_id": order.user_id,
                "order_id": order.order_id,
                "products": order.products,
                "discount": order.discount,
                "order_total": order.order_total,
                "shipping_fee": order.shipping_fee,
                "order_tax": order.order_tax,
                "city": order.city,
                "pincode": order.pincode,
                "country": order.country,
                "phone_number": order.phone_number,
                "landmark": order.landmark
            })

        return {
            'orders': order_entities
        }

    def retrieve_order(self, order_id, user_id, session):
        statement = select(Orders).where((Orders.id == order_id) & (Orders.user_id == user_id))
        order = session.exec(statement).first()
        if not order:
            return {'message': 'Orders not found'}

        return {
            'order': order
        }

    def create_order(self, order_model, user_id, session):
        statement = select(Products).where(Products.id.in_(order_model.products))
        products = session.exec(statement)
        if not products:
            return {'message': "No valid product found for this id"}

        order = Orders(
            user_id=user_id,
            discount=order_model.discount,
            order_total=order_model.order_total,
            shipping_fee=order_model.shipping_fee,
            order_tax=order_model.order_tax,
            city=order_model.city,
            pincode=order_model.pincode,
            country=order_model.country,
            phone_number=order_model.phone_number,
            landmark=order_model.landmark
        )
        session.add(order)
        session.commit()
        session.refresh(order)

        order_product_entity = []
        for product in products:
            order_product = OrderProductLink(order_id=order.id, product_id=product.id)
            order_product_entity.append(order_product)

        session.add_all(order_product_entity)
        session.commit()
        session.refresh(order)

        return {
            'message': 'Order has been created successfully',
            'order': {
                "user_id": order.user_id,
                "order_id": order.order_id,
                "products": order.products,
                "discount": order.discount,
                "order_total": order.order_total,
                "shipping_fee": order.shipping_fee,
                "order_tax": order.order_tax,
                "city": order.city,
                "pincode": order.pincode,
                "country": order.country,
                "phone_number": order.phone_number,
                "landmark": order.landmark
            }
        }

    def update_order(self, order_id, user_id, order_model, session):
        statement = select(Orders).where((Orders.order_id == order_id) & (Orders.user_id == user_id))
        order = session.exec(statement)
        if not order:
            return {'message': "Order doesnt exists"}

        order.discount = order_model.get('discount', order.discount)
        order.shipping_fee = order_model.get('shipping_fee', order.shipping_fee)
        order.order_tax = order_model.get('order_tax', order.order_tax)
        order.city = order_model.get('city', order.city)
        order.pincode = order_model.get('pincode', order.pincode)
        order.country = order_model.get('country', order.country)
        order.phone_number = order_model.get('phone_number', order.phone_number)
        order.landmark = order_model.get('landmark', order.landmark)

        session.add(order)
        session.commit()
        session.refresh(order)
        return {
            'message': 'Order status has been changed successfully',
            'order': {
                "user_id": order.user_id,
                "order_id": order.order_id,
                "products": order.products,
                "discount": order.discount,
                "order_total": order.order_total,
                "shipping_fee": order.shipping_fee,
                "order_tax": order.order_tax,
                "city": order.city,
                "pincode": order.pincode,
                "country": order.country,
                "phone_number": order.phone_number,
                "landmark": order.landmark
            }
        }
