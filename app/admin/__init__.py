# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.admin.views
import app.admin.project
import app.admin.product
import app.admin.devices
import app.admin.group
import app.admin.database