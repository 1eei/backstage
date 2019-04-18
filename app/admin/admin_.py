# ！/usr/bin/env python
# -*-coding:utf-8 -*-
from . import admin
from app import db
from flask import render_template, flash, request, redirect, url_for
from app.models import Admin, Project
from app.templates.database.forms import AdminDataForm, AuthDataForm, AdminEditForm
from werkzeug.security import generate_password_hash
from flask_login import login_required


@admin.route('/admin_user/<int:page>', methods=['GET', 'POST'])
# @login_required
def admin_user(page):
    if page is None:
        page = 1
    page_data = Admin.query.order_by(
        Admin.id.asc()
    ).paginate(page=page, per_page=5)

    _locked = request.args.get('_locked')
    id = request.args.get('id')
    admin = Admin.query.filter_by(id=id).first()

    if _locked == '1':  # 1 = 启用
        _locked = 0
        admin._locked = _locked
        db.session.add(admin)
        db.session.commit()
    elif _locked == '0':  # 0= 禁用
        _locked = 1
        admin._locked = _locked
        db.session.add(admin)
        db.session.commit()

    return render_template('admin_user.html', page_data=page_data)


@admin.route('/admin_power_form')
# @login_required
def admin_power_form():
    form = AuthDataForm()
    return render_template('edit/admin_power_form.html', form=form)


@admin.route('/admin_edit', methods=['GET', 'POST'])
# @login_required
def admin_edit():
    id = request.args.get('id')
    admin = Admin.query.get_or_404(id)
    form = AdminEditForm()
    if form.validate_on_submit():
        data = form.data
        admin.account = data['account']
        admin.pwd = data['pwd']
        admin.name = data['name']
        admin.role_id = data['role_id']
        db.session.add(admin)
        db.session.commit()
        flash("管理员表数据修改成功", "ok")

    return render_template('edit/admin_edit.html', form=form, admin=admin)


@admin.route('/admin_add', methods=['GET', 'POST'])
# @login_required
def admin_add():
    form = AdminDataForm()
    if form.validate_on_submit():
        account = form.account.data
        pwd = form.pwd.data
        name = form.name.data
        role_id = form.role_id.data
        _locked = int(form.locked.data)
        admin = Admin(account=account,
                      pwd=generate_password_hash(pwd),
                      name=name,
                      role_id=role_id,
                      _locked=_locked
                      )

        db.session.add(admin)
        db.session.commit()
        flash('管理员表数据添加成功!', 'ok')
        return redirect(url_for('admin.admin_add'))
    return render_template('database/admin_add.html', form=form)
