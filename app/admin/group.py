from . import admin
from flask import Flask, render_template
from app.admin.views import admin_login_required
import json

@admin.route('/group', methods=["GET"])
@admin_login_required
def group():
    return render_template('group.html')

@admin.route('/group_form')
@admin_login_required
def group_form():
    return render_template('form/group_form.html')

@admin.route('/group_edit')
@admin_login_required
def group_edit():
    return render_template('edit/group_edit.html')