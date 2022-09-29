from datetime import datetime

from flask_sqlalchemy import SQLAlchemy, Model


class Customer(Model):
    id = SQLAlchemy.Column(SQLAlchemy.Integer, primary_key=True)
    content = SQLAlchemy.Column(SQLAlchemy.String(200), nullable=False)
    date_created = SQLAlchemy.Column(SQLAlchemy.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id