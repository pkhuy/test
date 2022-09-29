from sqlalchemy.sql.schema import ForeignKey, Table
from .base import Base
from sqlalchemy import Column, Integer, String


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'))
    created_by_id = Column(Integer, ForeignKey('users.id'))
