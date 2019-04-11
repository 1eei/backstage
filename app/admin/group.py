from . import admin
from flask import Flask, render_template
import json

@admin.route('/group', methods=["GET"])
def group():
    return render_template('group.html')

@admin.route('/group_form')
def group_form():
    return render_template('form/group_form.html')

@admin.route('/group_edit')
def group_edit():
    return render_template('edit/group_edit.html')