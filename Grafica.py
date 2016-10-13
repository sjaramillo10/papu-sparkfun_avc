import time
import serial
from random import randint

ser = serial.Serial(
        port = "/dev/ttyAMA0",
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1       
)

while 1:
    a=randint(-100,100)
    b=randint(-100,100)
    s=str(a)+","+str(b)+"\n"
    print s
    ser.write(s)
    time.sleep(0.5)
