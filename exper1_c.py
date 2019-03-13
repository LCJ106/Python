import socket
addr=('localhost',9888)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect(addr)
except:
    print('未发现服务器')
while True:
    recv_data=s.recv(1024)
    #print(recv_data.decode(), ' ', end="")
    print(recv_data.decode())
    #if int(recv_data.decode()) == 100:
        #break
s.close()
