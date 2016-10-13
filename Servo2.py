import sys
import sys
import time

import navio.pwm
import navio.util

navio.util.check_apm()

PWM_OUTPUT = 1 
atras = 1.150 #ms servo min
adelante = 1.850 #ms servo max
neutral = atras+((adelante-atras)/2)

pwm = navio.pwm.PWM(PWM_OUTPUT)
pwm.set_period(50)

time.sleep(2)

while (True):
    pwm.set_duty_cycle(neutral)
    time.sleep(1)
    pwm.set_duty_cycle(adelante)
    time.sleep(1)	
    pwm.set_duty_cycle(neutral)
    time.sleep(1)
    pwm.set_duty_cycle(atras)
    time.sleep(1)
