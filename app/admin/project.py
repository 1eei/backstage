from . import admin
from app import db
from flask import render_template, flash, request, redirect, url_for
from app.models import Admin, Project, User
from app.templates.database.forms import ProjectDataForm, ProjectEditForm, ProjectAdminEditForm
from flask_login import login_required


@admin.route('/project_list/<int:page>', methods=["GET"])
# @login_required
def project_list(page):
    if page is None:
        page = 1
    page_data = Project.query.join(Admin).filter(
        Project.admin_id == Admin.id
    ).order_by(
        Admin.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('project_list.html', page_data=page_data)


@admin.route('/project_edit', methods=['GET', 'POST'])
# @login_required
def project_edit():
    id = request.args.get('id')
    project = Project.query.get_or_404(id)
    form = ProjectEditForm(user_id=project.user_id, admin_id=project.admin_id, type=project.type)
    if request.method == 'GET' or request.method == 'POST':
        form.user_id.choices = [(v.id, v.name) for v in User.query.all()]
        form.admin_id.choices = [(v.id, v.name) for v in Admin.query.all()]
    if form.validate_on_submit():
        data = form.data
        project.user_id = data['user_id']
        project.admin_id = data['admin_id']
        project.type = data['type']
        project.commpy = data['commpy']
        project.name = data['name']
        db.session.add(project)
        db.session.commit()
        flash("项目表数据修改成功", "ok")

    return render_template('edit/project_edit.html', form=form, project=project)


@admin.route('/project_admin', methods=['GET', 'POST'])
# @login_required
def project_admin():
    id = request.args.get('id')
    print(id)
    admin = Admin.query.get_or_404(id)
    form = ProjectAdminEditForm()
    if request.method == 'GET' or request.method == 'POST':
        form.role_id.choices = [(v.id, v.name) for v in Admin.query.all()]
    if form.validate_on_submit():
        data = form.data
        admin.account = data['account']
        admin.pwd = data['pwd']
        admin.role_id = data['role_id']
        admin._locked = data['locked']
        db.session.add(admin)
        db.session.commit()
        flash("管理员表数据修改成功", "ok")
    return render_template('edit/project_admin.html', admin=admin, form=form)


@admin.route('/project_add', methods=['GET', 'POST'])
# @login_required
def project_add():
    form = ProjectDataForm()
    if form.validate_on_submit():
        name = form.name.data
        user_id = form.user_id.data
        admin_id = form.admin_id.data
        number = form.number.data
        type = form.type.data
        commpy = form.commpy.data

        project = Project(name=name,
                          user_id=user_id,
                          admin_id=admin_id,
                          number=number,
                          type=type,
                          commpy=commpy)

        db.session.add(project)
        db.session.commit()
        flash('项目表数据添加成功!', 'ok')
        return redirect(url_for('admin.project_add'))
    return render_template('database/project_add.html', form=form)
