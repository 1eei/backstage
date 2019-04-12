from . import admin
from flask import Flask, render_template
from flask_login import login_required
import json


@admin.route('/devices_list', methods=["GET"])
@login_required
def devices_list():
    return render_template('devices_list.html')

@admin.route('/device_form')
@login_required
def device_form():
    return render_template('form/device_form.html')

@admin.route('/device_edit')
@login_required
def device_edit():
    return render_template('edit/device_edit.html')