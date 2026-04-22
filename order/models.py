from database import Base
from sqlalchemy import String, Integer, Column, Numeric, Text, DateTime, ForeignKey, Enum
from datetime import datetime
from sqlalchemy.orm import relationship


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    desc = Column(Text, nullable=True)
    price = Column(Numeric(10,2))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at  = Column(DateTime, default=datetime.now)

    order = relationship('Order',  back_populates='products')
    user = relationship('User',  back_populates='products')

class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'), unique=True)

    items = relationship('CardItem', back_populates='card')
    user = relationship('User',  back_populates='card')



class CardItem(Base):
    __tablename__ = 'carditem'
    id = Column(Integer, primary_key=True)
    cars_id = Column(ForeignKey('card.id'))
    products_id = Column(ForeignKey('products.id'))
    quantity = Column(Integer)

    card = relationship('Card', back_populates='items')



class Order(Base):
    STATUS = (
        ('new', 'New'),
        ('in_progress', 'In_progress'),
        ('done', 'Done')
    )
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'))
    status = Column(Enum('new', 'in_progress', 'done', name='order_status'), default='new')

    items_order = relationship('OrderItem', back_populates='order')
    user = relationship('User',  back_populates='order')




class OrderItem(Base):
    __tablename__ = 'orderitem'
    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    products_id = Column(ForeignKey('products.id'))
    quantity = Column(Integer)


    items_order = relationship('OrderItem', back_populates='order')
