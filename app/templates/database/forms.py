# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AdminDataForm(FlaskForm):
    account = StringField('account', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    pwd = StringField('id', validators=[DataRequired(message="请输入pwd")],
                      render_kw={'placeholder': '请输入pwd', 'class': "layui-input",
                                 'autocomplete': "off"})

    locked = StringField('_locked', validators=[DataRequired(message="请输入_locked")],
                         render_kw={'placeholder': '请输入_locked (1 or 0)', 'class': "layui-input",
                                    'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class UserDataForm(FlaskForm):
    acount = StringField('account', validators=[DataRequired(message="请输入account")],
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
                         render_kw={'placeholder': '请输入_locked (1 or 0)', 'class': "layui-input",
                                    'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class ProjectDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
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


class ProductDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    product_id = StringField('product_id',
                             render_kw={'placeholder': '请输入product_id (允许为空)',
                                        'class': "layui-input",
                                        'autocomplete': "off"})

    node = StringField('node',
                       render_kw={'placeholder': '请输入node (允许为空)', 'class': "layui-input",
                                  'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class DeviceDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入name")],
                       render_kw={'placeholder': '请输入name', 'class': "layui-input",
                                  'autocomplete': "off"})

    project_id = StringField('project_id',
                             render_kw={'placeholder': '请输入project_id (允许为空)', 'class': "layui-input",
                                        'autocomplete': "off"})

    product_id = StringField('product_id',
                             render_kw={'placeholder': '请输入product_id (允许为空)', 'class': "layui-input",
                                        'autocomplete': "off"})

    Device_group_id = StringField('Device_group_id',
                                  render_kw={'placeholder': '请输入Device_group_id (允许为空)', 'class': "layui-input",
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
    name = StringField('name',
                       render_kw={'placeholder': '请输入name (允许为空)', 'class': "layui-input",
                                  'autocomplete': "off"})

    submit = SubmitField('提交', render_kw={'class': "layui-btn"})


class AuthDataForm(FlaskForm):
    name = StringField('name',
                       render_kw={'placeholder': '请输入name (允许为空)', 'class': "layui-input",
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
    admin_id = StringField('admin_id',
                           render_kw={'placeholder': '请输入admin_id (允许为空)', 'class': "layui-input",
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
