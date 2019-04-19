from app import db
from datetime import datetime
from flask_login import UserMixin


# 用户表
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    account = db.Column(db.String(16), unique=True, nullable=False)  # 用户名
    pwd = db.Column(db.String(128), nullable=False)  # 密码
    name = db.Column(db.String(64))  # 客户姓名
    phone = db.Column(db.String(11), unique=True, nullable=False)  # 手机
    face = db.Column(db.String(255))  # 头像
    wechat = db.Column(db.String(64))  # 微信号
    regist_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    login_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 最后登陆时间
    _locked = db.Column(db.SmallInteger, nullable=False, default=True)  # 禁用/启用

    projects = db.relationship('Project', backref='user', uselist=False)
    order_tables = db.relationship('OrderTable', backref='user')

    def __repr__(self):
        return '<User %r>' % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 订单表
class OrderTable(db.Model):
    __tablename__ = 'order_table'
    id = db.Column(db.Integer, primary_key=True)  # 序号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    number = db.Column(db.String(64), unique=True)  # 订单编号
    money = db.Column(db.DECIMAL(), nullable=False)  # 订单金额
    pay_method = db.Column(db.SmallInteger, nullable=False)  # 支付方式 0=微信，1=支付宝，2=现金，3=银行卡
    stats = db.Column(db.SmallInteger, nullable=False)  # 订单状态 0=未支付，1=已支付，2=退款中，3=完成退款
    start_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 开始时间
    end_time = db.Column(db.DateTime, index=True)  # 结束时间

    def __repr__(self):
        return '<OrderTable %r>' % self.number


# 角色表
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(64), nullable=False)  # 角色名称
    auth = db.Column(db.String(64), nullable=True)  # 权限名称
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    admin_id = db.relationship('Admin', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


# 管理员表
class Admin(db.Model, UserMixin):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    account = db.Column(db.String(16), unique=True, nullable=False)  # 管理员账号
    pwd = db.Column(db.String(128), nullable=False)  # 管理员密码
    name = db.Column(db.String(128))  # 管理员姓名
    regist_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    login_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 最后登陆时间
    _locked = db.Column(db.SmallInteger, nullable=False)  # 禁用/启用

    projects = db.relationship('Project', backref='admin', uselist=False)

    def __repr__(self):
        return '<Admin %r>' % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 权限表
class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(64), nullable=False)  # 权限名称
    url = db.Column(db.String(64))  # 权限地址
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return '<Auth %r>' % self.name


# 设备组表
class DeviceGroup(db.Model):
    __tablename__ = 'device_group'
    id = db.Column(db.Integer, primary_key=True)  # 设备组编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 设备组名
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    devices = db.relationship('Device', backref='DeviceGroup')

    def __repr__(self):
        return '<DeviceGroup %r>' % self.name


# 设备表
class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)  # 设备编号
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    devicegroup_id = db.Column(db.Integer, db.ForeignKey('device_group.id'))
    number = db.Column(db.String(64))  # 设备编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 设备名
    node = db.Column(db.String(25))  # 设备类型
    _online = db.Column(db.SmallInteger, nullable=False)  # 设备的是否在线
    _active = db.Column(db.SmallInteger, nullable=False)  # 设备的运行状态
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间
    online_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 最后上线时间

    def __repr__(self):
        return '<Device %r>' % self.name


# 测试日志
class TestLog(db.Model):
    __tablename__ = 'test_log'
    id = db.Column(db.Integer, primary_key=True)  # 序号
    content = db.Column(db.String(255))  # 内容
    cause = db.Column(db.String(255))  # 原因
    report_time = db.Column(db.DateTime, index=True)  # 上报时间

    def __repr__(self):
        return '<TestLog %r>' % self.id


# 产品表
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)  # 序号
    product_id = db.Column(db.String(50))  # 产品编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 产品名
    node = db.Column(db.String(25))  # 产品类型
    is_gateway = db.Column(db.SmallInteger, nullable=False)  # 是否接入网关 0=否，1=是
    networking = db.Column(db.String(64), nullable=False)  # 联网方式
    data_format = db.Column(db.String(64), nullable=False)  # 数据格式
    is_authen = db.Column(db.SmallInteger, nullable=False)  # 是否单向ID认证 0=否，1=是
    authen_id = db.Column(db.String(64))  # 认证ID
    description = db.Column(db.String(255))  # 产品说明
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)

    devices = db.relationship('Device', backref='product')

    def __repr__(self):
        return '<Product %r>' % self.name


# 项目表
class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)  # 序号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    number = db.Column(db.String(50), unique=True)  # 项目编号
    name = db.Column(db.String(16), unique=True, nullable=False)  # 项目名
    type = db.Column(db.String(20))  # 项目类型
    commpy = db.Column(db.String(50))  # 项目所属公司
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    users = db.relationship('User')
    admins = db.relationship('Admin', backref='project')
    devices = db.relationship('Device', backref='project')

    def __repr__(self):
        return '<Project %r>' % self.name

    @property
    def type_desc(self):
        type_mapping = {
            "1": "智能城市",
            "2": "智能生活",
            "3": "智能工业",
            "4": "商业共享"

        }
        return type_mapping[str(self.type)]


if __name__ == '__main__':
    db.create_all()
