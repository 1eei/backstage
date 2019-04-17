from . import admin
from app import db
from flask import render_template, flash, request, redirect, url_for
from app.models import Device
from app.templates.database.forms import DeviceDataForm
from flask_login import login_required


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
    form = DeviceDataForm()
    return render_template('edit/device_edit.html', form=form)


@admin.route('/device_add', methods=['GET', 'POST'])
# @login_required
def device_add():
    form = DeviceDataForm()
    if form.validate_on_submit():
        name = form.name.data
        project_id = int(form.project_id.data)
        product_id = int(form.product_id.data)
        devicegroup_id = int(form.devicegroup_id.data)
        number = form.number.data
        node = form.node.data
        _online = int(form.online.data)
        _active = int(form.active.data)

        device = Device(name=name,
                        project_id=project_id,
                        product_id=product_id,
                        devicegroup_id=devicegroup_id,
                        number=number,
                        node=node,
                        _online=_online,
                        _active=_active)

        db.session.add(device)
        db.session.commit()
        flash('Device数据添加成功!', 'ok')
        return redirect(url_for('admin.device_add'))
    return render_template('database/device_add.html', form=form)
