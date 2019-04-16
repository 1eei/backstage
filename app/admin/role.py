# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from . import admin
from app import db
from flask import render_template, flash
from app.models import Role
from app.templates.database.forms import RoleDataForm
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
        flash('Auth数据添加成功!', 'ok')

    return render_template('database/role_add.html', form=form)
