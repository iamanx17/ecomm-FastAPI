from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr
from app.core.order import generate_order_id
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr = Field(unique=True, index=True)
    password: str
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)
    api_key: str = Field(default_factory=lambda: str(uuid.uuid4()))

    images: List["Images"] = Relationship(back_populates='user', cascade_delete=True)
    products: List["Products"] = Relationship(back_populates="user", cascade_delete=True)
    orders: List["Orders"] = Relationship(back_populates="user", cascade_delete=True)


class loginUser(SQLModel):
    email: EmailStr
    password: str

class Images(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    image_url: str
    product_id: int = Field(foreign_key="products.id")
    user_id: int = Field(foreign_key="user.id")

    user: Optional["User"] = Relationship(back_populates="images")
    product: Optional["Products"] = Relationship(back_populates="images")


class OrderProductLink(SQLModel, table=True):
    order_id: int = Field(foreign_key="orders.id", primary_key=True)
    product_id: int = Field(foreign_key="products.id", primary_key=True)


class Products(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    pname: str
    p_desc: str
    price: float
    user_id: Optional[int] = Field(foreign_key="user.id")


    user: Optional["User"] = Relationship(back_populates="products")
    images: List["Images"] = Relationship(back_populates="product")  
    orders: List["Orders"] = Relationship(back_populates="products", link_model=OrderProductLink)

class addProductModel(SQLModel):
    pname: str
    p_desc: str
    price: float
    images: List[str]

class StatusModel(Enum):
    CREATED = 'created'
    SHIPPED = 'shipped'
    REFUNDED = 'refunded'



class Orders(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: str = Field(default_factory=generate_order_id, unique=True, index=True)
    user_id: int = Field(foreign_key="user.id")

    user: Optional["User"] = Relationship(back_populates="orders")
    products: List["Products"] = Relationship(back_populates="orders", link_model=OrderProductLink)

    status: StatusModel = Field(default=StatusModel.CREATED)
    discount: float
    order_total: float
    shipping_fee: float
    order_tax: float
    city: str
    pincode: int
    country: str
    phone_number: int = Field(min_length=10, max_length=10)
    landmark: Optional[str] = None


class orderCreate(SQLModel):
    products: List[str]
    discount: float
    order_total: float
    shipping_fee: float
    order_tax: float
    
    city: str
    pincode: int
    country:str
    phone_number:int
    landmark: Optional[str]

class updateOrder(SQLModel):
    discount: Optional[float]
    shipping_fee: Optional[float]
    order_tax: Optional[float]

    city:Optional[str]
    pincode: Optional[int]
    country: Optional[str]
    phone_number:Optional[int]
    landmark: Optional[str]