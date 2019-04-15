from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin


class AdminForm(FlaskForm):
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