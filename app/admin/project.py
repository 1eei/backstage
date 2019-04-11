from . import admin
from flask import Flask, render_template
from app.admin.views import admin_login_required
import json

@admin.route('/project_list', methods=["GET"])
@admin_login_required
def project_list():
    return render_template('project_list.html')

@admin.route('/creat_project_form')
@admin_login_required
def creat_project_form():
    return render_template('form/creat_project_form.html')

@admin.route('/project_edit')
@admin_login_required
def project_edit():
    return render_template('edit/project_edit.html')

@admin.route('/project_user_add')
@admin_login_required
def project_user_add():
    return render_template('add/project_user_add.html')

@admin.route('/project_user_info')
@admin_login_required
def project_user_info():
    return render_template('info/project_user_info.html')