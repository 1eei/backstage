# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from . import admin
from flask import Flask, render_template, redirect, url_for, flash, request

from app.admin.forms import AdminForm
from app.models import Admin


@admin.route('/')
def index():
    return render_template('index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = AdminForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data['name']).first()
        if not admin.check_password(data['password']):
            flash('密码错误!', 'err')
            return redirect(url_for('admin.login'))
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('Login.html', form=form)


@admin.route('/admin_user', methods=["GET"])
def admin_user():
    return render_template('admin_user.html')


@admin.route('/log_server', methods=["GET"])
def log_server():
    return render_template('log_server.html')


@admin.route('/monitor', methods=["GET"])
def monitor():
    return render_template('monitor.html')


@admin.route('/online_test', methods=["GET"])
def online_test():
    return render_template('online_test.html')


@admin.route('/orderlist', methods=["GET"])
def orderlist():
    return render_template('orderlist.html')


@admin.route('/project_user', methods=["GET"])
def project_user():
    return render_template('project_user.html')


@admin.route('/admin_form')
def admin_form():
    return render_template('form/admin_form.html')


@admin.route('/power_form')
def power_form():
    return render_template('form/power_form.html')


# 绑定设备
@admin.route('/binding_device')
def binding_device():
    return render_template('form/binding_device.html')
