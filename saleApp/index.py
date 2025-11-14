from flask import render_template, request, redirect
import dao
from saleApp import app, login
import math
from flask_login import login_user, current_user


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = request.args.get("page")
    pages = math.ceil(dao.count_product() / app.config["PAGE_SIZE"])
    products = dao.load_products(q=q, cate_id=cate_id, page=page)
    return render_template("index.html", products=products, pages=pages)


@app.route("/products/<int:id>")
def detail(id):
    product = dao.load_products_by_id(id)
    return render_template("products-details.html", product=product)


@app.route("/login", methods=["get", "post"])
def login_my_user():
    if current_user.is_authenticated:
        return redirect('/')

    err_msg = None

    if request.method.__eq__("POST"):
        username = request.form.get("username")
        password = request.form.get("password")

        user = dao.auth_user(username, password)

        if user:
            login_user(user)
            return redirect('/')
        else:
            err_msg = "Tài khoản hoặc mật khẩu không đúng!"

    return render_template("login.html", err_msg=err_msg)


@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
