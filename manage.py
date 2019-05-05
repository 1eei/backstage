# ！/usr/bin/env python
# -*-coding:utf-8 -*-

import os
from app import create_app, db, socketio
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app(os.getenv('Flask_CONFIG') or 'development')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    try:
        # 启动项目

        socketio.run(app, host='127.0.0.1', port=8888)

        # 数据库迁移

        # manager.run()

    except BaseException:
        pass
