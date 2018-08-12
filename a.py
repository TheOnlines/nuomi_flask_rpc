#encoding:utf8
import socket

s = socket.socket()

host = socket.gethostname()

s.bind((host,12345))

s.listen(5)

while True:
    print 123;
    c,addr = s.accept()
    print addr;
    c.send('你好啊 连上啦')

    c.close()
