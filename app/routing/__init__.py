# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.routing.public
import app.routing.admin_
import app.routing.auth
import app.routing.devices
import app.routing.group
import app.routing.log
import app.routing.order
import app.routing.product
import app.routing.project
import app.routing.role
import app.routing.user
import app.routing.real_time
