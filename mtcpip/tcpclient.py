# 导入socket库:
import socket

url = '127.0.0.1'
port = 9999


def startClient():
    global url, port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect((url, port))
    # 接收欢迎消息:
    decode = s.recv(1024).decode('utf-8')
    print("--->%s" % decode)
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        print("%s--->" % data)
        s.send(data)
        print("--->%s" % s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()


startClient()
startClient()
startClient()
startClient()
startClient()
startClient()
startClient()
