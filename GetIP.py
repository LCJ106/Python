import socket
name = socket.getfqdn(socket.gethostname())

ip = socket.gethostbyname(name)

print(ip)
