# ！/usr/bin/env python
# -*-coding:utf-8 -*-

import os


class BaseConfig:
    # 表单配置
    WTF_CSRF_ENDABLE = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

    # 数据库配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/lot_db'


# 开发阶段下的数据库：开发
class DevelopConfig(BaseConfig):
    DEBUG = True


# 测试模式下的数据库：测试
class TestConfig(BaseConfig):
    TEST = True


# 上线产品阶段数据库：运维
class ProductConfig(BaseConfig):
    DEBUG = False


config = {
    'development': DevelopConfig,
    'testing': TestConfig,
    'production': ProductConfig,
}
