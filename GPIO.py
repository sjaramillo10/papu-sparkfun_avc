import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26 
GPIO.setup(led, GPIO.OUT)
ledstate=False

while(True):
	time.sleep(1)
	ledstate = not ledstate
	GPIO.output(led, ledstate)
	print ledstate

