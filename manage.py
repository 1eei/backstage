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
manager.add_command('run', socketio.run(app=app, host='127.0.0.1', port=8888))


if __name__ == '__main__':
    # 启动项目
    try:
        manager.run()
    except BaseException:
        pass

