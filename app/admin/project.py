from . import admin
from app import db
from flask import render_template, flash, request, redirect, url_for
from app.models import Admin, User, Project
from app.templates.database.forms import ProjectDataForm, AdminDataForm
from flask_login import login_required


@admin.route('/project_list/<int:page>', methods=["GET"])
# @login_required
def project_list(page):
    if page is None:
        page = 1
    page_data = Project.query.join(Admin).filter(
        Project.admin_id == Admin.id
    ).order_by(
        Project.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('project_list.html', page_data=page_data)


@admin.route('/project_edit/', methods=['GET', 'POST'])
# @login_required
def project_edit():
    form = ProjectDataForm()
    id = request.args.get('id')
    project = Project.query.filter_by(id=id).first()
    form.user_id.data = project.user_id
    form.admin_id.data = project.admin_id
    form.number.data = project.number
    form.name.data = project.name
    form.type.data = project.type
    form.commpy.data = project.commpy

    if form.validate_on_submit():
        form = ProjectDataForm()
        id = request.args.get('id')
        project = Project.query.filter_by(id=id).first()
        project.user_id = form.user_id.data
        project.admin_id = form.admin_id.data
        project.number = form.number.data
        project.name = form.name.data
        project.type = form.type.data
        project.commpy = form.commpy.data
        db.session.add(project)
        db.session.commit()
        flash('Project数据修改成功!', 'ok')

    return render_template('edit/project_edit.html', form=form)


@admin.route('/project_admin', methods=['GET', 'POST'])
# @login_required
def project_admin():
    form = AdminDataForm()
    id = request.args.get('id')
    admin = Admin.query.filter_by(id=id).first()
    form.account.data = admin.account
    form.role_id.data = admin.role_id
    form.locked.data = admin._locked

    if form.validate_on_submit():
        form = AdminDataForm()
        id = request.args.get('id')
        admin = Admin.query.filter_by(id=id).first()
        admin.account = form.account.data
        admin.pwd = form.pwd.data
        admin.role_id = form.role_id.data
        admin.locked = form.locked.data
        db.session.add(admin)
        db.session.commit()
        flash('Admin数据修改成功!', 'ok')

    return render_template('edit/project_admin.html', form=form)


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
        flash('Project数据添加成功!', 'ok')

    return render_template('database/project_add.html', form=form)
