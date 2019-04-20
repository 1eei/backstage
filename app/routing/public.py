from . import admin
from flask import render_template, redirect, url_for, flash, request, session
from app.forms import LoginForm
from app.models import Admin, Project
from flask_login import login_user, logout_user, login_required


@admin.route('/')
@login_required
def index():
    project = Project.query.all()

    # 保存管理员名字和角色id
    session_admin = session['admin']
    session_role_id = session['role']

    return render_template('index.html',
                           project=project,
                           session_admin=session_admin,
                           session_role_id=session_role_id)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(account=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash('密码错误!', 'err')
            return redirect(url_for('admin.login'))
        '''
        remember_me:
        记住：是否在会话过期后记住用户。
        默认为“假”。
        login_user()里的有个会话过期的方法session['remember_seconds']
        session['remember_seconds'] = (duration.microseconds +
                                               (duration.seconds +
                                                duration.days * 24 * 3600) *
                                               10**6) / 10.0**6                  
        session permanent为True时，
        用户退出浏览器不会删除session，
        其会保留permanent_session_lifetime s(默认是31天)，
        但是当其为False且SESSION_PROTECTION 设为strong时，
        用户的session就会被删除。
        
        当用户点击记住密码，在下次打开浏览器时无需登录，
        否则，就要登录
        '''
        session['admin'] = admin.account
        session['role'] = admin.role_id
        login_user(admin, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('login.html', form=form)


@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.login'))
