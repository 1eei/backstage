# ！/usr/bin/env python
# -*-coding:utf-8 -*-
from . import admin
from app import db
from flask import render_template, flash
from app.models import Admin, Project
from app.templates.database.forms import AdminDataForm,AuthDataForm
from werkzeug.security import generate_password_hash
from flask_login import login_required


@admin.route('/admin_user/<int:page>', methods=['GET', 'POST'])
# @login_required
def admin_user(page):
    if page is None:
        page = 1
    page_data = Project.query.join(Admin).filter(
        Project.admin_id == Admin.id
    ).order_by(
        Admin.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('admin_user.html', page_data=page_data)


@admin.route('/admin_power_form')
# @login_required
def admin_power_form():
    form = AuthDataForm()
    return render_template('edit/admin_power_form.html',form=form)


@admin.route('/admin_add', methods=['GET', 'POST'])
# @login_required
def admin_add():
    form = AdminDataForm()
    if form.validate_on_submit():
        account = form.account.data
        pwd = form.pwd.data
        role_id = form.role_id.data
        _locked = int(form.locked.data)
        admin = Admin(account=account,
                      pwd=generate_password_hash(pwd),
                      role_id=role_id,
                      _locked=_locked
                      )

        db.session.add(admin)
        db.session.commit()
        flash('Admin数据添加成功!', 'ok')

    return render_template('database/admin_add.html', form=form)
