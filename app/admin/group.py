from . import admin
from flask import render_template
from flask_login import login_required
from app.models import DeviceGroup


@admin.route('/group/<int:page>', methods=["GET"])
@login_required
def group(page):
    if page is None:
        page = 1
    page_data = DeviceGroup.query.order_by(
        DeviceGroup.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('group.html', page_data=page_data)


@admin.route('/group_form')
@login_required
def group_form():
    return render_template('form/group_form.html')


@admin.route('/group_edit')
@login_required
def group_edit():
    return render_template('edit/group_edit.html')
