with open('D:\\workspace\\py\\HMI\\mtcpip\\tcpclient.py', 'rb+') as f:
    read = f.read()
    print("度完成")
    with open('D:\\workspace\\py\\HMI\\mtcpip\\llll.py', 'wb') as d:
        d.write(read)
