"""
MS5611 driver code is placed under the BSD license.
Copyright (c) 2014, Emlid Limited, www.emlid.com
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
	* Redistributions of source code must retain the above copyright
	notice, this list of conditions and the following disclaimer.
	* Redistributions in binary form must reproduce the above copyright
	notice, this list of conditions and the following disclaimer in the
	documentation and/or other materials provided with the distribution.
	* Neither the name of the Emlid Limited nor the names of its contributors
	may be used to endorse or promote products derived from this software
	without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL EMLID LIMITED BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import spidev
import time
import sys
import navio.mpu9250
import navio.util
import math
import os
import socket

navio.util.check_apm()

imu = navio.mpu9250.MPU9250()
TCP_IP = "10.42.0.132"
TCP_PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))



if imu.testConnection():
    print "Connection established: True"
else:
    sys.exit("Connection established: False")

def calibrate():
    global DT,z
    n = 100	
    for i in range (n):
        m9a, m9g, m9m = imu.getMotion9()
        z[0] += round(m9g[0],2)
        z[1] += round(m9g[1],2)
        z[2] += round(m9g[2],2) 
        time.sleep(DT)
    z[0] /= n
    z[1] /= n
    z[2] /= n
    print "listo",z[0],z[1],z[2],

imu.initialize()
time.sleep(1)
DT = 0.5
z = [0.0]*3
px = py = pz = 0
gx = gy = gz = 0



print "while/n"
while True:
    # imu.read_all()
    # imu.read_gyro()
    # imu.read_acc()
    # imu.read_temp()
    # imu.read_mag()

    # print "Accelerometer: ", imu.accelerometer_data
    # print "Gyroscope:     ", imu.gyroscope_data
    # print "Temperature:   ", imu.temperature
    # print "Magnetometer:  ", imu.magnetometer_data

    # time.sleep(0.1)

    m9a, m9g, m9m = imu.getMotion9()

    if z[0] < 0:
        m9g[0] += round(abs(z[0]),2)
    else:
        m9g[0] -= round(abs(z[0]),2)
    if z[1] < 0:
        m9g[1] += round(abs(z[1]),2)
    else:
        m9g[1] -= round(abs(z[1]),2)
    if z[2] < 0:
        m9g[2] += round(abs(z[2]),2)
    else:
        m9g[2] -= round(abs(z[2]),2)
    

    px += round(m9g[0]*DT,2)
    py += round(m9g[1]*DT,2)
    pz += round(m9g[2]*DT,2)
  
    gx = round(math.degrees(px),2)
    gy = round(math.degrees(py),2)
    gz = round(math.degrees(pz),2)

    print "Acc:", "{:+7.3f}".format(m9a[0]), "{:+7.3f}".format(m9a[1]), "{:+7.3f}".format(m9a[2]),
    print "Gyr:", "{:+8.3f}".format(m9g[0]), "{:+8.3f}".format(m9g[1]), "{:+8.3f}".format(m9g[2]),
    print "Mag:", "{:+7.3f}".format(m9m[0]),"{:+7.3f}".format(m9m[1]), "{:+7.3f}".format(m9m[2]),
    print "Pos:", "{:+7.3f}".format(gx), "{:+7.3f}".format(gy), "{:+7.3f}".format(gz)
    time.sleep(DT)
    msg =  str("{:+7.3f}".format(m9m[0]))+","+str("{:+7.3f}".format(m9m[1]))+"\n"
    print msg
    s.send(msg)
    os.system("clear")
