from . import admin
from flask import Flask, render_template
from app.admin.views import admin_login_required
import json


@admin.route('/devices_list', methods=["GET"])
@admin_login_required
def devices_list():
    return render_template('devices_list.html')

@admin.route('/device_form')
@admin_login_required
def device_form():
    return render_template('form/device_form.html')

@admin.route('/device_edit')
@admin_login_required
def device_edit():
    return render_template('edit/device_edit.html')