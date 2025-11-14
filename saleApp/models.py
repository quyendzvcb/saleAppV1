import json

from sqlalchemy.orm import relationship
from saleApp import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, false, Boolean, DateTime, Enum
from flask_login import UserMixin
from datetime import datetime
from enum import Enum as RoleEnum

class UserEnum(RoleEnum):
    USER = 1
    ADMIN = 2

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), unique=True, nullable=False)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now)

    def __str__(self):
        return self.name

class User(Base, UserMixin):
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    avatar = Column(String(300), default="https://res.cloudinary.com/dy1unykph/image/upload/v1729091944/refurb-iphone-13-pro-max-blue-2023_tuhb2j.jpg")
    role = Column(Enum(UserEnum), nullable=False, default=UserEnum.USER)

class Category(Base):
    products = relationship('Product', backref="category", lazy=True)

class Product(Base):
    price = Column(Float, default=0.0)
    image = Column(String(300), default="https://res.cloudinary.com/dy1unykph/image/upload/v1729091944/refurb-iphone-13-pro-max-blue-2023_tuhb2j.jpg")
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # c1 = Category(name="Laptop")
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet")
        #
        #
        # db.session.add_all([c1,c2,c3])
        #
        # with open("data/product.json", encoding="utf-8") as f:
        #     products = json.load(f)
        #
        #     for p in products:
        #         db.session.add(Product(**p))

        import hashlib

        u = User(name="User", username="user", password= str(hashlib.md5("123".encode("utf-8")).hexdigest()))

        db.session.add(u)

        db.session.commit()