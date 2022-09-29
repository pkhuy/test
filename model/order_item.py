from sqlalchemy.sql.schema import ForeignKey, Table
from .base import Base
from sqlalchemy import Column, Integer, String


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    product_id = Integer, ForeignKey('products.id')
    cart_id = Column(Integer, ForeignKey('carts.id'))
    price = Column(Integer)
    created_by_id = Column(Integer, ForeignKey('users.id'))
