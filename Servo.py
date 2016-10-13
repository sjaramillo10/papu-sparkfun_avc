import sys
import time

import navio.pwm
import navio.util

navio.util.check_apm()

PWM_OUTPUT = 0
derecha = 1.150 #ms derecha servo min
izquierda = 1.850 #ms izquierda servo max
centro = derecha+((izquierda-derecha)/2)

pwm = navio.pwm.PWM(PWM_OUTPUT)
pwm.set_period(50)

while (True):
    pwm.set_duty_cycle(centro)
    time.sleep(1)
    pwm.set_duty_cycle(derecha)
    time.sleep(1)	
    pwm.set_duty_cycle(centro)
    time.sleep(1)
    pwm.set_duty_cycle(izquierda)
    time.sleep(1)
