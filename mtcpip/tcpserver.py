# 导入socket、threading多线程模块
import os
import socket
import threading
import time

import psutil

url = '127.0.0.1'
port = 9999


def tcplink(sock, addr):
    sock.send(b'Welcome!')
    print('Accept new connection from %s:%s...' % addr)
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    psutil.Process(os.getpid()).threads()

    print('Connection from %s:%s closed.' % addr)


def startTcpServer():
    global url
    global port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    s.bind((url, port))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
        print(t.getName(),)


startTcpServer()
