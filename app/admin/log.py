# ！/usr/bin/env python
# -*-coding:utf-8 -*-
from . import admin
from app import db
from flask import render_template, flash, redirect, url_for
from app.models import TestLog
from app.templates.database.forms import TestLogDataForm
from datetime import datetime
from flask_login import login_required


@admin.route('/log_server/<int:page>', methods=["GET"])
# @login_required
def log_server(page):
    if page is None:
        page = 1
    page_data = TestLog.query.order_by(
        TestLog.id.asc()
    ).paginate(page=page, per_page=5)
    return render_template('log_server.html', page_data=page_data)


@admin.route('/monitor', methods=["GET"])
# @login_required
def monitor():
    return render_template('monitor.html')


@admin.route('/online_test', methods=["GET"])
# @login_required
def online_test():
    return render_template('online_test.html')


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
        flash('Testlog数据添加成功!', 'ok')
        return redirect(url_for('admin.testlog_add'))
    return render_template('database/testlog_add.html', form=form)
