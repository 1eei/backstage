from . import admin
from app import db
from flask import render_template, flash, redirect, url_for
from app.models import DeviceGroup
from app.templates.database.forms import DeviceGroupDataForm
from flask_login import login_required


@admin.route('/group/<int:page>', methods=["GET"])
# @login_required
def group(page):
    if page is None:
        page = 1
    page_data = DeviceGroup.query.order_by(
        DeviceGroup.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('group.html', page_data=page_data)


@admin.route('/group_edit')
# @login_required
def group_edit():
    form = DeviceGroupDataForm()
    return render_template('edit/group_edit.html', form=form)


@admin.route('/device_group_add', methods=['GET', 'POST'])
# @login_required
def device_group_add():
    form = DeviceGroupDataForm()
    if form.validate_on_submit():
        name = form.name.data

        device_group = DeviceGroup(name=name)

        db.session.add(device_group)
        db.session.commit()
        flash('DeviceGroup数据添加成功!', 'ok')
        return redirect(url_for('admin.device_group_add'))
    return render_template('database/device_group_add.html', form=form)
