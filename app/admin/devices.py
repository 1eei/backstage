from . import admin
from flask import Flask, render_template
import json


@admin.route('/devices_list', methods=["GET"])
def devices_list():
    return render_template('devices_list.html')

@admin.route('/device_form')
def device_form():
    return render_template('form/device_form.html')

@admin.route('/device_edit')
def device_edit():
    return render_template('edit/device_edit.html')