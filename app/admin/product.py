from . import admin
from flask import render_template
from flask_login import login_required
from app.models import Product


@admin.route('/product_list/<int:page>', methods=["GET"])
@login_required
def product_list(page):
    if page is None:
        page = 1
    page_data = Product.query.order_by(
        Product.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('product_list.html', page_data=page_data)


@admin.route('/product_edit', methods=["GET", "POST"])
@login_required
def product_edit():
    return render_template('edit/product_edit.html')


@admin.route('/product_form')
@login_required
def product_form():
    return render_template('form/product_form.html')
