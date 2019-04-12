from app import db
from datetime import datetime
from flask_login import UserMixin


# 用户表
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    acount = db.Column(db.String(16), unique=True, nullable=False)  # 用户名
    pwd = db.Column(db.String(128), nullable=False)  # 密码
    name = db.Column(db.String(64))  # 客户姓名
    phone = db.Column(db.String(11), unique=True, nullable=False)  # 手机
    face = db.Column(db.String(255))  # 头像
    wechat = db.Column(db.String(64))  # 微信号
    regist_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    login_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 最后登陆时间
    _locked = db.Column(db.SmallInteger, nullable=False, default=True)  # 禁用/启用

    order_id = db.relationship('Order', backref='user')

    def __repr__(self):
        return 'name:%r' % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 订单表
class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)  # 序号
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    number = db.Column(db.String(64), unique=True)  # 订单编号
    money = db.Column(db.DECIMAL())  # 订单金额
    pay_method = db.Column(db.String(12))  # 支付方式
    stats = db.Column(db.SmallInteger)  # 订单状态
    start_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 开始时间
    end_time = db.Column(db.DateTime, index=True)  # 结束时间

    def __repr__(self):
        return 'number:%r' % self.number


# 角色表
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(64), nullable=False)  # 角色名称
    auth = db.Column(db.String(64), nullable=True)  # 权限名称
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    admin_id = db.relationship('Admin', backref='role')

    def __repr__(self):
        return 'name:%r' % self.name


# 管理员表
class Admin(db.Model, UserMixin):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    name = db.Column(db.String(16), unique=True, nullable=False)  # 管理员账号
    pwd = db.Column(db.String(128), nullable=False)  # 管理员密码
    regist_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    login_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 最后登陆时间
    _locked = db.Column(db.Boolean, nullable=False)  # 禁用/启用

    def __repr__(self):
        return 'name:%r' % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 权限表
class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(64))  # 权限名称
    url = db.Column(db.String(64))  # 权限地址
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return 'name:%r' % self.name


# 设备组表
class Device_group(db.Model):
    __tablename__ = 'Device_group'
    id = db.Column(db.Integer, primary_key=True)  # 设备组编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 设备组名
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    device_id = db.relationship('Device', backref='Device_group')

    def __repr__(self):
        return 'name:%r' % self.name


# 设备表
class Device(db.Model):
    __tablename__ = 'Device'
    id = db.Column(db.Integer, primary_key=True)  # 设备编号
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    Device_group_id = db.Column(db.Integer, db.ForeignKey('Device_group.id'))
    number = db.Column(db.String(64))  # 设备编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 设备名
    node = db.Column(db.String(25))  # 设备类型
    _online = db.Column(db.SmallInteger, nullable=False)  # 设备的是否在线
    _active = db.Column(db.SmallInteger, nullable=False)  # 设备的运行状态
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间
    online_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 最后上线时间

    def __repr__(self):
        return 'name:%r' % self.name


# 测试日志
class testlog(db.Model):
    __tablename__ = 'testlog'
    id = db.Column(db.Integer, primary_key=True)  # 序号
    content = db.Column(db.String(255))  # 内容
    cause = db.Column(db.String(255))  # 原因
    report_time = db.Column(db.DateTime, index=True)  # 上报时间

    def __repr__(self):
        return 'id:%r' % self.id


# 产品表
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)  # 序号
    product_id = db.Column(db.String(50))  # 产品编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 产品名
    node = db.Column(db.String(25))  # 产品类型
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)

    device_id = db.relationship('Device', backref='product')

    def __repr__(self):
        return 'name:%r' % self.name


# 项目表
class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)  # 序号
    number = db.Column(db.String(50), unique=True)  # 项目编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 项目名
    type = db.Column(db.String(20))  # 项目类型
    commpy = db.Column(db.String(50))  # 项目所属公司
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    device_id = db.relationship('Device', backref='project')

    def __repr__(self):
        return 'name:%r' % self.name


if __name__ == "__main__":
    db.create_all()
