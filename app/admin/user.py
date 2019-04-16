# ！/usr/bin/env python
# -*-coding:utf-8 -*-
from . import admin
from app import db
from flask import render_template, flash
from app.models import User
from app.templates.database.forms import UserDataForm, DeviceDataForm
from werkzeug.security import generate_password_hash
from flask_login import login_required


@admin.route('/project_user/<int:page>', methods=['GET', 'POST'])
# @login_required
def project_user(page):
    if page is None:
        page = 1
    page_data = User.query.order_by(
        User.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('project_user.html', page_data=page_data)


# 绑定设备
@admin.route('/user_binding_device')
# @login_required
def user_binding_device():
    form = DeviceDataForm()
    return render_template('edit/user_binding_device.html', form=form)


@admin.route('/user_add', methods=['GET', 'POST'])
# @login_required
def user_add():
    form = UserDataForm()
    if form.validate_on_submit():
        account = form.account.data
        pwd = form.pwd.data
        phone = form.phone.data
        name = form.name.data
        face = form.face.data
        wechat = form.wechat.data
        _locked = int(form.locked.data)

        user = User(account=account,
                    pwd=generate_password_hash(pwd),
                    phone=phone,
                    name=name,
                    face=face,
                    wechat=wechat,
                    _locked=_locked)

        db.session.add(user)
        db.session.commit()
        flash('User数据添加成功!', 'ok')

    return render_template('database/user_add.html', form=form)
