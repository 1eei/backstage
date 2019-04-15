# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from . import admin
from flask import render_template, redirect, url_for, flash, request, session
from app.admin.forms import LoginForm
from app.models import Admin, User, OrderTable, TestLog, Project
from flask_login import login_required, login_user, logout_user


@admin.route('/')
@login_required
def index():
    data = Project.query.all()
    return render_template('index.html', data=data)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(account=data['account']).first()
        if not admin.check_pwd(data['pwd']):
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
def admin_user(page):
    if page is None:
        page = 1
    page_data = Admin.query.order_by(
        Admin.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('admin_user.html', page_data=page_data)


@admin.route('/project_user/<int:page>', methods=['GET', 'POST'])
@login_required
def project_user(page):
    if page is None:
        page = 1
    page_data = User.query.order_by(
        User.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('project_user.html', page_data=page_data)


@admin.route('/log_server/<int:page>', methods=["GET"])
@login_required
def log_server(page):
    if page is None:
        page = 1
    page_data = TestLog.query.order_by(
        TestLog.id.asc()
    ).paginate(page=page, per_page=5)
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
    page_data = OrderTable.query.order_by(
        OrderTable.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('orderlist.html', page_data=page_data)


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
