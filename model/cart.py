from sqlalchemy.sql.schema import ForeignKey, Table
from .base import Base
from sqlalchemy import Column, Integer, String


class Cart(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    created_by_id = Column(Integer, ForeignKey('users.id'))
