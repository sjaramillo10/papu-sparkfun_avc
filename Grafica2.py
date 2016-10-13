import time
import socket
from random import randint

TCP_IP = "10.42.0.132"
TCP_PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
time.sleep(1)
while True:
    a=randint(-100,100)
    b=randint(-100,100)
    msg=str(a)+","+str(b)+"\n"
    print msg
    s.send(msg)
    time.sleep(0.3)
s.close()
