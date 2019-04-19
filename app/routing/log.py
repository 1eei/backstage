# ！/usr/bin/env python
# -*-coding:utf-8 -*-
from . import admin
from app import db
from flask import render_template, flash, redirect, url_for
from app.models import TestLog, Device, Product, DeviceGroup
from app.forms import TestLogDataForm
from datetime import datetime


@admin.route('/log_server/<int:page>', methods=["GET"])
# @login_required
def log_server(page):
    if page is None:
        page = 1
    page_data = TestLog.query.order_by(
        TestLog.id.asc()
    ).paginate(page=page, per_page=5)

    device_all = Device.query.all()
    device_count = Device.query.count()
    device_online = Device.query.filter_by(_online=2).count()

    return render_template('log_server.html',
                           page_data=page_data,
                           device_all=device_all,
                           device_count=device_count,
                           device_online=device_online)


@admin.route('/monitor', methods=["GET"])
# @login_required
def monitor():
    device_all = Device.query.all()
    device_count = Device.query.count()
    device_online = Device.query.filter_by(_online=1).count()
    device_active = Device.query.filter_by(_active=1).count()
    return render_template('monitor.html',
                           device_count=device_count,
                           device_all=device_all,
                           device_online=device_online,
                           device_active=device_active)


@admin.route('/online_test', methods=["GET"])
# @login_required
def online_test():
    device_all = Device.query.all()
    product_all = Product.query.all()
    group_all = DeviceGroup.query.all()

    return render_template('online_test.html',
                           group_all=group_all,
                           device_all=device_all,
                           product_all=product_all)


@admin.route('/testlog_add', methods=['GET', 'POST'])
# @login_required
def testlog_add():
    form = TestLogDataForm()
    if form.validate_on_submit():
        content = form.content.data
        cause = form.cause.data
        report_time = datetime.now()

        testlog = TestLog(content=content,
                          cause=cause,
                          report_time=report_time)

        db.session.add(testlog)
        db.session.commit()
        flash('日志表数据添加成功!', 'ok')
        return redirect(url_for('admin.testlog_add'))
    return render_template('add/testlog_add.html', form=form)
