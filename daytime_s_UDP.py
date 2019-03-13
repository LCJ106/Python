# coding=utf-8
# UDP服务器程序
from socket import *
from time import ctime

HOST = ''
# 确定使用UDP协议的“daytime”服务的端口号
PORT=getservbyname("daytime","udp")
print('使用UDP协议的“daytime”服务的端口号为%s' % PORT)
BUFSIZ = 1024
ADDR = (HOST, PORT)

# udpSerSock = socket(AF_INET, SOCK_STREAM)
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        print('waiting for message...')
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        if not data:
            break
        udpSerSock.sendto(bytes('[%s] %s' % (ctime(),data.decode('utf-8')),'utf-8'),addr)
        print('...received from and returned to:', addr)
except Exception as err:
    print("[UDP_SERVE_ERROR] " + str(err))
finally:
    udpSerSock.close()


