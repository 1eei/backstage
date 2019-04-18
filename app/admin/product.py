from . import admin
from app import db
from flask import render_template, flash, redirect, url_for, request
from app.models import Product
from app.templates.database.forms import ProductDataForm, ProductEditForm
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
    id = request.args.get('id')
    print(id)
    product = Product.query.get_or_404(id)
    form = ProductEditForm(product_id=product.product_id)
    if request.method == 'GET' or request.method == 'POST':
        form.product_id.choices = [(v.id, v.name) for v in Product.query.all()]
    if form.validate_on_submit():
        data = form.data
        product.name = data['name']
        product.product_id = data['product_id']
        product.node = data['node']
        db.session.add(product)
        db.session.commit()
        flash("产品表数据修改成功", "ok")
    return render_template('edit/product_edit.html', form=form, product=product)


@admin.route('/product_add', methods=['GET', 'POST'])
# @login_required
def product_add():
    form = ProductDataForm()
    if form.validate_on_submit():
        name = form.name.data
        product_id = form.product_id.data
        node = form.node.data
        is_gateway = form.is_gateway.data
        networking = form.networking.data
        data_format = form.data_format.data
        is_authen = form.is_authen.data
        authen_id = form.authen_id.data
        description = form.description.data

        product = Product(name=name,
                          product_id=product_id,
                          node=node,
                          is_gateway=is_gateway,
                          networking=networking,
                          data_format=data_format,
                          is_authen=is_authen,
                          authen_id=authen_id,
                          description=description)

        db.session.add(product)
        db.session.commit()
        flash('产品表数据添加成功!', 'ok')
        return redirect(url_for('admin.product_add'))
    return render_template('database/product_add.html', form=form)
