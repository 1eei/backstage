# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.admin.views
import app.admin.admin_
import app.admin.auth
import app.admin.devices
import app.admin.group
import app.admin.log
import app.admin.order
import app.admin.product
import app.admin.project
import app.admin.role
import app.admin.user
