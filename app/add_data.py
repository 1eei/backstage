# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from werkzeug.security import generate_password_hash

from app.models import User, Admin, Role
from app.models import db
import uuid


def create_user():
    user = User()
    user.name = 'leedad'
    user.pwd = generate_password_hash('qq111111.')
    user.phone = '17520350785'
    user.face = ''
    user.uuid = str(uuid.uuid4().hex)
    user._locked = 1
    db.session.add(user)
    db.session.commit()


def create_admin():
    admin = Admin()
    admin.name = 'admin'
    admin.password = generate_password_hash('admin')
    db.session.add(admin)
    db.session.commit()


def create_role():
    role = Role()
    role.name = 'admin'
    role.auths = ''
    db.session.add(role)
    db.session.commit()


create_user()
create_role()
create_admin()

print('数据添加完毕')
