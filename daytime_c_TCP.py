import socket
import sys
HOST = 'localhost'
# 确定使用TCP协议的“daytime”服务的端口号
#PORT=socket.getservbyname("daytime","tcp")
PORT=9666
BUFSIZ = 1024
ADDR = (HOST, PORT)
#客户端套接字建立
tcpCliSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    #连接服务器ADDR为服务器address
    tcpCliSock.connect(ADDR)
    print('connect')
except Exception as e:
    print('Server not found or not open')
    sys.exit()
while True:
    data0 = input('>')
    #发送数据
    tcpCliSock.sendall(data0.encode())
    data=tcpCliSock.recv(1024)
    print(data.decode('utf-8'))
    if data0.lower()=='close':
        break
tcpCliSock.close()
