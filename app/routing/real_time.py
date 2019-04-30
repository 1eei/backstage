# ！/usr/bin/env python
# -*-coding:utf-8 -*-
from . import admin
from flask import render_template, session
from flask_login import login_required
import time, socketserver, threading, traceback, json, socket, base64
from threading import Lock
from app import socketio, db
from app.models import RealTime

thread_lock = Lock()
client_addr = []
client_socket = []
global msgdata
msgdata = ""


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    ip = ""
    port = 0
    timeOut = 3600

    def setup(self):
        self.ip = self.client_address[0].strip()
        self.port = self.client_address[1]
        self.request.settimeout(self.timeOut)
        print(self.ip + ":" + str(self.port) + "连接到服务器！")
        client_addr.append(self.client_address)
        client_socket.append(self.request)

    def handle(self):
        while True:
            try:
                time.sleep(3)
                try:
                    data = self.request.recv(1024).decode()
                    data = base64.b64decode(data)
                except socket.timeout:
                    print(self.ip + ":" + str(self.port) + "接收超时！即将断开连接！")
                    break
                if data:
                    data = json.loads(data)
                    times = time.strftime('%H:%M:%S', time.localtime())

                    temperature = data['temperature']
                    humidity = data['humidity']
                    timestamp = data['times']
                    number = data['number']

                    socketio.emit('server_response', {'data': [times, humidity, temperature]})

                    humidity_data = RealTime(device_number=number,
                                             attr='humidity',
                                             par=humidity,
                                             times=timestamp
                                             )

                    temperature_data = RealTime(device_number=number,
                                                attr='temperature',
                                                par=temperature,
                                                times=timestamp
                                                )

                    db.session.add(humidity_data)
                    db.session.add(temperature_data)
                    db.session.commit()

            except BaseException:
                traceback.print_exc()
                break

    def finish(self):
        print(self.ip + ":" + str(self.port) + "断开连接！")
        client_addr.remove(self.client_address)
        client_socket.remove(self.request)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    ServerStart = False
    pass


HOST, PORT = "0.0.0.0", 10000
server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
ip, port = server.server_address
server.ServerStart = False
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True


@admin.route('/real_time', methods=['GET', 'POST'])
@login_required
def real_time():
    # 保存管理员名字和角色id
    session_admin = session['admin']
    session_role_id = session['role']

    if len(client_socket) == 0:

        if server.ServerStart:
            pass
        else:
            server_thread.start()
            server.ServerStart = True

    return render_template('real_time.html',
                           session_admin=session_admin,
                           session_role_id=session_role_id,
                           async_mode=socketio.async_mode
                           )
