from . import admin
from app import db
from flask import render_template, flash
from app.models import Product
from app.templates.database.forms import ProductDataForm
from flask_login import login_required


@admin.route('/product_list/<int:page>', methods=["GET"])
# @login_required
def product_list(page):
    if page is None:
        page = 1
    page_data = Product.query.order_by(
        Product.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('product_list.html', page_data=page_data)


@admin.route('/product_edit', methods=["GET", "POST"])
# @login_required
def product_edit():
    form = ProductDataForm()
    return render_template('edit/product_edit.html',form=form)


@admin.route('/product_add', methods=['GET', 'POST'])
# @login_required
def product_add():
    form = ProductDataForm()
    if form.validate_on_submit():
        name = form.name.data
        product_id = form.product_id.data
        node = form.node.data

        product = Product(name=name,
                          product_id=product_id,
                          node=node)

        db.session.add(product)
        db.session.commit()
        flash('Product数据添加成功!', 'ok')

    return render_template('database/product_add.html', form=form)
