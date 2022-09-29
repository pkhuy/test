from datetime import date, datetime
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.sql.schema import ForeignKey, Table
from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from flask_login import LoginManager


class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, nullable=False)
    password = Column(String)

    def __repr__(self):
        return f"{self.id}"

    def get_id(self):
        return self.id
