from flask import abort, render_template
from flask_simplelogin import login_required

from bmw_backend.models import CarSale


def index():
    products = CarSale.query.all()
    return render_template("index.html", products=products)


def product(product_id):
    product = CarSale.query.filter_by(id=product_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("product.html", product=product)


@login_required
def secret():
    return "This can be seen only if user is logged in"


@login_required(username="admin")
def only_admin():
    return "only admin user can see this text"
