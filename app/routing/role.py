# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from . import admin
from app import db
from flask import render_template, flash, redirect, url_for
from app.models import Role
from app.forms import RoleDataForm
from flask_login import login_required


@admin.route('/role_add', methods=['GET', 'POST'])
# @login_required
def role_add():
    form = RoleDataForm()
    if form.validate_on_submit():
        name = form.name.data
        auth = form.auth.data

        role = Role(name=name,
                    auth=auth)

        db.session.add(role)
        db.session.commit()
        flash('角色表数据添加成功!', 'ok')
        return redirect(url_for('admin.role_add'))
    return render_template('add/role_add.html', form=form)
