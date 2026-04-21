from xmlrpc.client import DateTime

from database import Base
from sqlalchemy import String, Integer, Column, Numeric, Text, DateTime, ForeignKey
from sqlalchemy_utils import Choice
from datetime import datetime
from sqlalchemy.orm import relationship


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    desc = Column(Text, nullable=True)
    price = Column(Numeric(10,2))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at  = Column(DateTime, default=datetime.now())

    # order = relationship('Orders',  back_populates='products')
    # user = relationship('User',  back_populates='products')

class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'), unique=True)


class CardItem(Base):
    __tablename__ = 'carditem'
    id = Column(Integer, primary_key=True)
    cars_id = Column(ForeignKey('card.id'), unique=True)
    products_id = Column(ForeignKey('products.id'))
    quantity = Column(Integer)


