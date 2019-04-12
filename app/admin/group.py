from . import admin
from flask import Flask, render_template
from flask_login import login_required
import json

@admin.route('/group', methods=["GET"])
@login_required
def group():
    return render_template('group.html')

@admin.route('/group_form')
@login_required
def group_form():
    return render_template('form/group_form.html')

@admin.route('/group_edit')
@login_required
def group_edit():
    return render_template('edit/group_edit.html')