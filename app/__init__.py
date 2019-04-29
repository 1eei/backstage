import json
import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_socketio import SocketIO # 新加入的内容
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
async_mode = None
socketio = SocketIO()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    with app.app_context():
        db.init_app(app)
        db.app = app
    socketio.init_app(app=app, async_mode=async_mode)  # 新加入的内容
    # 实例化login_user
    from app.models import Admin
    login_manager = LoginManager()
    login_manager.login_view = 'admin.login'
    login_manager.init_app(app=app)

    # 通过session的id获取用户信息：,不获取id值无法登录
    @login_manager.user_loader
    def load_user(id):
        return Admin.query.get(id)

    register_errorhandlers(app)
    CSRFProtect(app)
    register_blueprints(app)
    ajax_api(app)

    return app


def register_blueprints(app):
    from app.routing import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')


def ajax_api(app):
    # 条形图数据接口
    @app.route('/post_bar_data', methods=['GET', 'POST'])
    def post_bar_data():
        bar_data = []

        now_day = ((datetime.datetime.now() - datetime.timedelta()).strftime("%m-%d"))
        last1_day = ((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%m-%d"))
        last2_day = ((datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%m-%d"))
        last3_day = ((datetime.datetime.now() - datetime.timedelta(days=3)).strftime("%m-%d"))
        last4_day = ((datetime.datetime.now() - datetime.timedelta(days=4)).strftime("%m-%d"))
        last5_day = ((datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%m-%d"))
        last6_day = ((datetime.datetime.now() - datetime.timedelta(days=6)).strftime("%m-%d"))

        data = [80, 10, 10, 10, 10, 10, 80]

        now = [last6_day, last5_day, last4_day, last3_day, last2_day, last1_day, now_day]

        bar_data.append({"data": data,
                         "time": now})

        return json.dumps(bar_data)

    # 气泡图数据接口
    @app.route('/post_bubble_data', methods=['GET', 'POST'])
    def post_bubble_data():
        bubble_data = []

        data = {'x': 200, 'y': 20, 'r': 20}, \
               {'x': 250, 'y': 25, 'r': 20}, \
               {'x': 300, 'y': 30, 'r': 20}, \
               {'x': 350, 'y': 35, 'r': 20}, \
               {'x': 400, 'y': 40, 'r': 20}, \
               {'x': 450, 'y': 45, 'r': 20}, \
               {'x': 500, 'y': 50, 'r': 20}, \
               {'x': 550, 'y': 55, 'r': 20},

        bubble_data.append({"data": data})

        return json.dumps(bubble_data)

    # 线状图数据接口
    @app.route('/post_line_data', methods=['GET', 'POST'])
    def post_line_data():
        line_data = []

        now_day = ((datetime.datetime.now() - datetime.timedelta()).strftime("%m-%d"))
        last1_day = ((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%m-%d"))
        last2_day = ((datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%m-%d"))
        last3_day = ((datetime.datetime.now() - datetime.timedelta(days=3)).strftime("%m-%d"))
        last4_day = ((datetime.datetime.now() - datetime.timedelta(days=4)).strftime("%m-%d"))
        last5_day = ((datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%m-%d"))
        last6_day = ((datetime.datetime.now() - datetime.timedelta(days=6)).strftime("%m-%d"))

        data = [800, 700, 600, 500, 400, 300, 200], \
               [100, 200, 300, 400, 500, 600, 700], \
               [700, 600, 500, 400, 300, 200, 100], \
               [200, 300, 400, 500, 600, 700, 800]

        now = [last6_day, last5_day, last4_day, last3_day, last2_day, last1_day, now_day]

        line_data.append({"data": data,
                          "time": now})

        return json.dumps(line_data)

    # 饼状图数据接口
    @app.route('/post_area_data', methods=['GET', 'POST'])
    def post_area_data():
        area_data = []
        data = [10, 50, 100]
        area_data.append({"data": data})
        return json.dumps(area_data)

    # 实时监控数据接口
    @app.route('/post_monitor_data', methods=['GET', 'POST'])
    def post_monitor_data():
        monitor_data = []

        now_hour = ((datetime.datetime.now() - datetime.timedelta()).strftime("%H:00"))
        last1_hour = ((datetime.datetime.now() - datetime.timedelta(minutes=60)).strftime("%H:00"))
        last2_hour = ((datetime.datetime.now() - datetime.timedelta(minutes=120)).strftime("%H:00"))
        last3_hour = ((datetime.datetime.now() - datetime.timedelta(minutes=180)).strftime("%H:00"))
        last4_hour = ((datetime.datetime.now() - datetime.timedelta(minutes=240)).strftime("%H:00"))

        data = [80, 79, 83, 93, 84], \
               [84, 93, 82, 73, 80], \
               [10, 20, 30, 40, 50]

        now = [last4_hour, last3_hour, last2_hour, last1_hour, now_hour]

        monitor_data.append({"data": data,
                             "time": now})

        return json.dumps(monitor_data)


def register_errorhandlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('errors/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('errors/400.html', description=e.description), 500
