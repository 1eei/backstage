from . import admin
from flask import render_template
from flask_login import login_required
from app.models import Device


@admin.route('/devices_list/<int:page>', methods=["GET"])
@login_required
def devices_list(page):
    if page is None:
        page = 1
    page_data = Device.query.order_by(
        Device.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('devices_list.html', page_data=page_data)


@admin.route('/device_form')
@login_required
def device_form():
    return render_template('form/device_form.html')


@admin.route('/device_edit')
@login_required
def device_edit():
    return render_template('edit/device_edit.html')
