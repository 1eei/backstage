# ！/usr/bin/env python
# -*-coding:utf-8 -*-
from . import admin
from app import db
from flask import render_template, flash, redirect, url_for
from app.models import OrderTable
from app.templates.database.forms import OrderDataForm
from flask_login import login_required


@admin.route('/orderlist/<int:page>', methods=["GET"])
# @login_required
def orderlist(page):
    if page is None:
        page = 1
    page_data = OrderTable.query.order_by(
        OrderTable.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('orderlist.html', page_data=page_data)


@admin.route('/order_add', methods=['GET', 'POST'])
# @login_required
def order_add():
    form = OrderDataForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        number = form.number.data
        money = int(form.money.data)
        pay_method = form.pay_method.data
        stats = form.stats.data

        order = OrderTable(user_id=user_id,
                           number=number,
                           money=money,
                           pay_method=pay_method,
                           stats=stats)

        db.session.add(order)
        db.session.commit()
        flash('Order数据添加成功!', 'ok')
        return redirect(url_for('admin.order_add'))
    return render_template('database/order_add.html', form=form)
