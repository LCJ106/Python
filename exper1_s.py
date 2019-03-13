import socket
addr=('',9888)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(addr)
s.listen(1)
i=0
conn, address = s.accept()
print('Connected with {0}'.format(address))
while True:
    i += 1
    str="%s"%i
    conn.send(str.encode())
    if i == 100:
        i=0

s.close()
conn.close()
