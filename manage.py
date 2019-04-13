# ！/usr/bin/env python
# -*-coding:utf-8 -*-

import os
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app(os.getenv('Flask_CONFIG') or 'development')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # 启动项目

    app.run(host='127.0.0.1', port=7777)

    # 迁移数据库

    # manager.run()
