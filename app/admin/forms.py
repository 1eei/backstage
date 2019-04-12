from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin


class AdminForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="请输入用户名")], render_kw={'placeholder': '请输入用户名'})
    password = PasswordField('password', validators=[DataRequired(message="请输入密码")], render_kw={'placeholder': '请输入密码'})
    remember_me = BooleanField('remember_Me', default=False)
    submit = SubmitField('登录')

    def validate_name(self, field):
        name = field.data
        admin = Admin.query.filter_by(name=name).count()
        if admin == 0:
            raise ValidationError("账号不存在")
