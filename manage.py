# ！/usr/bin/env python
# -*-coding:utf-8 -*-

from app import create_app
from app.models import db, app

db.init_app(app)

if __name__ == '__main__':
    app = create_app('development')
    app.run(host='127.0.0.1', port=7777)
