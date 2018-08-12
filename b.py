import socket

s = socket.socket()

host = socket.gethostname()

s.connect((host,12345))

print s.recv(1024)
s.close();