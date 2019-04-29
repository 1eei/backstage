# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from . import admin
from flask import render_template, session
from flask_login import login_required


@admin.route('/real_time', methods=['GET', 'POST'])
@login_required
def real_time():
    # 保存管理员名字和角色id
    session_admin = session['admin']
    session_role_id = session['role']
    return render_template('real_time.html',
                           session_admin=session_admin,
                           session_role_id=session_role_id
                           )
