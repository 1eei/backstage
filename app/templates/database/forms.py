# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired
from app.models import Admin,User

class AdminDataForm(FlaskForm):
    account = StringField('account', validators=[DataRequired(message="请输入name")],
                          render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                     'autocomplete': "off"})

    pwd = StringField('pwd', validators=[DataRequired(message="请输入pwd")],
                      render_kw={'placeholder': '请输入pwd', 'class': "layui-input",
                                 'autocomplete': "off"})

    name = StringField('name',
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    role_id = StringField('role_id', validators=[DataRequired(message="请输入role_id")],
                          render_kw={'placeholder': '请输入role_id', 'class': "layui-input",
                                     'autocomplete': "off"})

    locked = StringField('_locked', validators=[DataRequired(message="请输入_locked")],
                         render_kw={'placeholder': '请输入_locked (0=禁用,1=启用)', 'class': "layui-input",
                                    'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class UserDataForm(FlaskForm):
    account = StringField('account', validators=[DataRequired(message="请输入account")],
                          render_kw={'placeholder': '请输入account', 'class': "layui-input",
                                     'autocomplete': "off"})

    pwd = StringField('id', validators=[DataRequired(message="请输入pwd")],
                      render_kw={'placeholder': '请输入pwd', 'class': "layui-input",
                                 'autocomplete': "off"})

    phone = StringField('phone', validators=[DataRequired(message="请输入phone")],
                        render_kw={'placeholder': '请输入phone', 'class': "layui-input",
                                   'autocomplete': "off"})

    name = StringField('name',
                       render_kw={'placeholder': '请输入name (允许为空)', 'class': "layui-input",
                                  'autocomplete': "off"})

    face = StringField('face',
                       render_kw={'placeholder': '请输入face (允许为空)', 'class': "layui-input",
                                  'autocomplete': "off"})

    wechat = StringField('wechat',
                         render_kw={'placeholder': '请输入wechat (允许为空)', 'class': "layui-input",
                                    'autocomplete': "off"})

    locked = StringField('_locked', validators=[DataRequired(message="请输入_locked")],
                         render_kw={'placeholder': '请输入_locked (0=禁用,1=启用)', 'class': "layui-input",
                                    'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class ProjectDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    user_id = StringField('user_id', validators=[DataRequired(message="请输入user_id")],
                          render_kw={'placeholder': '请输入user_id', 'class': "layui-input",
                                     'autocomplete': "off"})

    admin_id = StringField('admin_id', validators=[DataRequired(message="请输入admin_id")],
                           render_kw={'placeholder': '请输入admin_id', 'class': "layui-input",
                                      'autocomplete': "off"})

    number = StringField('number',
                         render_kw={'placeholder': '请输入number (允许为空)', 'class': "layui-input",
                                    'autocomplete': "off"})

    type = StringField('type',
                       render_kw={'placeholder': '请输入type (允许为空)', 'class': "layui-input",
                                  'autocomplete': "off"})

    commpy = StringField('commpy',
                         render_kw={'placeholder': '请输入commpy (允许为空)', 'class': "layui-input",
                                    'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})

class ProjectEditForm(FlaskForm):
    name = StringField('项目名称', validators=[DataRequired(message="请输入项目名称")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})
    user_id = SelectField(
        "项目用户",
        coerce=int,
        choices=[(v.id, v.name) for v in User.query.all()],
        description="项目用户",
        render_kw={
            'lay-filter': "aihao"
        },
    )

    admin_id = SelectField(
        "系统用户",
        coerce=int,
        choices=[(v.id, v.name) for v in Admin.query.all()],
        description="系统用户",
        render_kw={
            'lay-filter': "aihao"
        },
    )
    number = StringField('项目编号',
                         render_kw={'placeholder': '请输入项目编号 (允许为空)', 'class': "layui-input",
                                    'autocomplete': "off"})

    type = SelectField('类型',
                       render_kw={
                            'lay-filter':"aihao"
                       },
                       choices=[(1, '智能城市'), (2, '智能生活'), (3, '智能工业'),(4,'商业共享')],
                       description="类型",
                       coerce=int
                       )

    commpy = StringField('项目所属公司',
                         render_kw={'placeholder': '请输入commpy (允许为空)', 'class': "layui-input",
                                    'autocomplete': "off"})

    submit = SubmitField('编辑', render_kw={'class': "layui-btn",'id':'close'})



class ProductDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    is_gateway = StringField('is_gateway', validators=[DataRequired(message="请输入is_gateway")],
                             render_kw={'placeholder': '请输入is_gateway', 'class': "layui-input",
                                        'autocomplete': "off"})

    networking = StringField('networking', validators=[DataRequired(message="请输入networking")],
                             render_kw={'placeholder': '请输入networking', 'class': "layui-input",
                                        'autocomplete': "off"})

    data_format = StringField('data_format', validators=[DataRequired(message="请输入data_format")],
                              render_kw={'placeholder': '请输入data_format', 'class': "layui-input",
                                         'autocomplete': "off"})

    is_authen = StringField('is_authen', validators=[DataRequired(message="请输入is_authen")],
                            render_kw={'placeholder': '请输入is_authen', 'class': "layui-input",
                                       'autocomplete': "off"})

    authen_id = StringField('authen_id',
                            render_kw={'placeholder': '请输入authen_id (允许为空)',
                                       'class': "layui-input",
                                       'autocomplete': "off"})

    product_id = StringField('product_id',
                             render_kw={'placeholder': '请输入product_id (允许为空)',
                                        'class': "layui-input",
                                        'autocomplete': "off"})

    node = StringField('node',
                       render_kw={'placeholder': '请输入node (允许为空)', 'class': "layui-input",
                                  'autocomplete': "off"})

    description = StringField('description',
                              render_kw={'placeholder': '请输入description (允许为空)', 'class': "layui-input",
                                         'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class DeviceDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    project_id = StringField('project_id', validators=[DataRequired(message="请输入project_id")],
                             render_kw={'placeholder': '请输入project_id', 'class': "layui-input",
                                        'autocomplete': "off"})

    product_id = StringField('product_id', validators=[DataRequired(message="请输入product_id")],
                             render_kw={'placeholder': '请输入product_id', 'class': "layui-input",
                                        'autocomplete': "off"})

    devicegroup_id = StringField('devicegroup_id', validators=[DataRequired(message="devicegroup_id")],
                                 render_kw={'placeholder': '请输入devicegroup_id', 'class': "layui-input",
                                            'autocomplete': "off"})

    number = StringField('number',
                         render_kw={'placeholder': '请输入number (允许为空)', 'class': "layui-input",
                                    'autocomplete': "off"})

    node = StringField('node',
                       render_kw={'placeholder': '请输入node (允许为空)', 'class': "layui-input",
                                  'autocomplete': "off"})

    online = StringField('_online', validators=[DataRequired(message="请输入_online")],
                         render_kw={'placeholder': '请输入_online (1 or 0)', 'class': "layui-input",
                                    'autocomplete': "off"})

    active = StringField('_active', validators=[DataRequired(message="请输入_active")],
                         render_kw={'placeholder': '请输入_active (1 or 0)', 'class': "layui-input",
                                    'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class DeviceGroupDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class AuthDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    url = StringField('url',
                      render_kw={'placeholder': '请输入url (允许为空)', 'class': "layui-input",
                                 'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class RoleDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    auth = StringField('auth',
                       render_kw={'placeholder': '请输入auth (允许为空)', 'class': "layui-input",
                                  'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class OrderDataForm(FlaskForm):
    user_id = StringField('user_id', validators=[DataRequired(message="请输入user_id")],
                           render_kw={'placeholder': '请输入user_id', 'class': "layui-input",
                                      'autocomplete': "off"})

    number = StringField('number',
                         render_kw={'placeholder': '请输入number (允许为空)', 'class': "layui-input",
                                    'autocomplete': "off"})

    money = StringField('money',
                        render_kw={'placeholder': '请输入money (允许为空)', 'class': "layui-input",
                                   'autocomplete': "off"})

    pay_method = StringField('pay_method',
                             render_kw={'placeholder': '请输入pay_method (允许为空)', 'class': "layui-input",
                                        'autocomplete': "off"})

    stats = StringField('stats',
                        render_kw={'placeholder': '请输入stats (允许为空)', 'class': "layui-input",
                                   'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class TestLogDataForm(FlaskForm):
    content = StringField('content',
                          render_kw={'placeholder': '请输入content (允许为空)', 'class': "layui-input",
                                     'autocomplete': "off"})

    cause = StringField('cause',
                        render_kw={'placeholder': '请输入cause (允许为空)', 'class': "layui-input",
                                   'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})
