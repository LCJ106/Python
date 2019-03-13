# coding=utf-8
import socket
from time import ctime

HOST=''
#PORT=socket.getservbyname('daytime','tcp')
PORT=9666
print('使用TCP协议的“daytime”服务的端口号为%s' % PORT)

ADDR = (HOST, PORT)
#建立套接字
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定主机地址和端口号
tcpSerSock.bind(ADDR)
#监听
tcpSerSock.listen(1)
#返回1.新的可以收发数据的套接字2.连接另一端套接字对应的address，格式（IP地质，端口号）
conn,addr=tcpSerSock.accept()
print('Connected by ',addr)
try:
    while True:
        #1024.立即接收数据的最大量,未收到数据conn会阻塞
        data=conn.recv(1024)
        #decode解码
        data=data.decode()
        if not data:
            break
        print('Received data:',data)
        #conn.sendall(bytes('[%s] %s' % (ctime(), data.encode('utf-8')), 'utf-8'))
        conn.sendall(ctime().encode('utf-8'))
except Exception as err:
    print("[TCP_SERVE_ERROR] " + str(err))
finally:
    print('close')
    conn.close()
    tcpSerSock.close()

