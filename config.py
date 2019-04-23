# ！/usr/bin/env python
# -*-coding:utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    # WTF_CSRF_ENDABLE = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

    # 数据库配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qq111111@127.0.0.1:3306/lot_db?charset=utf8'

    @staticmethod
    def init_app(app):
        pass


# 开发阶段下的数据库：开发
class DevelopConfig(BaseConfig):
    DEBUG = True


# 上线产品阶段数据库：运维
class ProductConfig(BaseConfig):
    DEBUG = False


config = {
    'development': DevelopConfig,
    'production': ProductConfig,
}
