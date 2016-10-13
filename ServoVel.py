import sys
import time

import navio.util
import velocity

navio.util.check_apm()

vel = velocity.Velocity()
vel.daemon = True
vel.start()
time.sleep(5)
while (True):
    time.sleep(2)
    vel.accelerate()
    time.sleep(2)
    vel.decelerate()

