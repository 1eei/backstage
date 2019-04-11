# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from datetime import datetime
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/lot_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 用户名
    pwd = db.Column(db.String(128), nullable=False)  # 密码
    phone = db.Column(db.String(11), unique=True, nullable=False)  # 手机
    face = db.Column(db.String(255))  # 头像
    uuid = db.Column(db.String(32), unique=True, nullable=False)  # 唯一标识符
    regist_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    login_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 最后登陆时间
    _locked = db.Column(db.Boolean, nullable=False)  # 禁用/启用

    def __repr__(self):
        return 'name:%r' % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 管理员表
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    adminlog_id = db.relationship('Adminlog', backref='admin')

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


# 管理员日志表
class Adminlog(db.Model):
    __tablename__ = 'adminlog'
    id = db.Column(db.Integer, primary_key=True)
    Admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip_addr = db.Column(db.String(20))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)


# 角色表
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    role_id = db.relationship("Admin", backref='role')


# 权限表
class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(64))  # 权限名称
    url = db.Column(db.String(64))  # 权限地址
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return 'name:%r' % self.name


# 产品表
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)  # 产品编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 产品名
    node = db.Column(db.String(25))  # 产品类型
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)


if __name__ == '__main__':
    manager.run()
