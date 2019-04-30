from . import admin
from app import db
from flask import render_template, flash, request, redirect, url_for, session
from app.models import Device, Project, Product, DeviceGroup, RealTime
from app.forms import DeviceDataForm
from flask_login import login_required
import time


@admin.route('/devices_list/<int:page>', methods=["GET", "POST"])
@login_required
def devices_list(page):
    if page is None:
        page = 1
    page_data = Device.query.join(Product).filter(
        Product.id == Device.product_id
    ).order_by(
        Device.id.asc()
    ).paginate(page=page, per_page=5)

    # 获取最后上线时间时间戳
    last_times = RealTime.query.join(Device).filter(
        Device.number == RealTime.device_number
    ).order_by(RealTime.times.desc()).first()
    # 格式化时间戳
    last_times = last_times.times
    last_times = time.localtime(last_times)
    last_times = time.strftime("%Y-%m-%d %H:%M:%S", last_times)

    # 保存管理员名字和角色id
    session_admin = session['admin']
    session_role_id = session['role']

    id = request.args.get('id')
    _active = request.args.get('_active')
    device = Device.query.filter_by(id=id).first()

    device_all = Device.query.all()
    device_count = Device.query.count()
    device_online = Device.query.filter_by(_online=1).count()
    device_active = Device.query.filter_by(_active=1).count()

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

    return render_template('devices_list.html',
                           page_data=page_data,
                           device_all=device_all,
                           device_count=device_count,
                           device_online=device_online,
                           device_active=device_active,
                           session_admin=session_admin,
                           session_role_id=session_role_id,
                           last_times=last_times
                           )


@admin.route('/device_edit', methods=["GET", "POST"])
@login_required
def device_edit():
    id = request.args.get('id')
    device = Device.query.get_or_404(id)
    form = DeviceDataForm(project_id=device.project_id, product_id=device.product_id,
                          devicegroup_id=device.devicegroup_id, online=device._online, active=device._active)
    if request.method == 'GET' or request.method == 'POST':
        form.project_id.choices = [(v.id, v.name) for v in Project.query.all()]
        form.product_id.choices = [(v.id, v.name) for v in Product.query.all()]
        form.devicegroup_id.choices = [(v.id, v.name) for v in DeviceGroup.query.all()]
        form.node.choices = [(1, '设备'), (2, '路由')]
    if form.validate_on_submit():
        data = form.data
        device.name = data['name']
        device.project_id = data['project_id']
        device.product_id = data['product_id']
        device.devicegroup_id = data['devicegroup_id']
        device.number = data['number']
        device.node = data['node']
        device._online = data['online']
        device._active = data['active']
        db.session.add(device)
        db.session.commit()
        flash("项目表数据修改成功", "ok")
    return render_template('edit/device_edit.html', form=form, device=device)


@admin.route('/device_add', methods=['GET', 'POST'])
@login_required
def device_add():
    form = DeviceDataForm()

    if request.method == 'GET' or request.method == 'POST':
        form.project_id.choices = [(v.id, v.name) for v in Project.query.all()]
        form.product_id.choices = [(v.id, v.name) for v in Product.query.all()]
        form.devicegroup_id.choices = [(v.id, v.name) for v in DeviceGroup.query.all()]
        form.node.choices = [(1, '设备'), (2, '路由')]

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
        flash('设备表数据添加成功!', 'ok')
        return redirect(url_for('admin.device_add'))
    return render_template('add/device_add.html', form=form)


@admin.route('/device_delete', methods=['GET', 'POST'])
@login_required
def device_delete():
    id = request.args.get('id')
    page = request.args.get('page')
    device = Device.query.get_or_404(id)
    device.id = id
    db.session.delete(device)
    db.session.commit()
    flash("设备表数据删除成功", "ok")
    return redirect(url_for('admin.devices_list', page=page))
