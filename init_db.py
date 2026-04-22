from database import Base, engine
from users.models import User
from order.models import Products, OrderItem, Order, Card, CardItem

Base.metadata.create_all(bind=engine)