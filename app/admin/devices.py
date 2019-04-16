from . import admin
from flask import render_template, request
from flask_login import login_required
from app.models import Device
from app import db


@admin.route('/devices_list/<int:page>', methods=["GET", "POST"])
# @login_required
def devices_list(page):
    if page is None:
        page = 1
    page_data = Device.query.order_by(
        Device.id.asc()
    ).paginate(page=page, per_page=5)

    _active = request.args.get('_active')
    id = request.args.get('id')
    device = Device.query.filter_by(id=id).first()

    if _active == '1':  # 1 = 启用
        _active = 0
        device._active = _active
        db.session.add(device)
        db.session.commit()
    elif _active == '0':  # 0= 禁用
        _active = 1
        device._active = _active
        db.session.add(device)
        db.session.commit()

    return render_template('devices_list.html', page_data=page_data)


@admin.route('/device_edit')
# @login_required
def device_edit():
    return render_template('edit/device_edit.html')
