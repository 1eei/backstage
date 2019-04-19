# ！/usr/bin/env python
# -*-coding:utf-8 -*-
from . import admin
from app import db
from flask import render_template, flash, redirect, url_for, request
from app.models import User, Device
from app.templates.database.forms import UserDataForm, UserBindingDeviceForm
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

    _locked = request.args.get('_locked')
    id = request.args.get('id')
    user = User.query.filter_by(id=id).first()

    if _locked == '1':  # 1 = 启用
        _locked = 0
        user._locked = _locked
        db.session.add(user)
        db.session.commit()
    elif _locked == '0':  # 0= 禁用
        _locked = 1
        user._locked = _locked
        db.session.add(user)
        db.session.commit()

    return render_template('project_user.html', page_data=page_data)


# 绑定设备
@admin.route('/user_binding_device', methods=['GET', 'POST'])
# @login_required
def user_binding_device():
    id = request.args.get('id')
    device = Device.query.get_or_404(id)
    form = UserBindingDeviceForm(name=device.name)
    if request.method == 'GET' or request.method == 'POST':
        form.name.choices = [(v.id, v.name) for v in Device.query.all()]
    if form.validate_on_submit():
        pass
    return render_template('edit/user_binding_device.html', form=form, device=device)


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
        flash('用户表数据添加成功!', 'ok')
        return redirect(url_for('admin.user_add'))
    return render_template('database/user_add.html', form=form)
