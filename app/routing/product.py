from . import admin
from app import db
from flask import render_template, flash, redirect, url_for, request
from app.models import Product
from app.forms import ProductDataForm


@admin.route('/product_list/<int:page>', methods=["GET"])
# @login_required
def product_list(page):
    if page is None:
        page = 1
    page_data = Product.query.order_by(
        Product.id.asc()
    ).paginate(page=page, per_page=5)

    product_count = Product.query.count()
    return render_template('product_list.html',
                           page_data=page_data,
                           product_count=product_count)


@admin.route('/product_edit', methods=["GET", "POST"])
# @login_required
def product_edit():
    id = request.args.get('id')
    print(id)
    product = Product.query.get_or_404(id)
    form = ProductDataForm(name=product.name, is_gateway=product.is_gateway, networking=product.networking,
                           data_format=product.data_format, is_authen=product.is_authen, authen_id=product.authen_id,
                           product_id=product.product_id, node=product.node, description=product.description)
    if request.method == 'GET' or request.method == 'POST':
        form.is_gateway.choices = [(0, '否'), (1, '是')]
        form.data_format.choices = [(0, '滴咚物理网标准协议'), (1, '定制标准协议')]
        form.networking.choices = [(0, 'WIFI'), (1, '蜂窝(2G/3G/4G)'), (2, '以太网'), (3, 'LoRaWAN'), (4, '其他')]
        form.is_authen.choices = [(0, '否'), (1, '是')]
        form.node.choices = [(1, '设备'), (2, '路由')]

    if form.validate_on_submit():
        data = form.data
        product.name = data['name']
        product.product_id = data['product_id']
        product.node = data['node']
        db.session.add(product)
        db.session.commit()
        flash("产品表数据修改成功", "ok")
    return render_template('edit/product_edit.html', form=form)


@admin.route('/product_add', methods=['GET', 'POST'])
# @login_required
def product_add():
    form = ProductDataForm()
    if request.method == 'GET' or request.method == 'POST':
        form.is_gateway.choices = [(0, '否'), (1, '是')]
        form.data_format.choices = [(0, '滴咚物理网标准协议'), (1, '定制标准协议')]
        form.networking.choices = [(0, 'WIFI'), (1, '蜂窝(2G/3G/4G)'), (2, '以太网'), (3, 'LoRaWAN'), (4, '其他')]
        form.is_authen.choices = [(0, '否'), (1, '是')]
        form.node.choices = [(1, '设备'), (2, '路由')]

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
    return render_template('add/product_add.html', form=form)


@admin.route('/product_delete', methods=['GET', 'POST'])
# @login_required
def product_delete():
    id = request.args.get('id')
    page = request.args.get('page')
    product = Product.query.get_or_404(id)
    product.id = id
    db.session.delete(product)
    db.session.commit()
    flash("产品表数据修改成功", "ok")
    return redirect(url_for('admin.product_list', page=page))