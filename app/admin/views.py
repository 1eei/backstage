# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from . import admin
from app import db
from flask import render_template, redirect, url_for, flash, request, session
from app.admin.forms import AdminForm
from app.models import Admin, User, testlog, Order, Role, Project, Product, Device, Device_group, testlog
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash


@admin.route('/')
@login_required
def index():
    return render_template('index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = AdminForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data['name']).first()
        if not admin.check_pwd(data['password']):
            flash('密码错误!', 'err')
            return redirect(url_for('admin.login'))
        '''
        remember_me:
        记住：是否在会话过期后记住用户。
        默认为“假”。
        login_user()里的有个会话过期的方法session['remember_seconds']
        session['remember_seconds'] = (duration.microseconds +
                                               (duration.seconds +
                                                duration.days * 24 * 3600) *
                                               10**6) / 10.0**6                  
        session permanent为True时，
        用户退出浏览器不会删除session，
        其会保留permanent_session_lifetime s(默认是31天)，
        但是当其为False且SESSION_PROTECTION 设为strong时，
        用户的session就会被删除。
        
        当用户点击记住密码，在下次打开浏览器时无需登录，
        否则，就要登录
        '''
        login_user(admin, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('Login.html', form=form)


@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.login'))


@admin.route('/admin_user/<int:page>', methods=['GET', 'POST'])
@login_required
def admin_user(page=None):
    if page is None:
        page = 1
    page_data = Admin.query.order_by(
        Admin.id.asc()
    ).paginate(page=page, per_page=1)
    return render_template('admin_user.html', page_data=page_data)


@admin.route('/log_server/<int:page>', methods=["GET"])
@login_required
def log_server(page):
    if page is None:
        page = 1
    page_data = testlog.query.order_by(
        testlog.id.asc()
    ).paginate(page=page, per_page=1)
    return render_template('log_server.html', page_data=page_data)


@admin.route('/monitor', methods=["GET"])
@login_required
def monitor():
    return render_template('monitor.html')


@admin.route('/online_test', methods=["GET"])
@login_required
def online_test():
    return render_template('online_test.html')


@admin.route('/orderlist/<int:page>', methods=["GET"])
@login_required
def orderlist(page):
    if page is None:
        page = 1
    page_data = Order.query.order_by(
        Order.id.asc()
    ).paginate(page=page, per_page=1)
    return render_template('orderlist.html', page_data=page_data)


@admin.route('/project_user/<int:page>', methods=["GET"])
@login_required
def project_user(page):
    if page is None:
        page = 1
    page_data = User.query.order_by(
        User.id.asc()
    ).paginate(page=page, per_page=1)
    return render_template('project_user.html', page_data=page_data)


@admin.route('/admin_form')
@login_required
def admin_form():
    return render_template('form/admin_form.html')


@admin.route('/power_form')
@login_required
def power_form():
    return render_template('form/power_form.html')


# 绑定设备
@admin.route('/binding_device')
@login_required
def binding_device():
    return render_template('form/binding_device.html')


@admin.route('/data_add/')
def add():
    admin = Admin(name='admin', pwd=generate_password_hash('admin'), _locked=True)

    role = Role(name='admin', auth='admin')

    user = User(acount='user', pwd=generate_password_hash('user'), phone='11111111111', _locked=True)

    project = Project(name='project1')

    product = Product(name='product1')

    device = Device(name='device1', _online=1, _active=1)

    group = Device_group(name='group1')

    log = testlog(content='log2')

    order = Order(admin_id=1, money='777', pay_method='支付宝')

    db.session.add(admin)
    db.session.add(role)
    db.session.add(user)
    db.session.add(project)
    db.session.add(product)
    db.session.add(device)
    db.session.add(group)
    db.session.add(log)
    db.session.add(order)

    db.session.commit()
    return '添加数据成功'
