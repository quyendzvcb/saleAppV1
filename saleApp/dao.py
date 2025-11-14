import json
from saleApp import app
from models import Category, Product, User
import hashlib


def load_categories():
    # with open("data/category.json", encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query.all()


def load_products(q=None, cate_id=None, page=None):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #
    # if q:
    #     products = [p for p in products if p["name"].find(q) >= 0]
    #
    # if cate_id:
    #     products = [p for p in products if p["cate_id"].__eq__(int(cate_id))]
    #
    # return products
    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if cate_id:
        query = query.filter(Product.cate_id.__eq__(cate_id))

    if page:
        size = app.config["PAGE_SIZE"]
        start =(int(page) - 1)*size
        query = query.slice(start, (start+size))

    return query.all()

def get_user_by_id(id):
    return User.query.get(id)

def auth_user(username, password):
    password = str(hashlib.md5(password.encode("utf-8")).hexdigest())
    return User.query.filter(User.username.__eq__(username)and User.password.__eq__(password)).first()

def count_product():
    return Product.query.count()

def load_products_by_id(id):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #
    #     for q in products:
    #         if q["id"].__eq__(id):
    #             return q
    # return None
    return Product.query.get(id)

if __name__ == "__main__":
    with app.app_context():
        print(auth_user("user", "123"))
