from . import admin
from flask import render_template
from flask_login import login_required
from app.models import Project


@admin.route('/project_list/<int:page>', methods=["GET"])
@login_required
def project_list(page):
    if page is None:
        page = 1
    page_data = Project.query.order_by(
        Project.id.asc()
    ).paginate(page=page, per_page=1)
    return render_template('project_list.html', page_data=page_data)


@admin.route('/creat_project_form')
@login_required
def creat_project_form():
    return render_template('form/creat_project_form.html')


@admin.route('/project_edit')
@login_required
def project_edit():
    return render_template('edit/project_edit.html')


@admin.route('/project_user_add')
@login_required
def project_user_add():
    return render_template('add/project_user_add.html')


@admin.route('/project_user_info')
@login_required
def project_user_info():
    return render_template('info/project_user_info.html')
