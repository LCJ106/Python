# coding=utf-8
# UDP客户端
from socket import *

HOST = 'localhost'
# 确定使用UDP协议的“daytime”服务的端口号
PORT=getservbyname("daytime","udp")
print('使用UDP协议的“daytime”服务的端口号为%s' % PORT)
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)
try:
    while True:
        data = input('> ')
        if not data:
            break
        udpCliSock.sendto(bytes(data,'utf-8'),ADDR)
        data,ADDR = udpCliSock.recvfrom(BUFSIZ)
        print(data.decode('utf-8'))
except EOFError as err:
    print("[UDP_CLIENT_ERROR] " + str(err))
finally:
    udpCliSock.close()
