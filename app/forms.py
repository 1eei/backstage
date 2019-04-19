# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from flask_wtf import FlaskForm
from app.models import Admin
from wtforms import StringField, SubmitField, SelectField, PasswordField, TextAreaField, BooleanField, ValidationError
from wtforms.widgets.core import PasswordInput
from wtforms.validators import DataRequired


class MyPasswordField(PasswordField):
    widget = PasswordInput(hide_value=False)


class LoginForm(FlaskForm):
    account = StringField('account', validators=[DataRequired(message="请输入用户名")],
                          render_kw={'placeholder': '请输入用户名', 'autocomplete': "off"})
    pwd = PasswordField('pwd', validators=[DataRequired(message="请输入密码")],
                        render_kw={'placeholder': '请输入密码', 'autocomplete': "off"})
    remember_me = BooleanField('remember_Me', default=False)
    submit = SubmitField('登录')

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(account=account).count()
        if admin == 0:
            raise ValidationError("账号不存在")


class AdminDataForm(FlaskForm):
    account = StringField('account', validators=[DataRequired(message="必填字段")],
                          render_kw={'placeholder': '', 'class': "layui-input",
                                     'autocomplete': "off"})

    pwd = MyPasswordField('pwd', validators=[DataRequired(message="必填字段")],
                          render_kw={'placeholder': '', 'class': "layui-input",
                                     'autocomplete': "off"})

    name = StringField('name',
                       render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                  'autocomplete': "off"})

    role_id = SelectField(
        "角色id",
        choices='',
        coerce=int,
        description="角色id",
        render_kw={
            'lay-filter': "aihao",
        },
    )

    locked = SelectField(
        "启用/禁用",
        coerce=int,
        choices='',
        description="启用/禁用",
        render_kw={
            'lay-filter': "aihao",
        },
    )

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class AdminEditForm(FlaskForm):
    account = StringField('account', validators=[DataRequired(message="必填字段")],
                          render_kw={'placeholder': '', 'class': "layui-input",
                                     'autocomplete': "off"})

    pwd = MyPasswordField('pwd', validators=[DataRequired(message="必填字段")],
                          render_kw={'placeholder': '', 'class': "layui-input",
                                     'autocomplete': "off"})

    name = StringField('name',
                       render_kw={'placeholder': '', 'class': "layui-input",
                                  'autocomplete': "off"})

    role_id = SelectField(
        "角色id",
        choices='',
        coerce=int,
        description="角色id",
        render_kw={
            'lay-filter': "aihao",
        },
    )

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class UserDataForm(FlaskForm):
    account = StringField('account', validators=[DataRequired(message="必填字段")],
                          render_kw={'placeholder': '', 'class': "layui-input",
                                     'autocomplete': "off"})

    pwd = MyPasswordField('id', validators=[DataRequired(message="必填字段")],
                          render_kw={'placeholder': '', 'class': "layui-input",
                                     'autocomplete': "off"})

    phone = StringField('phone', validators=[DataRequired(message="必填字段")],
                        render_kw={'placeholder': '', 'class': "layui-input",
                                   'autocomplete': "off"})

    name = StringField('name',
                       render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                  'autocomplete': "off"})

    face = StringField('face',
                       render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                  'autocomplete': "off"})

    wechat = StringField('wechat',
                         render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                    'autocomplete': "off"})

    locked = SelectField(
        "启用/禁用",
        choices='',
        coerce=int,
        description="启用/禁用",
        render_kw={
            'lay-filter': "aihao",
        },
    )

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class ProjectDataForm(FlaskForm):
    name = StringField('项目名称', validators=[DataRequired(message="必填字段")],
                       render_kw={'placeholder': '', 'class': "layui-input",
                                  'autocomplete': "off"})
    user_id = SelectField(
        "项目用户",
        coerce=int,
        choices='',
        description="项目用户",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    admin_id = SelectField(
        "系统用户",
        coerce=int,
        choices='',
        description="系统用户",
        render_kw={
            'lay-filter': "aihao"
        },
    )
    number = StringField('项目编号',
                         render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                    'autocomplete': "off"})

    type = SelectField('类型',
                       render_kw={
                           'lay-filter': "aihao"
                       },
                       choices=[(1, '智能城市'), (2, '智能生活'), (3, '智能工业'), (4, '商业共享')],
                       description="类型",
                       coerce=int
                       )

    commpy = StringField('项目所属公司',
                         render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                    'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class ProductDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="必填字段")],
                       render_kw={'placeholder': '', 'class': "layui-input",
                                  'autocomplete': "off"})

    is_gateway = SelectField(
        "是否接入网关",
        choices='',
        coerce=int,
        render_kw={
        },
    )

    networking = SelectField(
        "网络连接方式",
        choices='',
        coerce=int,
        render_kw={
        },
    )

    data_format = SelectField(
        "数据类型",
        choices='',
        coerce=int,
        render_kw={
        },
    )

    is_authen = SelectField(
        "是否id认证",
        choices='',
        coerce=int,
        render_kw={
        },
    )

    authen_id = StringField('authen_id',
                            render_kw={'placeholder': '允许为空',
                                       'class': "layui-input",
                                       'autocomplete': "off"})

    product_id = StringField('产品编号',
                             render_kw={'placeholder': '允许为空',
                                        'class': "layui-input",
                                        'autocomplete': "off"})

    node = SelectField(
        "产品节点",
        choices='',
        coerce=int,
        render_kw={
        },
    )

    description = TextAreaField('产品描述',
                                render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                           'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class DeviceDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="必填字段")],
                       render_kw={'placeholder': '', 'class': "layui-input",
                                  'autocomplete': "off"})

    project_id = SelectField(
        "设备所属项目id",
        coerce=int,
        choices='',
        description="设备所属项目id",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    product_id = SelectField(
        "设备所属产品id",
        coerce=int,
        choices='',
        description="设备所属产品id",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    devicegroup_id = SelectField(
        "设备所属设备组id",
        coerce=int,
        choices='',
        description="设备所属设备组id",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    number = StringField('number',
                         render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                    'autocomplete': "off"})

    node = SelectField(
        "节点类型",
        coerce=int,
        choices='',
        description="设备所属产品id",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    online = SelectField('在线状态',
                         render_kw={
                             'lay-filter': "aihao"
                         },
                         choices=[(0, '离线'), (1, '在线'), (2, '异常')],
                         description="类型",
                         coerce=int
                         )

    active = SelectField('在线状态',
                         render_kw={
                             'lay-filter': "aihao"
                         },
                         choices=[(0, '禁用'), (1, '启用')],
                         description="类型",
                         coerce=int
                         )

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class UserBindingDeviceForm(FlaskForm):
    name = SelectField(
        "绑定设备",
        coerce=int,
        choices='',
        description="绑定设备",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class DeviceGroupDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="必填字段")],
                       render_kw={'placeholder': '', 'class': "layui-input",
                                  'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class AuthDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="必填字段")],
                       render_kw={'placeholder': '', 'class': "layui-input",
                                  'autocomplete': "off"})

    url = StringField('url',
                      render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                 'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class RoleDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="必填字段")],
                       render_kw={'placeholder': '', 'class': "layui-input",
                                  'autocomplete': "off"})

    auth = StringField('auth',
                       render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                  'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class OrderDataForm(FlaskForm):
    money = StringField('money', validators=[DataRequired(message="必填字段")],
                        render_kw={'placeholder': '', 'class': "layui-input",
                                   'autocomplete': "off"})

    number = StringField('number',
                         render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                    'autocomplete': "off"})

    user_id = SelectField(
        "所属用户id",
        coerce=int,
        choices='',
        description="所属用户id",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    pay_method = SelectField(
        "支付方式",
        coerce=int,
        choices='',
        description="支付方式",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    stats = SelectField(
        "订单状态",
        coerce=int,
        choices='',
        description="订单状态",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class TestLogDataForm(FlaskForm):
    content = StringField('content',
                          render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                     'autocomplete': "off"})

    cause = StringField('cause',
                        render_kw={'placeholder': '允许为空', 'class': "layui-input",
                                   'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})
