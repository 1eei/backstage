# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from . import admin
from app import db
from flask import render_template, flash
from app.models import Admin, User, Project, Product, Device, Device_group, Auth, Role, OrderTable, Testlog
from app.templates.database.forms import AdminDataForm, UserDataForm, ProjectDataForm, ProductDataForm, DeviceDataForm, \
    DeviceGroupDataForm, AuthDataForm, RoleDataForm, OrderDataForm, TestLogDataForm
from werkzeug.security import generate_password_hash
from datetime import datetime


@admin.route('/admin_add', methods=['GET', 'POST'])
def admin_add():
    form = AdminDataForm()
    if form.validate_on_submit():
        account = form.account.data
        pwd = form.pwd.data
        _locked = int(form.locked.data)

        admin = Admin(account=account,
                      pwd=generate_password_hash(pwd),
                      _locked=_locked
                      )

        db.session.add(admin)
        db.session.commit()
        flash('Admin数据添加成功!', 'ok')

    return render_template('database/admin_add.html', form=form)


@admin.route('/user_add', methods=['GET', 'POST'])
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


@admin.route('/project_add', methods=['GET', 'POST'])
def project_add():
    form = ProjectDataForm()
    if form.validate_on_submit():
        name = form.name.data
        number = form.number.data
        type = form.type.data
        commpy = form.commpy.data

        project = Project(name=name,
                          number=number,
                          type=type,
                          commpy=commpy)

        db.session.add(project)
        db.session.commit()
        flash('Project数据添加成功!', 'ok')

    return render_template('database/project_add.html', form=form)


@admin.route('/product_add', methods=['GET', 'POST'])
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


@admin.route('/device_add', methods=['GET', 'POST'])
def device_add():
    form = DeviceDataForm()
    if form.validate_on_submit():
        name = form.name.data
        project_id = int(form.project_id.data)
        product_id = int(form.product_id.data)
        Device_group_id = int(form.Device_group_id.data)
        number = form.number.data
        node = form.node.data
        _online = int(form.online.data)
        _active = int(form.active.data)

        device = Device(name=name,
                        project_id=project_id,
                        product_id=product_id,
                        Device_group_id=Device_group_id,
                        number=number,
                        node=node,
                        _online=_online,
                        _active=_active)

        db.session.add(device)
        db.session.commit()
        flash('Device数据添加成功!', 'ok')

    return render_template('database/device_add.html', form=form)


@admin.route('/device_group_add', methods=['GET', 'POST'])
def device_group_add():
    form = DeviceGroupDataForm()
    if form.validate_on_submit():
        name = form.name.data

        device_group = Device_group(name=name)

        db.session.add(device_group)
        db.session.commit()
        flash('DeviceGroup数据添加成功!', 'ok')

    return render_template('database/device_group_add.html', form=form)


@admin.route('/auth_add', methods=['GET', 'POST'])
def auth_add():
    form = AuthDataForm()
    if form.validate_on_submit():
        name = form.name.data
        url = form.url.data

        auth = Auth(name=name,
                    url=url)

        db.session.add(auth)
        db.session.commit()
        flash('Auth数据添加成功!', 'ok')

    return render_template('database/auth_add.html', form=form)


@admin.route('/role_add', methods=['GET', 'POST'])
def role_add():
    form = RoleDataForm()
    if form.validate_on_submit():
        name = form.name.data
        auth = form.auth.data

        role = Role(name=name,
                    auth=auth)

        db.session.add(role)
        db.session.commit()
        flash('Auth数据添加成功!', 'ok')

    return render_template('database/role_add.html', form=form)


@admin.route('/order_add', methods=['GET', 'POST'])
def order_add():
    form = OrderDataForm()
    if form.validate_on_submit():
        admin_id = form.admin_id.data
        number = form.number.data
        money = int(form.money.data)
        pay_method = form.pay_method.data
        stats = form.stats.data

        order = OrderTable(admin_id=admin_id,
                      number=number,
                      money=money,
                      pay_method=pay_method,
                      stats=stats)

        db.session.add(order)
        db.session.commit()
        flash('Order数据添加成功!', 'ok')

    return render_template('database/order_add.html', form=form)


@admin.route('/testlog_add', methods=['GET', 'POST'])
def testlog_add():
    form = TestLogDataForm()
    if form.validate_on_submit():
        content = form.content.data
        cause = form.cause.data
        report_time = datetime.now()

        testlog = Testlog(content=content,
                          cause=cause,
                          report_time=report_time)

        db.session.add(testlog)
        db.session.commit()
        flash('Testlog数据添加成功!', 'ok')

    return render_template('database/testlog_add.html', form=form)
