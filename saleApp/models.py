import json

from sqlalchemy.orm import relationship
from saleApp import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, false


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), unique=True, nullable=False)
    products = relationship('Product', backref="category", lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), unique=True, nullable=False)
    price = Column(Float, default=0.0)
    image = Column(String(300), default="https://res.cloudinary.com/dy1unykph/image/upload/v1729091944/refurb-iphone-13-pro-max-blue-2023_tuhb2j.jpg")
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        c1 = Category(name="Laptop")
        c2 = Category(name="Mobile")
        c3 = Category(name="Tablet")
        # db.session.commit()
        #
        # db.session.add_all([c1,c2,c3])
        db.session.query(Product).delete()
        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)

            for p in products:
                db.session.add(Product(**p))

        db.session.commit()